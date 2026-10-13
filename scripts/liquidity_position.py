"""Round-trip cost for a ~$7,500 position (≈2.99 ETH at $2,508.69) built from the cheapest OpenSea listings and
exited immediately into the funded OpenSea collection-bid ladder (snapshot 2026-10-13 ~22:30 UTC).
Inputs: data/raw/opensea_book/*_listings.json, *_offers.json, data/processed/liquidity_orderbook.csv,
        data/processed/liquidity_activity.csv
Output: data/processed/liquidity_position.csv
Limitations: OpenSea-only book; bids refresh every few minutes (bot bids with 15-min expiry); a patient seller can
do better than the instant bid by listing near floor; seller fees included (FEE map).
"""
import json, os
import pandas as pd
from common import RAW, PROC
BUDGET_ETH = 7500 / 2508.69
S = {"milady": "milady", "remilio-babies": "remilio", "cryptodickbutts-s3": "cryptodickbutts", "pudgypenguins": "pudgy",
     "lilpudgys": "lil_pudgys", "azuki": "azuki", "terraforms": "terraforms",
     "chromie-squiggle-by-snowfro": "chromie_squiggle", "official-v1-punks": "v1punks"}
# seller-side fees observed in OpenSea listing consideration items (2026-10-13): marketplace 1% + enforced creator
# royalty where applicable (Squiggle 7.5% → 8.5% total; wrapped V1 0%)
FEE = {"chromie_squiggle": 0.085, "v1punks": 0.0}
act = pd.read_csv(os.path.join(PROC, "liquidity_activity.csv")).set_index("key")
rows = []
for slug, k in S.items():
    L = json.load(open(os.path.join(RAW, "opensea_book", f"{slug}_listings.json")))["data"]
    O = json.load(open(os.path.join(RAW, "opensea_book", f"{slug}_offers.json")))["data"]
    asks = sorted(int(l["price"]["current"]["value"]) / 1e18 for l in L)
    n, cost = 0, 0.0
    while n < len(asks) and (n == 0 or cost + asks[n] <= BUDGET_ETH * 1.02):
        cost += asks[n]; n += 1
    ladder = []
    for o in O:
        c = o.get("criteria") or {}
        if c.get("traits") or c.get("encoded_token_ids") not in (None, "*", ""):
            continue
        q0 = int(o["protocol_data"]["parameters"]["consideration"][0]["startAmount"])
        q = int(o.get("remaining_quantity") or q0)
        p = int(o["price"]["value"]) / 1e18 / q0
        ladder += [p] * min(q, 20)
    ladder.sort(reverse=True)
    fee = FEE.get(k, 0.01)
    proceeds = sum(ladder[:n]) * (1 - fee) if len(ladder) >= n else float("nan")
    rows.append(dict(key=k, floor_ask=asks[0], seller_fee=fee, items_for_budget=n, entry_cost_eth=round(cost, 4),
                     instant_exit_eth=round(proceeds, 4), roundtrip_haircut=round(1 - proceeds / cost, 4) if cost else None,
                     sales_per_day_90d=round(act.loc[k, "sales_per_day_90d"], 2) if k in act.index else None,
                     days_of_typical_volume=round(n / act.loc[k, "sales_per_day_90d"], 2) if k in act.index else None))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "liquidity_position.csv"), index=False)
print(f"Budget {BUDGET_ETH:.3f} ETH"); print(df.to_string())
