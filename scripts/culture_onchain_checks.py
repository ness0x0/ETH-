"""On-chain checks backing the cultural-research dossiers (dossiers/_research/*_culture.md).

Run: python3 scripts/culture_onchain_checks.py
RPC: Tenderly public archive gateway (scripts/common.py RPCS[0]); single throttled calls.
Outputs (raw, with fetched_at_utc): data/raw/culture/onchain_checks.json
         data/processed/culture/cult_price_samples.csv (CULT/WETH Uni v3 slot0 samples -> USD via prices_daily)

Checks
 1. First mints (Transfer from 0x0) and sampled mint-tx ETH value: Milady, Remilio, CryptoDickbutts S3.
 2. Milady transfers to/from vitalik.eth (0xd8dA...6045) since block 21.3M, and current ownerOf.
 3. CULT token (0x0000000000c5dc95539589fbD24BE07c6C14eCa4): totalSupply; genesis mint block; first
    distribution block; balances of the largest TGE recipients at historical blocks.
 4. CULT/WETH 1% Uni v3 pool 0xc4ce8e63921b8b6cbdb8fcb6bd64cc701fb926f2 slot0 price at monthly blocks.
"""
import csv
import datetime as dt
import os

from common import RPC, TRANSFER_TOPIC, PROC, save_raw, utcnow

rpc = RPC()
ZERO32 = "0x" + "0" * 64
VIT = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
MIL = "0x5af0d9827e0c53e4799bb226655a1de152a425a5"
REM = "0xd3d9ddd0cf0a5f0bfb8f7fceae075df687eaebab"
CDB = "0x42069abfe407c60cf4ae4112bedead391dba1cdb"
CULT = "0x0000000000c5dc95539589fbD24BE07c6C14eCa4"
POOL = "0xc4ce8e63921b8b6cbdb8fcb6bd64cc701fb926f2"
_ts = {}


def pad(a):
    return "0x" + "0" * 24 + a.lower()[2:]


def ts(bn):
    if bn not in _ts:
        b = rpc.call("eth_getBlockByNumber", [hex(bn), False])
        _ts[bn] = dt.datetime.fromtimestamp(int(b["timestamp"], 16), dt.timezone.utc)
    return _ts[bn]


def first_mints(addr, start, stop, step=20_000, n_tx=4):
    cur = start
    while cur <= stop:
        logs = rpc.call("eth_getLogs", [{"address": addr, "fromBlock": hex(cur), "toBlock": hex(cur + step - 1),
                                         "topics": [TRANSFER_TOPIC, ZERO32]}])
        if logs:
            out, seen = [], set()
            for lg in logs:
                tx = lg["transactionHash"]
                if tx in seen:
                    continue
                seen.add(tx)
                t = rpc.call("eth_getTransactionByHash", [tx])
                k = sum(1 for x in logs if x["transactionHash"] == tx)
                bn = int(lg["blockNumber"], 16)
                out.append({"block": bn, "time_utc": ts(bn).isoformat(), "tx": tx, "tokens": k,
                            "value_eth": int(t["value"], 16) / 1e18})
                if len(out) >= n_tx:
                    break
            return out
        cur += step
    return []


def balance(token, holder, block):
    r = rpc.call("eth_call", [{"to": token, "data": "0x70a08231" + holder.lower()[2:].rjust(64, "0")},
                              block if block == "latest" else hex(block)])
    return int(r, 16) / 1e18


def main():
    res = {"query_started_utc": utcnow()}
    head = rpc.block_number()
    res["head_block"] = head
    res["first_mints"] = {"milady": first_mints(MIL, 12_900_000, 13_200_000),
                          "remilio": first_mints(REM, 15_200_000, 15_400_000),
                          "cryptodickbutts_s3": first_mints(CDB, 12_900_000, 13_000_000)}
    vit = []
    for label, topics in (("to", [TRANSFER_TOPIC, None, pad(VIT)]), ("from", [TRANSFER_TOPIC, pad(VIT)])):
        for lg in rpc.get_logs(MIL, topics, 21_300_000, head, step=2_000_000):
            bn = int(lg["blockNumber"], 16)
            vit.append({"dir": label, "block": bn, "time_utc": ts(bn).isoformat(),
                        "token_id": int(lg["topics"][3], 16), "tx": lg["transactionHash"]})
    for v in vit:
        r = rpc.call("eth_call", [{"to": MIL, "data": "0x6352211e" + hex(v["token_id"])[2:].rjust(64, "0")}, "latest"])
        v["owner_now"] = "0x" + r[-40:]
    res["milady_vitalik"] = vit
    res["cult_total_supply"] = int(rpc.call("eth_call", [{"to": CULT, "data": "0x18160ddd"}, "latest"]), 16) / 1e18
    holders = {"cult_contract_self": CULT, "tge_40B_recipient": "0x000000f534caa75bd1a3950ab32d6bd24d2e6b76",
               "deployer": "0x635cb66ce14ba44e78b3105bbb5d93d7d2b073c6", "uni_v3_pool": POOL}
    blocks = {"2024-12-09": 21361245, "2025-01-01": 21529475, "2025-07-01": 22825424, "2025-12-01": 23920895,
              "2026-07-01": 25438802, "latest": "latest"}
    res["cult_balances"] = {h: {b: balance(CULT, a, n) for b, n in blocks.items()} for h, a in holders.items()}

    # CULT pool price samples (token0 = CULT, token1 = WETH; both 18 decimals)
    eth = {}
    with open(os.path.join(PROC, "prices_daily.csv")) as f:
        for r in csv.DictReader(f):
            eth[r["date"]] = float(r["eth_usd"])
    ref_b, ref_t = 21361238, dt.datetime(2024, 12, 9, 0, 4, 11, tzinfo=dt.timezone.utc)
    rate = (ts(head) - ref_t).total_seconds() / (head - ref_b)
    rows = []
    d = dt.date(2024, 12, 10)
    targets = [(dt.date(2024, 12, 9), 1), (dt.date(2024, 12, 10), 12), (dt.date(2025, 1, 19), 12),
               (dt.date(2025, 1, 25), 12), (dt.date(2026, 1, 2), 12), (dt.date.today(), 12)]
    while d <= dt.date.today():
        targets.append((d, 12))
        d = (d.replace(day=1) + dt.timedelta(days=32)).replace(day=1)
    for day, hour in sorted(set(targets)):
        t = dt.datetime.combine(day, dt.time(hour), dt.timezone.utc)
        bn = min(head, int(ref_b + (t - ref_t).total_seconds() / rate))
        r = rpc.call("eth_call", [{"to": POOL, "data": "0x3850c7bd"}, hex(bn)])
        p = (int(r[2:66], 16) / 2 ** 96) ** 2
        bt = ts(bn)
        e = eth.get(bt.date().isoformat())
        rows.append({"date": bt.date().isoformat(), "block": bn, "block_time_utc": bt.isoformat(), "cult_eth": p,
                     "eth_usd_close": e, "cult_usd": p * e if e else "", "fdv_usd_100B": p * e * 1e11 if e else ""})
    res["query_finished_utc"] = utcnow()
    save_raw("culture/onchain_checks.json", res)
    os.makedirs(os.path.join(PROC, "culture"), exist_ok=True)
    with open(os.path.join(PROC, "culture", "cult_price_samples.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("ok", res["head_block"], len(vit), "vitalik transfers;", len(rows), "CULT samples")


if __name__ == "__main__":
    main()
