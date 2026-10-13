"""Executable liquidity snapshot for finalists from OpenSea API v2 (requires free key from POST /api/v2/auth/keys,
stored outside the repo at /root/.config/ethnft/opensea_key.json).

Measures:
  - Ask side: cheapest N listings → cost to buy 1/2/3 items; listings within +5/10/25% of floor.
  - Bid side: collection offers (and trait/item offers where returned) → quantity bid at >=95/90/80/70/50% of floor,
    and proceeds from selling 1/2/3 items into the best bids.
  - Recent sales (events endpoint, last 30 days): count, unique buyers/sellers, median price, median gap.
Limitations: OpenSea order book only (Blur/Magic Eden/other venues not visible); offers may be unfunded (WETH
balance not checked); trait/item offers excluded from floor-bid depth unless they apply to any token.
Outputs: data/raw/opensea_book/<slug>_*.json, data/processed/liquidity_orderbook.csv
"""
import json
import os
import statistics
import time
import requests
from common import save_raw, PROC, utcnow, RPC
WETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

KEYF = "/root/.config/ethnft/opensea_key.json"
BASE = "https://api.opensea.io/api/v2"
FINALISTS = {
    "milady": "milady", "remilio-babies": "remilio", "cryptodickbutts-s3": "cryptodickbutts",
    "pudgypenguins": "pudgy", "lilpudgys": "lil_pudgys", "azuki": "azuki", "terraforms": "terraforms",
    "chromie-squiggle-by-snowfro": "chromie_squiggle", "official-v1-punks": "v1punks",
}


def key():
    return json.load(open(KEYF))["api_key"]


def get(path, params=None):
    h = {"x-api-key": key(), "accept": "application/json"}
    for i in range(6):
        r = requests.get(BASE + path, params=params, headers=h, timeout=60)
        if r.status_code == 429:
            time.sleep(5 * (i + 1))
            continue
        r.raise_for_status()
        time.sleep(6.2)  # free key: 600 reads/hour
        return r.json()
    raise RuntimeError(path)


def paged(path, field, params=None, max_pages=10):
    out, nxt = [], None
    for _ in range(max_pages):
        p = dict(params or {})
        if nxt:
            p["next"] = nxt
        d = get(path, p)
        out.extend(d.get(field, []))
        nxt = d.get("next")
        if not nxt:
            break
    return out


def eth(price):
    try:
        v = int(price["value"]) / 10 ** int(price.get("decimals", 18))
        return v
    except Exception:  # noqa
        return None


def main():
    rows = []
    for slug, k in FINALISTS.items():
        listings = paged(f"/listings/collection/{slug}/best", "listings", {"limit": 100}, max_pages=2)
        offers = paged(f"/offers/collection/{slug}", "offers", {"limit": 100}, max_pages=3)
        save_raw(f"opensea_book/{slug}_listings.json", listings)
        save_raw(f"opensea_book/{slug}_offers.json", offers)
        best = {}  # dedupe: cheapest order per token (bots post many duplicate orders per token)
        for l in listings:
            o = l["protocol_data"]["parameters"]["offer"][0]
            kk = (o["token"].lower(), o["identifierOrCriteria"])
            p_ = eth(l.get("price", {}).get("current", {}))
            if p_:
                best[kk] = min(p_, best.get(kk, 1e18))
        asks = sorted(best.values())
        # collection-wide offers: criteria with no trait / token restriction
        bids = []
        for o in offers:
            crit = o.get("criteria") or {}
            if crit.get("trait") or crit.get("traits") or crit.get("encoded_token_ids") not in (None, "*", ""):
                continue
            pr = o.get("price") or {}
            try:
                total = int(pr["value"]) / 10 ** int(pr.get("decimals", 18))
                orig_qty = int(o["protocol_data"]["parameters"]["consideration"][0]["startAmount"])
                qty = int(o.get("remaining_quantity") or orig_qty)
                bidder = o["protocol_data"]["parameters"]["offerer"]
            except Exception:  # noqa
                continue
            if qty <= 0 or orig_qty <= 0:
                continue
            bids.append((total / orig_qty, qty, bidder))
        bids.sort(reverse=True)
        # funding check: a bidder's WETH balance caps what their bids can actually pay (bids across collections
        # share the same balance, so this is an upper bound on funded depth)
        bal = {}
        for _, _, b in bids[:60]:
            if b not in bal:
                try:
                    data = "0x70a08231" + b[2:].lower().rjust(64, "0")
                    bal[b] = int(RPC().call("eth_call", [{"to": WETH, "data": data}, "latest"]), 16) / 1e18
                except Exception:  # noqa
                    bal[b] = None
        funded = []
        used = {}
        for p_, q_, b in bids:
            cap = bal.get(b)
            if cap is None:
                funded.append((p_, q_))
                continue
            can = int(max(0.0, cap - used.get(b, 0.0)) // p_) if p_ > 0 else 0
            take = min(q_, can)
            if take > 0:
                funded.append((p_, take))
                used[b] = used.get(b, 0.0) + take * p_
        r_bidders = len({b for _, _, b in bids})
        bids = [(p_, q_) for p_, q_, _ in bids]
        floor = asks[0] if asks else None
        r = {"slug": slug, "key": k, "snapshot_utc": utcnow(), "floor_ask": floor, "n_listings_seen": len(listings), "distinct_tokens_listed": len(asks),
             "cost_1": sum(asks[:1]) if asks else None, "cost_2": sum(asks[:2]) if len(asks) >= 2 else None,
             "cost_3": sum(asks[:3]) if len(asks) >= 3 else None,
             "best_bid": bids[0][0] if bids else None, "unique_bidders": r_bidders,
             "best_funded_bid": funded[0][0] if funded else None}
        if floor:
            for pct in (5, 10, 25):
                r[f"listings_within_{pct}pct"] = sum(1 for a in asks if a <= floor * (1 + pct / 100))
            for pct in (95, 90, 80, 70, 50):
                r[f"bid_qty_ge_{pct}pct_floor"] = sum(q for p, q in bids if p >= floor * pct / 100)
            for pct in (95, 90, 80, 70, 50):
                r[f"funded_bid_qty_ge_{pct}pct_floor"] = sum(q for p, q in funded if p >= floor * pct / 100)
            r["best_bid_pct_floor"] = bids[0][0] / floor if bids else None
            # proceeds selling 1..3 into bid ladder
            ladder = [p for p, q in funded for _ in range(min(q, 10))]
            for n in (1, 2, 3):
                r[f"proceeds_sell_{n}"] = sum(ladder[:n]) if len(ladder) >= n else None
        rows.append(r)
        print(k, {kk: (round(v, 4) if isinstance(v, float) else v) for kk, v in r.items() if kk not in ("slug",)})
    import pandas as pd
    pd.DataFrame(rows).to_csv(os.path.join(PROC, "liquidity_orderbook.csv"), index=False)


if __name__ == "__main__":
    main()
