"""Shared helpers: HTTP with retry + on-disk raw cache, JSON-RPC client, paths.

All raw API responses are written under data/raw/ with the UTC fetch time so every
number in the reports can be traced back to a stored response.
"""
import json
import os
import time
import datetime as dt
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
PROC = os.path.join(ROOT, "data", "processed")
os.makedirs(RAW, exist_ok=True)
os.makedirs(PROC, exist_ok=True)

UA = {"User-Agent": "eth-nft-research/1.0 (public research)", "Accept": "application/json"}


def utcnow():
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def get_json(url, params=None, retries=5, sleep=2.0, timeout=60):
    last = None
    for i in range(retries):
        try:
            r = requests.get(url, params=params, headers=UA, timeout=timeout)
            if r.status_code == 429:
                time.sleep(sleep * (2 ** i) + 5)
                continue
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa
            last = e
            time.sleep(sleep * (2 ** i))
    raise RuntimeError(f"GET failed {url} {params}: {last}")


def save_raw(name, obj):
    """Save a raw response with a fetched_at stamp. Returns path."""
    path = os.path.join(RAW, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump({"fetched_at_utc": utcnow(), "data": obj}, f)
    return path


def load_raw(name):
    path = os.path.join(RAW, name)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)["data"]


# ---------------------------------------------------------------- JSON-RPC
# Public archive endpoints verified 2026-10-13 to serve historical eth_getLogs.
RPCS = [
    "https://gateway.tenderly.co/public/mainnet",       # <=20k results / query
    "https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7",  # chainlist public key, <=50k block range
]
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"


class RPC:
    def __init__(self, urls=None, min_interval=0.25):
        self.urls = urls or RPCS
        self.i = 0
        self.min_interval = min_interval
        self.last = 0.0

    def call(self, method, params, retries=8):
        last = None
        for k in range(retries):
            wait = self.min_interval - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            url = self.urls[self.i % len(self.urls)]
            self.last = time.time()
            try:
                r = requests.post(url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params},
                                  timeout=120)
                d = r.json()
                if "result" in d:
                    return d["result"]
                last = d.get("error")
                msg = json.dumps(last)
                if "more than" in msg or "range" in msg.lower() or "too large" in msg.lower():
                    raise RangeError(msg)
            except RangeError:
                raise
            except Exception as e:  # noqa
                last = e
            self.i += 1
            time.sleep(min(30, 1.5 * (2 ** k)))
        raise RuntimeError(f"RPC {method} failed: {last}")

    def block_number(self):
        return int(self.call("eth_blockNumber", []), 16)

    def get_logs(self, address, topics, from_block, to_block, step=200_000):
        """Adaptive-range eth_getLogs. Yields log dicts."""
        out = []
        cur = from_block
        while cur <= to_block:
            end = min(to_block, cur + step - 1)
            try:
                res = self.call("eth_getLogs", [{"address": address, "fromBlock": hex(cur), "toBlock": hex(end),
                                                 "topics": topics}])
                out.extend(res)
                cur = end + 1
                if len(res) < 5000:
                    step = min(step * 2, 2_000_000)
            except RangeError:
                step = max(500, step // 4)
        return out


class RangeError(Exception):
    pass


# ---------------------------------------------------------------- on-chain extensions (onchain_* scripts)
import re as _re

_SUGGEST = _re.compile(r"\[(0x[0-9a-fA-F]+),\s*(0x[0-9a-fA-F]+)\]")


def iter_logs(rpc, address, topics, from_block, to_block, step=500_000, max_step=5_000_000):
    """Adaptive eth_getLogs generator yielding (chunk_from, chunk_to, logs) in ascending block order.

    Honours the Tenderly hint "Query returned more than 20000 results. Try with this block range [a, b]" and the
    NodeReal 50k-block limit (falls back to shrinking the range). Callers can checkpoint after every chunk.
    """
    cur = from_block
    while cur <= to_block:
        end = min(to_block, cur + step - 1)
        try:
            res = rpc.call("eth_getLogs", [{"address": address, "fromBlock": hex(cur), "toBlock": hex(end),
                                            "topics": topics}])
        except RangeError as e:
            m = _SUGGEST.search(str(e))
            if m and int(m.group(1), 16) == cur and int(m.group(2), 16) >= cur:
                step = max(1, int(m.group(2), 16) - cur + 1)
            else:
                step = max(1, step // 4)
            continue
        yield cur, end, res
        cur = end + 1
        if len(res) < 8000:
            step = min(step * 2, max_step)


def rpc_multi(urls, min_interval=0.25):
    """Return one RPC client per endpoint (for thread-per-endpoint fan-out of single throttled calls)."""
    return [RPC([u], min_interval=min_interval) for u in urls]


# Additional public endpoints verified 2026-10-13 to serve eth_getTransactionReceipt / eth_getTransactionByHash
# for historical (post-merge) transactions. Used only for per-tx receipt fetching, not for log scans.
RECEIPT_RPCS = RPCS + [
    "https://eth.drpc.org",
    "https://rpc.mevblocker.io",
    "https://eth-mainnet.public.blastapi.io",
    "https://eth-pokt.nodies.app",
]
