"""BTC-relative scenario model for finalists.

Return identity (per scenario s, collection c):
    R_btc = M[c,s] * (1 - h[c,s]) * ETHBTC_s / ETHBTC_0 - 1
    R_eth = M[c,s] * (1 - h[c,s]) - 1
    R_usd = (1 + R_eth) * ETHUSD_s / ETHUSD_0 - 1
where M = floor multiple in ETH terms at exit vs today's executable entry, h = exit haircut (spread to executable bid
+ marketplace fee + optional royalty), ETHBTC_s / BTC_s are explicit scenario assumptions (not forecasts).

Two exit conventions for the up-scenarios:
  - "disciplined": sells within the rally window (M_peak_capture = assumed realized fraction of the peak multiple)
  - "hold-through": holds to end of horizon; applies the empirical post-peak retention (~0.35-0.5 of peak, see
    data/processed/rally_analysis.csv).
No probabilities are assigned. For each collection we compute the break-even weight on the favorable scenarios
(S3+S4, in their observed relative frequency mix 2:1) required for E[R_btc] = 0, holding S1/S2 weights equal.

All M parameters and their evidence anchors live in PARAMS below and are discussed in reports/scenario_model.md.
Output: data/processed/scenarios.csv
"""
import os
import pandas as pd
from common import PROC

ETHBTC_0, BTC_0, ETHUSD_0 = 0.03010, 83350.0, 2508.69
HORIZON = "18 months (Apr 2028), range 6-24m"

SCEN = {  # name: (ETH/BTC, BTC USD, description)
    "S1_weak": (0.024, 70000, "Continued NFT weakness; crypto chop/bear; ETH underperforms BTC"),
    "S2_moderate": (0.032, 110000, "Moderate crypto recovery; no project-specific catalysts; NFTs drift"),
    "S3_strong": (0.040, 135000, "Strong recovery: BTC & ETH revisit/exceed ATH; NFT rotation like Dec-2024/Aug-2025"),
    "S4_mania": (0.050, 160000, "Speculative mania with leverage/incentives (tokens, points, airdrops)"),
}

# M multiples (ETH terms, exit floor / entry floor) and haircuts. Filled from research; see scenario_model.md.
PARAMS = {}


def run(params, retention=None):
    rows = []
    for c, p in params.items():
        for s, (eb, btc, _) in SCEN.items():
            e = p.get("e", 1.0)
            m = p["M"][s] / e
            h = p["h"][s]
            r_eth = m * (1 - h) - 1
            r_btc = m * (1 - h) * eb / ETHBTC_0 - 1
            r_usd = (1 + r_eth) * (eb * btc) / ETHUSD_0 - 1
            rows.append(dict(collection=c, scenario=s, M_eth=m, haircut=h, eth_btc=eb, btc_usd=btc,
                             eth_usd=eb * btc, R_eth=r_eth, R_btc=r_btc, R_usd=r_usd,
                             exit="disciplined" if s in ("S3_strong", "S4_mania") else "end-of-horizon"))
            if s in ("S3_strong", "S4_mania") and "hold" in p:
                mh = p["hold"][s] / e
                rows.append(dict(collection=c, scenario=s, M_eth=mh, haircut=h, eth_btc=eb, btc_usd=btc,
                                 eth_usd=eb * btc, R_eth=mh * (1 - h) - 1, R_btc=mh * (1 - h) * eb / ETHBTC_0 - 1,
                                 R_usd=mh * (1 - h) * (eb * btc) / ETHUSD_0 - 1, exit="hold-through"))
    return pd.DataFrame(rows)


def breakeven(df):
    """Weight w on {S3,S4} (mixed 2:1) vs (1-w) on {S1,S2} (equal) such that E[R_btc]=0 (disciplined exits)."""
    out = {}
    for c, g in df[df.exit != "hold-through"].groupby("collection"):
        r = g.set_index("scenario")["R_btc"]
        down = (r["S1_weak"] + r["S2_moderate"]) / 2
        up = (2 * r["S3_strong"] + r["S4_mania"]) / 3
        out[c] = (-down / (up - down)) if up > down else float("nan")
        gh = df[(df.collection == c) & (df.exit != "disciplined")].set_index("scenario")["R_btc"]
        uph = (2 * gh["S3_strong"] + gh["S4_mania"]) / 3
        out[c + "|hold"] = (-down / (uph - down)) if uph > down else float("nan")
    return out


if __name__ == "__main__":
    from scenario_params_v1_draft import PARAMS as P
    df = run(P)
    df.to_csv(os.path.join(PROC, "scenarios.csv"), index=False)
    pd.set_option("display.width", 220)
    # ETH itself as the clean alternative vehicle for the same macro view (no haircut)
    for s, (eb, btc, _) in SCEN.items():
        df.loc[len(df)] = dict(collection="ETH (benchmark)", scenario=s, M_eth=1.0, haircut=0.0, eth_btc=eb, btc_usd=btc,
                               eth_usd=eb * btc, R_eth=0.0, R_btc=eb / ETHBTC_0 - 1, R_usd=eb * btc / ETHUSD_0 - 1,
                               exit="end-of-horizon" if s in ("S1_weak", "S2_moderate") else "disciplined")
        if s in ("S3_strong", "S4_mania"):
            df.loc[len(df)] = dict(df.iloc[-1]) | {"exit": "hold-through"}
    df.to_csv(os.path.join(PROC, "scenarios.csv"), index=False)
    piv = df.pivot_table(index=["collection"], columns=["scenario", "exit"], values="R_btc").round(2)
    print(piv.to_string())
    be = breakeven(df)
    print("\nBreak-even weight on S3/S4 (2:1) for E[R_btc]=0  [disciplined | hold-through]")
    be.update(breakeven(df[df.collection == "ETH (benchmark)"]))
    for c in list(P) + ["ETH (benchmark)"]:
        print(f"  {c:18s} {be[c]:.0%} | {be[c + '|hold']:.0%}")
