"""The 2024–25 cycle as the analog (investor's preferred framing, 2026-10-14).

Analog: BTC bottomed ~$58k in Aug–Sep 2024 and topped at $124,659 on 2025-10-06 (≈2.1×) — close to the investor's
forward hurdle (BTC $83.35k → $180–210k = 2.16–2.52×). NFT euphorias inside the leg: Dec-2024 (post-election,
PENGU/CULT/ANIME token season) and Aug-2025 (ETH all-time high).

Per collection (NFTPriceFloor 3-day bars, outlier-cleaned):
  low window   2024-06-15 → 2024-10-31 (own minimum USD floor)
  exit windows P1 = 2024-11-01 → 2025-01-31 (Dec-2024 euphoria) ; BEST = 2024-11-01 → 2025-10-06 (best euphoria up to
               BTC's top)
Tiers (as in cycle_analysis.py): perfect; rough = entry mean ±45d around own low (clipped to the window), exit mean ±15d
around own peak, −10% costs; blind = entry median of the low window, same exit, −10%.
Metrics: NFT USD multiple; BTC from the entry date to BTC's cycle top (the investor's exact comparison: NFT low→high vs
BTC low→top); NFT÷BTC at the NFT exit (if rotated into BTC); NFT÷ETH.
Token flag: collections whose holders received/anticipated a token in the window (PENGU: Pudgy, Lil Pudgys; CULT:
Milady, Remilio; ANIME: Azuki; DOOD: Doodles).
Outputs: data/processed/cycle2024.csv, cycle2024_summary.csv, cycle2024_forward.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series
from universe_config import UNIVERSE

LOW = ("2024-06-15", "2024-10-31")
EXITS = {"P1_dec2024": ("2024-11-01", "2025-01-31"), "BEST_to_btc_top": ("2024-11-01", "2025-10-06")}
BTC_TOP_DATE = pd.Timestamp("2025-10-06")
TOKEN = {"Pudgy Penguins", "Lil Pudgys", "Milady Maker", "Redacted Remilio Babies", "Azuki", "Doodles"}
FINALISTS = {"Milady Maker", "Redacted Remilio Babies", "CryptoDickbutts", "Pudgy Penguins", "Azuki",
             "Chromie Squiggle", "Terraforms", "V1 CryptoPunks (wrapped)"}
ART = {"historical-pfp", "generative-art", "generative-art-historical", "onchain-art", "historical-art", "historical",
       "art-editions", "artist-pfp", "artist-editions", "onchain-text", "historical-game"}
COST = 0.10
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
BTC_TOP = px.btc_usd.loc[BTC_TOP_DATE]
NOW = {"eth_usd": 2508.69, "btc_usd": 83350.0, "eth_btc": 0.0301}


def run():
    rows = []
    for name, npf, oss, cat in UNIVERSE:
        if not os.path.exists(os.path.join(PROC, "npf_series", f"{npf}.csv")):
            continue
        s = load_series(npf, start="2024-01-01")
        low = s.loc[LOW[0]:LOW[1]]
        if len(low) < 10:
            continue
        ld = low.floorUsd.idxmin()
        for ex, (a, b) in EXITS.items():
            pk = s.loc[max(pd.Timestamp(a), ld):b]
            if len(pk) < 3:
                continue
            pdt = pk.floorUsd.idxmax()
            xw = s.loc[pdt - pd.Timedelta(days=15): pdt + pd.Timedelta(days=15)]
            ew = low.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)]
            r = dict(name=name, group="art/historical" if cat in ART else "PFP", finalist=name in FINALISTS,
                     token=name in TOKEN, exit=ex, low_date=ld.date(), peak_date=pdt.date(),
                     low_usd=low.floorUsd.min(), peak_usd=pk.floorUsd.max(),
                     usd_perfect=pk.floorUsd.max() / low.floorUsd.min(),
                     vs_btc_perfect=pk.floorBtc.max() / low.floorBtc.loc[ld],
                     btc_to_top_perfect=BTC_TOP / px.btc_usd.asof(ld))
            for tier, ent, agg in (("rough", ew, "mean"), ("blind", low, "median")):
                e_usd, e_btc, e_eth = (getattr(ent[c], agg)() for c in ("floorUsd", "floorBtc", "floorNative"))
                r[f"usd_{tier}"] = xw.floorUsd.mean() / e_usd * (1 - COST)
                r[f"vs_btc_{tier}"] = xw.floorBtc.mean() / e_btc * (1 - COST)       # rotate into BTC at exit
                r[f"eth_{tier}"] = xw.floorNative.mean() / e_eth * (1 - COST)
                btc_entry = e_usd / e_btc
                r[f"btc_to_top_{tier}"] = BTC_TOP / btc_entry
                r[f"usd_vs_btc_to_top_{tier}"] = r[f"usd_{tier}"] / r[f"btc_to_top_{tier}"]  # investor's framing
            r["ethbtc_change"] = px.eth_btc.asof(pdt) / px.eth_btc.asof(ld)
            # today vs that cycle (positioning)
            r["now_usd"] = s.floorUsd.iloc[-1]
            r["now_vs_2024_low_usd"] = r["now_usd"] / r["low_usd"]
            r["now_vs_2024_low_eth"] = s.floorNative.iloc[-1] / low.floorNative.loc[ld]
            r["revisit_peak_usd_mult"] = r["peak_usd"] / r["now_usd"]
            rows.append(r)
    return pd.DataFrame(rows)


def summarise(df):
    out = []
    for ex in EXITS:
        for lab, g in [("all", df), ("ex-token", df[~df.token]), ("token-catalyst", df[df.token]),
                       ("PFP", df[df.group == "PFP"]), ("art/historical", df[df.group == "art/historical"]),
                       ("finalists", df[df.finalist])]:
            g = g[g.exit == ex]
            if g.empty:
                continue
            o = {"exit": ex, "sample": lab, "n": len(g), "btc_to_top_rough_median": g.btc_to_top_rough.median(),
                 "ethbtc_change_median": g.ethbtc_change.median()}
            for t in ("perfect", "rough", "blind"):
                o[f"usd_{t}_med"] = g[f"usd_{t}"].median()
            for t in ("rough", "blind"):
                o[f"beat_btc_to_top_{t}"] = (g[f"usd_vs_btc_to_top_{t}"] > 1).mean()
                o[f"beat_btc_rotate_{t}"] = (g[f"vs_btc_{t}"] > 1).mean()
                o[f"usd_ge_2.5_{t}"] = (g[f"usd_{t}"] >= 2.5).mean()
                o[f"eth_{t}_med"] = g[f"eth_{t}"].median()
            out.append(o)
    return pd.DataFrame(out)


def forward(df):
    """Apply each collection's own 2024-cycle NFT/ETH swing (rough) to today, at ETH/BTC scenarios at the NFT exit."""
    g = df[df.exit == "BEST_to_btc_top"]
    rows = []
    for lab, h in [("all", g), ("ex-token", g[~g.token]), ("PFP", g[g.group == "PFP"]),
                   ("art/historical", g[g.group == "art/historical"]), ("finalists", g[g.finalist])]:
        x = h.eth_rough.values
        r = {"sample": lab, "n": len(x), "nft_eth_median": np.median(x)}
        for lv in (0.025, 0.030, 0.035, 0.040, 0.050):
            r[f"P_beat_BTC@{lv}"] = float(np.mean(x * lv / NOW["eth_btc"] > 1))
            r[f"P_2x_BTC@{lv}"] = float(np.mean(x * lv / NOW["eth_btc"] > 2))
        rows.append(r)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = run()
    df.to_csv(os.path.join(PROC, "cycle2024.csv"), index=False)
    sm = summarise(df)
    sm.to_csv(os.path.join(PROC, "cycle2024_summary.csv"), index=False)
    fw = forward(df)
    fw.to_csv(os.path.join(PROC, "cycle2024_forward.csv"), index=False)
    pd.set_option("display.width", 260)
    pd.set_option("display.max_columns", 40)
    print(sm.round(2).to_string())
    print(fw.round(2).T.to_string())
    b = df[df.exit == "BEST_to_btc_top"].sort_values("usd_vs_btc_to_top_rough", ascending=False)
    print(b[["name", "group", "token", "low_date", "peak_date", "usd_perfect", "usd_rough", "btc_to_top_rough",
             "usd_vs_btc_to_top_rough", "vs_btc_rough", "eth_rough", "now_vs_2024_low_usd",
             "revisit_peak_usd_mult"]].round(2).to_string())
