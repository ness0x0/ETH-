"""Load NFTPriceFloor 3-day series with single-bar outlier removal.

A bar is treated as a glitch when it deviates >35% from the centred 5-bar median while its two neighbours agree
with each other within 15% (e.g., Pudgy 2024-05-11: 5.74 ETH between ~11 ETH bars) *and* the bar's sales count is not elevated — one-bar crashes with heavy sales are real
flash crashes (bid dumps/liquidations) and are kept. Glitch bars are replaced by
the previous bar's value. Bars before 2022-06-01 are dropped (provider glitches).
"""
import os
import numpy as np
import pandas as pd
from common import PROC


def load_series(slug, start="2022-06-01"):
    s = pd.read_csv(os.path.join(PROC, "npf_series", f"{slug}.csv"), index_col=0, parse_dates=True)
    s = s[(s.floorNative > 0) & (s.index >= start)].copy()
    f = s["floorNative"]
    med = f.rolling(5, center=True, min_periods=3).median()
    prev, nxt = f.shift(1), f.shift(-1)
    neighbours_agree = (prev / nxt - 1).abs() < 0.15
    sc = s["salesCount"]
    normal_volume = sc <= 1.5 * ((sc.shift(1) + sc.shift(-1)) / 2 + 5)
    # Spikes with elevated sales are kept: they are real flash crashes (bid dumps / liquidations), not glitches.
    glitch = ((f / med - 1).abs() > 0.35) & neighbours_agree & normal_volume
    s["glitch"] = glitch
    for col in ("floorNative", "floorUsd", "floorBtc"):
        s.loc[glitch, col] = np.nan
        s[col] = s[col].ffill()
    return s
