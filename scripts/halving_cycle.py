"""Halving-cycle trade, phase-matched (investor's clarified strategy, 2026-10-14).

Strategy: buy in the bear ~18 months before a halving, hold through the quiet stretch, sell into the on-chain
euphoria of the halving / post-halving years, rotate the proceeds into BTC.
Analog: today (Oct-2026) is ~18 months before the expected Apr-2028 halving; Oct-2022 was ~18 months before the
Apr-2024 halving. So: entry in 2022, exit in the 2024-25 euphorias.

Entries (BTC-terms floor, NFTPriceFloor 3-day bars, outlier-cleaned):
  phase  mean floor in Oct-2022 (same point in the halving cycle as today; no knowledge of the low)
  bear   median floor Jun-Dec 2022 (anywhere in the bear year)
  low    mean floor +-45 days around the collection's own 2022-23 low (needs luck/skill; as in section B2)
Exits (each window's mean floor, i.e. scaling out through the euphoria; no knowledge of the peak date):
  ETF    2024-02-01..2024-03-31 (halving year, pre-halving)
  TOK    2024-11-01..2025-01-31 (halving year, post-election / token season)
  ETHATH 2025-07-01..2025-09-30 (post-halving year, ETH all-time high)
  ladder one third in each window (no hindsight about which euphoria is biggest)
  best   the best of the three windows (hindsight on the window, not the day)
  target list at 2x vs BTC net of costs from 2023-11-01; first floor touch fills; otherwise sell in ETHATH
Every exit rotates into BTC; 10% round-trip costs. Result = NFT/BTC multiple. With BTC doing 2x entry->top,
NFT/BTC >= 2 means >= 4x in dollars.
Forward: each collection's NFT/ETH ladder multiple applied to today's ETH/BTC (0.0301) at scenario ETH/BTC levels.
Outputs: data/processed/halving_cycle.csv, halving_cycle_summary.csv, halving_cycle_forward.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series
from universe_config import UNIVERSE

ENTRY = {"phase": ("2022-10-01", "2022-10-31", "mean"), "bear": ("2022-06-15", "2022-12-31", "median")}
LOW_WIN = ("2022-06-15", "2023-10-31")
EXITS = {"ETF": ("2024-02-01", "2024-03-31"), "TOK": ("2024-11-01", "2025-01-31"), "ETHATH": ("2025-07-01", "2025-09-30")}
TARGET_FROM, COST, NOW_ETHBTC = "2023-11-01", 0.10, 0.0301


def run():
    sm = pd.read_csv(os.path.join(PROC, "screen_metrics.csv")).set_index("name")
    rows = []
    for name, npf, _, cat in UNIVERSE:
        if not os.path.exists(os.path.join(PROC, "npf_series", f"{npf}.csv")):
            continue
        s = load_series(npf, start="2022-06-15")
        if s.loc[ENTRY["phase"][0]:ENTRY["phase"][1]].empty or s.loc[EXITS["ETHATH"][0]:EXITS["ETHATH"][1]].empty:
            continue
        low = s.loc[LOW_WIN[0]:LOW_WIN[1]]
        ld = low.floorUsd.idxmin()
        ent = {k: getattr(s.loc[a:b], agg)() for k, (a, b, agg) in ENTRY.items()}
        ent["low"] = low.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)].mean()
        xb = {k: s.loc[a:b].floorBtc.mean() for k, (a, b) in EXITS.items()}
        xe = {k: s.loc[a:b].floorNative.mean() for k, (a, b) in EXITS.items()}
        supply = sm.loc[name, "supply"] if name in sm.index else np.nan
        path = s.floorBtc.loc[TARGET_FROM:EXITS["ETHATH"][1]]
        for tier, e in ent.items():
            r = dict(name=name, category=cat, pfp="pfp" in cat, entry=tier,
                     cap_at_entry_usd_m=e.floorUsd * supply / 1e6)
            for k in EXITS:
                r[f"vs_btc_{k}"] = xb[k] / e.floorBtc * (1 - COST)
            r["vs_btc_ladder"] = np.mean([r[f"vs_btc_{k}"] for k in EXITS])
            r["vs_btc_best"] = max(r[f"vs_btc_{k}"] for k in EXITS)
            r["eth_ladder"] = np.mean([xe[k] / e.floorNative for k in EXITS]) * (1 - COST)
            hit = path[path >= 2 / (1 - COST) * e.floorBtc]
            r["target_hit"] = not hit.empty
            r["target_hit_date"] = hit.index[0].date() if not hit.empty else None
            r["vs_btc_target"] = 2.0 if not hit.empty else r["vs_btc_ETHATH"]
            rows.append(r)
    return pd.DataFrame(rows)


def summarise(df):
    out = []
    for tier, g in df.groupby("entry", sort=False):
        for lab, h in (("all", g), ("PFP", g[g.pfp]), ("art/historical", g[~g.pfp]),
                       ("cap<$10M at entry", g[g.cap_at_entry_usd_m < 10]),
                       ("cap>=$50M at entry", g[g.cap_at_entry_usd_m >= 50])):
            o = dict(entry=tier, sample=lab, n=len(h))
            for x in ("ETF", "TOK", "ETHATH", "ladder", "best", "target"):
                v = h[f"vs_btc_{x}"]
                o[f"{x}_beat"] = (v > 1).mean()
                o[f"{x}_ge2"] = (v >= 2).mean()
                o[f"{x}_median"] = v.median()
            out.append(o)
    return pd.DataFrame(out)


def forward(df):
    rows = []
    for tier, g in df.groupby("entry", sort=False):
        for lab, h in (("all", g), ("PFP", g[g.pfp]), ("cap<$10M at entry", g[g.cap_at_entry_usd_m < 10])):
            x = h.eth_ladder.values
            r = dict(entry=tier, sample=lab, n=len(x), nft_eth_ladder_median=np.median(x))
            for lv in (0.025, 0.030, 0.035, 0.040):
                r[f"beat@{lv}"] = float(np.mean(x * lv / NOW_ETHBTC > 1))
                r[f"ge2@{lv}"] = float(np.mean(x * lv / NOW_ETHBTC >= 2))
            rows.append(r)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 40)
    df = run()
    df.to_csv(os.path.join(PROC, "halving_cycle.csv"), index=False)
    sm = summarise(df)
    sm.to_csv(os.path.join(PROC, "halving_cycle_summary.csv"), index=False)
    fw = forward(df)
    fw.to_csv(os.path.join(PROC, "halving_cycle_forward.csv"), index=False)
    print(sm.round(2).to_string())
    print(fw.round(2).to_string())
    g = df[df.entry == "phase"].sort_values("vs_btc_ladder", ascending=False)
    print(g[["name", "pfp", "cap_at_entry_usd_m", "vs_btc_ETF", "vs_btc_TOK", "vs_btc_ETHATH", "vs_btc_ladder",
             "vs_btc_best", "target_hit", "eth_ladder"]].round(2).to_string())
