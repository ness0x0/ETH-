"""Tail outcomes: how often did an Ethereum NFT do 4-10x against BTC from its cycle low? (investor follow-up 2026-10-14)

The investor's bar moved from "beat BTC" to "plausibly 4-10x against a BTC 2x". Two readings, both reported:
  (a) NFT USD multiple 4-10x while BTC does ~2x   -> roughly 2-5x vs BTC
  (b) NFT 4-10x *relative to* BTC                 -> roughly 8-20x in USD if BTC does 2x
Inputs (already built): cycle2024.csv (2024-25 leg, exit BEST_to_btc_top), cycle_episodes.csv (BIG_2022_2025),
cycleA_summary.csv (2021; 13 survivors, launch-phase lows; context only), screen_metrics.csv (supply, created).
Parts:
  A  counts at >=2/4/10x vs BTC and >=4/10x USD, rough (and perfect = unattainable upper bound)
  B  profile of the >=4x vs BTC winners: floor cap at the low (USD floor x current supply), drawdown from the prior
     peak (max USD floor in the 2 years before the low; series start 2022-06-15 truncates this for 2022 lows)
  C  cap buckets at the low vs tail frequency
  D  recent launches in the universe (created 2023+): first-month floor -> peak -> now, in BTC
  E  equal-weight baskets (every k-combination) from each cycle: P(basket >= 2x / 4x vs BTC), P(holds a 4x)
  F  collections matching the winners' pre-catalyst profile today (watchlist, not a buy list)
Outputs: data/processed/cycle_tail_counts.csv, cycle_tail_profile.csv, cycle_tail_buckets.csv, recent_launches.csv,
         cycle_tail_baskets.csv, cycle_tail_watchlist.csv
"""
import itertools
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series
from universe_config import UNIVERSE

NPF = {n: s for n, s, _, _ in UNIVERSE}
MIGRATIONS = {"Chimpers", "DeGods (ETH)"}  # new contract for an existing collection; not a fresh launch


def cycles():
    c24 = pd.read_csv(os.path.join(PROC, "cycle2024.csv"))
    c24 = c24[c24.exit == "BEST_to_btc_top"]
    cb = pd.read_csv(os.path.join(PROC, "cycle_episodes.csv"))
    cb = cb[cb.episode == "BIG_2022_2025"]
    ca = pd.read_csv(os.path.join(PROC, "cycleA_summary.csv"))
    ca = ca[ca.low_date != ca.peak_date]  # Pudgy's sampled series has no post-mint low before its Aug-2021 peak
    return {"2024-25": c24, "2022-25": cb, "2021 (survivors, launch-phase lows)": ca}


def counts(cy):
    rows = []
    for lab, d in cy.items():
        r = {"cycle": lab, "n": len(d)}
        for t in (2, 4, 10):
            r[f"vs_btc_ge{t}_rough"] = int((d.vs_btc_rough >= t).sum())
            r[f"vs_btc_ge{t}_perfect"] = int((d.vs_btc_perfect >= t).sum())
        for t in (4, 10):
            r[f"usd_ge{t}_rough"] = int((d.usd_rough >= t).sum())
        r["winners_ge4_vs_btc_rough"] = "; ".join(f"{n} {v:.2f}" for n, v in d[d.vs_btc_rough >= 4]
                                                 .sort_values("vs_btc_rough", ascending=False)[["name", "vs_btc_rough"]]
                                                 .itertuples(index=False))
        rows.append(r)
    return pd.DataFrame(rows)


def profile(cy):
    sm = pd.read_csv(os.path.join(PROC, "screen_metrics.csv")).set_index("name")
    rows = []
    for lab in ("2024-25", "2022-25"):
        for _, r in cy[lab].iterrows():
            name = r["name"]
            if name not in sm.index or pd.isna(sm.loc[name, "supply"]) or name not in NPF:
                continue
            s = load_series(NPF[name], start="2022-06-15")
            ld = pd.Timestamp(r.low_date)
            fl = s.floorUsd.asof(ld)
            prior = s.floorUsd.loc[ld - pd.Timedelta(days=730):ld].max()
            rows.append(dict(cycle=lab, name=name, category=sm.loc[name, "category"], low_date=r.low_date,
                             cap_at_low_usd_m=fl * sm.loc[name, "supply"] / 1e6, dd_from_prior_peak=fl / prior - 1,
                             vs_btc_rough=r.vs_btc_rough, usd_rough=r.usd_rough, vs_btc_perfect=r.vs_btc_perfect))
    return pd.DataFrame(rows)


def buckets(pr):
    rows = []
    for lab, g in pr.groupby("cycle", sort=False):
        for lo, hi in ((0, 5), (5, 15), (15, 50), (50, 5000)):
            h = g[(g.cap_at_low_usd_m >= lo) & (g.cap_at_low_usd_m < hi)]
            rows.append(dict(cycle=lab, cap_bucket=f"${lo}-{hi}M", n=len(h), ge2=int((h.vs_btc_rough >= 2).sum()),
                             ge4=int((h.vs_btc_rough >= 4).sum()), median_vs_btc=h.vs_btc_rough.median()))
    return pd.DataFrame(rows)


def recent_launches():
    sm = pd.read_csv(os.path.join(PROC, "screen_metrics.csv"))
    sm["created"] = pd.to_datetime(sm.created, errors="coerce")
    rows = []
    for _, m in sm[sm.created >= "2023-01-01"].iterrows():
        if m["name"] not in NPF:
            continue
        s = load_series(NPF[m["name"]], start="2022-06-01").loc[m.created:]
        if len(s) < 5:
            continue
        first = s.floorBtc.iloc[:10].mean()  # first ~30 days of 3-day bars after (re)launch
        pk = s.floorBtc.idxmax()
        rows.append(dict(name=m["name"], created=m.created.date(), migration=m["name"] in MIGRATIONS,
                         first_month_floor_btc=first, peak_date=pk.date(), days_to_peak=(pk - s.index[0]).days,
                         peak_vs_first_btc=s.floorBtc.max() / first, now_vs_first_btc=s.floorBtc.iloc[-1] / first,
                         now_vs_peak_btc=s.floorBtc.iloc[-1] / s.floorBtc.max(),
                         floor_cap_now_usd_m=m.floor_cap_usd_m))
    return pd.DataFrame(rows).sort_values("created")


def baskets(cy, pr):
    """Equal-weight k-pick baskets drawn from each cycle's population (every combination): does diversifying across
    small-cap tickets get the *position* to 4x vs BTC, or only raise the odds of holding one winner?"""
    rows = []
    for lab in ("2024-25", "2022-25"):
        g = pr[pr.cycle == lab]
        for pop, v in (("all", cy[lab].vs_btc_rough.values), ("cap<$5M at low", g[g.cap_at_low_usd_m < 5]
                                                               .vs_btc_rough.values)):
            for k in (1, 3, 5):
                m = np.array([np.mean(c) for c in itertools.combinations(v, k)])
                hit = np.array([max(c) >= 4 for c in itertools.combinations(v, k)])
                rows.append(dict(cycle=lab, population=pop, n=len(v), k=k, P_basket_ge1=(m >= 1).mean(),
                                 P_basket_ge2=(m >= 2).mean(), P_basket_ge4=(m >= 4).mean(),
                                 P_holds_a_4x=hit.mean(), median_basket=np.median(m)))
    return pd.DataFrame(rows)


def profile_matches_now():
    """Collections that look like the past winners *before* their catalyst (PFP, floor cap <= $10M, >= 85% below ATH
    in BTC, still trading >= 1 sale/day). A watchlist for catalysts, not a buy list."""
    sm = pd.read_csv(os.path.join(PROC, "screen_metrics.csv"))
    m = sm[sm.category.str.contains("pfp") & (sm.floor_cap_usd_m <= 10) & (sm.drawdown_from_ath_btc <= -0.85)
           & (sm.sales_per_day_30d >= 1)]
    return m[["name", "category", "created", "floor_cap_usd_m", "os_floor_eth", "drawdown_from_ath_btc",
              "sales_per_day_30d", "owners_per_supply"]].sort_values("floor_cap_usd_m")


if __name__ == "__main__":
    pd.set_option("display.width", 250)
    pd.set_option("display.max_columns", 30)
    cy = cycles()
    c = counts(cy)
    pr = profile(cy)
    b = buckets(pr)
    rl = recent_launches()
    c.to_csv(os.path.join(PROC, "cycle_tail_counts.csv"), index=False)
    pr.to_csv(os.path.join(PROC, "cycle_tail_profile.csv"), index=False)
    b.to_csv(os.path.join(PROC, "cycle_tail_buckets.csv"), index=False)
    rl.to_csv(os.path.join(PROC, "recent_launches.csv"), index=False)
    bk = baskets(cy, pr)
    bk.to_csv(os.path.join(PROC, "cycle_tail_baskets.csv"), index=False)
    wl = profile_matches_now()
    wl.to_csv(os.path.join(PROC, "cycle_tail_watchlist.csv"), index=False)
    print(c.T.to_string())
    print(pr[pr.vs_btc_rough >= 4].round(2).to_string())
    print(pr[pr.vs_btc_rough >= 2].sort_values(["cycle", "vs_btc_rough"], ascending=False).round(2).to_string())
    print(b.round(2).to_string())
    print(rl.round(3).to_string())
    print(bk.round(3).to_string())
    print(wl.round(3).to_string())
