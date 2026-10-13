"""Holder quality, contract/escrow exposure, Blend + lending-escrow overhang and retention from Transfer logs.

Inputs   : data/raw/onchain/<key>_transfers.jsonl (onchain_fetch_transfers.py; full history to HEAD_BLOCK 26,186,366,
           2026-10-13T21:49:23Z), data/raw/onchain/codesize.json (onchain_codes.py), data/processed/onchain/
           address_labels.csv (onchain_labels.py).
Method   : ownership is replayed log-by-log (no chain breaks were found: every Transfer.from equals the replayed owner).
           Supply = tokens whose current owner is not 0x0/0x...dead/0x...1. "Holder" = address with >=1 token (wallet !=
           individual: one person can run many wallets; one Safe can represent a group). Contracts = non-empty code at
           head (EIP-7702-delegated EOAs counted as EOAs). Monthly snapshots are taken at 00:00 UTC on the first day of
           each month (= state at the end of the previous month) plus the head block.
Outputs  : data/processed/onchain/holders_summary.csv, holders_monthly_<key>.csv, top_holders_<key>.csv,
           blend_escrow_monthly.csv, lending_escrow_current.csv, retention.csv
Retention: (a) % of live supply whose last Transfer is older than 6/12/24 months before head (mint counts as a
           transfer); (b) of EOA addresses holding >=1 token at head-6/12/24 months, % still holding >=1 at head;
           (c) % of current supply held by EOAs that also held >=1 token at head-12/24 months. Contracts (incl. Safes and
           escrows) are EXCLUDED from (b)/(c); a variant counts an EOA as retained if a token it deposited into a
           lending escrow (Blend, Gondi, NFTfi...) is still in that escrow ("escrow-adjusted").
"""
import collections
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onchain_config import BLEND, COLLECTIONS, DEAD  # noqa: E402
import onchain_lib as L  # noqa: E402

CATS = ["lending", "amm_pool", "strategy_vault", "staking", "bridge_wrapper", "marketplace_escrow", "fractional_vault", "safe",
        "smart_wallet", "contract_unlabelled"]


def snapshot_metrics(bal):
    lb = L.live_balances(bal)
    supply = sum(lb.values())
    vals = sorted(lb.values(), reverse=True)
    cat_cnt = collections.Counter()
    eoa_holders = 0
    eoa_tokens = 0
    wallet_vals = []
    for a, n in lb.items():
        c = L.category(a)
        if c == "eoa":
            eoa_holders += 1
            eoa_tokens += n
        else:
            cat_cnt[c] += n
        if c in L.WALLET_CATS:
            wallet_vals.append(n)
    wallet_vals.sort(reverse=True)
    m = {"supply": supply, "holders": len(lb), "holders_eoa": eoa_holders,
         "top1_share": vals[0] / supply if vals else np.nan,
         "top10_share": sum(vals[:10]) / supply if vals else np.nan,
         "top50_share": sum(vals[:50]) / supply if vals else np.nan,
         "top10_wallet_share": sum(wallet_vals[:10]) / supply if vals else np.nan,
         "eoa_share": eoa_tokens / supply if supply else np.nan,
         "contract_share": sum(cat_cnt.values()) / supply if supply else np.nan,
         "blend_tokens": lb.get(BLEND, 0)}
    for c in CATS:
        m[f"{c}_share"] = cat_cnt.get(c, 0) / supply if supply else np.nan
    m["lending_tokens"] = cat_cnt.get("lending", 0)
    return m


def run(key, summary_rows, blend_rows, lend_rows, ret_rows):
    contract, slug, name = COLLECTIONS[key]
    df = L.load_transfers(key)
    head = L.HEAD
    start = df["ts"].iloc[0]
    cps = L.month_ends(start, head)
    ref = {m: head - pd.DateOffset(months=m) for m in (6, 12, 24)}
    ref_cps = sorted(ref.values())
    all_cps = sorted(set(cps) | set(ref_cps))
    monthly, ref_state = [], {}

    def on_cp(ts, owner, bal, last_t):
        if ts in cps:
            m = snapshot_metrics(bal)
            m["month_end"] = (ts - pd.Timedelta(seconds=1)).strftime("%Y-%m-%d")
            monthly.append(m)
        for k, v in ref.items():
            if ts == v:
                ref_state[k] = {a for a, n in L.live_balances(bal).items() if n > 0}

    owner, bal, last_t = L.replay(df, all_cps, on_cp)
    mh = snapshot_metrics(bal)
    mh["month_end"] = head.strftime("%Y-%m-%d") + " (head)"
    monthly.append(mh)
    mon = pd.DataFrame(monthly)
    mon.insert(0, "collection", key)
    mon = mon[["collection", "month_end"] + [c for c in mon.columns if c not in ("collection", "month_end")]]
    L.write_csv(mon, f"holders_monthly_{key}.csv")

    lb = L.live_balances(bal)
    supply = sum(lb.values())

    # ---- first-received / acquisition stats per address
    first_rx = df.groupby("to")["ts"].min()
    # token age per current holder
    tok_age = collections.defaultdict(list)
    for tid, a in owner.items():
        if a not in DEAD:
            tok_age[a].append((L.HEAD_TS - last_t[tid]) / 86400)
    # ---- top holders + all contracts
    ranked = sorted(lb.items(), key=lambda x: -x[1])
    rank = {a: i + 1 for i, (a, _) in enumerate(ranked)}
    rows = []
    labs = L.labels()
    for a, n in ranked:
        if rank[a] > 50 and not L.is_contract(a):
            continue
        lab = labs.get(a, {})
        rows.append({"collection": key, "rank": rank[a], "address": a, "tokens": n, "share": n / supply,
                     "type": "contract" if L.is_contract(a) else ("eoa_7702" if L.is_7702(a) else "eoa"),
                     "category": L.category(a), "protocol": L.protocol(a), "name": lab.get("name", ""),
                     "ens": lab.get("ens", ""), "first_received": first_rx.get(a).strftime("%Y-%m-%d"),
                     "median_token_age_days": round(float(np.median(tok_age[a])), 1) if tok_age[a] else np.nan,
                     "in_top50": rank[a] <= 50})
    top = pd.DataFrame(rows)
    L.write_csv(top, f"top_holders_{key}.csv")

    # ---- lending escrow current (by contract)
    for a, n in ranked:
        if L.category(a) == "lending":
            lend_rows.append({"collection": key, "protocol": L.protocol(a), "address": a,
                              "name": labs.get(a, {}).get("name", ""), "tokens": n, "pct_supply": n / supply})

    # ---- Blend + lending daily -> monthly since May 2023
    is_lend = {a: L.category(a) == "lending" for a in set(df["to"]) | set(df["f"])}
    proto = {a: L.protocol(a) for a, v in is_lend.items() if v}
    d = df[df["ts"] >= pd.Timestamp("2023-05-01", tz="UTC")].copy()
    # counts before the window
    pre = df[df["ts"] < pd.Timestamp("2023-05-01", tz="UTC")]
    cnt = collections.Counter()
    for fr, to in zip(pre["f"].values, pre["to"].values):
        if is_lend.get(fr):
            cnt[proto[fr]] -= 1
        if is_lend.get(to):
            cnt[proto[to]] += 1
    daily = []
    cur_day = None
    for t, fr, to in zip(d["ts"].dt.floor("D").values, d["f"].values, d["to"].values):
        if cur_day is not None and t != cur_day:
            daily.append((cur_day, dict(cnt)))
        cur_day = t
        if is_lend.get(fr):
            cnt[proto[fr]] -= 1
        if is_lend.get(to):
            cnt[proto[to]] += 1
    if cur_day is not None:
        daily.append((cur_day, dict(cnt)))
    dd = pd.DataFrame([{"day": pd.Timestamp(t), **c} for t, c in daily]).fillna(0)
    if len(dd):
        dd = dd.set_index("day").asfreq("D", method="ffill")
        protos = [c for c in dd.columns]
        dd["lending_total"] = dd[protos].sum(axis=1)
        if "blur_blend" not in dd:
            dd["blur_blend"] = 0
        g = dd.groupby(dd.index.to_period("M"))
        for per, gg in g:
            last = gg.iloc[-1]
            row = {"collection": key, "month": str(per), "supply": supply,
                   "blend_month_end": int(last["blur_blend"]), "blend_pct_month_end": last["blur_blend"] / supply,
                   "blend_max_daily": int(gg["blur_blend"].max()), "blend_min_daily": int(gg["blur_blend"].min()),
                   "lending_total_month_end": int(last["lending_total"]),
                   "lending_total_pct_month_end": last["lending_total"] / supply,
                   "lending_total_max_daily": int(gg["lending_total"].max())}
            for p_ in protos:
                if p_ != "blur_blend":
                    row[f"{p_}_month_end"] = int(last[p_])
            blend_rows.append(row)

    # ---- retention
    live_tokens = [tid for tid, a in owner.items() if a not in DEAD]
    eoa_held_tokens = [tid for tid in live_tokens if L.category(owner[tid]) == "eoa"]
    # escrow depositor attribution (last transfer into a lending contract for tokens still there)
    depositor = {}
    last_in = {}
    for fr, to, tid in zip(df["f"].values, df["to"].values, df["id"].values):
        if is_lend.get(to):
            last_in[tid] = fr
    for tid in live_tokens:
        if is_lend.get(owner[tid]) and tid in last_in:
            depositor[tid] = last_in[tid]
    escrow_owners = collections.Counter(depositor.values())
    eoa_now = {a for a in lb if L.category(a) == "eoa"}
    r = {"collection": key, "supply": supply, "head_utc": head.strftime("%Y-%m-%dT%H:%M:%SZ")}
    for m in (6, 12, 24):
        cutoff = ref[m].timestamp()
        r[f"a_supply_untouched_{m}m"] = np.mean([last_t[t] < cutoff for t in live_tokens])
        r[f"a_eoa_held_untouched_{m}m"] = np.mean([last_t[t] < cutoff for t in eoa_held_tokens]) \
            if eoa_held_tokens else np.nan
        held = ref_state.get(m, set())
        eoa_then = {a for a in held if L.category(a) == "eoa"}
        r[f"b_eoa_holders_{m}m_ago"] = len(eoa_then)
        r[f"b_still_holding_{m}m"] = len(eoa_then & eoa_now) / len(eoa_then) if eoa_then else np.nan
        r[f"b_still_holding_{m}m_escrow_adj"] = len(eoa_then & (eoa_now | set(escrow_owners))) / len(eoa_then) \
            if eoa_then else np.nan
        if m in (12, 24):
            num = sum(lb[a] for a in eoa_now & eoa_then)
            r[f"c_supply_held_by_{m}m_eoa_holders"] = num / supply
            r[f"c_eoa_supply_held_by_{m}m_eoa_holders"] = num / sum(lb[a] for a in eoa_now) if eoa_now else np.nan
    ret_rows.append(r)

    # ---- summary
    bal_counts = np.array(list(lb.values()))
    eoa_bal = np.array([n for a, n in lb.items() if L.category(a) == "eoa"])
    lend = collections.Counter()
    for a, n in lb.items():
        if L.category(a) == "lending":
            lend[L.protocol(a)] += n
    cat_tok = collections.Counter()
    for a, n in lb.items():
        cat_tok[L.category(a)] += n
    s = {"collection": key, "name": name, "contract": contract, "head_block": L.HEAD_BLOCK,
         "head_utc": head.strftime("%Y-%m-%dT%H:%M:%SZ"), "tokens_ever": len(owner), "supply_live": supply,
         "transfers": len(df), "holders": len(lb), "holders_eoa": int((eoa_bal > 0).sum()),
         "holders_eoa_7702": sum(1 for a in lb if L.is_7702(a)),
         "holders_contract": sum(1 for a in lb if L.is_contract(a)),
         "tokens_per_holder": supply / len(lb), "pct_holders_1_token": float((bal_counts == 1).mean()),
         "holders_ge5": int((bal_counts >= 5).sum()), "holders_ge10": int((bal_counts >= 10).sum()),
         "share_in_wallets_ge10_eoa": float(eoa_bal[eoa_bal >= 10].sum() / supply),
         "top1_share": mh["top1_share"], "top10_share": mh["top10_share"], "top50_share": mh["top50_share"],
         "top10_wallet_share": mh["top10_wallet_share"], "eoa_share": mh["eoa_share"],
         "contract_share": mh["contract_share"]}
    for c in CATS:
        s[f"{c}_share"] = cat_tok.get(c, 0) / supply
    s["blend_tokens"] = lb.get(BLEND, 0)
    s["blend_pct"] = lb.get(BLEND, 0) / supply
    s["lending_total_tokens"] = sum(lend.values())
    s["lending_total_pct"] = sum(lend.values()) / supply
    s["lending_by_protocol"] = "; ".join(f"{k}:{v}" for k, v in lend.most_common())
    s["median_token_age_days"] = float(np.median([(L.HEAD_TS - last_t[t]) / 86400 for t in live_tokens]))
    summary_rows.append(s)
    print(key, "supply", supply, "holders", len(lb), "blend", lb.get(BLEND, 0), "lending", dict(lend), flush=True)


def main():
    keys = sys.argv[1:] or list(COLLECTIONS)
    summary_rows, blend_rows, lend_rows, ret_rows = [], [], [], []
    for k in keys:
        run(k, summary_rows, blend_rows, lend_rows, ret_rows)
    L.write_csv(pd.DataFrame(summary_rows), "holders_summary.csv")
    L.write_csv(pd.DataFrame(blend_rows), "blend_escrow_monthly.csv")
    L.write_csv(pd.DataFrame(lend_rows), "lending_escrow_current.csv")
    L.write_csv(pd.DataFrame(ret_rows), "retention.csv")


if __name__ == "__main__":
    main()
