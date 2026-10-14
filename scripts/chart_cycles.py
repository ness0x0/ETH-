"""Cycle charts for the investor's framing.
1) reports/charts/cycles_overview.png — three stacked panels sharing the time axis (no dual axes):
   CryptoPunks floor in USD (on-chain weekly p10, 2019→2022; NFTPriceFloor 2022→), the NFT sector EW floor index in
   USD (2022-06-15 = 1), and BTC in USD; NFT euphoria windows shaded.
2) reports/charts/cycleB_low_to_high_vs_btc.png — each collection's cycle-low → best-euphoria multiple vs BTC
   (rough timing, −10% costs), coloured by collection type.
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter, NullFormatter
from matplotlib.patches import Patch
from common import PROC, ROOT
from npf_utils import load_series

SURF, INK, INK2, GRID, NEUTRAL = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#8a8985"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
EUPH = [("2021-08-01", "2021-10-31", "2021 OG/PFP mania"), ("2022-01-01", "2022-04-30", "2022 blue-chip peak"),
        ("2023-01-01", "2023-03-15", "Blur"), ("2024-02-01", "2024-03-31", "ETF"),
        ("2024-11-15", "2025-01-15", "Tokens"), ("2025-07-15", "2025-09-15", "ETH ATH")]
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)


def logfmt(ax, axis="y"):
    a = ax.yaxis if axis == "y" else ax.xaxis
    a.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.6g}"))
    a.set_minor_formatter(NullFormatter())


def style(ax):
    ax.set_facecolor(SURF)
    ax.grid(color=GRID, lw=0.6, which="both")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(NEUTRAL)
    ax.tick_params(colors=INK2, labelsize=8)


def overview():
    pw = pd.read_csv(os.path.join(PROC, "punks_weekly.csv"), index_col=0, parse_dates=True)
    pw = pw.loc["2019-01-01":"2022-06-14", "floor_proxy_p10"].dropna()
    pw_usd = pw * px["eth_usd"].reindex(pw.index, method="ffill")
    pn = load_series("cryptopunks", start="2022-06-15").floorUsd
    sec = pd.read_csv(os.path.join(PROC, "sector_index_usd_weekly.csv"), index_col=0, parse_dates=True)
    fig, ax = plt.subplots(3, 1, figsize=(12, 9), sharex=True, facecolor=SURF,
                           gridspec_kw={"height_ratios": [1.4, 1.4, 1.1]})
    for a in ax:
        style(a)
        for s, e, lab in EUPH:
            a.axvspan(pd.Timestamp(s), pd.Timestamp(e), color=C4, alpha=0.18, lw=0)
    ax[0].plot(pw_usd.index, pw_usd, color=C1, lw=1.6)
    ax[0].plot(pn.index, pn, color=C1, lw=1.6)
    ax[0].set_yscale("log")
    logfmt(ax[0])
    ax[0].set_ylabel("CryptoPunks floor, USD", color=INK2)
    ax[0].set_title("NFT euphorias (shaded) vs BTC — CryptoPunks floor, sector index, BTC (log scales)",
                    loc="left", color=INK)
    for i, (s, e, lab) in enumerate(EUPH):
        ax[0].text(pd.Timestamp(s), pw_usd.max() * (2.2 if i % 2 == 0 else 0.9), lab, fontsize=7,
                   color=INK2, va="top")
    ax[1].plot(sec.index, sec.nft_usd, color=C2, lw=1.8)
    ax[1].axhline(1, color=INK2, lw=0.7)
    ax[1].set_yscale("log")
    logfmt(ax[1])
    ax[1].set_yticks([0.3, 0.4, 0.6, 1.0, 1.5])
    ax[1].set_ylabel("NFT sector index, USD\n(37 collections, 2022-06-15 = 1)", color=INK2)
    b = px.loc["2019-01-01":, "btc_usd"]
    ax[2].plot(b.index, b, color=NEUTRAL, lw=1.6)
    ax[2].set_yscale("log")
    logfmt(ax[2])
    ax[2].set_ylabel("BTC, USD", color=INK2)
    ax[2].xaxis.set_major_locator(mdates.YearLocator())
    ax[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.text(0.01, 0.005, "Sources: CryptoPunks PunkBought events (on-chain, weekly 10th-percentile sale price) to "
             "2022-06; NFTPriceFloor 3-day floors after; Binance BTCUSDT.\nShading = NFT euphoria windows used in "
             "reports/cycle_analysis.md. The sector index starts 2022-06 (no earlier coverage).",
             fontsize=7.2, color=INK2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(os.path.join(ROOT, "reports", "charts", "cycles_overview.png"), dpi=125, facecolor=SURF)
    plt.close(fig)


def distribution():
    d = pd.read_csv(os.path.join(PROC, "cycle_episodes.csv"))
    b = d[d.episode == "BIG_2022_2025"].sort_values("vs_btc_rough")
    grp = {"historical-pfp": "Historical / art", "generative-art": "Historical / art",
           "generative-art-historical": "Historical / art", "onchain-art": "Historical / art",
           "historical-art": "Historical / art", "historical": "Historical / art", "art-editions": "Historical / art",
           "artist-pfp": "Historical / art", "artist-editions": "Historical / art", "onchain-text": "Historical / art",
           "pfp-brand": "Brand PFP (operator-run)", "pfp-dao": "Brand PFP (operator-run)",
           "pfp-meme-culture": "Meme / culture PFP", "pfp": "Other PFP", "onchain-pfp": "Other PFP"}
    col = {"Historical / art": C1, "Brand PFP (operator-run)": C2, "Meme / culture PFP": C3, "Other PFP": C4}
    g = b.category.map(grp).fillna("Other PFP")
    fig, ax = plt.subplots(figsize=(10, 10), facecolor=SURF)
    style(ax)
    ax.barh(range(len(b)), b.vs_btc_rough, color=[col[x] for x in g], height=0.72)
    ax.axvline(1, color=INK, lw=1)
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}×"))
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.set_yticks(range(len(b)))
    ax.set_yticklabels(b.name, fontsize=8, color=INK)
    for i, v in enumerate(b.vs_btc_rough):
        ax.text(v * 1.06, i, f"{v:.2f}×", va="center", fontsize=7, color=INK2)
    ax.set_xlabel("NFT ÷ BTC from the 2022-23 cycle low to the best 2023-25 euphoria (rough timing, −10% costs)",
                  color=INK2, fontsize=8.5)
    ax.set_title(f"Cycle B: {(b.vs_btc_rough > 1).sum()} of {len(b)} collections beat BTC buying near the low and "
                 "selling in the euphoric month", loc="left", color=INK, fontsize=10.5)
    ax.legend(handles=[Patch(color=c, label=k) for k, c in col.items()], loc="lower right", fontsize=8, frameon=False)
    fig.text(0.01, 0.005, "Entry = mean floor ±45 days around each collection's 2022-06→2023-10 low; exit = mean floor "
             "±15 days around its highest 2023-11→2025-10 floor.\nSource: NFTPriceFloor, Binance; "
             "scripts/cycle_analysis.py. Survivors only (collections still trading in 2026).", fontsize=7, color=INK2)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    fig.savefig(os.path.join(ROOT, "reports", "charts", "cycleB_low_to_high_vs_btc.png"), dpi=125, facecolor=SURF)


if __name__ == "__main__":
    overview()
    distribution()
    print("ok")
