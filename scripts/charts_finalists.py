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


def chart(key, slug, title):
    s = load_series(slug)
    fig, axes = plt.subplots(3, 1, figsize=(12, 9.5), sharex=True, gridspec_kw={"height_ratios": [3, 1.6, 1.2]})
    ax = axes[0]
    ax.plot(s.index, s.floorNative, color="#2c3e50", lw=1.6, label="Floor (ETH)")
    ax.set_yscale("log")
    ax.set_ylabel("Floor, ETH (log)")
    ax2 = ax.twinx()
    ax2.plot(s.index, s.floorBtc, color="#e67e22", lw=1.3, alpha=0.9, label="Floor (BTC)")
    ax2.set_yscale("log")
    ax2.set_ylabel("Floor, BTC (log)", color="#e67e22")
    ax.set_title(f"{title} — floor history (NFTPriceFloor 3-day bars) with catalysts")
    h1, l1 = ax.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax.legend(h1 + h2, l1 + l2, loc="upper right", fontsize=8)
    ax.grid(alpha=0.3, which="both")
    ev = load_events(key, s)
    ymax = s.floorNative.max()
    for i, (d, txt) in enumerate(ev):
        for a in axes:
            a.axvline(d, color="#8e44ad", lw=0.7, alpha=0.6, ls=":")
        ax.annotate(f"{i + 1}", xy=(d, ymax), xytext=(0, -2 - 10 * (i % 3)), textcoords="offset points",
                    fontsize=8, color="#8e44ad", ha="center", va="top", fontweight="bold")
    # relative to sector (BTC terms)
    sec = sector.ew_floor_btc.reindex(s.index, method="ffill")
    ok = sec.notna()
    rel = (s.floorBtc[ok] / s.floorBtc[ok].iloc[0]) / (sec[ok] / sec[ok].iloc[0])
    axes[1].plot(rel.index, rel, color="#16a085", lw=1.4)
    axes[1].axhline(1, color="black", lw=0.6)
    axes[1].set_yscale("log")
    axes[1].set_ylabel("vs sector index\n(BTC terms)")
    axes[1].grid(alpha=0.3, which="both")
    axes[2].bar(s.index, s.salesCount, width=3, color="#7f8c8d")
    axes[2].set_ylabel("Sales / 3 days")
    axes[2].grid(alpha=0.3)
    axes[2].xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1, 7]))
    axes[2].xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    legend = "  ".join(f"{i + 1}) {d.date()} {textwrap.shorten(str(t), 60)}" for i, (d, t) in enumerate(ev))
    fig.text(0.01, 0.005, "\n".join(textwrap.wrap(legend, 210)) + "\nSources: NFTPriceFloor; Binance ETHBTC; "
             "catalyst dates from data/processed/catalysts (cited).", fontsize=7, color="#333", va="bottom")
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(os.path.join(CH, f"{key}_history.png"), dpi=120)
    plt.close(fig)
    return s


def overlay():
    fig, ax = plt.subplots(figsize=(12, 6))
    for key, slug, title in F:
        s = pd.read_csv(os.path.join(PROC, "npf_series", f"{slug}.csv"), index_col=0, parse_dates=True)
        s = s[(s.floorNative > 0) & (s.index >= "2023-01-01")]
        ax.plot(s.index, s.floorBtc / s.floorBtc.iloc[0], lw=1.3, label=title)
    ax.plot(sector.loc["2023-01-01":].index, sector.loc["2023-01-01":].ew_floor_btc /
            sector.loc["2023-01-01":].ew_floor_btc.iloc[0], color="black", lw=2.2, ls="--", label="Sector EW index")
    ax.axhline(1, color="grey", lw=0.6)
    ax.set_yscale("log")
    ax.set_title("Finalists: floor in BTC terms, rebased to 2023-01-01 (log). 1.0 = matched BTC")
    ax.legend(fontsize=8, ncol=2)
    ax.grid(alpha=0.3, which="both")
    fig.text(0.01, 0.01, "Source: NFTPriceFloor 3-day floors, Binance ETHBTC.", fontsize=7.5, color="#555")
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(os.path.join(CH, "finalists_btc_rebased.png"), dpi=120)


if __name__ == "__main__":
    for k, sl, t in F:
        chart(k, sl, t)
    overlay()
    print("ok")
