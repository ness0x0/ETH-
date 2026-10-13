"""Build the one-row-per-collection comparison table used in reports/onchain_collector_analysis.md.

Inputs: holders_summary.csv, retention.csv, buyers_summary.csv (t12m), liquidity_summary.csv, reconciliation.csv,
cohort_flows.csv, blend_escrow_monthly.csv, entity_accumulators_t12m.csv (all in data/processed/onchain/).
Output: data/processed/onchain/collector_comparison.csv
"""
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onchain_config import PROC_ON  # noqa: E402


def rd(n):
    return pd.read_csv(os.path.join(PROC_ON, n))


def main():
    h = rd("holders_summary.csv").set_index("collection")
    r = rd("retention.csv").set_index("collection")
    b = rd("buyers_summary.csv")
    b = b[b["window"] == "t12m"].set_index("collection")
    liq = rd("liquidity_summary.csv")
    rc = rd("reconciliation.csv").set_index("collection")
    c = rd("cohort_flows.csv")
    c = c[c["window"] == "t12m"]
    bl = rd("blend_escrow_monthly.csv")
    ent = rd("entity_accumulators_t12m.csv")
    out = pd.DataFrame(index=h.index)
    out["supply"] = h["supply_live"]
    out["holders"] = h["holders"]
    out["opensea_owners_2026_10_13"] = rc["opensea_owners"]
    out["holders_eoa"] = h["holders_eoa"]
    out["pct_holders_1_token"] = h["pct_holders_1_token"]
    out["top1_share"] = h["top1_share"]
    out["top10_share"] = h["top10_share"]
    out["top50_share"] = h["top50_share"]
    out["contract_share"] = h["contract_share"]
    out["safe_share"] = h["safe_share"]
    out["lending_escrow_tokens"] = h["lending_total_tokens"]
    out["lending_escrow_pct"] = h["lending_total_pct"]
    out["lending_by_protocol"] = h["lending_by_protocol"]
    out["blend_tokens"] = h["blend_tokens"]
    out["blend_pct"] = h["blend_pct"]
    for k in out.index:
        g = bl[bl["collection"] == k]
        if len(g):
            i = g["blend_max_daily"].idxmax()
            out.loc[k, "blend_peak_tokens"] = g.loc[i, "blend_max_daily"]
            out.loc[k, "blend_peak_month"] = g.loc[i, "month"]
            yr = g[g["month"] == "2025-10"]
            out.loc[k, "lending_escrow_tokens_2025_10"] = yr["lending_total_month_end"].iloc[0] if len(yr) else None
    out["strategy_vault_share"] = h["strategy_vault_share"]
    out["amm_pool_share"] = h["amm_pool_share"]
    out["median_token_age_days"] = h["median_token_age_days"]
    for m in (12, 24):
        out[f"supply_untouched_{m}m"] = r[f"a_supply_untouched_{m}m"]
        out[f"eoa_holders_retained_{m}m"] = r[f"b_still_holding_{m}m"]
        out[f"supply_held_by_{m}m_eoa_holders"] = r[f"c_supply_held_by_{m}m_eoa_holders"]
    for col in ["sales", "unique_buyers", "new_buyers", "pct_buyers_new", "pct_sales_to_new_buyers",
                "top10_buyer_share", "churn_share", "suspect_share", "non_churn_sales", "median_price",
                "median_price_to_npf_floor", "volume_eth", "strategy_contract_buys"]:
        out[f"t12m_{col}"] = b[col]
    for d in (30, 90, 365):
        for v in ("all", "ex_suspect_ex_churn"):
            x = liq[(liq["trailing_days"] == d) & (liq["variant"] == v)].set_index("collection")
            out[f"sales_per_day_{d}d_{v}"] = x["sales_per_day"]
            out[f"median_gap_hours_{d}d_{v}"] = x["median_gap_hours"]
    out["npf_sales_gap_pct"] = rc["sales_gap_pct"]
    out["npf_bar_corr"] = rc["bar_corr_sales"]
    pv = c.pivot_table(index="collection", columns="cohort", values="net_change")
    for col in ["0_new", "1_4", "5_19", "ge20", "pre2024"]:
        if col in pv:
            out[f"t12m_net_change_{col}"] = pv[col]
    acc = ent[ent["side"] == "accumulator"].groupby("collection").head(1).set_index("collection")
    out["top_accumulator_entity"] = acc["entity_root"]
    out["top_accumulator_net"] = acc["net_change"]
    out["top_accumulator_t12m_buy_share"] = acc["t12m_buy_share"]
    dis = ent[ent["side"] == "distributor"].groupby("collection").head(1).set_index("collection")
    out["top_distributor_entity"] = dis["entity_root"]
    out["top_distributor_net"] = dis["net_change"]
    out.reset_index().to_csv(os.path.join(PROC_ON, "collector_comparison.csv"), index=False)
    print(out.T.to_string())


if __name__ == "__main__":
    main()
