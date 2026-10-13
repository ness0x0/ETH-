"""Fetch the complete ERC-721 Transfer history for the 9 finalist collections.

Source   : Ethereum mainnet event logs, eth_getLogs(address=<collection>, topics=[Transfer topic0]).
Endpoints: Tenderly public archive gateway https://gateway.tenderly.co/public/mainnet (primary; <=20k results per
           query, its "Try with this block range" hint is honoured); NodeReal public endpoint as fallback (<=50k blocks).
Range    : block 11,000,000 (2020-10-06) .. HEAD_BLOCK 26,186,366 (2026-10-13) — see onchain_config.py.
Timestamp: both endpoints return `blockTimestamp` on every log, so each transfer carries the exact block timestamp
           (no interpolation needed; checked on 2020-12 and 2026-10 logs).
Output   : data/raw/onchain/<key>_transfers.jsonl — one compact record per log:
           {"b": block, "t": unix ts, "tx": tx hash, "ti": tx index, "li": log index, "f": from, "to": to, "id": tokenId}
           plus data/raw/onchain/<key>_transfers.ckpt.json (last fully written block, line count, endpoint, fetch time).
           Resumable: on restart the jsonl is truncated to the checkpointed line count and the scan continues.
Limits   : ERC-721 logs only (4 topics). Chromie Squiggle shares Art Blocks V1 contract with projects 1-2; ALL logs are
           cached here and the tokenId < 1,000,000 filter is applied in the analysis scripts.

Usage: python3 scripts/onchain_fetch_transfers.py [key ...]
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, RPCS, iter_logs, utcnow  # noqa: E402
from onchain_config import COLLECTIONS, HEAD_BLOCK, RAW_ON, SCAN_START, TRANSFER_TOPIC  # noqa: E402


def topic_addr(t):
    return "0x" + t[-40:]


def fetch(key):
    contract = COLLECTIONS[key][0]
    path = os.path.join(RAW_ON, f"{key}_transfers.jsonl")
    ck = os.path.join(RAW_ON, f"{key}_transfers.ckpt.json")
    start, nlines = SCAN_START, 0
    if os.path.exists(ck):
        c = json.load(open(ck))
        start, nlines = c["last_block"] + 1, c["lines"]
        if c.get("complete"):
            print(key, "already complete", nlines, flush=True)
            return
    # truncate to checkpointed line count
    if os.path.exists(path):
        with open(path) as f:
            lines = f.readlines()
        if len(lines) != nlines:
            with open(path, "w") as f:
                f.writelines(lines[:nlines])
    elif nlines:
        raise RuntimeError("checkpoint without data file")
    rpc = RPC([RPCS[0]], min_interval=0.3)
    t0 = time.time()
    with open(path, "a") as out:
        for a, b, logs in iter_logs(rpc, contract, [TRANSFER_TOPIC], start, HEAD_BLOCK):
            logs.sort(key=lambda x: (int(x["blockNumber"], 16), int(x["logIndex"], 16)))
            for lg in logs:
                if len(lg["topics"]) != 4 or lg.get("removed"):
                    continue
                rec = {"b": int(lg["blockNumber"], 16), "t": int(lg["blockTimestamp"], 16),
                       "tx": lg["transactionHash"], "ti": int(lg["transactionIndex"], 16),
                       "li": int(lg["logIndex"], 16), "f": topic_addr(lg["topics"][1]),
                       "to": topic_addr(lg["topics"][2]), "id": int(lg["topics"][3], 16)}
                out.write(json.dumps(rec, separators=(",", ":")) + "\n")
                nlines += 1
            out.flush()
            json.dump({"last_block": b, "lines": nlines, "endpoint": RPCS[0], "contract": contract,
                       "updated_utc": utcnow(), "complete": b >= HEAD_BLOCK}, open(ck, "w"))
            print(f"{key} {a}-{b} +{len(logs)} total={nlines} {time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    keys = sys.argv[1:] or list(COLLECTIONS)
    for k in keys:
        for attempt in range(5):
            try:
                fetch(k)
                break
            except Exception as e:  # noqa
                print("ERROR", k, e, flush=True)
                time.sleep(30)
