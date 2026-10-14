"""Cycle-low → euphoria-high analysis (investor's framing, 2026-10-14).

Question: if NFTs are bought near a cycle low and sold into the next on-chain euphoria, how often does that beat
BTC — over the same window, and against the investor's hurdle of BTC going 2.0–2.5× from $83k to its cycle top?

Cycle B (2022 → 2025, NFTPriceFloor 3-day bars, 37 collections with history from mid-June 2022): four NFT euphoria
episodes identified from the equal-weight sector index (USD terms) turning points:
  E1 Blur season       low window 2022-09-01..2022-12-31  → peak window 2023-01-01..2023-03-31
  E2 ETF season        low window 2023-08-01..2023-11-15  → peak window 2023-11-16..2024-04-15
  E3 Election/tokens   low window 2024-06-15..2024-10-31  → peak window 2024-11-01..2025-01-31
  E4 ETH-ATH season    low window 2025-03-01..2025-06-30  → peak window 2025-07-01..2025-09-30
  BIG  full cycle      low window 2022-06-15..2023-10-31  → peak window 2023-11-01..2025-10-31
Per collection and episode:
  perfect   : buy at own minimum USD floor in the low window, sell at own max USD floor in the peak window (after low)
  rough     : buy at the mean floor within ±45 days of own low (the investor's premise: roughly identify the low);
              sell at the mean floor within ±15 days of own peak (the euphoric month, not the top bar); −10% costs
  blind     : buy at the MEDIAN floor of the whole low window (no idea where the bottom is); same exit; −10% costs
Metrics: USD multiple; BTC's USD multiple between the same dates; BTC-terms multiple (= NFT/BTC; >1 means it beat
holding BTC over that window, i.e. selling into the euphoria and rotating back into BTC); ETH-terms multiple.
Outputs: data/processed/cycle_episodes.csv (per collection × episode), cycle_episode_summary.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series
from universe_config import UNIVERSE

EP = {
    "E1_2023_blur": (("2022-09-01", "2022-12-31"), ("2023-01-01", "2023-03-31")),
    "E2_2024_etf": (("2023-08-01", "2023-11-15"), ("2023-11-16", "2024-04-15")),
    "E3_2024_tokens": (("2024-06-15", "2024-10-31"), ("2024-11-01", "2025-01-31")),
    "E4_2025_eth_ath": (("2025-03-01", "2025-06-30"), ("2025-07-01", "2025-09-30")),
    "BIG_2022_2025": (("2022-06-15", "2023-10-31"), ("2023-11-01", "2025-10-31")),
}
FINALISTS = {"Milady Maker", "Redacted Remilio Babies", "CryptoDickbutts", "Pudgy Penguins", "Azuki",
             "Chromie Squiggle", "Terraforms", "V1 CryptoPunks (wrapped)"}
COST = 0.10
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)


def p_at(col, d):
    return px[col].asof(pd.Timestamp(d))


def main():
    rows = []
    for name, npf, oss, cat in UNIVERSE:
        if not os.path.exists(os.path.join(PROC, "npf_series", f"{npf}.csv")):
            continue
        s = load_series(npf, start="2022-06-15")
        for ep, (lw, pw) in EP.items():
            low = s.loc[lw[0]:lw[1]]
            if len(low) < 5 or s.index[0] > pd.Timestamp(lw[0]) + pd.Timedelta(days=10):
                continue
            ld = low.floorUsd.idxmin()
            peak = s.loc[max(pd.Timestamp(pw[0]), ld):pw[1]]
            if len(peak) < 3:
                continue
            pd_ = peak.floorUsd.idxmax()
            r = dict(name=name, category=cat, finalist=name in FINALISTS, episode=ep, low_date=ld.date(),
                     peak_date=pd_.date())
            # perfect timing
            r["usd_perfect"] = peak.floorUsd.max() / low.floorUsd.min()
            r["eth_perfect"] = s.floorNative[pd_] / s.floorNative[ld]
            r["btcusd_mult_perfect"] = p_at("btc_usd", pd_) / p_at("btc_usd", ld)
            r["vs_btc_perfect"] = r["usd_perfect"] / r["btcusd_mult_perfect"]
            # exit for both non-perfect tiers: mean floor within ±15 days of own peak ("sold into the euphoric month")
            xw = s.loc[pd_ - pd.Timedelta(days=15): pd_ + pd.Timedelta(days=15)]
            # ROUGH timing (investor's premise: roughly identify the low): entry = mean floor within ±45 days of own
            # low, clipped to the low window
            ew = low.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)]
            # BLIND timing: entry = median floor of the whole low window (no idea where the bottom is)
            for tier, ent in (("rough", ew), ("blind", low)):
                agg = (lambda c: ent[c].mean()) if tier == "rough" else (lambda c: ent[c].median())
                r[f"usd_{tier}"] = xw.floorUsd.mean() / agg("floorUsd") * (1 - COST)
                r[f"vs_btc_{tier}"] = xw.floorBtc.mean() / agg("floorBtc") * (1 - COST)
                r[f"eth_{tier}"] = xw.floorNative.mean() / agg("floorNative") * (1 - COST)
                r[f"btcusd_mult_{tier}"] = r[f"usd_{tier}"] / r[f"vs_btc_{tier}"]
            r["ethbtc_change"] = p_at("eth_btc", pd_) / p_at("eth_btc", ld)
            r["days_low_to_peak"] = (pd_ - ld).days
            rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(PROC, "cycle_episodes.csv"), index=False)

    def summ(g):
        o = {"n": len(g), "btc_usd_mult_perfect": g.btcusd_mult_perfect.median(),
             "ethbtc_change": g.ethbtc_change.median()}
        for tier in ("perfect", "rough", "blind"):
            o[f"usd_{tier}_median"] = g[f"usd_{tier}"].median()
            o[f"vs_btc_{tier}_median"] = g[f"vs_btc_{tier}"].median()
            o[f"share_beat_btc_{tier}"] = (g[f"vs_btc_{tier}"] > 1).mean()
            o[f"share_vs_btc_ge_1.5_{tier}"] = (g[f"vs_btc_{tier}"] >= 1.5).mean()
            o[f"eth_{tier}_median"] = g[f"eth_{tier}"].median()
        return pd.Series(o)
    out = df.groupby("episode").apply(summ)
    fin = df[df.finalist].groupby("episode").apply(summ).add_prefix("fin_")
    res = pd.concat([out, fin[["fin_n", "fin_vs_btc_rough_median", "fin_share_beat_btc_rough", "fin_usd_rough_median"]]], axis=1)
    res.to_csv(os.path.join(PROC, "cycle_episode_summary.csv"))
    return df, res


if __name__ == "__main__":
    df, res = main()
    pd.set_option("display.width", 250)
    print(res.round(2).T.to_string())
    for tier in ("rough", "blind"):
        print(f"\nFinalists, {tier}-timing multiple vs BTC (−10% costs)")
        print(df[df.finalist].pivot_table(index="name", columns="episode", values=f"vs_btc_{tier}").round(2).to_string())
