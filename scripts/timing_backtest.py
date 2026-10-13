"""Does an ETH/BTC trend filter improve BTC-relative outcomes for ETH-NFT exposure? (2022-06 → 2026-10)

Weekly series: EW sector floor index (BTC terms) and finalist floors (BTC terms, NFTPriceFloor 3-day bars).
Strategy HOLD: always long the NFT floor.  Strategy TREND: long only when ETH/BTC weekly close > its N-week moving
average; otherwise in BTC. Each switch in/out costs a round-trip haircut c (applied half on entry, half on exit).
Output: BTC-terms terminal multiple, number of round trips. Floors are not executable prices; costs approximate.
Output file: data/processed/timing_backtest.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series

px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
eb = px["eth_btc"].resample("W").last()
sec = pd.read_csv(os.path.join(PROC, "sector_index.csv"), index_col=0, parse_dates=True)["ew_floor_btc"]
assets = {"sector_EW": sec.resample("W").last()}
for k, slug in [("milady", "milady"), ("pudgy", "pudgy-penguins"), ("chromie_squiggle", "chromie-squiggle-art-blocks-curated"),
                ("terraforms", "terraforms-by-mathcastles"), ("v1punks", "v1-cryptopunks-wrapped"),
                ("azuki", "azuki"), ("cryptodickbutts", "cryptodickbutts")]:
    assets[k] = load_series(slug)["floorBtc"].resample("W").last()
COST = {"sector_EW": 0.12, "milady": 0.10, "pudgy": 0.08, "chromie_squiggle": 0.25, "terraforms": 0.20,
        "v1punks": 0.12, "azuki": 0.12, "cryptodickbutts": 0.25}
rows = []
for k, s in assets.items():
    s = s.dropna()
    s = s[s.index >= "2022-07-01"]
    for n in (10, 20, 30):
        ma = eb.rolling(n).mean()
        sig = (eb > ma).reindex(s.index).shift(1).fillna(False)  # act on last week's signal
        r = s.pct_change().fillna(0)
        c = COST[k]
        val, inpos, trips = 1.0, False, 0
        for t in s.index:
            if sig[t] and not inpos:
                val *= (1 - c / 2); inpos = True; trips += 1
            elif not sig[t] and inpos:
                val *= (1 - c / 2); inpos = False
            if inpos:
                val *= (1 + r[t])
        hold = s.iloc[-1] / s.iloc[0] * (1 - c)
        rows.append(dict(asset=k, ma_weeks=n, hold_btc_multiple=round(hold, 3), trend_btc_multiple=round(val, 3),
                         round_trips=trips, pct_time_in=round(sig.mean(), 2), cost=c))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "timing_backtest.csv"), index=False)
print(df.to_string())
