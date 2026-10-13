"""Shared loaders and helpers for the onchain_* analysis scripts (no network access here)."""
import datetime as dt
import json
import os

import numpy as np
import pandas as pd

from onchain_config import (BLEND, COLLECTIONS, DEAD, HEAD_BLOCK, HEAD_TS, PROC_ON, RAW_ON, token_filter)  # noqa: F401

HEAD = pd.Timestamp(HEAD_TS, unit="s", tz="UTC")  # 2026-10-13T21:49:23Z


def load_transfers(key):
    rows = []
    with open(os.path.join(RAW_ON, f"{key}_transfers.jsonl")) as f:
        for line in f:
            r = json.loads(line)
            if token_filter(key, r["id"]):
                rows.append((r["b"], r["t"], r["tx"], r["ti"], r["li"], r["f"], r["to"], r["id"]))
    df = pd.DataFrame(rows, columns=["b", "t", "tx", "ti", "li", "f", "to", "id"])
    df = df.sort_values(["b", "li"]).reset_index(drop=True)
    df["ts"] = pd.to_datetime(df["t"], unit="s", utc=True)
    return df


_codes = None


def codes():
    global _codes
    if _codes is None:
        _codes = json.load(open(os.path.join(RAW_ON, "codesize.json")))["data"]
    return _codes


def is_contract(addr):
    v = codes().get(addr)
    if v is None or addr in DEAD:
        return False
    return v["size"] > 0 and not v["7702"]


def is_7702(addr):
    v = codes().get(addr)
    return bool(v and v["7702"])


_labels = None


def labels():
    """address -> dict(category, protocol, name, ens) from data/processed/onchain/address_labels.csv."""
    global _labels
    if _labels is None:
        p = os.path.join(PROC_ON, "address_labels.csv")
        _labels = {}
        if os.path.exists(p):
            d = pd.read_csv(p, dtype=str).fillna("")
            for r in d.itertuples():
                _labels[r.address] = {"category": r.category, "protocol": r.protocol, "name": r.name,
                                      "ens": r.ens}
    return _labels


def category(addr):
    if addr in DEAD:
        return "burn"
    if addr == BLEND:
        return "lending"
    lab = labels().get(addr)
    if lab and lab["category"]:
        return lab["category"]
    if is_contract(addr):
        return "contract_unlabelled"
    return "eoa"


def protocol(addr):
    if addr == BLEND:
        return "blur_blend"
    lab = labels().get(addr)
    return lab["protocol"] if lab else ""


ESCROW_CATS = {"lending", "amm_pool", "strategy_vault", "staking", "bridge_wrapper", "marketplace_escrow",
               "fractional_vault"}
WALLET_CATS = {"eoa", "safe", "smart_wallet"}


def month_ends(start_ts, end_ts):
    """List of UTC month boundaries (first instant of next month) between start and end."""
    s = pd.Timestamp(start_ts).tz_convert("UTC") if pd.Timestamp(start_ts).tzinfo else pd.Timestamp(start_ts, tz="UTC")
    cur = pd.Timestamp(year=s.year, month=s.month, day=1, tz="UTC") + pd.offsets.MonthBegin(1)
    out = []
    while cur <= end_ts:
        out.append(cur)
        cur = cur + pd.offsets.MonthBegin(1)
    return out


def replay(df, checkpoints, on_checkpoint):
    """Replay transfers in order; at each checkpoint timestamp (ascending, tz-aware) call
    on_checkpoint(ts, owner: dict id->addr, bal: dict addr->n, last_t: dict id->unix ts). Returns final state."""
    owner, bal, last_t = {}, {}, {}
    cps = list(checkpoints)
    ci = 0
    ts_arr = df["t"].values
    f_arr, to_arr, id_arr = df["f"].values, df["to"].values, df["id"].values
    cp_unix = [int(c.timestamp()) for c in cps]
    for i in range(len(df)):
        t = ts_arr[i]
        while ci < len(cps) and t >= cp_unix[ci]:
            on_checkpoint(cps[ci], owner, bal, last_t)
            ci += 1
        fr, to, tid = f_arr[i], to_arr[i], id_arr[i]
        if fr in bal:
            bal[fr] -= 1
            if bal[fr] == 0:
                del bal[fr]
        bal[to] = bal.get(to, 0) + 1
        owner[tid] = to
        last_t[tid] = t
    while ci < len(cps):
        on_checkpoint(cps[ci], owner, bal, last_t)
        ci += 1
    return owner, bal, last_t


def live_balances(bal):
    return {a: n for a, n in bal.items() if a not in DEAD and n > 0}


def write_csv(df, name):
    p = os.path.join(PROC_ON, name)
    df.to_csv(p, index=False)
    return p
