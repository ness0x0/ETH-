"""Sector trading activity: monthly sales count and volume (ETH, USD) summed across the screened universe
(NFTPriceFloor 3-day bars, so month boundaries are approximate). Indicator of buyer participation trend.
Output: data/processed/sector_activity_monthly.csv, reports/charts/sector_activity.png
"""
import os, glob
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import PROC, ROOT
from universe_config import UNIVERSE
frames = []
for name, npf, oss, cat in UNIVERSE:
    p = os.path.join(PROC, "npf_series", f"{npf}.csv")
    if os.path.exists(p):
        s = pd.read_csv(p, index_col=0, parse_dates=True)
        s = s.loc["2022-06-01":]
        frames.append(s[["salesCount", "volumeNative", "volumeUsd"]].assign(name=name))
a = pd.concat(frames)
m = a.groupby(pd.Grouper(freq="ME"))[["salesCount", "volumeNative", "volumeUsd"]].sum()
m = m.iloc[:-1] if m.index[-1] > pd.Timestamp("2026-10-01") else m  # drop partial month
m.to_csv(os.path.join(PROC, "sector_activity_monthly.csv"))
fig, ax = plt.subplots(2, 1, figsize=(11, 6.5), sharex=True)
ax[0].bar(m.index, m.salesCount, width=20, color="#34495e"); ax[0].set_ylabel("Sales / month")
ax[0].set_title("Trading activity across the 47-collection universe (NFTPriceFloor), monthly")
ax[1].bar(m.index, m.volumeUsd / 1e6, width=20, color="#c0392b"); ax[1].set_ylabel("Volume, $M / month")
for x in ax: x.grid(alpha=0.3)
fig.text(0.01, 0.01, "Source: NFTPriceFloor 3-day bars summed by month; includes wash trades where present.", fontsize=7.5)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(os.path.join(ROOT, "reports", "charts", "sector_activity.png"), dpi=120)
q = m.resample("QE").sum()
print(q.assign(volumeUsd_m=(q.volumeUsd / 1e6).round(1)).drop(columns="volumeUsd").round(0).to_string())
