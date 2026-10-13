"""Rally anatomy and ETH/BTC beta for every universe collection.

For each recent sector-wide rally window, measure trough->peak multiple (ETH and BTC terms) and how much of the
peak was retained 90 / 180 days after the peak. Also estimate weekly log-return beta of BTC-denominated floor to
ETH/BTC (2022-06 -> 2026-10).

Windows (chosen from sector index turning points, reports/charts/sector_index_btc.png):
  R2023: trough 2022-11-01..2023-01-05, peak 2023-01-05..2023-03-15   (generative-art / Blur-airdrop rally)
  R2024: trough 2024-08-01..2024-10-31, peak 2024-11-01..2025-01-31   (post-election, PENGU TGE)
  R2025: trough 2025-04-01..2025-06-30, peak 2025-07-01..2025-09-30   (ETH treasury-company rally)
Inputs: data/processed/npf_series/*.csv ; Outputs: data/processed/rally_analysis.csv
Limitation: 3-day floor bars; floor = cheapest listing (can be spoofed / thin).
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from universe_config import UNIVERSE

W = {
    "R2023": (("2022-11-01", "2023-01-05"), ("2023-01-05", "2023-03-15")),
    "R2024": (("2024-08-01", "2024-10-31"), ("2024-11-01", "2025-01-31")),
    "R2025": (("2025-04-01", "2025-06-30"), ("2025-07-01", "2025-09-30")),
}
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
rows = []
for name, npf, oss, cat in UNIVERSE:
    p = os.path.join(PROC, "npf_series", f"{npf}.csv")
    if not os.path.exists(p):
        continue
    s = pd.read_csv(p, index_col=0, parse_dates=True)
    s = s[s.floorNative > 0]
    r = {"name": name, "category": cat}
    for k, (tr, pk) in W.items():
        a = s.loc[tr[0]:tr[1]]
        b = s.loc[pk[0]:pk[1]]
        if len(a) < 3 or len(b) < 3:
            continue
        for unit, col in [("eth", "floorNative"), ("btc", "floorBtc")]:
            t = a[col].min()
            pk_date = b[col].idxmax()
            pv = b[col].max()
            r[f"{k}_mult_{unit}"] = pv / t
            for d in (90, 180):
                after = s.loc[pk_date + pd.Timedelta(days=d - 4): pk_date + pd.Timedelta(days=d + 4), col]
                r[f"{k}_retain{d}_{unit}"] = (after.mean() / pv) if len(after) else np.nan
        r[f"{k}_peak_date"] = b["floorBtc"].idxmax().date()
    # weekly beta of log floorBtc to log ETH/BTC
    wk = s["floorBtc"].resample("W").last().dropna()
    eb = px["eth_btc"].resample("W").last().reindex(wk.index)
    x = np.log(eb).diff().dropna()
    y = np.log(wk).diff().reindex(x.index).dropna()
    x = x.reindex(y.index)
    if len(y) > 50:
        beta = np.cov(y, x)[0, 1] / np.var(x, ddof=1)
        r["beta_floorbtc_to_ethbtc"] = beta
        r["corr"] = np.corrcoef(y, x)[0, 1]
        r["ann_vol_floorbtc"] = y.std() * np.sqrt(52)
    rows.append(r)
df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "rally_analysis.csv"), index=False)
pd.set_option("display.width", 250)
pd.set_option("display.max_rows", 100)
cols = ["name", "R2023_mult_btc", "R2023_retain180_btc", "R2024_mult_btc", "R2024_retain90_btc",
        "R2024_retain180_btc", "R2025_mult_btc", "R2025_retain90_btc", "R2025_retain180_btc",
        "beta_floorbtc_to_ethbtc", "corr", "ann_vol_floorbtc"]
print(df[cols].round(2).sort_values("R2025_mult_btc", ascending=False).to_string())
print("\nMEDIANS\n", df[cols[1:]].median().round(2))
