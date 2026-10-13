"""Fetch transaction + receipt for every transaction that moved a token of a collection inside the analysis windows.

Source   : eth_getTransactionReceipt + eth_getTransactionByHash (single, throttled JSON-RPC calls — no batching).
Endpoints: fan-out over public endpoints listed in common.RECEIPT_RPCS (Tenderly public gateway, NodeReal public
           key, dRPC, MEV Blocker, Blast public, Nodies/POKT). Each endpoint has its own worker threads and a per-endpoint
           minimum interval; failed/null responses are retried on a different endpoint. Responses are deterministic
           chain data, so the serving endpoint does not change content (endpoint recorded per record anyway).
Windows  : trailing 12 months 2025-10-13T00:00Z .. HEAD_BLOCK (2026-10-13) for every collection, plus
           Milady 2023-04-15..2023-07-15 and Pudgy 2024-11-01..2025-02-15 (bull-run windows requested by the PM).
Output   : data/raw/onchain/receipts/<key>.jsonl, one record per tx:
           {tx, b, from, to, value(hex wei), sel (4-byte selector), status, ep, logs:[[address, topics, data, logIndex]]}
           Resumable: tx hashes already present are skipped on restart (a truncated final line is ignored).

Usage: python3 scripts/onchain_fetch_receipts.py [key ...]
"""
import datetime as dt
import json
import os
import queue
import sys
import threading
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RECEIPT_RPCS  # noqa: E402
from onchain_config import COLLECTIONS, RAW_ON, token_filter  # noqa: E402

RDIR = os.path.join(RAW_ON, "receipts")
os.makedirs(RDIR, exist_ok=True)


def ts(s):
    return int(dt.datetime.fromisoformat(s).replace(tzinfo=dt.timezone.utc).timestamp())


WINDOWS = {"t12m": (ts("2025-10-13"), 10**12)}
EXTRA = {"milady": [("milady_2023", ts("2023-04-15"), ts("2023-07-16"))],
         "pudgy": [("pudgy_2024", ts("2024-11-01"), ts("2025-02-16"))]}


def windows_for(key):
    w = [("t12m",) + WINDOWS["t12m"]]
    return w + EXTRA.get(key, [])


def tx_list(key):
    wins = windows_for(key)
    seen, out = set(), []
    for line in open(os.path.join(RAW_ON, f"{key}_transfers.jsonl")):
        r = json.loads(line)
        if not token_filter(key, r["id"]):
            continue
        if any(a <= r["t"] < b for _, a, b in wins) and r["tx"] not in seen:
            seen.add(r["tx"])
            out.append((r["tx"], r["b"]))
    return out


# endpoint -> (threads, min interval seconds per thread)
EP_CFG = {u: (3, 0.15) for u in RECEIPT_RPCS}
EP_CFG["https://rpc.mevblocker.io"] = (1, 0.3)


def post(sess, url, method, params):
    r = sess.post(url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=45)
    d = r.json()
    if d.get("result") is None:
        raise RuntimeError(str(d.get("error") or "null result")[:200])
    return d["result"]


def run(key):
    path = os.path.join(RDIR, f"{key}.jsonl")
    done = set()
    if os.path.exists(path):
        good = []
        with open(path) as f:
            for line in f:
                try:
                    done.add(json.loads(line)["tx"])
                    good.append(line)
                except Exception:  # noqa  truncated last line
                    pass
        with open(path, "w") as f:
            f.writelines(good)
    todo = [t for t in tx_list(key) if t[0] not in done]
    print(f"{key}: {len(done)} cached, {len(todo)} to fetch", flush=True)
    if not todo:
        return
    q = queue.Queue()
    for t in todo:
        q.put((t[0], t[1], 0))
    outq = queue.Queue()
    stats = {u: [0, 0] for u in EP_CFG}
    stop = threading.Event()

    def worker(url, interval):
        sess = requests.Session()
        last = 0.0
        while not stop.is_set():
            try:
                tx, b, tries = q.get(timeout=1)
            except queue.Empty:
                if q.unfinished_tasks == 0:
                    return
                continue
            try:
                w = interval - (time.time() - last)
                if w > 0:
                    time.sleep(w)
                last = time.time()
                rc = post(sess, url, "eth_getTransactionReceipt", [tx])
                t = post(sess, url, "eth_getTransactionByHash", [tx])
                rec = {"tx": tx, "b": b, "from": rc["from"], "to": rc.get("to"), "value": t["value"],
                       "sel": (t.get("input") or "0x")[:10], "status": rc.get("status"), "ep": url.split("/")[2],
                       "logs": [[lg["address"].lower(), lg["topics"], lg["data"], int(lg["logIndex"], 16)]
                                for lg in rc["logs"]]}
                outq.put(rec)
                stats[url][0] += 1
            except Exception as e:  # noqa
                stats[url][1] += 1
                if tries < 12:
                    q.put((tx, b, tries + 1))
                else:
                    print("GIVEUP", tx, e, flush=True)
                time.sleep(min(20, 0.5 * (2 ** min(stats[url][1] % 6, 5))))
            finally:
                q.task_done()

    threads = []
    for url, (n, iv) in EP_CFG.items():
        for _ in range(n):
            th = threading.Thread(target=worker, args=(url, iv), daemon=True)
            th.start()
            threads.append(th)
    n = 0
    t0 = time.time()
    with open(path, "a") as out:
        while True:
            try:
                rec = outq.get(timeout=2)
                out.write(json.dumps(rec, separators=(",", ":")) + "\n")
                n += 1
                if n % 2000 == 0:
                    out.flush()
                    print(f"{key} {n}/{len(todo)} {time.time()-t0:.0f}s "
                          + " ".join(f"{u.split('/')[2][:12]}:{s[0]}/{s[1]}" for u, s in stats.items()), flush=True)
            except queue.Empty:
                if q.unfinished_tasks == 0 and outq.empty():
                    break
    stop.set()
    print(f"{key} done {n} in {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    keys = sys.argv[1:] or list(COLLECTIONS)
    for k in keys:
        run(k)
