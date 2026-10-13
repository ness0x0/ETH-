"""Fetch daily Binance spot klines for collection-linked tokens (PENGU, ANIME).

Writes raw responses to data/raw/binance/klines_<SYMBOL>_1d.json (with fetched_at_utc)
and a tidy CSV data/processed/token_prices_daily.csv (date, symbol, open, high, low, close, quote_volume).
Used by the cultural-research dossiers to describe token price paths with primary exchange data.
Usage: python3 scripts/fetch_token_klines.py
"""
import csv
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import PROC, get_json, save_raw  # noqa: E402

SYMBOLS = ["PENGUUSDT", "ANIMEUSDT"]
URL = "https://data-api.binance.vision/api/v3/klines"


def fetch(symbol):
    out, start = [], 0
    while True:
        batch = get_json(URL, {"symbol": symbol, "interval": "1d", "limit": 1000, "startTime": start})
        if not batch:
            break
        out.extend(batch)
        if len(batch) < 1000:
            break
        start = batch[-1][0] + 1
    return out


def main():
    rows = []
    for s in SYMBOLS:
        k = fetch(s)
        save_raw(f"binance/klines_{s}_1d.json", k)
        for r in k:
            d = dt.datetime.fromtimestamp(r[0] / 1000, dt.timezone.utc).date().isoformat()
            rows.append([d, s, r[1], r[2], r[3], r[4], r[7]])
    path = os.path.join(PROC, "token_prices_daily.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "symbol", "open", "high", "low", "close", "quote_volume_usdt"])
        w.writerows(rows)
    print(path, len(rows))


if __name__ == "__main__":
    main()
