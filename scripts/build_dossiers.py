"""Assemble collection dossiers: hand-written analysis in dossiers/src/<key>.md + generated quantitative tables.

The marker `<!-- TABLES -->` in each source file is replaced with tables built from the processed datasets so the
numbers in every dossier stay consistent with the models. Output: dossiers/<key>.md
"""
import os
import pandas as pd
from common import ROOT, PROC

KEYS = {  # key: (universe name, opensea liquidity key)
    "chromie_squiggle": "Chromie Squiggle", "v1punks": "V1 CryptoPunks (wrapped)", "pudgy": "Pudgy Penguins",
    "milady": "Milady Maker", "terraforms": "Terraforms", "cryptodickbutts": "CryptoDickbutts",
    "remilio": "Redacted Remilio Babies", "azuki": "Azuki",
}
U = pd.read_csv(os.path.join(ROOT, "universe.csv")).set_index("name")
VERDICT = {
    "v1punks": ("> **Verdict: conditional shortlist #1 — only if an NFT is bought at all** (the headline recommendation is "
                "no NFT purchase now; see `reports/EXECUTIVE_MEMO.md`). It has the smallest weak-scenario loss of the "
                "finalists, one of only two attainable hold-through break-evens, no team to fail and 0% fees; one item "
                "uses ~half the budget. Main risks: contested legitimacy (artists disowned it, the IP holder ignores it) "
                "and concentrated dormant supply (27.9% of V1s in four wallets incl. a likely-Yuga Safe with 1,084)."),
    "milady": ("> **Verdict: conditional shortlist #2 — a mandate exception.** It has the strongest living culture of "
               "any affordable ETH PFP, is divisible (3 items) and is liquid, but it fails the founder-independence "
               "test: its price has been driven by Remilia and celebrity events that fully retraced, and every quiet "
               "window since the CULT TGE lost 28–59% in ETH terms. Own it only with rule-B exit discipline."),
    "cryptodickbutts": ("> **Verdict: conditional shortlist #3 — small, patient, bid-side only.** It is the only "
                        "finalist that has already passed the 'team vanished' test (handover 2023), with strong holder "
                        "retention and an attainable hold-through break-even. But exit liquidity at size is poor "
                        "(~1.1 organic sales/day, best bid 84% of floor) and its meme IP is contested."),
    "chromie_squiggle": ("> **Verdict: conditional shortlist #4 — a collectible, not an investment.** It is the most "
                         "durable cultural object in the set (locked on-chain script, project #0, museum gifts), but "
                         "it is the worst investment case: rule-B break-even 55% (ETH 14%). It beat BTC in 2–13% of "
                         "historical 18-month windows, carries 8.5% seller fees and has its best bid at 78% of floor. "
                         "Buy one only if owning it is the goal, and expect it to under-perform BTC and ETH."),
    "pudgy": ("> **Verdict: not ranked — a tactical alternative outside the mandate.** It is the most liquid finalist "
              "and has the best historical exit-rule record (beat BTC in 80% of windows with rule B), but that record "
              "was produced by operator catalysts (toys, PENGU, ETF hype) that have since reversed. It fails "
              "founder-independence, holders have no claim on IP or revenue, PENGU insiders unlock through 2028, and "
              "~58% of its trailing-year liquidity ran through Blur/Blend, which closes 2026-11-12. One item (81% of "
              "budget) cannot be scaled in or out."),
    "terraforms": ("> **Verdict: not recommended.** Engaged holders and genuine on-chain novelty, but founder-dependent "
                   "'living' features, a latent 1,193-token owner mint controlled by a single EOA, one buyer making "
                   "13.5% of purchases, a ~28% instant round trip and a rule-B break-even of 28%."),
    "remilio": ("> **Verdict: not recommended.** A derivative of a founder-dependent parent (~1.3× Milady beta), "
                "trading below its mint price, with no identity independent of Remilia. Its scenario value is almost "
                "entirely the mania branch. Prefer Milady for Remilia exposure."),
    "azuki": ("> **Verdict on the held Azuki: exit patiently; do not sell into the current forced-selling bid.** It "
              "fails the mandate (founder-dependent; the company's IP strategy bypasses the NFT; −75% vs BTC in the "
              "weak scenario; beat BTC in 1% of historical 18-month windows held and 7% with rule B). Measured against "
              "selling at today's net bid (0.461 ETH), its rule-B scenario case is similar to the other PFPs, so there "
              "is no urgency. List near the prevailing floor after the 2026-11-12 Blend deadline clears (182 Blend + "
              "158 BendDAO tokens in escrow), or on any rebound. If you want to keep one NFT as a mania ticket, V1 is "
              "the better ticket on every mandate criterion."),
}
OC = pd.read_csv(os.path.join(PROC, "onchain", "collector_comparison.csv")).set_index("collection")
LP = pd.read_csv(os.path.join(PROC, "liquidity_position.csv")).set_index("key")
OB = pd.read_csv(os.path.join(PROC, "liquidity_orderbook.csv")).set_index("key")
SC = pd.read_csv(os.path.join(PROC, "scenarios.csv"))
BE = pd.read_csv(os.path.join(PROC, "breakeven.csv"))
EX = pd.read_csv(os.path.join(PROC, "exit_rule_backtest.csv"))
RA = pd.read_csv(os.path.join(PROC, "rally_analysis.csv")).set_index("name")


def pct(x, d=0):
    return "n/a" if pd.isna(x) else f"{x * 100:+.{d}f}%"


def tables(key):
    n = KEYS[key]
    u, oc, lp, ob, ra = U.loc[n], OC.loc[key], LP.loc[key], OB.loc[key], RA.loc[n]
    out = ["### Snapshot (2026-10-13)", "",
           "| Metric | Value | Source |", "|---|---|---|",
           f"| Floor (OpenSea stats / live ask) | {u.os_floor_eth:.3f} / {ob.floor_ask:.3f} ETH ≈ ${u.floor_usd:,.0f} ≈ {u.floor_btc:.4f} BTC | OpenSea API |",
           f"| Supply / holders / holders per item | {int(oc.supply):,} / {int(oc.holders):,} / {oc.holders / oc.supply:.2f} | on-chain |",
           f"| Floor-implied cap | ${u.floor_cap_usd_m:.1f}M | floor × supply |",
           f"| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | {pct(u.chg_btc_1y)} / {pct(u.chg_btc_2y)} / {pct(u.chg_btc_3y)} / {pct(u.drawdown_from_ath_btc)} | NPF + Binance |",
           f"| Rally trough→peak vs BTC (2024 / 2025) | {ra.R2024_mult_btc:.2f}× / {ra.R2025_mult_btc:.2f}× | rally_analysis.csv |",
           f"| Share of 2025 peak kept 180d later (BTC terms) | {ra.R2025_retain180_btc:.2f} | rally_analysis.csv |",
           f"| β of BTC-terms floor to ETH/BTC; annualised vol | {ra.beta_floorbtc_to_ethbtc:.2f}; {ra.ann_vol_floorbtc * 100:.0f}% | weekly, 2022–26 |",
           "", "### Collector behaviour (on-chain, head 2026-10-13)", "",
           "| Metric | Value |", "|---|---|",
           f"| Top-10 / top-50 holder share | {oc.top10_share * 100:.1f}% / {oc.top50_share * 100:.1f}% |",
           f"| Supply untouched 12m / 24m | {oc.supply_untouched_12m * 100:.0f}% / {oc.supply_untouched_24m * 100:.0f}% |",
           f"| EOA holders from 24m ago still holding | {oc.eoa_holders_retained_24m * 100:.0f}% |",
           f"| Median token age | {oc.median_token_age_days:,.0f} days |",
           f"| Lending escrow (all protocols) | {int(oc.lending_escrow_tokens)} tokens ({oc.lending_escrow_pct * 100:.1f}%) — {oc.lending_by_protocol} |",
           f"| Trailing-12m sales / unique buyers / dealer-churn share | {int(oc.t12m_sales):,} / {int(oc.t12m_unique_buyers):,} / {oc.t12m_churn_share * 100:.0f}% |",
           f"| Organic sales per day (365d, ex-churn, ex-flagged) | {oc['sales_per_day_365d_ex_suspect_ex_churn']:.1f} |",
           f"| Purchases by first-time wallets (t12m) | {oc.t12m_pct_sales_to_new_buyers * 100:.0f}% |",
           f"| Top-10 buyers' share of purchases (t12m) | {oc.t12m_top10_buyer_share * 100:.0f}% |",
           f"| Pre-2024 holders' net change (t12m) | {int(oc.t12m_net_change_pre2024):+,} tokens |",
           f"| Wash-type flags (share of t12m sales) | {oc.t12m_suspect_share * 100:.1f}% |",
           "", "### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)", "",
           "| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |",
           "|---|---|---|---|---|---|---|",
           f"| {int(lp.items_for_budget)} | {lp.entry_cost_eth:.3f} ETH | {lp.instant_exit_eth:.3f} ETH | {lp.roundtrip_haircut * 100:.1f}% | {ob.best_bid_pct_floor * 100:.0f}% | {int(ob.funded_bid_qty_ge_90pct_floor)} / {int(ob.funded_bid_qty_ge_80pct_floor)} | {lp.seller_fee * 100:.1f}% |",
           "", "### BTC-relative scenarios, ~18 months (v2 rule-based model; `reports/scenario_model.md`)", "",
           "| Scenario (ETH/BTC) | Floor peak / end (ETH multiple) | Return vs BTC: hold | Return vs BTC: rule B | Return in USD: rule B |",
           "|---|---|---|---|---|"]
    g = SC[SC.collection == key]
    for s, lab in [("S1_weak", "S1 weak (0.024)"), ("S2_moderate", "S2 moderate (0.032)"), ("S3_strong", "S3 strong (0.040)"),
                   ("S4_mania", "S4 mania (0.050)")]:
        h = g[(g.scenario == s) & (g.rule == "HOLD")].iloc[0]
        b = g[(g.scenario == s) & (g.rule == "B")].iloc[0]
        out.append(f"| {lab} | {h.P_eth:.2f}× / {h.E_eth:.2f}× | {pct(h.R_btc)} | {pct(b.R_btc)} | {pct(b.R_usd)} |")
    e = SC[(SC.collection == "ETH") & (SC.rule == "HOLD")]
    be = BE[(BE.collection == key) & (BE.variant == "base")].set_index("rule").breakeven
    beth = BE[(BE.collection == "ETH") & (BE.variant == "base") & (BE.rule == "HOLD")].breakeven.iloc[0]
    out.append("")
    out.append("Plain ETH vs BTC: " + ", ".join(f"{s.split('_')[0]} {pct(v)}" for s, v in zip(e.scenario, e.R_btc)) + ".")
    fmt = lambda v: "never" if pd.isna(v) else f"{v * 100:.0f}%"
    out.append(f"Break-even weight on S3+S4 (base mix): rule B {fmt(be['B'])}, hold {fmt(be['HOLD'])} "
               f"(ETH: {beth * 100:.0f}%). Rule B = once ≥1.5× vs BTC, sell on a 30% drawdown from peak.")
    x = EX[EX.collection == key].set_index("rule")
    out.append(f"History (350 overlapping 18-month windows, 2022-06→2025-04 starts): beat BTC in "
               f"{x.loc['HOLD', 'p_beat_btc'] * 100:.0f}% of windows holding, {x.loc['B', 'p_beat_btc'] * 100:.0f}% "
               f"with rule B; median multiple vs BTC {x.loc['HOLD', 'median_multiple_vs_btc']:.2f}× / "
               f"{x.loc['B', 'median_multiple_vs_btc']:.2f}× (`exit_rule_backtest.csv`).")
    return "\n".join(out)


if __name__ == "__main__":
    for key in KEYS:
        src = os.path.join(ROOT, "dossiers", "src", f"{key}.md")
        if not os.path.exists(src):
            continue
        txt = open(src).read().replace("<!-- TABLES -->", tables(key)).replace("<!-- VERDICT -->", VERDICT.get(key, ""))
        open(os.path.join(ROOT, "dossiers", f"{key}.md"), "w").write(txt)
        print("built", key)
