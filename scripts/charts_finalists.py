"""Historical charts for finalists: floor in ETH and BTC terms, relative-to-sector, sales activity, with catalyst
annotations from data/processed/catalysts/<key>.csv (if present; events flagged major via the MAJOR list or the
'major' column when provided).

Output: reports/charts/<key>_history.png and reports/charts/finalists_btc_rebased.png
"""
import os
import textwrap
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from common import PROC, ROOT
from npf_utils import load_series

CH = os.path.join(ROOT, "reports", "charts")
F = [  # key, npf slug, title
    ("milady", "milady", "Milady Maker"),
    ("remilio", "remilio-babies", "Redacted Remilio Babies"),
    ("cryptodickbutts", "cryptodickbutts", "CryptoDickbutts"),
    ("pudgy", "pudgy-penguins", "Pudgy Penguins"),
    ("azuki", "azuki", "Azuki"),
    ("chromie_squiggle", "chromie-squiggle-art-blocks-curated", "Chromie Squiggle"),
    ("terraforms", "terraforms-by-mathcastles", "Terraforms"),
    ("v1punks", "v1-cryptopunks-wrapped", "V1 CryptoPunks (wrapped)"),
    ("moonbirds", "proof-moonbirds", "Moonbirds"),
]
sector = pd.read_csv(os.path.join(PROC, "sector_index.csv"), index_col=0, parse_dates=True)
prices = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
MAX_EVENTS = 9


def load_events(key, s):
    p = os.path.join(PROC, "catalysts", f"{key}.csv")
    if not os.path.exists(p):
        return []
    c = pd.read_csv(p)
    c["date"] = pd.to_datetime(c["date"].astype(str).str[:10], errors="coerce")
    c = c.dropna(subset=["date"])
    c = c[(c.date >= s.index[0]) & (c.date <= s.index[-1])]
    if "major" in c.columns:
        c = c[c["major"].astype(str).str.lower().isin(["1", "true", "yes", "y"])]
    else:
        # rank by absolute 90d BTC move from the event study when available
        es = os.path.join(PROC, "event_study.csv")
        if os.path.exists(es):
            e = pd.read_csv(es)
            e = e[e.file == key][["date", "event", "btc_90d"]]
            e["date"] = pd.to_datetime(e["date"])
            c = c.merge(e, on=["date", "event"], how="left")
            c["rank"] = c["btc_90d"].abs().fillna(0)
            c = c.sort_values("rank", ascending=False).head(MAX_EVENTS)
        else:
            c = c.head(MAX_EVENTS)
    return list(c.sort_values("date")[["date", "event"]].itertuples(index=False))


SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
C1, C2, C3 = "#2a78d6", "#eb6834", "#1baf7a"  # reference palette slots 1-3 (validated adjacent & all-pairs)
NEUTRAL = "#8a8985"


def style(ax):
    ax.set_facecolor(SURF)
    ax.grid(color=GRID, lw=0.6, which="both")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(NEUTRAL)
    ax.tick_params(colors=INK2, labelsize=8)


def plain_log(ax):
    from matplotlib.ticker import FuncFormatter, NullFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
    ax.yaxis.set_minor_formatter(NullFormatter())


def chart(key, slug, title):
    s = load_series(slug)
    fig, axes = plt.subplots(4, 1, figsize=(12, 11), sharex=True, gridspec_kw={"height_ratios": [2.2, 2.2, 1.4, 1.1]},
                             facecolor=SURF)
    for a in axes:
        style(a)
    axes[0].plot(s.index, s.floorNative, color=C1, lw=2)
    axes[0].set_yscale("log")
    plain_log(axes[0])
    axes[0].set_ylabel("Floor, ETH (log)", color=INK2)
    axes[0].set_title(f"{title} — floor history (NFTPriceFloor 3-day bars) with numbered catalysts", color=INK, loc="left")
    axes[1].plot(s.index, s.floorBtc, color=C2, lw=2)
    axes[1].set_yscale("log")
    plain_log(axes[1])
    axes[1].set_ylabel("Floor, BTC (log)", color=INK2)
    ev = load_events(key, s)
    ymax = s.floorNative.max()
    for i, (d, txt) in enumerate(ev):
        for a in axes:
            a.axvline(d, color=NEUTRAL, lw=0.8, alpha=0.7, ls=":")
        axes[0].annotate(f"{i + 1}", xy=(d, ymax), xytext=(0, -2 - 10 * (i % 3)), textcoords="offset points",
                         fontsize=8, color=INK, ha="center", va="top", fontweight="bold")
    sec = sector.ew_floor_btc.reindex(s.index, method="ffill")
    ok = sec.notna()
    rel = (s.floorBtc[ok] / s.floorBtc[ok].iloc[0]) / (sec[ok] / sec[ok].iloc[0])
    axes[2].plot(rel.index, rel, color=C3, lw=2)
    axes[2].axhline(1, color=INK2, lw=0.8)
    axes[2].set_yscale("log")
    plain_log(axes[2])
    axes[2].set_ylabel("vs sector index\n(BTC terms, rebased)", color=INK2)
    axes[3].bar(s.index, s.salesCount, width=2.6, color=NEUTRAL)
    axes[3].set_ylabel("Sales / 3 days", color=INK2)
    axes[3].xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    axes[3].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    legend = "  ".join(f"{i + 1}) {d.date()} {textwrap.shorten(str(t), 60)}" for i, (d, t) in enumerate(ev))
    fig.text(0.01, 0.005, "\n".join(textwrap.wrap(legend, 210)) + "\nSources: NFTPriceFloor (outlier-cleaned); Binance "
             "ETHBTC; catalyst dates from data/processed/catalysts (cited). Panels share the x-axis; no dual y-axes.",
             fontsize=7, color=INK2, va="bottom")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(os.path.join(CH, f"{key}_history.png"), dpi=120, facecolor=SURF)
    plt.close(fig)
    return s


def overlay():
    """Small multiples: each finalist's BTC-terms floor rebased to 2023-01-01 vs the sector index (grey)."""
    fig, axes = plt.subplots(3, 3, figsize=(13, 9.5), sharex=True, sharey=True, facecolor=SURF)
    sec = sector.loc["2023-01-01":].ew_floor_btc
    for ax, (key, slug, title) in zip(axes.flat, F):
        style(ax)
        s = load_series(slug)
        s = s[s.index >= "2023-01-01"]
        ax.plot(sec.index, sec / sec.iloc[0], color=NEUTRAL, lw=1.4)
        ax.plot(s.index, s.floorBtc / s.floorBtc.iloc[0], color=C1, lw=1.8)
        ax.axhline(1, color=INK2, lw=0.7)
        ax.set_yscale("log")
        plain_log(ax)
        last = s.floorBtc.iloc[-1] / s.floorBtc.iloc[0]
        ax.set_title(f"{title}  ({last:.2f}× BTC)", fontsize=9.5, color=INK, loc="left")
        ax.xaxis.set_major_locator(mdates.YearLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    fig.suptitle("Floor in BTC terms, rebased to 2023-01-01 (log). Blue = collection, grey = sector EW index; 1.0 = matched BTC",
                 color=INK, x=0.01, ha="left", fontsize=11)
    fig.text(0.01, 0.005, "Source: NFTPriceFloor 3-day floors (outlier-cleaned), Binance ETHBTC. Rebasing date changes "
             "the picture (e.g., Remilio starts near its Jan-2023 low).", fontsize=7.5, color=INK2)
    fig.tight_layout(rect=(0, 0.02, 1, 0.96))
    fig.savefig(os.path.join(CH, "finalists_btc_rebased.png"), dpi=120, facecolor=SURF)


if __name__ == "__main__":
    for k, sl, t in F:
        chart(k, sl, t)
    overlay()
    print("ok")
