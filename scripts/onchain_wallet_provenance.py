"""Provenance of tokens held by specific wallets (coordinator request: OpenSea floor "walls" seen 2026-10-13 22:30Z).

For each wallet and each token it holds at HEAD_BLOCK: the acquisition = last Transfer of that token INTO the wallet
(from data/raw/onchain/<key>_transfers.jsonl), skipping returns of the wallet's own deposits (wallet -> escrow such as
Blend/Gondi/NFTX -> wallet, e.g. a repaid loan) so the original acquisition is shown. The acquisition tx receipt is fetched (eth_getTransactionReceipt +
eth_getTransactionByHash, public endpoints as in onchain_fetch_receipts.py; cached to
data/raw/onchain/receipts/provenance_<key>.jsonl) and classified with onchain_sales.classify_tx. Transfers out of
Blur Blend are typed with the Blend event in the same tx: Seize = lender took defaulted collateral; Repay = loan repaid
and collateral returned to borrower; BuyLocked = purchase of a locked token.
Output: data/processed/onchain/wallet_provenance.csv (token-level) and wallet_provenance_summary.csv.
"""
import json
import os
import sys
import time

import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RECEIPT_RPCS  # noqa: E402
from onchain_config import BLEND, COLLECTIONS, RAW_ON  # noqa: E402
import onchain_lib as L  # noqa: E402
import onchain_sales as S  # noqa: E402

WALLETS = [("remilio", "0x54c6d73baf9dd8612978b694b23a309263b54cfa"),
           ("remilio", "0x163a9f0048a64b5bffca3a67d3084717bca22094"),
           ("terraforms", "0x00330fffa1ee8503d09fabed9bff204dc3cb3059"),
           ("terraforms", "0xcd8c2549af5c59d84f6f2f1de15e5c4d5ea6c1ca")]
T_SEIZE = "0xb71caf41fe0e019dbe21a1ae3493f11a729c31548ed1e304ae7f6e8c8df275de"
T_REPAY = "0x2469cc9e12e74c63438d5b1117b318cd3a4cdaf9d659d9eac6d975d14d963254"


def fetch(txs, path):
    have = {}
    if os.path.exists(path):
        for line in open(path):
            try:
                r = json.loads(line)
                have[r["tx"]] = r
            except Exception:  # noqa
                pass
    s = requests.Session()
    urls = RECEIPT_RPCS[:3]
    with open(path, "a") as f:
        for i, (tx, b) in enumerate(t for t in txs if t[0] not in have):
            for k in range(8):
                u = urls[(i + k) % len(urls)]
                try:
                    rc = s.post(u, json={"jsonrpc": "2.0", "id": 1, "method": "eth_getTransactionReceipt",
                                         "params": [tx]}, timeout=30).json()["result"]
                    t = s.post(u, json={"jsonrpc": "2.0", "id": 1, "method": "eth_getTransactionByHash",
                                        "params": [tx]}, timeout=30).json()["result"]
                    rec = {"tx": tx, "b": b, "from": rc["from"], "to": rc.get("to"), "value": t["value"],
                           "sel": (t.get("input") or "0x")[:10], "status": rc.get("status"), "ep": u.split("/")[2],
                           "logs": [[lg["address"].lower(), lg["topics"], lg["data"], int(lg["logIndex"], 16)]
                                    for lg in rc["logs"]]}
                    f.write(json.dumps(rec) + "\n")
                    have[tx] = rec
                    break
                except Exception:  # noqa
                    time.sleep(1 + k)
    return have


def main():
    rows = []
    for key in sorted({k for k, _ in WALLETS}):
        contract = COLLECTIONS[key][0]
        df = L.load_transfers(key)
        owner = df.groupby("id").tail(1).set_index("id")["to"]
        wallets = [w for k, w in WALLETS if k == key]
        acq = []
        for w in wallets:
            held = owner[owner == w].index
            first_in = df[df["to"] == w]["ts"].min()
            hist = df[df["id"].isin(held)]
            for tid, h in hist.groupby("id"):
                h = h.reset_index(drop=True)
                ins = h.index[h["to"] == w].tolist()
                j = ins[-1]
                # skip returns of the wallet's own collateral/deposits (wallet -> escrow -> wallet)
                while True:
                    src = h.loc[j, "f"]
                    if L.category(src) in L.ESCROW_CATS and j > 0 and h.loc[j - 1, "f"] == w \
                            and h.loc[j - 1, "to"] == src:
                        prev = [i for i in ins if i < j - 1]
                        if prev:
                            j = prev[-1]
                            continue
                    break
                r = h.loc[j]
                acq.append((w, tid, r["tx"], r["b"], r["ts"], r["f"], first_in))
        recs = fetch(sorted({(a[2], a[3]) for a in acq}), os.path.join(RAW_ON, "receipts", f"provenance_{key}.jsonl"))
        for w, tid, tx, b, ts, src, first_in in acq:
            rec = recs.get(tx)
            moves = df[df["tx"] == tx].sort_values("li").to_dict("records")
            res = [x for x in S.classify_tx(key, contract, rec, moves) if x["id"] == tid] if rec else []
            x = res[0] if res else {}
            topics = {lg[1][0] for lg in (rec or {}).get("logs", []) if lg[1] and lg[0] == BLEND}
            if src == "0x0000000000000000000000000000000000000000":
                how = "mint"
            elif src == BLEND or x.get("seller") == BLEND:
                how = ("blend_seized_collateral" if T_SEIZE in topics else
                       "blend_buy_locked" if x.get("method") == "blend_buy_locked" else
                       "blend_sale_of_locked" if x.get("type") == "sale" else
                       "blend_repaid_release" if T_REPAY in topics else "blend_other")
            elif x.get("type") == "sale":
                how = "purchase:" + x.get("method", "")
            else:
                how = "transfer_in:" + (x.get("type") or "unknown") + ":" + L.category(src)
            rows.append({"collection": key, "wallet": w, "tokenId": tid, "acquired_utc": ts.strftime("%Y-%m-%d %H:%M"),
                         "tx": tx, "from": src, "from_category": L.category(src), "acquisition": how,
                         "price_eth": x.get("price_eth") if x.get("type") == "sale" else None,
                         "wallet_first_received_utc": first_in.strftime("%Y-%m-%d")})
    out = pd.DataFrame(rows)
    L.write_csv(out, "wallet_provenance.csv")
    summ = []
    for (k, w), g in out.groupby(["collection", "wallet"]):
        vc = g["acquisition"].value_counts()
        summ.append({"collection": k, "wallet": w, "tokens_held": len(g),
                     "wallet_type": "contract" if L.is_contract(w) else ("eoa_7702" if L.is_7702(w) else "eoa"),
                     "first_received": g["wallet_first_received_utc"].iloc[0],
                     "acq_first": g["acquired_utc"].min(), "acq_last": g["acquired_utc"].max(),
                     "acq_median": pd.to_datetime(g["acquired_utc"]).median().strftime("%Y-%m-%d"),
                     "breakdown": "; ".join(f"{a}:{n}" for a, n in vc.items()),
                     "priced_purchases": int(g["price_eth"].notna().sum()),
                     "median_purchase_price_eth": g["price_eth"].median(),
                     "sum_purchase_price_eth": g["price_eth"].sum()})
    L.write_csv(pd.DataFrame(summ), "wallet_provenance_summary.csv")
    print(pd.DataFrame(summ).to_string())


if __name__ == "__main__":
    main()
