"""Midterm-year check (investor question, 2026-10-16): has on-chain euphoria ever happened in a US-midterm year
(2018, 2022, 2026)? Uses prices_daily.csv (Binance, from 2017-08), sector_activity_monthly.csv (NPF universe volume,
from 2022-06), punks_weekly.csv and cycleA_summary.csv. 2014 predates the data (and Ethereum).
"""
import os
import pandas as pd
from common import PROC

p = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
qr = p.btc_usd.resample("QE").last().pct_change()
for y in (2018, 2019, 2022, 2023, 2026):
    print(y, "BTC by quarter:", [f"{v:+.0%}" for v in qr.loc[str(y)].values])
for a, b in (("2018-01-01", "2019-06-30"), ("2022-01-01", "2023-06-30"), ("2025-10-07", "2026-12-31")):
    s = p.btc_usd.loc[a:b]
    print(f"BTC low in window from {a}: {s.idxmin().date()} ${s.min():,.0f}")
v = pd.read_csv(os.path.join(PROC, "sector_activity_monthly.csv"), index_col=0, parse_dates=True).volumeUsd / 1e6
print("NFT universe volume by quarter ($M):", {str(k.date())[:7]: round(x) for k, x in v.resample("QE").sum().items()})
c = pd.read_csv(os.path.join(PROC, "cycleA_summary.csv"))
pk = pd.to_datetime(c.peak_date)
print(f"2021-22 sampled collections peaking Jan-Apr 2022: {((pk >= '2022-01-01') & (pk <= '2022-04-30')).sum()} of {len(c)}")
