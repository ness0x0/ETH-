"""Label holder addresses (contracts + top holders) for the 9 collections.

Sources  : Blockscout Ethereum API v2 GET https://eth.blockscout.com/api/v2/addresses/<addr> (verified contract name,
           proxy implementation names, ENS name, public/metadata tags) — cached in
           data/raw/onchain/blockscout/addresses.jsonl with fetch time.
           For contracts Blockscout cannot name: eth_getCode (EIP-1167 / clone-with-immutable-args implementation
           address -> Blockscout name of the implementation), EIP-1967 implementation slot, and eth_call probes
           (Sudoswap `nft()`/`pairVariant()`, Safe `getThreshold()`, NFTX `assetAddress()`), at HEAD_BLOCK via
           Tenderly, NodeReal, dRPC and Blast public endpoints (threaded single calls).
Scope    : every address with contract code (non-EIP-7702) that ever received a token of any of the 9 collections,
           plus the top-60 holders at head of each collection (EOAs included, for ENS names).
Output   : data/processed/onchain/address_labels.csv
           (address, is_contract, is_7702, name, impl_names, tags, ens, category, protocol, label_source)
Category : lending | amm_pool | strategy_vault (NFT 'Strategy' tokens that auto-buy floors) | staking | bridge_wrapper | marketplace_escrow | fractional_vault | safe | smart_wallet
           | burn | contract_unlabelled | eoa. Rules are keyword rules on verified names (see RULES) plus a small manual
           list of addresses verified by hand (MANUAL). Keyword classification can mislabel; labels are best-effort.
"""
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RECEIPT_RPCS, utcnow  # noqa: E402
from onchain_config import BLEND, COLLECTIONS, DEAD, HEAD_BLOCK, PROC_ON, RAW_ON  # noqa: E402
import onchain_lib as L  # noqa: E402

BS = "https://eth.blockscout.com/api/v2/addresses/"
CACHE = os.path.join(RAW_ON, "blockscout", "addresses.jsonl")

# Addresses verified by hand (Blockscout name / source) — protocol, category
MANUAL = {
    BLEND: ("blur_blend", "lending"),
    "0x0000000000a39bb272e79075ade125fd351887ac": ("blur_pool", "marketplace_escrow"),
    # "UUPSProxy" accounts deployed by an AccountFactory (0x665766368ee511ebd3cd5f9300520dac915e941c) — ERC-4337 wallets
    "0xf37d69f29346bc633c71ef34a3e2b9d2152fc7e3": ("smart_wallet", "smart_wallet"),
    "0x8ea0de226713ffd8f0f9a1a52fd275b141cc4b22": ("smart_wallet", "smart_wallet"),
}

# (regex on "name | impl names | tags", category, protocol) — first match wins
RULES = [
    (r"MultiSourceLoan|(?i:gondi)", "lending", "gondi"),
    (r"Strategy", "strategy_vault", "nft_strategy_token"),
    (r"\bBlend\b", "lending", "blur_blend"),
    (r"DirectLoan|NFTfi|LoanCoordinator|AssetOfferLoan|CollectionOfferLoan|NftfiHub|Nftfi", "lending", "nftfi"),
    (r"Arcade|AssetVault|LoanCore|OriginationController|VaultFactory", "lending", "arcade"),
    (r"Zharta|CollateralVault", "lending", "zharta"),
    (r"Astaria|ClearingHouse", "lending", "astaria"),
    (r"BendDAO|\bBNFT|BoundNFT|LendPool|bend", "lending", "benddao"),
    (r"ParaSpace|NToken|Parallel", "lending", "paraspace"),
    (r"XY3|X2Y2.*Loan|LoanX2Y2", "lending", "x2y2_loan"),
    (r"Cyan", "lending", "cyan"),
    (r"MetaStreet|Metastreet", "lending", "metastreet"),
    (r"NFTVault|JPEG", "lending", "jpegd"),
    (r"CErc721|Comptroller", "lending", "compound_fork_nft"),
    (r"Pine|Drops|MetaLend|Ethos|Teller", "lending", "other_lending"),
    (r"Loan|Lend|Lien|Borrow|Credit", "lending", "other_lending"),
    (r"NFTXVault|NFTX", "amm_pool", "nftx"),
    (r"LSSVMPair|Sudo", "amm_pool", "sudoswap"),
    (r"^FWA", "marketplace_escrow", "fwa_random_pool"),
    (r"HibernationDen", "marketplace_escrow", "game_raffle_escrow"),
    (r"IndexERC721|NFT Basket", "fractional_vault", "index_basket"),
    (r"Flooring|FloorGetter|^fp[A-Z]", "fractional_vault", "flooring"),
    (r"Collectionswap|Caviar|Pair\b|Pool\b|AMM", "amm_pool", "other_amm"),
    (r"GnosisSafe|SafeL2|^Safe\b|SafeProxy|\bSafe\b", "safe", "gnosis_safe"),
    (r"Argent|Ambire|Kernel|CoinbaseSmartWallet|LightAccount|SimpleAccount|BiconomySmart|SmartAccount|Sequence|"
     r"Loopring|InstaAccount|DSProxy|Wallet|Account|Vault4337|Delegate", "smart_wallet", "smart_wallet"),
    (r"Stak|Lock|Farm|Reward|Bank|Yield|Escrowed", "staking", "staking"),
    (r"Bridge|Wrapper|Wrapped|ONFT|Adapter|Portal|Wormhole|LayerZero|Mirror|Tunnel|Ascend|Migrat", "bridge_wrapper",
     "bridge_wrapper"),
    (r"Seaport|Exchange|Escrow|Auction|Market|Conduit|Swap|Router|Zap|Blur|OpenSea|LooksRare|X2Y2|Gem|Genie|"
     r"Reservoir|TransferHelper|Aggregator|Batch|Bulk|Multicall|Executor", "marketplace_escrow", "marketplace"),
    (r"Fraction|Tessera|Unicly|Vault|Fractional|Shard|NIFTEX|Party", "fractional_vault", "fractional"),
]

_lock = threading.Lock()


def load_cache():
    out = {}
    if os.path.exists(CACHE):
        for line in open(CACHE):
            try:
                d = json.loads(line)
                out[d["addr"]] = d
            except Exception:  # noqa
                pass
    return out


def bs_fetch(addr, sess):
    for k in range(6):
        try:
            r = sess.get(BS + addr, timeout=30)
            if r.status_code == 404:
                return {"addr": addr, "fetched_at_utc": utcnow(), "status": 404, "data": None}
            if r.status_code == 429:
                time.sleep(5 * (k + 1))
                continue
            r.raise_for_status()
            d = r.json()
            keep = {k2: d.get(k2) for k2 in ["is_contract", "name", "implementations", "proxy_type",
                                            "ens_domain_name", "is_verified", "metadata", "token",
                                            "public_tags", "creator_address_hash"]}
            if keep.get("token"):
                keep["token"] = {k3: keep["token"].get(k3) for k3 in ["name", "symbol", "type"]}
            return {"addr": addr, "fetched_at_utc": utcnow(), "status": 200, "data": keep}
        except Exception:  # noqa
            time.sleep(2 * (k + 1))
    return {"addr": addr, "fetched_at_utc": utcnow(), "status": -1, "data": None}


def fetch_all(addrs, cache):
    todo = [a for a in addrs if a not in cache or cache[a].get("status") == -1]
    print("blockscout to fetch", len(todo), flush=True)
    local = threading.local()

    def one(a):
        if not hasattr(local, "s"):
            local.s = requests.Session()
            local.s.headers.update({"User-Agent": "eth-nft-research/1.0"})
        rec = bs_fetch(a, local.s)
        time.sleep(0.15)
        with _lock:
            with open(CACHE, "a") as f:
                f.write(json.dumps(rec) + "\n")
            cache[a] = rec
        return rec

    with ThreadPoolExecutor(4) as ex:
        for i, _ in enumerate(ex.map(one, todo)):
            if i % 500 == 0:
                print("bs", i, flush=True)


PROXY_PAT = re.compile(r"73([0-9a-f]{40})5af4")  # minimal proxy / clones: PUSH20 <impl> GAS DELEGATECALL
CLONE_IA = re.compile(r"^0x3d3d3d3d363d3d37[0-9a-f]{0,40}?73([0-9a-f]{40})")


def _post(sess, url, method, params):
    r = sess.post(url, json={"jsonrpc": "2.0", "id": 1, "method": method, "params": params}, timeout=30).json()
    if "result" not in r:
        raise RuntimeError(str(r.get("error"))[:120])
    return r["result"]


def probe(addrs, urls):
    """On-chain probes for unnamed contracts (threaded, one session per worker). Returns addr -> dict."""
    out = {}
    local = threading.local()
    counter = [0]

    def one(a):
        if not hasattr(local, "s"):
            local.s = requests.Session()
            with _lock:
                counter[0] += 1
                local.url = urls[counter[0] % len(urls)]
        d = {}
        for attempt in range(3):
            try:
                code = _post(local.s, local.url, "eth_getCode", [a, hex(HEAD_BLOCK)])
                m = PROXY_PAT.search(code[:400]) or CLONE_IA.search(code[:200])
                if m:
                    d["impl"] = "0x" + m.group(1)
                slot = _post(local.s, local.url, "eth_getStorageAt",
                             [a, "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc", hex(HEAD_BLOCK)])
                if int(slot, 16):
                    d["impl1967"] = "0x" + slot[-40:]
                for sel, nm in [("0x47ccca02", "nft"), ("0xe75235b8", "getThreshold"),
                                ("0x1ba46cfd", "assetAddress"), ("0x3053fc58", "pairVariant")]:
                    try:
                        res = _post(local.s, local.url, "eth_call", [{"to": a, "data": sel}, hex(HEAD_BLOCK)])
                        if res and res != "0x" and len(res) == 66:
                            d[nm] = res
                    except Exception:  # noqa — reverted call = function absent
                        pass
                d.pop("err", None)
                break
            except Exception as e:  # noqa
                d["err"] = str(e)[:100]
                time.sleep(1 + attempt)
        return a, d

    with ThreadPoolExecutor(12) as ex:
        for a, d in ex.map(one, addrs):
            out[a] = d
    return out


def text_of(rec):
    d = (rec or {}).get("data") or {}
    parts = [d.get("name") or ""]
    parts += [(i or {}).get("name") or "" for i in d.get("implementations") or []]
    for t in ((d.get("metadata") or {}).get("tags") or []):
        parts.append(t.get("name") or "")
    tok = d.get("token") or {}
    parts.append(tok.get("name") or "")
    return " | ".join(p for p in parts if p)


def classify(addr, rec, prb, impl_names):
    if addr in DEAD:
        return "burn", "burn", "rule:dead"
    if addr in MANUAL:
        return MANUAL[addr][1], MANUAL[addr][0], "manual"
    txt = text_of(rec) + (" | " + " | ".join(impl_names) if impl_names else "")
    for pat, cat, proto in RULES:
        if txt and re.search(pat, txt):
            return cat, proto, "name:" + pat.split("|")[0][:20]
    if prb:
        if "nft" in prb and "pairVariant" in prb:
            return "amm_pool", "sudoswap", "probe:nft()+pairVariant()"
        if "nft" in prb:
            return "amm_pool", "sudoswap?", "probe:nft()"
        if "getThreshold" in prb:
            return "safe", "gnosis_safe", "probe:getThreshold()"
        if "assetAddress" in prb:
            return "amm_pool", "nftx", "probe:assetAddress()"
    return "contract_unlabelled", "", "none"


def main():
    contracts = set()
    top = set()
    for k in COLLECTIONS:
        df = L.load_transfers(k)
        for a in set(df["to"]):
            if L.is_contract(a):
                contracts.add(a)
        owner, bal, _ = L.replay(df, [], lambda *a: None)
        lb = L.live_balances(bal)
        top.update([a for a, _ in sorted(lb.items(), key=lambda x: -x[1])[:60]])
    addrs = sorted(contracts | top)
    print("contracts ever holding", len(contracts), "top holders", len(top), "total", len(addrs), flush=True)
    cache = load_cache()
    fetch_all(addrs, cache)
    unnamed = [a for a in contracts if not text_of(cache.get(a))]
    print("probing unnamed contracts", len(unnamed), flush=True)
    pcache_p = os.path.join(RAW_ON, "blockscout", "probes.json")
    pcache = json.load(open(pcache_p)) if os.path.exists(pcache_p) else {}
    todo = [a for a in unnamed if a not in pcache or pcache[a].get("err")]
    urls = RECEIPT_RPCS[:2] + RECEIPT_RPCS[2:3] + RECEIPT_RPCS[4:5]
    for i in range(0, len(todo), 300):
        pcache.update(probe(todo[i:i + 300], urls))
        json.dump(pcache, open(pcache_p, "w"))
        print("probed", i + 300, flush=True)
    impls = sorted({v.get("impl") or v.get("impl1967") for v in pcache.values()
                    if v.get("impl") or v.get("impl1967")} - set(cache))
    fetch_all(impls, cache)
    rows = []
    for a in addrs:
        rec = cache.get(a)
        prb = pcache.get(a) if a in contracts else None
        impl_names = []
        if prb:
            for key in ("impl", "impl1967"):
                if prb.get(key):
                    t = text_of(cache.get(prb[key]))
                    if t:
                        impl_names.append(t)
        cat, proto, src = classify(a, rec, prb, impl_names)
        if not L.is_contract(a) and a not in DEAD:
            cat, proto, src = "eoa", "", "no code" + (" (EIP-7702 delegated)" if L.is_7702(a) else "")
        d = (rec or {}).get("data") or {}
        rows.append({"address": a, "is_contract": L.is_contract(a), "is_7702": L.is_7702(a),
                     "name": d.get("name") or "", "impl_names": "; ".join(impl_names) or "; ".join(
                         (i or {}).get("name") or "" for i in d.get("implementations") or []),
                     "tags": "; ".join((t.get("name") or "") for t in ((d.get("metadata") or {}).get("tags") or [])),
                     "ens": d.get("ens_domain_name") or "", "category": cat, "protocol": proto, "label_source": src})
    out = pd.DataFrame(rows)
    p = L.write_csv(out, "address_labels.csv")
    print(p, len(out))
    print(out[out.is_contract].groupby(["category", "protocol"]).size().sort_values(ascending=False).head(40))


if __name__ == "__main__":
    main()
