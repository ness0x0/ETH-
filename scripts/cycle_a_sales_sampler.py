"""Cycle A (2020 → mid-2022) floor proxies from sampled OpenSea sales, where NFTPriceFloor has no coverage.

Source  : OpenSea API v2 GET /api/v2/events/collection/{slug}?event_type=sale&after=&before=&limit=50 (free key,
          stored outside the repo). OpenSea carried the large majority of ETH NFT volume in 2021–H1 2022 (Blur launched
          Oct-2022), so sale prices there are representative for the period.
Method  : every 7 days, take a 48-hour window and fetch one page (≤50 most recent sales in the window). Keep sales
          paid in ETH/WETH. Floor proxy = 10th percentile of single-item sale prices in the window (requires ≥5
          sales; otherwise NaN). Also record median price and sale count. 10th percentile of executed sales is a
          lower-variance, executable proxy for the listing floor; it can sit slightly above the true floor.
Output  : data/raw/opensea_events_cycleA/<slug>.json (raw events, compact), data/processed/cycleA_weekly.csv
Limits  : 600 reads/hour on the free key → sleep 6.2s/request. Resumable (skips windows already fetched).
"""
import datetime as dt
import json
import os
import sys
import time

import numpy as np
import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RAW, PROC  # noqa: E402

KEY = json.load(open("/root/.config/ethnft/opensea_key.json"))["api_key"]
H = {"x-api-key": KEY, "accept": "application/json"}
OUTDIR = os.path.join(RAW, "opensea_events_cycleA")
os.makedirs(OUTDIR, exist_ok=True)
END = dt.datetime(2022, 6, 15, tzinfo=dt.timezone.utc)
# slug: first sample date (≈ collection start or 2020-10 for older collections)
COLS = {
    "chromie-squiggle-by-snowfro": dt.datetime(2020, 12, 1, tzinfo=dt.timezone.utc),
    "milady": dt.datetime(2021, 8, 25, tzinfo=dt.timezone.utc),
    "pudgypenguins": dt.datetime(2021, 7, 25, tzinfo=dt.timezone.utc),
    "cryptodickbutts-s3": dt.datetime(2021, 7, 30, tzinfo=dt.timezone.utc),
    "boredapeyachtclub": dt.datetime(2021, 5, 1, tzinfo=dt.timezone.utc),
    "meebits": dt.datetime(2021, 5, 5, tzinfo=dt.timezone.utc),
    "hashmasks": dt.datetime(2021, 2, 1, tzinfo=dt.timezone.utc),
    "cool-cats-nft": dt.datetime(2021, 7, 5, tzinfo=dt.timezone.utc),
    "doodles-official": dt.datetime(2021, 10, 20, tzinfo=dt.timezone.utc),
    "azuki": dt.datetime(2022, 1, 15, tzinfo=dt.timezone.utc),
    "terraforms": dt.datetime(2021, 12, 20, tzinfo=dt.timezone.utc),
    "mutant-ape-yacht-club": dt.datetime(2021, 9, 1, tzinfo=dt.timezone.utc),
}


def fetch(slug, a, b):
    for i in range(6):
        try:
            r = requests.get(f"https://api.opensea.io/api/v2/events/collection/{slug}",
                             params={"event_type": "sale", "after": a, "before": b, "limit": 50}, headers=H, timeout=60)
            time.sleep(6.2)
            if r.status_code == 429:
                time.sleep(60 * (i + 1))
                continue
            r.raise_for_status()
            return r.json().get("asset_events", [])
        except Exception as e:  # noqa
            time.sleep(20 * (i + 1))
    return None


def compact(e):
    p = e.get("payment") or {}
    return dict(ts=e.get("event_timestamp"), q=p.get("quantity"), sym=p.get("symbol"), dec=p.get("decimals"),
                n=e.get("quantity", 1), tok=(e.get("nft") or {}).get("identifier"), tx=e.get("transaction"))


def main(only=None):
    for slug, start in COLS.items():
        if only and slug not in only:
            continue
        path = os.path.join(OUTDIR, f"{slug}.json")
        store = json.load(open(path)) if os.path.exists(path) else {}
        t = start
        while t < END:
            key = t.strftime("%Y-%m-%d")
            if key not in store:
                a = int(t.timestamp())
                ev = fetch(slug, a, a + 2 * 86400)
                if ev is not None:
                    store[key] = [compact(e) for e in ev]
                    json.dump(store, open(path, "w"))
            t += dt.timedelta(days=7)
        print(slug, "windows", len(store), flush=True)


def build():
    rows = []
    for slug in COLS:
        path = os.path.join(OUTDIR, f"{slug}.json")
        if not os.path.exists(path):
            continue
        for key, evs in json.load(open(path)).items():
            px = []
            for e in evs:
                if e["sym"] not in ("ETH", "WETH") or not e["q"]:
                    continue
                n = int(e.get("n") or 1)
                if n != 1:
                    continue
                px.append(float(e["q"]) / 10 ** int(e["dec"] or 18))
            px = [p for p in px if p > 0]
            if px:  # drop zero/near-zero transfers recorded as sales (gifts, wash, mispriced bundles)
                med = float(np.median(px))
                px = [p for p in px if p >= 0.2 * med]
            rows.append(dict(slug=slug, date=key, n_sales=len(px),
                             floor_proxy_p10=float(np.quantile(px, 0.10)) if len(px) >= 5 else np.nan,
                             median=float(np.median(px)) if px else np.nan))
    df = pd.DataFrame(rows).sort_values(["slug", "date"])
    df.to_csv(os.path.join(PROC, "cycleA_weekly.csv"), index=False)
    return df


if __name__ == "__main__":
    if "--build" in sys.argv:
        print(build().groupby("slug").floor_proxy_p10.describe().round(3))
    else:
        main([a for a in sys.argv[1:] if not a.startswith("--")] or None)
        build()
