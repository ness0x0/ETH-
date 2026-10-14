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
  G  the investor's clarified bar (2026-10-14): "4x in dollars if BTC 2x" = 2x vs BTC (10x in dollars = 5x vs BTC).
     Tested with a rule that needs no hindsight: buy near the low, list at the target (net of 10% costs) and let it
     fill the first time the floor reaches it; otherwise hold to BTC's top (2025-10-06).
  H  buy near a cycle low and *hold* (the investor's original "hold to 2028-29" idea): value vs BTC at BTC's top
     (2025-10-06) and today, from the 2022-23, 2023 and 2024 lows
Outputs: data/processed/cycle_tail_counts.csv, cycle_tail_profile.csv, cycle_tail_buckets.csv, recent_launches.csv,
         cycle_tail_baskets.csv, cycle_tail_watchlist.csv, cycle_tail_target_rule.csv, cycle_tail_target_summary.csv,
         cycle_tail_hold.csv
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


TARGET_CYCLES = {"2024-25": (("2024-06-15", "2024-10-31"), ("2024-11-01", "2025-10-06")),
                 "2022-25": (("2022-06-15", "2023-10-31"), ("2023-11-01", "2025-10-06"))}
COST = 0.10


def target_rule(targets=(2.0, 5.0)):
    rows = []
    for cyc, (lw, xw) in TARGET_CYCLES.items():
        for name, npf, _, cat in UNIVERSE:
            if not os.path.exists(os.path.join(PROC, "npf_series", f"{npf}.csv")):
                continue
            s = load_series(npf, start="2022-06-15")
            low = s.loc[lw[0]:lw[1]]
            if len(low) < 10:
                continue
            ld = low.floorUsd.idxmin()
            path = s.floorBtc.loc[xw[0]:xw[1]]
            if len(path) < 10:
                continue
            ent = {"rough": low.floorBtc.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)].mean(),
                   "blind": low.floorBtc.median()}
            for tier, e in ent.items():
                r = dict(cycle=cyc, name=name, category=cat, tier=tier, low_date=ld.date(),
                         end_vs_btc=path.iloc[-1] / e * (1 - COST), max_vs_btc=path.max() / e * (1 - COST))
                for T in targets:
                    hit = path[path >= T / (1 - COST) * e]
                    r[f"hit_{T:g}x"] = not hit.empty
                    r[f"hit_{T:g}x_date"] = hit.index[0].date() if not hit.empty else None
                    r[f"outcome_{T:g}x"] = T if not hit.empty else r["end_vs_btc"]
                rows.append(r)
    return pd.DataFrame(rows)


def target_summary(tr, pr):
    cap = pr.set_index(["cycle", "name"]).cap_at_low_usd_m
    tr = tr.assign(cap_at_low_usd_m=[cap.get((c, n), np.nan) for c, n in zip(tr.cycle, tr.name)])
    pfp = tr.category.str.contains("pfp")
    rows = []
    for (cyc, tier), g in tr.groupby(["cycle", "tier"], sort=False):
        for lab, h in (("all", g), ("PFP", g[pfp.loc[g.index]]), ("cap<$5M at low", g[g.cap_at_low_usd_m < 5]),
                       ("cap>=$15M at low", g[g.cap_at_low_usd_m >= 15])):
            o = dict(cycle=cyc, tier=tier, sample=lab, n=len(h))
            for T in (2, 5):
                o[f"P_hit_{T}x"] = h[f"hit_{T}x"].mean()
                o[f"median_outcome_{T}x_rule"] = h[f"outcome_{T}x"].median()
                o[f"mean_outcome_{T}x_rule"] = h[f"outcome_{T}x"].mean()
            o["P_lose_vs_btc_2x_rule"] = (h["outcome_2x"] < 1).mean()
            o["median_if_missed_2x"] = h.loc[~h["hit_2x"], "end_vs_btc"].median()
            o["median_days_to_hit_2x_from_xw_start"] = (pd.to_datetime(h["hit_2x_date"]).dropna()
                                                         - pd.Timestamp(TARGET_CYCLES[cyc][1][0])).dt.days.median()
            rows.append(o)
    return pd.DataFrame(rows)


HOLD_LOWS = {"2022-23 low": ("2022-06-15", "2023-10-31"), "Aug-Nov 2023 low": ("2023-08-01", "2023-11-15"),
             "2024 low": ("2024-06-15", "2024-10-31")}


def hold_from_low():
    rows = []
    for name, npf, _, cat in UNIVERSE:
        if not os.path.exists(os.path.join(PROC, "npf_series", f"{npf}.csv")):
            continue
        s = load_series(npf, start="2022-06-15")
        for lab, (a, b) in HOLD_LOWS.items():
            low = s.loc[a:b]
            if len(low) < 10:
                continue
            ld = low.floorUsd.idxmin()
            e = low.floorBtc.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)].mean()  # rough entry
            rows.append(dict(low=lab, name=name, category=cat,
                             at_btc_top=s.floorBtc.asof(pd.Timestamp("2025-10-06")) / e * (1 - COST),
                             today=s.floorBtc.iloc[-1] / e * (1 - COST)))
    d = pd.DataFrame(rows)
    sm = d.groupby("low", sort=False).agg(n=("name", "size"),
                                          beat_btc_at_top=("at_btc_top", lambda x: (x > 1).mean()),
                                          median_at_top=("at_btc_top", "median"),
                                          ge2_at_top=("at_btc_top", lambda x: (x >= 2).mean()),
                                          beat_btc_today=("today", lambda x: (x > 1).mean()),
                                          median_today=("today", "median"))
    return d, sm


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
    tr = target_rule()
    tr.to_csv(os.path.join(PROC, "cycle_tail_target_rule.csv"), index=False)
    ts = target_summary(tr, pr)
    ts.to_csv(os.path.join(PROC, "cycle_tail_target_summary.csv"), index=False)
    print(ts.round(2).to_string())
    print(tr[(tr.tier == "rough") & tr.hit_2x].sort_values(["cycle", "hit_2x_date"])[
        ["cycle", "name", "low_date", "hit_2x_date", "hit_5x", "hit_5x_date", "max_vs_btc", "end_vs_btc"]].round(2)
          .to_string())
    hd, hs = hold_from_low()
    hd.to_csv(os.path.join(PROC, "cycle_tail_hold.csv"), index=False)
    print(hs.round(2).to_string())
