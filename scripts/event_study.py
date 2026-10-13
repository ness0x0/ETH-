"""Catalyst event study.

For each dated catalyst in data/processed/catalysts/*.csv, measure the collection's floor before and ~30/90/180
days after, in ETH and BTC terms, and the *abnormal* BTC-relative change versus the equal-weight sector index
(data/processed/sector_index.csv). Also compares trading activity (sales/day) 30 days before vs 30 days after.

Baseline = last 3-day bar strictly before (event_date - 1d). Post value = mean of bars within +/-6 days of the
horizon (smooths single-bar noise). Events before NFTPriceFloor coverage (~May 2022) are reported as n/a.

Inputs: catalysts CSVs (date,collection,event,category,...), npf_series, sector_index.csv
Output: data/processed/event_study.csv
"""
import glob
import os
import numpy as np
import pandas as pd
from common import PROC

SLUG = {  # catalyst file stem -> NFTPriceFloor slug
    "milady": "milady", "remilio": "remilio-babies", "cryptodickbutts": "cryptodickbutts",
    "pudgy": "pudgy-penguins", "azuki": "azuki", "moonbirds": "proof-moonbirds",
    "chromie_squiggle": "chromie-squiggle-art-blocks-curated", "terraforms": "terraforms-by-mathcastles",
    "v1punks": "v1-cryptopunks-wrapped",
}
sector = pd.read_csv(os.path.join(PROC, "sector_index.csv"), index_col=0, parse_dates=True)["ew_floor_btc"]


def val(s, d, col, win=6):
    sub = s.loc[d - pd.Timedelta(days=win): d + pd.Timedelta(days=win), col]
    return sub.mean() if len(sub) else np.nan


def base(s, d, col):
    sub = s.loc[: d - pd.Timedelta(days=1), col].dropna()
    return sub.iloc[-1] if len(sub) else np.nan


def sector_at(d):
    sub = sector.loc[:d]
    return sub.iloc[-1] if len(sub) else np.nan


rows = []
for f in sorted(glob.glob(os.path.join(PROC, "catalysts", "*.csv"))):
    stem = os.path.basename(f)[:-4]
    slug = SLUG.get(stem)
    if not slug:
        continue
    s = pd.read_csv(os.path.join(PROC, "npf_series", f"{slug}.csv"), index_col=0, parse_dates=True)
    s = s[s.floorNative > 0]
    cat = pd.read_csv(f)
    for _, e in cat.iterrows():
        try:
            d = pd.Timestamp(str(e["date"])[:10])
        except Exception:  # noqa
            continue
        r = {"file": stem, "date": d.date(), "event": e.get("event"), "category": e.get("category")}
        if d < s.index[0] + pd.Timedelta(days=3) or d > s.index[-1]:
            r["note"] = "outside NPF coverage"
            rows.append(r)
            continue
        b_eth, b_btc = base(s, d, "floorNative"), base(s, d, "floorBtc")
        sb = sector_at(d - pd.Timedelta(days=1))
        r["floor_eth_before"] = b_eth
        pre = s.loc[d - pd.Timedelta(days=30): d - pd.Timedelta(days=1), "salesCount"].sum() / 30
        post = s.loc[d: d + pd.Timedelta(days=30), "salesCount"].sum() / 30
        r["sales_per_day_30d_before"] = pre
        r["sales_per_day_30d_after"] = post
        for h in (30, 90, 180):
            t = d + pd.Timedelta(days=h)
            if t > s.index[-1] + pd.Timedelta(days=3):
                continue
            ve, vb = val(s, t, "floorNative"), val(s, t, "floorBtc")
            r[f"eth_{h}d"] = ve / b_eth - 1
            r[f"btc_{h}d"] = vb / b_btc - 1
            r[f"abn_btc_{h}d"] = (vb / b_btc) / (sector_at(t) / sb) - 1 if sb == sb else np.nan
        # peak within 90d after event (BTC terms) — how much upside an exit-disciplined holder could capture
        w = s.loc[d: d + pd.Timedelta(days=90), "floorBtc"]
        if len(w):
            r["max_btc_within_90d"] = w.max() / b_btc - 1
            r["days_to_peak"] = (w.idxmax() - d).days
        rows.append(r)

df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "event_study.csv"), index=False)
pd.set_option("display.width", 250)
pd.set_option("display.max_colwidth", 60)
pd.set_option("display.max_rows", 300)
cols = ["file", "date", "category", "event", "floor_eth_before", "btc_30d", "btc_90d", "btc_180d", "abn_btc_90d",
        "max_btc_within_90d", "sales_per_day_30d_before", "sales_per_day_30d_after"]
print(df[[c for c in cols if c in df.columns]].round(2).to_string())
