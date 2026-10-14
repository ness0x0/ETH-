"""Sector-level BTC-relative performance of the screened universe.

Builds an equal-weight index of floor prices (ETH and BTC terms) across all universe collections with NFTPriceFloor
history covering the window, plus median drawdowns. Purpose: establish the base rate — how ETH NFT floors have
behaved relative to BTC since 2022 — before judging any single collection.

Inputs: data/processed/npf_series/*.csv, data/processed/prices_daily.csv
Outputs: data/processed/sector_index.csv, reports/charts/sector_index_btc.png
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import PROC, ROOT
from universe_config import UNIVERSE

CH = os.path.join(ROOT, "reports", "charts")
os.makedirs(CH, exist_ok=True)

grid = pd.date_range("2022-06-01", "2026-10-13", freq="7D")
floors_eth, floors_btc = {}, {}
for name, npf, oss, cat in UNIVERSE:
    p = os.path.join(PROC, "npf_series", f"{npf}.csv")
    if not os.path.exists(p):
        continue
    s = pd.read_csv(p, index_col=0, parse_dates=True)
    s = s[s.floorNative > 0]
    if s.index[0] > pd.Timestamp("2022-07-01"):
        continue  # only collections with history through the whole window
    floors_eth[name] = s["floorNative"].reindex(grid, method="ffill")
    floors_btc[name] = s["floorBtc"].reindex(grid, method="ffill")

fe = pd.DataFrame(floors_eth)
fb = pd.DataFrame(floors_btc)
# equal-weight index = geometric mean of floor relative to start
idx_eth = np.exp(np.log(fe / fe.iloc[0]).mean(axis=1))
idx_btc = np.exp(np.log(fb / fb.iloc[0]).mean(axis=1))
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True).reindex(grid, method="ffill")
ethbtc = px["eth_btc"] / px["eth_btc"].iloc[0]
out = pd.DataFrame({"n": fe.notna().sum(axis=1), "ew_floor_eth": idx_eth, "ew_floor_btc": idx_btc, "eth_btc_rel": ethbtc,
                    "median_floor_btc_rel": (fb / fb.iloc[0]).median(axis=1)})
out.to_csv(os.path.join(PROC, "sector_index.csv"))

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(out.index, out.ew_floor_eth, label="EW NFT floor index (ETH terms)", color="#2a78d6", lw=1.8)
ax.plot(out.index, out.ew_floor_btc, label="EW NFT floor index (BTC terms)", color="#eb6834", lw=2.2)
ax.plot(out.index, out.eth_btc_rel, label="ETH/BTC", color="#8a8985", lw=1.4, ls="--")
ax.set_yscale("log")
ax.axhline(1, color="black", lw=0.6)
ax.set_title(f"Equal-weight floor index of {fe.shape[1]} ETH NFT collections, rebased 2022-06-01 (log scale)")
ax.set_ylabel("Relative to 2022-06-01")
ax.legend(loc="lower left")
ax.grid(alpha=0.3, which="both")
fig.text(0.01, 0.01, "Source: NFTPriceFloor 3d floors; Binance ETHBTC daily close. Survivorship: universe chosen in 2026 "
         "(collections still traded) — true sector loss is worse.", fontsize=7.5, color="#555")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(os.path.join(CH, "sector_index_btc.png"), dpi=130)

print(fe.shape[1], "collections")
print(out.iloc[[0, 26, 52, 78, 104, 130, 156, 182, 208, -1]].round(3).to_string())
# annual BTC-relative return of EW index
yr = out["ew_floor_btc"].resample("YE").last()
print((yr / yr.shift(1) - 1).round(3))
