"""CryptoPunks weekly floor proxy from on-chain PunkBought events (2017 → head) — Punks trade on their own market
contract, so OpenSea/NPF are incomplete for 2020-21.

Contract 0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB, event PunkBought(uint256 indexed punkIndex, uint256 value,
address indexed fromAddress, address indexed toAddress), topic0 0x58e5d5a5…b9e3. Known quirk: sales that accept a
bid emit value = 0 → excluded. Block timestamps interpolated linearly between sampled blocks (±minutes).
Floor proxy = 10th percentile of weekly sale prices (≥3 sales). Output: data/processed/punks_weekly.csv
"""
import os
import numpy as np
import pandas as pd
from common import RPC, PROC, save_raw

PUNKS = "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB"
TOPIC = "0x58e5d5a525e3b40bc15abaa38b5882678db1ee68befd2f60bafe3a7fd06db9e3"


def main():
    r = RPC(min_interval=0.2)
    head = r.block_number()
    logs = r.get_logs(PUNKS, [TOPIC], 3914495, head, step=500_000)
    save_raw("onchain_punks/punkbought_logs.json", [[l["blockNumber"], l["data"][:66], l["topics"][1]] for l in logs])
    blocks = sorted({int(l["blockNumber"], 16) for l in logs})
    # sample timestamps every ~20k blocks and interpolate
    samp = list(range(3914495, head, 20000)) + [head]
    ts = {}
    for b in samp:
        ts[b] = int(r.call("eth_getBlockByNumber", [hex(b), False])["timestamp"], 16)
    sb, st = np.array(sorted(ts)), np.array([ts[b] for b in sorted(ts)])
    rows = []
    for l in logs:
        b = int(l["blockNumber"], 16)
        v = int(l["data"][2:66], 16) / 1e18
        rows.append(dict(block=b, ts=pd.to_datetime(np.interp(b, sb, st), unit="s"), price_eth=v))
    df = pd.DataFrame(rows)
    df = df[df.price_eth > 0]
    w = df.set_index("ts").price_eth.resample("W").agg(["count", lambda x: x.quantile(0.10), "median"])
    w.columns = ["n_sales", "floor_proxy_p10", "median"]
    w.loc[w.n_sales < 3, "floor_proxy_p10"] = np.nan
    w.to_csv(os.path.join(PROC, "punks_weekly.csv"))
    print(len(df), "priced sales;", w.dropna().iloc[[0, -1]])


if __name__ == "__main__":
    main()
