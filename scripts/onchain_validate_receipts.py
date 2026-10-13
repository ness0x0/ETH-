"""Validate cached receipts against the independently fetched Transfer logs and repair bad records.

Why: a spot check found that one public endpoint (eth.drpc.org) occasionally returned a receipt whose `logs` belonged
to a different transaction (tx hash/from/to correct, logs wrong). Every cached receipt is therefore checked: each
collection Transfer log we hold for that tx (from eth_getLogs, keyed by logIndex) must appear in the receipt with the
same contract address and token topics. Failing records are re-fetched from Tenderly / NodeReal (verifying
`transactionHash` on every returned log) and replaced. Writes a per-endpoint failure tally to
data/raw/onchain/receipts/validation.json.

Usage: python3 scripts/onchain_validate_receipts.py [key ...]
"""
import collections
import json
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPCS, utcnow  # noqa: E402
from onchain_config import COLLECTIONS, RAW_ON  # noqa: E402

RDIR = os.path.join(RAW_ON, "receipts")


def expected(key):
    contract = COLLECTIONS[key][0]
    exp = collections.defaultdict(dict)
    for line in open(os.path.join(RAW_ON, f"{key}_transfers.jsonl")):
        r = json.loads(line)
        exp[r["tx"]][r["li"]] = (contract, r["id"])
    return exp


def ok(rec, exp_tx):
    logs = {lg[3]: lg for lg in rec["logs"]}
    for li, (addr, tid) in exp_tx.items():
        lg = logs.get(li)
        if lg is None or lg[0] != addr or len(lg[1]) != 4 or int(lg[1][3], 16) != tid:
            return False
    return True


def refetch(tx, b, sess):
    for k in range(10):
        u = RPCS[k % len(RPCS)]
        try:
            rc = sess.post(u, json={"jsonrpc": "2.0", "id": 1, "method": "eth_getTransactionReceipt", "params": [tx]},
                           timeout=45).json()["result"]
            t = sess.post(u, json={"jsonrpc": "2.0", "id": 1, "method": "eth_getTransactionByHash", "params": [tx]},
                          timeout=45).json()["result"]
            if rc["transactionHash"].lower() != tx or any(lg["transactionHash"].lower() != tx for lg in rc["logs"]):
                raise RuntimeError("hash mismatch")
            return {"tx": tx, "b": b, "from": rc["from"], "to": rc.get("to"), "value": t["value"],
                    "sel": (t.get("input") or "0x")[:10], "status": rc.get("status"), "ep": u.split("/")[2],
                    "revalidated": True,
                    "logs": [[lg["address"].lower(), lg["topics"], lg["data"], int(lg["logIndex"], 16)]
                             for lg in rc["logs"]]}
        except Exception:  # noqa
            time.sleep(1 + k)
    return None


def main():
    keys = sys.argv[1:] or list(COLLECTIONS)
    vp = os.path.join(RDIR, "validation.json")
    tally = json.load(open(vp)) if os.path.exists(vp) else {}
    sess = requests.Session()
    for key in keys:
        p = os.path.join(RDIR, f"{key}.jsonl")
        if not os.path.exists(p):
            continue
        exp = expected(key)
        recs, bad = [], collections.Counter()
        total = collections.Counter()
        for line in open(p):
            try:
                recs.append(json.loads(line))
            except Exception:  # noqa
                pass
        fixed = 0
        for i, r in enumerate(recs):
            total[r["ep"]] += 1
            if ok(r, exp[r["tx"]]):
                continue
            bad[r["ep"]] += 1
            nr = refetch(r["tx"], r["b"], sess)
            if nr and ok(nr, exp[r["tx"]]):
                recs[i] = nr
                fixed += 1
            else:
                print("UNFIXED", key, r["tx"], flush=True)
        with open(p + ".tmp", "w") as f:
            for r in recs:
                f.write(json.dumps(r, separators=(",", ":")) + "\n")
        os.replace(p + ".tmp", p)
        tally[key] = {"checked_utc": utcnow(), "records": len(recs), "bad_by_endpoint": dict(bad),
                      "records_by_endpoint": dict(total), "fixed": fixed}
        print(key, tally[key], flush=True)
        json.dump(tally, open(vp, "w"), indent=1)


if __name__ == "__main__":
    main()
