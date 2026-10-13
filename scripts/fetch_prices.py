"""Daily ETH/BTC, BTC/USD, ETH/USD closes from Binance public market data (data-api.binance.vision).

Output: data/processed/prices_daily.csv  (date, eth_btc, btc_usd, eth_usd)
Source: https://data-api.binance.vision/api/v3/klines  (symbols ETHBTC, BTCUSDT, ETHUSDT; 1d; close = UTC 23:59:59)
Limitation: USDT used as USD proxy.
"""
import os
import time
import pandas as pd
from common import get_json, save_raw, PROC

BASE = "https://data-api.binance.vision/api/v3/klines"


def klines(symbol, start_ms=1502928000000):
    rows = []
    cur = start_ms
    while True:
        d = get_json(BASE, {"symbol": symbol, "interval": "1d", "startTime": cur, "limit": 1000})
        if not d:
            break
        rows.extend(d)
        cur = d[-1][0] + 86400000
        if len(d) < 1000:
            break
        time.sleep(0.3)
    save_raw(f"binance/klines_{symbol}_1d.json", rows)
    s = pd.Series({pd.to_datetime(r[0], unit="ms").date(): float(r[4]) for r in rows}, name=symbol)
    return s


if __name__ == "__main__":
    df = pd.concat([klines("ETHBTC"), klines("BTCUSDT"), klines("ETHUSDT")], axis=1)
    df.columns = ["eth_btc", "btc_usd", "eth_usd"]
    df.index.name = "date"
    df.to_csv(os.path.join(PROC, "prices_daily.csv"))
    print(df.tail(3))
    print("rows", len(df))
