"""Classify every address that ever received a token of the 9 collections as EOA vs contract.

Method   : "deployless" eth_call (no `to`; data = 59-byte init code + N 32-byte addresses). The init code copies the
           appended addresses to memory and, for each, returns EXTCODESIZE | (first 3 code bytes << 128) (via
           EXTCODECOPY). 700 addresses per call (returned array must stay under the 24,576-byte EIP-170 code-size cap).
           Evaluated at HEAD_BLOCK. Code that starts with 0xef0100 (size 23) is an EIP-7702 delegation designator -
           an EOA that delegated to a smart-account implementation - and is treated as an EOA.
Endpoints: Tenderly public gateway (primary), NodeReal public (fallback) — via common.RPC.
Output   : data/raw/onchain/codesize.json  {"fetched_at_utc", "block", "data": {address: {"size": n, "7702": bool}}}
Limits   : Code status is taken at the head block and applied to all history (a counterfactual Safe that held tokens
           before deployment is classed as contract; a self-destructed contract is classed as EOA).

Usage: python3 scripts/onchain_codes.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RPC, RPCS, utcnow  # noqa: E402
from onchain_config import COLLECTIONS, HEAD_BLOCK, RAW_ON  # noqa: E402

L = 59
INIT = ("61%04x" % L + "38" + "03" + "80" + "61%04x" % L + "6000" + "39" + "6000"   # copy args to mem[0:sz]
        + "5b" + "8181" + "10" + "15" + "61%04x" % 54 + "57"                          # loop: if i >= sz goto end
        + "80" + "51" + "80" + "3b" + "90"                                             # addr, size
        + "6020" + "6000" + "85" + "83" + "3c" + "50"                                  # EXTCODECOPY(addr, sz, 0, 32)
        + "82" + "51" + "60e8" + "1c" + "6080" + "1b" + "17"                           # (mem[sz] >> 232) << 128 | size
        + "81" + "52" + "6020" + "01" + "61000e" + "56"                                # mem[i] = v; i += 32
        + "5b" + "50" + "6000" + "f3")                                                 # end: return mem[0:sz]
assert len(INIT) // 2 == L
OUT = os.path.join(RAW_ON, "codesize.json")


def all_addresses():
    s = set()
    for k in COLLECTIONS:
        for line in open(os.path.join(RAW_ON, f"{k}_transfers.jsonl")):
            r = json.loads(line)
            s.add(r["to"])
            s.add(r["f"])
    return sorted(s)


def main():
    have = json.load(open(OUT))["data"] if os.path.exists(OUT) else {}
    addrs = [a for a in all_addresses() if a not in have]
    print("to check", len(addrs), "cached", len(have), flush=True)
    rpc = RPC(RPCS, min_interval=0.2)
    for i in range(0, len(addrs), 700):
        chunk = addrs[i:i + 700]
        data = "0x" + INIT + "".join(a[2:].rjust(64, "0") for a in chunk)
        res = rpc.call("eth_call", [{"data": data, "gas": hex(50_000_000)}, hex(HEAD_BLOCK)])
        vals = [int(res[2 + 64 * j: 2 + 64 * (j + 1)], 16) for j in range(len(chunk))]
        for a, v in zip(chunk, vals):
            size, prefix = v & ((1 << 128) - 1), v >> 128
            have[a] = {"size": size, "7702": size == 23 and prefix == 0xef0100}
        if (i // 700) % 50 == 0:
            print(i + len(chunk), flush=True)
            json.dump({"fetched_at_utc": utcnow(), "block": HEAD_BLOCK, "partial": True, "data": have}, open(OUT, "w"))
    json.dump({"fetched_at_utc": utcnow(), "block": HEAD_BLOCK, "method": "deployless EXTCODESIZE eth_call",
               "data": have}, open(OUT, "w"))
    n_c = sum(1 for v in have.values() if v["size"] > 0 and not v["7702"])
    print("addresses", len(have), "contracts", n_c, "7702", sum(v["7702"] for v in have.values()))


if __name__ == "__main__":
    main()
