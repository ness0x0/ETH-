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
OC = pd.read_csv(os.path.join(PROC, "onchain", "collector_comparison.csv")).set_index("collection")
LP = pd.read_csv(os.path.join(PROC, "liquidity_position.csv")).set_index("key")
OB = pd.read_csv(os.path.join(PROC, "liquidity_orderbook.csv")).set_index("key")
SC = pd.read_csv(os.path.join(PROC, "scenarios.csv"))
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
           "", "### BTC-relative scenarios (18-month horizon; `reports/scenario_model.md`)", "",
           "| Scenario | ETH/BTC | Floor multiple (ETH) | Return vs BTC | Return in ETH | Return in USD |", "|---|---|---|---|---|---|"]
    g = SC[SC.collection == key]
    for _, r in g.iterrows():
        lab = {"S1_weak": "S1 weak", "S2_moderate": "S2 moderate", "S3_strong": "S3 strong", "S4_mania": "S4 mania"}[r.scenario]
        ex = "" if r.exit == "end-of-horizon" else f" ({r.exit})"
        out.append(f"| {lab}{ex} | {r.eth_btc:.3f} | {r.M_eth:.2f}× | {pct(r.R_btc)} | {pct(r.R_eth)} | {pct(r.R_usd)} |")
    e = SC[SC.collection == "ETH (benchmark)"].drop_duplicates("scenario")
    out.append("")
    out.append("For comparison, plain ETH vs BTC: " + ", ".join(
        f"{s.split('_')[0]} {pct(v)}" for s, v in zip(e.scenario, e.R_btc)) + ".")
    return "\n".join(out)


if __name__ == "__main__":
    for key in KEYS:
        src = os.path.join(ROOT, "dossiers", "src", f"{key}.md")
        if not os.path.exists(src):
            continue
        txt = open(src).read().replace("<!-- TABLES -->", tables(key))
        open(os.path.join(ROOT, "dossiers", f"{key}.md"), "w").write(txt)
        print("built", key)
