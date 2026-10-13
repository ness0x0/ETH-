"""Buyer behaviour, wash/affiliation indicators, exit-liquidity and NFTPriceFloor reconciliation from classified sales.

Inputs   : data/processed/onchain/movements_<key>.csv (onchain_sales.py), full Transfer history
           (data/raw/onchain/<key>_transfers.jsonl), NFTPriceFloor 3-day bars
           (data/raw/nftpricefloor/charts_<slug>.json, fetched 2026-10-13 by screen_universe.py).
Windows  : t12m = 2025-10-13T00:00Z .. head (2026-10-13T21:49Z); milady_2023 = 2023-04-15..2023-07-15;
           pudgy_2024 = 2024-11-01..2025-02-15. Partial months at window edges are marked partial=True.
Definitions
  sale            : movement typed "sale" by onchain_sales.py (price > 0.001 ETH or non-ETH currency).
  new buyer       : the buyer address had never received a token of the collection before the sale tx (from the
                    full Transfer history since mint, incl. mints/gifts). Wallet-level, not person-level.
  size cohort     : buyer/seller balance immediately before the sale tx: 0, 1-4, >=5 tokens.
  tenure cohort   : first receipt of any token of the collection before 2024-01-01 ("pre2024") or later.
  net flow        : buys - sells by addresses of the cohort (sales only; gifts/escrow moves excluded).
  floor proxy     : NFTPriceFloor floorNative (3-day bar containing the sale) and on-chain 10th percentile price.
Wash / affiliated-support indicators (flags, not proof):
  round_trip_30d  : sold A->B and the token returned B->A (any transfer) within 30 days.
  hot_token_3in30 : the token sold >=3 times within 30 days.
  price_hi_3x / price_lo_half: price > 3x or < 0.5x the trailing 30-day median sale price (>=10 prior sales).
  linked_wallets  : buyer and seller exchanged a token of this collection via a non-sale transfer at any time.
  self_trade      : buyer == seller after escrow attribution.
  bid_cluster     : buyer took >=25% of the month's bid-fill sales and >=10 fills (one or two wallets absorbing
                    floor bids — liquidity support that may be affiliated or a market maker).
Outputs  : buyers_monthly_<key>.csv, buyers_summary.csv, wash_flags.csv, wash_summary.csv, liquidity_summary.csv,
           reconciliation.csv, reconciliation_bars_<key>.csv
"""
import collections
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onchain_config import COLLECTIONS, PROC_ON, RAW  # noqa: E402
import onchain_lib as L  # noqa: E402

WINDOWS = {"t12m": ("2025-10-13", None), "milady_2023": ("2023-04-15", "2023-07-16"),
           "pudgy_2024": ("2024-11-01", "2025-02-16")}
WIN_KEYS = {"milady": ["t12m", "milady_2023"], "pudgy": ["t12m", "pudgy_2024"]}


def win_bounds(w):
    a, b = WINDOWS[w]
    return pd.Timestamp(a, tz="UTC"), (pd.Timestamp(b, tz="UTC") if b else L.HEAD + pd.Timedelta(seconds=1))


def npf_bars(slug):
    p = os.path.join(RAW, "nftpricefloor", f"charts_{slug}.json")
    d = json.load(open(p))["data"]
    df = pd.DataFrame({"ts": pd.to_datetime(d["timestamps"], unit="ms", utc=True), "floor": d["floorNative"],
                       "sales": d["salesCount"], "vol": d["volumeNative"]})
    # drop the live (partial, non-midnight) point NPF appends at fetch time; bars are at 00:00 UTC every 3 days
    df = df[df["ts"] == df["ts"].dt.normalize()]
    return df.sort_values("ts").reset_index(drop=True)


def load_moves(key):
    mv = pd.read_csv(os.path.join(PROC_ON, f"movements_{key}.csv"), dtype={"flags": str, "side": str})
    mv["ts"] = pd.to_datetime(mv["ts"], utc=True)
    mv["flags"] = mv["flags"].fillna("")
    mv["side"] = mv["side"].fillna("")
    return mv


def balances_before(df, txs):
    """(tx, addr) -> balance before the tx, for txs in `txs`; also first receipt ts per address."""
    bal = collections.Counter()
    out = {}
    for tx, f, to in zip(df["tx"].values, df["f"].values, df["to"].values):
        if tx in txs:
            for a in (f, to):
                if (tx, a) not in out:
                    out[(tx, a)] = bal[a]
        bal[f] -= 1
        bal[to] += 1
    return out


def size_cohort(n):
    return "0" if n <= 0 else ("1_4" if n < 5 else "ge5")


def run(key, out):
    contract, slug, name = COLLECTIONS[key]
    mv = load_moves(key)
    df = L.load_transfers(key)
    first_rx = df.groupby("to")["t"].min()
    sales = mv[mv["type"] == "sale"].copy()
    sales["t"] = ((sales["ts"] - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(seconds=1)).astype("int64")
    bb = balances_before(df, set(sales["tx"]))
    sales["buyer_bal_before"] = [bb.get((tx, b), 0) for tx, b in zip(sales["tx"], sales["buyer"])]
    sales["seller_bal_before"] = [bb.get((tx, s), 0) for tx, s in zip(sales["tx"], sales["seller"])]
    sales["new_buyer"] = [(b not in first_rx.index) or (first_rx[b] >= t) for b, t in zip(sales["buyer"],
                                                                                         sales["t"])]
    cut = int(pd.Timestamp("2024-01-01", tz="UTC").timestamp())
    sales["buyer_tenure"] = ["pre2024" if (b in first_rx.index and first_rx[b] < cut) else "post2024"
                             for b in sales["buyer"]]
    sales["seller_tenure"] = ["pre2024" if (s in first_rx.index and first_rx[s] < cut) else "post2024"
                              for s in sales["seller"]]
    sales["month"] = sales["ts"].dt.strftime("%Y-%m")
    bars = npf_bars(slug)
    # floor at sale: NPF bar with ts <= sale ts (latest)
    bi = np.searchsorted(bars["ts"].values.astype("datetime64[ns]"),
                         sales["ts"].dt.tz_localize(None).values.astype("datetime64[ns]"), side="right") - 1
    sales["npf_floor"] = [bars["floor"].iloc[i] if i >= 0 else np.nan for i in bi]

    # ---------------- wash / affiliation flags
    sales = sales.sort_values("ts").reset_index(drop=True)
    flags = collections.defaultdict(set)
    # round trip: token returns to seller within 30 days (any transfer, full history)
    by_tok = df.groupby("id")
    tok_moves = {tid: g[["t", "f", "to"]].values for tid, g in by_tok}
    for i, r in sales.iterrows():
        mvs = tok_moves.get(r["tokenId"])
        if mvs is None:
            continue
        later = mvs[(mvs[:, 0] > r["t"]) & (mvs[:, 0] <= r["t"] + 30 * 86400)]
        if any(to == r["seller"] for _, _, to in later):
            flags[i].add("round_trip_30d")
    # hot token: >=3 sales of same token within 30 days
    for tid, g in sales.groupby("tokenId"):
        ts = g["t"].values
        idx = g.index.values
        for j in range(len(ts)):
            k = np.searchsorted(ts, ts[j] + 30 * 86400, side="right")
            if k - j >= 3:
                for q in idx[j:k]:
                    flags[q].add("hot_token_3in30")
    # price outliers vs trailing 30d median (>=10 prior priced sales)
    pr = sales[sales["price_eth"].notna()][["ts", "price_eth"]].set_index("ts")["price_eth"]
    med = pr.rolling("30D", closed="left", min_periods=10).median()
    sales.loc[sales["price_eth"].notna(), "trail30_median"] = med.values
    for i, r in sales.iterrows():
        m = r.get("trail30_median")
        if pd.notna(m) and pd.notna(r["price_eth"]):
            if r["price_eth"] > 3 * m:
                flags[i].add("price_hi_3x")
            elif r["price_eth"] < 0.5 * m:
                flags[i].add("price_lo_half")
    # linked wallets: non-sale transfer between buyer and seller at any time (either direction)
    sale_keys = set(zip(mv.loc[mv["type"] == "sale", "tx"], mv.loc[mv["type"] == "sale", "tokenId"]))
    pairs = set()
    for tx, f, to, tid in zip(df["tx"].values, df["f"].values, df["to"].values, df["id"].values):
        if (tx, tid) not in sale_keys and f not in L.DEAD and to not in L.DEAD and to != f:
            pairs.add((f, to))
    for i, r in sales.iterrows():
        wallets = L.category(r["seller"]) in L.WALLET_CATS and L.category(r["buyer"]) in L.WALLET_CATS
        if wallets and ((r["seller"], r["buyer"]) in pairs or (r["buyer"], r["seller"]) in pairs):
            flags[i].add("linked_wallets")
        if r["buyer"] == r["seller"]:
            flags[i].add("self_trade")
    # bid cluster
    for mth, g in sales[sales["side"] == "bid"].groupby("month"):
        vc = g["buyer"].value_counts()
        for b, n in vc.items():
            if n >= 10 and n / len(g) >= 0.25:
                for q in g.index[g["buyer"] == b]:
                    flags[q].add("bid_cluster")
    sales["wash_flags"] = [";".join(sorted(flags[i])) for i in sales.index]
    strong = {"round_trip_30d", "hot_token_3in30", "self_trade", "linked_wallets"}
    sales["suspect"] = [bool(flags[i] & strong) for i in sales.index]

    wf = sales[sales["wash_flags"] != ""][["block", "ts", "tx", "tokenId", "seller", "buyer", "price_eth", "method",
                                            "side", "trail30_median", "wash_flags"]].copy()
    wf.insert(0, "collection", key)
    out["wash"].append(wf)

    # ---------------- per-window monthly buyer behaviour
    rows = []
    for w in WIN_KEYS.get(key, ["t12m"]):
        a, b = win_bounds(w)
        s = sales[(sales["ts"] >= a) & (sales["ts"] < b)]
        if s.empty:
            continue
        for mth, g in s.groupby("month"):
            ms = pd.Timestamp(mth + "-01", tz="UTC")
            me = ms + pd.offsets.MonthBegin(1)
            vc = g["buyer"].value_counts()
            bids = g[g["side"] == "bid"]
            bvc = bids["buyer"].value_counts()
            new_b = g.loc[g["new_buyer"], "buyer"].nunique()
            r = {"collection": key, "window": w, "month": mth, "partial": bool(ms < a or me > b),
                 "sales": len(g), "priced_sales": int(g["price_eth"].notna().sum()),
                 "volume_eth": g["price_eth"].sum(), "median_price": g["price_eth"].median(),
                 "p10_price": g["price_eth"].quantile(0.1), "npf_floor_mean": g["npf_floor"].mean(),
                 "median_price_to_npf_floor": g["price_eth"].median() / g["npf_floor"].mean(),
                 "unique_buyers": g["buyer"].nunique(), "unique_sellers": g["seller"].nunique(),
                 "new_buyers": new_b, "returning_buyers": g["buyer"].nunique() - new_b,
                 "pct_sales_to_new_buyers": g["new_buyer"].mean(),
                 "top1_buyer_share": vc.iloc[0] / len(g), "top10_buyer_share": vc.iloc[:10].sum() / len(g),
                 "bid_fill_share": len(bids) / len(g),
                 "top2_bidder_share_of_bid_fills": (bvc.iloc[:2].sum() / len(bids)) if len(bids) else np.nan,
                 "suspect_sales": int(g["suspect"].sum()),
                 "blend_share_of_sales": g["method"].eq("blend_buy_locked").mean()
                 + g["flags"].str.contains("blend_buy_to_borrow").mean()}
            for coh in ("0", "1_4", "ge5"):
                buys = (g["buyer_bal_before"].map(size_cohort) == coh).sum()
                sells = (g["seller_bal_before"].map(size_cohort) == coh).sum()
                r[f"net_size_{coh}"] = int(buys - sells)
            for coh in ("pre2024", "post2024"):
                r[f"net_tenure_{coh}"] = int((g["buyer_tenure"] == coh).sum() - (g["seller_tenure"] == coh).sum())
            rows.append(r)
        vc = s["buyer"].value_counts()
        out["buyers_summary"].append({
            "collection": key, "window": w, "start": a.strftime("%Y-%m-%d"), "end": b.strftime("%Y-%m-%d"),
            "sales": len(s), "priced_sales": int(s["price_eth"].notna().sum()), "volume_eth": s["price_eth"].sum(),
            "median_price": s["price_eth"].median(),
            "unique_buyers": s["buyer"].nunique(), "unique_sellers": s["seller"].nunique(),
            "new_buyers": s.loc[s["new_buyer"], "buyer"].nunique(),
            "pct_buyers_new": s.loc[s["new_buyer"], "buyer"].nunique() / s["buyer"].nunique(),
            "pct_sales_to_new_buyers": s["new_buyer"].mean(),
            "top1_buyer_share": vc.iloc[0] / len(s), "top10_buyer_share": vc.iloc[:10].sum() / len(s),
            "top1_buyer": vc.index[0], "bid_fill_share": (s["side"] == "bid").mean(),
            "suspect_share": s["suspect"].mean(),
            "net_size_ge5": int((s["buyer_bal_before"] >= 5).sum() - (s["seller_bal_before"] >= 5).sum()),
            "net_size_1_4": int(((s["buyer_bal_before"] >= 1) & (s["buyer_bal_before"] < 5)).sum()
                                - ((s["seller_bal_before"] >= 1) & (s["seller_bal_before"] < 5)).sum()),
            "net_size_0_new_entrants": int((s["buyer_bal_before"] == 0).sum() - (s["seller_bal_before"] == 0).sum()),
            "net_tenure_pre2024": int((s["buyer_tenure"] == "pre2024").sum() - (s["seller_tenure"] == "pre2024").sum()),
            "net_tenure_post2024": int((s["buyer_tenure"] == "post2024").sum()
                                       - (s["seller_tenure"] == "post2024").sum()),
            "median_price_to_npf_floor": s["price_eth"].median() / s["npf_floor"].median(),
            "methods": "; ".join(f"{k}:{v}" for k, v in s["method"].value_counts().items()),
            "flag_counts": "; ".join(f"{k}:{v}" for k, v in collections.Counter(
                f for x in s["wash_flags"] for f in x.split(";") if f).most_common())})
    bm = pd.DataFrame(rows)
    L.write_csv(bm, f"buyers_monthly_{key}.csv")

    # ---------------- liquidity (trailing windows from head)
    for days in (30, 90, 365):
        s = sales[sales["ts"] >= L.HEAD - pd.Timedelta(days=days)]
        for variant, ss in (("all", s), ("ex_suspect", s[~s["suspect"]])):
            gaps = ss["ts"].sort_values().diff().dt.total_seconds().dropna() / 3600
            out["liq"].append({"collection": key, "trailing_days": days, "variant": variant, "sales": len(ss),
                               "sales_per_day": len(ss) / days,
                               "median_gap_hours": gaps.median() if len(gaps) else np.nan,
                               "p90_gap_hours": gaps.quantile(0.9) if len(gaps) else np.nan,
                               "volume_eth": ss["price_eth"].sum(), "median_price": ss["price_eth"].median(),
                               "unique_buyers": ss["buyer"].nunique(), "unique_sellers": ss["seller"].nunique(),
                               "unique_tokens": ss["tokenId"].nunique(),
                               "bid_fill_share": (ss["side"] == "bid").mean() if len(ss) else np.nan})

    # ---------------- reconciliation vs NFTPriceFloor 3-day bars (t12m)
    a, b = win_bounds("t12m")
    s = sales[(sales["ts"] >= a) & (sales["ts"] < b)]
    allmv = mv[(mv["ts"] >= a) & (mv["ts"] < b)]
    bars_w = bars[(bars["ts"] >= a) & (bars["ts"] <= b)].copy()
    res = {}
    for align in ("start", "end"):
        recs = []
        for i in range(len(bars_w)):
            t0 = bars_w["ts"].iloc[i]
            lo, hi = (t0, t0 + pd.Timedelta(days=3)) if align == "start" else (t0 - pd.Timedelta(days=3), t0)
            if lo < a or hi > b:
                continue
            ss = s[(s["ts"] >= lo) & (s["ts"] < hi)]
            recs.append({"bar_ts": t0, "lo": lo, "hi": hi, "npf_sales": bars_w["sales"].iloc[i],
                         "npf_vol": bars_w["vol"].iloc[i], "onchain_sales": len(ss),
                         "onchain_vol": ss["price_eth"].sum()})
        rb = pd.DataFrame(recs)
        corr = rb[["npf_sales", "onchain_sales"]].corr().iloc[0, 1] if len(rb) > 3 else np.nan
        res[align] = (corr, rb)
    best = max(res, key=lambda k: (res[k][0] if pd.notna(res[k][0]) else -9))
    corr, rb = res[best]
    rb.insert(0, "collection", key)
    L.write_csv(rb, f"reconciliation_bars_{key}.csv")
    lo, hi = rb["lo"].min(), rb["hi"].max()
    ss = s[(s["ts"] >= lo) & (s["ts"] < hi)]
    am = allmv[(allmv["ts"] >= lo) & (allmv["ts"] < hi)]
    n_np, v_np = rb["npf_sales"].sum(), rb["npf_vol"].sum()
    out["recon"].append({
        "collection": key, "npf_slug": slug, "period_start": lo.strftime("%Y-%m-%d"),
        "period_end": hi.strftime("%Y-%m-%d"), "npf_bar_alignment": best, "bars": len(rb),
        "npf_sales": int(n_np), "onchain_sales": len(ss), "sales_gap_pct": (len(ss) - n_np) / n_np if n_np else np.nan,
        "npf_volume_eth": v_np, "onchain_volume_eth": ss["price_eth"].sum(),
        "volume_gap_pct": (ss["price_eth"].sum() - v_np) / v_np if v_np else np.nan,
        "bar_corr_sales": corr,
        "bar_corr_volume": rb[["npf_vol", "onchain_vol"]].corr().iloc[0, 1] if len(rb) > 3 else np.nan,
        "onchain_movements_all": len(am), "onchain_non_sale_movements": int((am["type"] != "sale").sum()),
        "onchain_zero_price_trades": int((am["type"] == "zero_price_trade").sum()),
        "onchain_sales_fallback_priced": int(ss["flags"].str.contains("price_from_fallback").sum()),
        "onchain_sales_unpriced": int(ss["price_eth"].isna().sum()),
        "onchain_sales_blend_buy_locked": int((ss["method"] == "blend_buy_locked").sum()),
        "onchain_sales_amm": int(ss["method"].isin(["nftx", "sudoswap_v2"]).sum())})
    sales.to_csv(os.path.join(PROC_ON, f"sales_enriched_{key}.csv"), index=False)
    print(key, "sales", len(sales), "suspect", int(sales["suspect"].sum()), "recon", out["recon"][-1]["sales_gap_pct"],
          best, round(corr, 3) if pd.notna(corr) else None, flush=True)


def main():
    keys = sys.argv[1:] or [k for k in COLLECTIONS if os.path.exists(os.path.join(PROC_ON, f"movements_{k}.csv"))]
    out = collections.defaultdict(list)
    for k in keys:
        run(k, out)
    L.write_csv(pd.DataFrame(out["buyers_summary"]), "buyers_summary.csv")
    L.write_csv(pd.concat(out["wash"]) if out["wash"] else pd.DataFrame(), "wash_flags.csv")
    L.write_csv(pd.DataFrame(out["liq"]), "liquidity_summary.csv")
    L.write_csv(pd.DataFrame(out["recon"]), "reconciliation.csv")
    w = pd.concat(out["wash"]) if out["wash"] else pd.DataFrame()
    if len(w):
        rows = []
        for k, g in w.groupby("collection"):
            c = collections.Counter(f for x in g["wash_flags"] for f in x.split(";") if f)
            rows.append({"collection": k, **c})
        L.write_csv(pd.DataFrame(rows).fillna(0), "wash_summary.csv")


if __name__ == "__main__":
    main()
