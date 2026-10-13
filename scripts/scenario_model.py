"""BTC-relative scenario model, v2 (post-critic). Every parameter comes from one documented rule applied uniformly to
all collections. Full documentation: reports/scenario_model.md. The draft v1 (hand-set parameters) is archived as
scripts/scenario_model_v1_draft.py + scenario_params_v1_draft.py -> data/processed/scenarios_v1_draft.csv.

Identity (collection c, scenario s), BTC terms relative to the entry basis:
    peak_btc = P[c,s] * (ETHBTC_s / ETHBTC_0) / e[c]          (P = peak floor multiple in ETH terms vs current floor)
    end_btc  = E[c,s] * (ETHBTC_s / ETHBTC_0) / e[c]          (E = end-of-horizon floor multiple in ETH terms)
    payoff   = exit_rule(peak_btc, end_btc) * (1 - h[c,s]) - 1
Exit rules (all executable with a single item):
    HOLD : end_btc
    A    : sell everything at 2.0x BTC-terms if peak_btc >= 2.0, else end_btc
    B    : once peak_btc >= 1.5, sell on a 30% drawdown from the post-entry peak  -> 0.7*peak_btc; else end_btc
    TOP  : discretionary near-top sale capturing 75% of the peak gain, 1 + 0.75*(peak_btc - 1)  [optimistic bound]
Parameter rules (ETH terms, from data/processed/npf_series via npf_utils, 2022-06 → 2026-10):
    S1 (weak)     : E = mean(sector 18m decay 0.55, own 1y/2y/3y ETH-terms trends each extrapolated to 18m and capped
                    at 1.0), bounded to [0.30, 0.90]; P = E (no rally)
    S2 (moderate) : E = 0.90 for all (no catalysts; sector floors have drifted down in ETH terms outside rallies); P = E
    S3 (strong)   : P = own Aug-2025 rally trough->peak ETH multiple (most recent rally; its token/Blur mechanisms
                    absent); E = P x RET365
    S4 (mania)    : P = own best trough->peak ETH multiple of the 2023/2024/2025 rallies; E = P x RET365
    Cap (S3, S4)  : P <= own 2024-25 cycle-high floor / current floor (no new highs above the last cycle's peak)
    RET365        : own mean ETH-terms floor 365d after the 2024 and 2025 rally peaks / peak
    e (entry)     : 1 + half the instant-book average-cost premium over floor for a ~$7.5k position; Azuki (held)
                    uses the sell-now net bid as basis: e = (0.466 x 0.99) / 0.548
    h (exit)      : S1 = instant bid gap for the position + seller fee; S2/S3 = half the gap + fee; S4 = fee + 2%
Scenario ETH/BTC (BTC USD): S1 0.024 ($70k) · S2 0.032 ($110k) · S3 0.040 ($135k) · S4 0.050 ($160k).
Outputs: data/processed/scenarios.csv, scenario_params_v2.csv, breakeven.csv, expected_illustrative.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series

ETHBTC_0, BTC_0, ETHUSD_0 = 0.03010, 83350.0, 2508.69
NOW = pd.Timestamp("2026-10-13")
SCEN = {"S1_weak": (0.024, 70000), "S2_moderate": (0.032, 110000), "S3_strong": (0.040, 135000),
        "S4_mania": (0.050, 160000)}
W = {"R2023": (("2022-11-01", "2023-01-05"), ("2023-01-05", "2023-03-15")),
     "R2024": (("2024-08-01", "2024-10-31"), ("2024-11-01", "2025-01-31")),
     "R2025": (("2025-04-01", "2025-06-30"), ("2025-07-01", "2025-09-30"))}
F = {"milady": "milady", "remilio": "remilio-babies", "cryptodickbutts": "cryptodickbutts", "pudgy": "pudgy-penguins",
     "azuki": "azuki", "chromie_squiggle": "chromie-squiggle-art-blocks-curated",
     "terraforms": "terraforms-by-mathcastles", "v1punks": "v1-cryptopunks-wrapped"}
SECTOR_18M = 0.55  # EW sector index ETH-terms 2023-05 → 2026-10: ~-33%/yr → 0.67^1.5
RULES = ("HOLD", "A", "B", "TOP")


def derive():
    lp = pd.read_csv(os.path.join(PROC, "liquidity_position.csv")).set_index("key")
    rows = {}
    for k, slug in F.items():
        s = load_series(slug)["floorNative"]
        fn = s.iloc[-1]
        mult, ret = {}, []
        for w, (tr, pk) in W.items():
            a, b = s.loc[tr[0]:tr[1]], s.loc[pk[0]:pk[1]]
            mult[w] = b.max() / a.min()
            if w != "R2023":
                pdt = b.idxmax()
                ret.append(s.loc[pdt + pd.Timedelta(days=355): pdt + pd.Timedelta(days=375)].mean() / b.max())
        tr1 = min(1.0, (fn / s.loc[:NOW - pd.DateOffset(years=1)].iloc[-1]) ** 1.5)
        tr2 = min(1.0, (fn / s.loc[:NOW - pd.DateOffset(years=2)].iloc[-1]) ** 0.75)
        tr3 = min(1.0, (fn / s.loc[:NOW - pd.DateOffset(years=3)].iloc[-1]) ** 0.5)
        cap = s.loc["2024-01-01":"2025-12-31"].max() / fn  # no new highs above the 2024-25 cycle high
        L = lp.loc[k]
        n_floor = L.items_for_budget * L.floor_ask
        gap = 1 - (L.instant_exit_eth / (1 - L.seller_fee)) / n_floor
        e = 1 + 0.5 * (L.entry_cost_eth / n_floor - 1)
        if k == "azuki":
            e = (0.466 * 0.99) / 0.548  # incumbent: hold vs sell-now at net bid
        rows[k] = dict(S1_E=float(np.clip(np.mean([SECTOR_18M, tr1, tr2, tr3]), 0.30, 0.90)), S2_E=0.90,
                       S3_P=min(mult["R2025"], cap), S4_P=min(max(mult.values()), cap), RET365=float(np.mean(ret)),
                       cycle_high_cap=cap, own_1y_18m=tr1, own_2y_18m=tr2, own_3y_18m=tr3, R2023=mult["R2023"], R2024=mult["R2024"], R2025=mult["R2025"],
                       e=e, gap=gap, fee=L.seller_fee,
                       h_S1=gap + L.seller_fee, h_S2=0.5 * gap + L.seller_fee, h_S3=0.5 * gap + L.seller_fee,
                       h_S4=L.seller_fee + 0.02)
    return pd.DataFrame(rows).T.astype(float)


def payoff(rule, peak, end):
    if rule == "HOLD":
        return end
    if rule == "A":
        return 2.0 if peak >= 2.0 else end
    if rule == "B":
        return 0.7 * peak if peak >= 1.5 else end
    if rule == "TOP":
        return 1 + 0.75 * (peak - 1) if peak > 1 else end
    raise ValueError(rule)


def run(P):
    rows = []
    for k, p in P.iterrows():
        for s, (eb, btc) in SCEN.items():
            x = eb / ETHBTC_0
            if s in ("S1_weak", "S2_moderate"):
                pk = en = p[f"{s[:2]}_E"]
            else:
                pk = p[f"{s[:2]}_P"]
                en = pk * p.RET365
            peak_btc, end_btc = pk * x / p.e, en * x / p.e
            h = p[f"h_{s[:2]}"]
            for rule in RULES:
                v = payoff(rule, peak_btc, end_btc) * (1 - h)
                rows.append(dict(collection=k, scenario=s, rule=rule, eth_btc=eb, btc_usd=btc, P_eth=pk, E_eth=en,
                                 peak_btc=peak_btc, R_btc=v - 1, R_eth=v / x - 1,
                                 R_usd=v * (eb * btc) / (ETHBTC_0 * BTC_0) - 1))
    for s, (eb, btc) in SCEN.items():
        for rule in RULES:
            rows.append(dict(collection="ETH", scenario=s, rule=rule, eth_btc=eb, btc_usd=btc, P_eth=1, E_eth=1,
                             peak_btc=eb / ETHBTC_0, R_btc=eb / ETHBTC_0 - 1, R_eth=0.0,
                             R_usd=eb * btc / ETHUSD_0 - 1))
    return pd.DataFrame(rows)


def breakeven(df, w_down=(0.5, 0.5), w_up=(2 / 3, 1 / 3)):
    """Weight on the favorable block {S3,S4} (internal mix w_up) vs {S1,S2} (mix w_down) for E[R_btc]=0.
    NaN = never attainable (the favorable block itself is not positive)."""
    out = {}
    for (c, rule), g in df.groupby(["collection", "rule"]):
        r = g.set_index("scenario")["R_btc"]
        down = w_down[0] * r["S1_weak"] + w_down[1] * r["S2_moderate"]
        up = w_up[0] * r["S3_strong"] + w_up[1] * r["S4_mania"]
        out[(c, rule)] = (-down / (up - down)) if (up > 0 and down < 0) else (0.0 if down >= 0 else np.nan)
    return out


def expected(df, w):
    return df.assign(x=df.scenario.map(w) * df.R_btc).groupby(["collection", "rule"]).x.sum()


if __name__ == "__main__":
    P = derive()
    P.to_csv(os.path.join(PROC, "scenario_params_v2.csv"))
    df = run(P)
    df.to_csv(os.path.join(PROC, "scenarios.csv"), index=False)
    pd.set_option("display.width", 260)
    print(P[["S1_E", "S2_E", "S3_P", "S4_P", "RET365", "e", "h_S1", "h_S2", "h_S4"]].round(3).to_string())
    print(df.pivot_table(index="collection", columns=["scenario", "rule"], values="R_btc").round(2).to_string())
    variants = {"base": ((.5, .5), (2 / 3, 1 / 3)), "S1heavy": ((.6, .4), (2 / 3, 1 / 3)),
                "S3heavy": ((.5, .5), (.75, .25))}
    be = []
    for name, (wd, wu) in variants.items():
        for (c, rule), v in breakeven(df, wd, wu).items():
            be.append(dict(variant=name, collection=c, rule=rule, breakeven=v))
    be = pd.DataFrame(be)
    be.to_csv(os.path.join(PROC, "breakeven.csv"), index=False)
    print(be.pivot_table(index="collection", columns=["rule", "variant"], values="breakeven", dropna=False).round(2).to_string())
    ev = []
    for name, w in {"bearish": {"S1_weak": .45, "S2_moderate": .35, "S3_strong": .13, "S4_mania": .07},
                    "neutral": {"S1_weak": .35, "S2_moderate": .35, "S3_strong": .20, "S4_mania": .10},
                    "constructive": {"S1_weak": .25, "S2_moderate": .35, "S3_strong": .27, "S4_mania": .13}}.items():
        ev.append(expected(df, w).rename(name))
    ev = pd.concat(ev, axis=1)
    ev.to_csv(os.path.join(PROC, "expected_illustrative.csv"))
    print(ev.round(2).unstack("rule").to_string())
