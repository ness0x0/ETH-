"""Classify every collection-token movement in the fetched transactions as SALE vs NON-SALE and price sales.

Inputs   : data/raw/onchain/<key>_transfers.jsonl (token movements) and data/raw/onchain/receipts/<key>.jsonl
           (tx + receipt for every tx in the analysis windows; see onchain_fetch_receipts.py).
Method   : per transaction, the collection's Transfer logs are collapsed per tokenId into one movement
           (first `from` -> last `to`, so router/aggregator hops are removed). Price candidates per tokenId are decoded
           from marketplace events in the same receipt, in priority order:
             1. Blur Exchange v2 (0xb2ec..) Execution721Packed / TakerFeePacked / MakerFeePacked:
                tokenId = word>>168, trader = low 160 bits; price = bits 160..247 of collectionPriceSide, side = top
                byte (1 = bid/offer filled, trader = buyer; 0 = listing filled, trader = seller). Gross price.
             2. Blur Exchange v1 (0x0000..ad05) OrdersMatched: sell order (trader, collection, tokenId, price).
             3. Seaport 1.1/1.4/1.5/1.6 OrderFulfilled: for each order holding this collection's ERC-721 items, price
                = currency items on the other side (native ETH, WETH, Blur Pool; other ERC-20 -> flagged, no ETH price)
                divided by the number of NFTs in the order. Listing: sum of consideration currency (gross incl. fees
                and royalties). Bid: offer currency amount. When several orders cover the same token (matchOrders /
                counter-orders) the maximum (gross) candidate is used.
             4. LooksRare v2 TakerBid/TakerAsk, Magic Eden / Limit Break Payment Processor BuyListingERC721 /
                AcceptOfferERC721, NFTX v2 zap Buy/Sell (ethSpent|ethReceived / count), Sudoswap v2 pair
                SwapNFTOutPair/SwapNFTInPair (amount / len(ids)).
             5. Blend BuyLocked (buyer buys an NFT locked as Blend collateral): price = Blur Pool/WETH paid by the
                buyer in the tx; seller = borrower from the event.
             6. Fallback "value flow": WETH / Blur Pool Transfer from the recipient (or tx sender) to the token
                sender, or tx.value when the recipient sent the tx — split equally over tokens moving to that recipient.
           Escrow corrections: a token leaving a lending escrow (Blend, Gondi, NFTfi...) in a sale is attributed to the
           borrower (first wallet hop after the escrow, else tx.from, or the Blend BuyLocked seller); a token bought
           straight into an escrow (Blend buyToBorrow with LoanOfferTaken, Gondi buy-with-loan) is attributed to the
           borrower (Blend event borrower, else last wallet hop before the escrow, else tx.from). Movements with no price are NON-SALE and
           typed: mint, burn, lending_lock / lending_release (Blend, Gondi, NFTfi... escrows), amm/vault deposit or
           withdrawal, wallet_transfer (EOA<->EOA, no payment), other.
Flags    : multi_nft_tx (several tokens of the collection in the tx), bundle_price_split, price_from_fallback,
           non_eth_currency, escrow_seller_attributed, blend_buy_to_borrow, failed_tx.
Failure modes: private OTC deals paid in a separate tx look like gifts (non-sale); NFT-for-NFT swaps have no price;
           mixed-collection bundles are split equally; fallback can mistake an unrelated WETH payment for a sale;
           tx.value fallback assumes the full value paid for the NFTs; Blur Pool deposits in the same tx are ignored.
Output   : data/processed/onchain/sales_<key>.csv (sales, tx-level), data/processed/onchain/movements_<key>.csv (all
           collapsed movements in the windows with sale/non-sale type).
"""
import collections
import json
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from onchain_config import (BLEND, BLUR_POOL, BLUR_V1, BLUR_V2, COLLECTIONS, DEAD, RAW_ON, SEAPORT, WETH,  # noqa
                            ZERO, token_filter)
import onchain_lib as L  # noqa: E402

T_TRANSFER = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
T_SEAPORT = "0x9d9af8e38d66c62e2c12f0225249fd9d721c54b83f48d9352c97c6cacdcb6f31"
T_BLUR2 = {"0x1d5e12b51dee5e4d34434576c3fb99714a85f57b0fd546ada4b0bddd736d12b2": "packed",
           "0x0fcf17fac114131b10f37b183c6a60f905911e52802caeeb3e6ea210398b81ab": "taker_fee",
           "0x7dc5c0699ac8dd5250cbe368a2fc3b4a2daadb120ad07f6cccea29f83482686e": "maker_fee"}
T_BLUR2_EXEC = "0xf2f66294df6fae7ac681cbe2f6d91c6904485929679dce263e8f6539b7d5c559"
T_BLUR1 = "0x61cbb2a3dee0b6064c2e681aadd61677fb4ef319f0b547508d495626f5a62f64"
T_LOAN_TAKEN = "0x06a333c2d6fe967ca967f7a35be2eb45e8caeb6cf05e16f55d42b91b5fe31255"
T_BUY_LOCKED = "0x7ffb5bd9cdc79a6f9bc6e00c82f43836e0afbb204d47972001f6e853764a8ef1"
T_LR_BID = "0x3ee3de4684413690dee6fff1a0a4f92916a1b97d1c5a83cdf24671844306b2e3"
T_LR_ASK = "0x9aaa45d6db2ef74ead0751ea9113263d1dec1b50cea05f0ca2002cb8063564a4"
T_PP_BUY = "0xffb29e9cf48456d56b6d414855b66a7ec060ce2054dcb124a1876310e1b7355c"
T_PP_ACCEPT = "0x8b87c0b049fe52718fe6ff466b514c5a93c405fb0de8fbd761a23483f9f9e198"
T_NFTX_BUY = "0xf7735c8cb2a65788ca663fc8415b7c6a66cd6847d58346d8334e8d52a599d3df"
T_NFTX_SELL = "0x1cdb5ee3c47e1a706ac452b89698e5e3f2ff4f835ca72dde8936d0f4fcf37d81"
T_SUDO_OUT = "0xa13c46268c53408442d94eb370f2e476cb7f0fbe027ae5bad73ce13d4469c8b9"
T_SUDO_IN = "0x7a0e7e58d91fd23a96b0008604db1b2d1cee4aae434e3aad9a20fdd7c0995f89"
ETH_LIKE = {ZERO, WETH, BLUR_POOL}


def words(data):
    d = data[2:]
    return [d[i:i + 64] for i in range(0, len(d), 64)]


def w_int(w):
    return int(w, 16)


def w_addr(w):
    return "0x" + w[-40:]


def dec_seaport(data, contract):
    """Return (orderHash, recipient, offer[(type, token, id, amt)], consideration[(type, token, id, amt, rcpt)])."""
    w = words(data)
    off_o, off_c = w_int(w[2]) // 32, w_int(w[3]) // 32
    n_o = w_int(w[off_o])
    offer = [(w_int(w[off_o + 1 + 4 * i]), w_addr(w[off_o + 2 + 4 * i]), w_int(w[off_o + 3 + 4 * i]),
              w_int(w[off_o + 4 + 4 * i])) for i in range(n_o)]
    n_c = w_int(w[off_c])
    cons = [(w_int(w[off_c + 1 + 5 * i]), w_addr(w[off_c + 2 + 5 * i]), w_int(w[off_c + 3 + 5 * i]),
             w_int(w[off_c + 4 + 5 * i]), w_addr(w[off_c + 5 + 5 * i])) for i in range(n_c)]
    return w_addr(w[1]), offer, cons


def classify_tx(key, contract, rec, moves):
    """moves: list of collection Transfer rows (dicts) for this tx in log order. Returns list of movement dicts."""
    logs = rec["logs"] if rec else []
    status_ok = (rec is None) or (rec.get("status") in ("0x1", 1, None))
    txfrom = (rec or {}).get("from")
    txto = ((rec or {}).get("to") or "") .lower() if rec else ""
    value = int((rec or {}).get("value") or "0x0", 16)

    # collapse token paths
    path = collections.OrderedDict()
    for m in moves:
        tid = m["id"]
        if tid not in path:
            path[tid] = {"id": tid, "seller": m["f"], "buyer": m["to"], "li": m["li"], "hops": 1,
                         "addrs": [m["f"], m["to"]]}
        else:
            path[tid]["buyer"] = m["to"]
            path[tid]["hops"] += 1
            path[tid]["addrs"].append(m["to"])
    n_tokens = len(path)

    cand = {}   # tid -> (price_wei or None, method, flags set, seller_override, buyer_override)

    def add(tid, price, method, flags=(), seller=None, buyer=None, prio=5, side=""):
        if tid not in path:
            return
        cur = cand.get(tid)
        if cur is None or (prio < cur[5]) or (prio == cur[5] and (price or 0) > (cur[0] or 0)):
            cand[tid] = (price, method, set(flags), seller, buyer, prio, side)

    blend_loan_tokens = {}   # tid -> borrower (LoanOfferTaken in tx)
    erc20 = []   # (token, from, to, amount)
    for a, tp, data, li in logs:
        if not tp:
            continue
        t0 = tp[0]
        try:
            if t0 == T_TRANSFER and len(tp) == 3 and a in (WETH, BLUR_POOL):
                erc20.append((a, w_addr(tp[1]), w_addr(tp[2]), int(data, 16)))
            elif t0 in T_BLUR2 and a == BLUR_V2:
                w = words(data)
                tl, cps = w_int(w[1]), w_int(w[2])
                coll = "0x%040x" % (cps & ((1 << 160) - 1))
                if coll != contract:
                    continue
                tid = tl >> 168
                trader = "0x%040x" % (tl & ((1 << 160) - 1))
                price = (cps >> 160) & ((1 << 88) - 1)
                side = cps >> 248
                add(tid, price, "blur_v2", (), prio=1, side="bid" if side == 1 else "listing")
            elif t0 == T_BLUR2_EXEC and a == BLUR_V2:
                w = words(data)  # Transfer(trader, id, amount, collection, assetType), orderHash, listingIndex, price
                coll = w_addr(w[3])
                if coll == contract:
                    add(w_int(w[1]), w_int(w[7]), "blur_v2", (), prio=1)
            elif t0 == T_BLUR1 and a == BLUR_V1:
                w = words(data)
                so = w_int(w[0]) // 32
                bo = w_int(w[2]) // 32
                coll = w_addr(w[so + 3])
                if coll != contract:
                    continue
                tid = w_int(w[so + 4])
                price = w_int(w[so + 7])
                pay = w_addr(w[so + 6])
                fl = () if pay in ETH_LIKE else ("non_eth_currency",)
                maker = w_addr(tp[1]) if len(tp) > 1 else ""
                sd = "bid" if maker == w_addr(w[bo]) else "listing"
                add(tid, price if not fl else None, "blur_v1", fl, prio=1, side=sd)
            elif t0 == T_SEAPORT and a in SEAPORT:
                rcpt, offer, cons = dec_seaport(data, a)
                nft_o = [i for i in offer if i[0] in (2, 4) and i[1] == contract]
                nft_c = [i for i in cons if i[0] in (2, 4) and i[1] == contract]
                other_nft_o = [i for i in offer if i[0] in (2, 3, 4, 5) and i[1] != contract]
                other_nft_c = [i for i in cons if i[0] in (2, 3, 4, 5) and i[1] != contract]
                if nft_o:
                    cur = [i for i in cons if i[0] in (0, 1)]
                    nfts, other, sd = nft_o, other_nft_o, "listing"
                elif nft_c:
                    cur = [i for i in offer if i[0] in (0, 1)]
                    nfts, other, sd = nft_c, other_nft_c, "bid"
                else:
                    continue
                if not cur:
                    for it in nfts:
                        add(it[2], None, SEAPORT[a] + "_swap", ("nft_for_nft_or_zero_price",), prio=4)
                    continue
                non_eth = any(i[1] not in ETH_LIKE for i in cur)
                total = sum(i[3] for i in cur if i[1] in ETH_LIKE)
                n = len(nfts) + len(other)
                fl = []
                if n > 1:
                    fl.append("bundle_price_split")
                if other:
                    fl.append("mixed_collection_bundle")
                if non_eth:
                    fl.append("non_eth_currency")
                for it in nfts:
                    add(it[2], (total // n) if not non_eth else None, SEAPORT[a], fl, prio=2, side=sd)
            elif t0 in (T_LR_BID, T_LR_ASK):
                w = words(data)
                # nonceInvalidationParameters(3) askUser/bidUser bidUser/bidRecipient strategyId currency collection
                # itemIds(off) amounts(off) feeRecipients[2] feeAmounts[3]
                coll = w_addr(w[7])
                if coll != contract:
                    continue
                cur_tok = w_addr(w[6])
                total = w_int(w[12]) + w_int(w[13]) + w_int(w[14])
                ids_off = w_int(w[8]) // 32
                ids = [w_int(w[ids_off + 1 + i]) for i in range(w_int(w[ids_off]))]
                fl = ["bundle_price_split"] if len(ids) > 1 else []
                if cur_tok not in ETH_LIKE:
                    fl.append("non_eth_currency")
                for tid in ids:
                    add(tid, total // len(ids) if cur_tok in ETH_LIKE else None, "looksrare_v2", fl, prio=2,
                        side="bid" if t0 == T_LR_ASK else "listing")
            elif t0 in (T_PP_BUY, T_PP_ACCEPT) and len(tp) == 4 and w_addr(tp[3]) == contract:
                w = words(data)
                pay, tid, price = w_addr(w[1]), w_int(w[2]), w_int(w[3])
                fl = [] if pay in ETH_LIKE else ["non_eth_currency"]
                add(tid, price if not fl else None, "payment_processor", fl, prio=2,
                    side="bid" if t0 == T_PP_ACCEPT else "listing")
            elif t0 == T_LOAN_TAKEN and a == BLEND:
                w = words(data)
                if w_addr(w[2]) == contract:
                    blend_loan_tokens[w_int(w[7])] = w_addr(w[4])
            elif t0 == T_BUY_LOCKED and a == BLEND:
                w = words(data)
                if w_addr(w[1]) == contract:
                    buyer, seller, tid = w_addr(w[2]), w_addr(w[3]), w_int(w[4])
                    paid = sum(x[3] for x in erc20_all(logs) if x[1] == buyer and x[2] != ZERO)
                    add(tid, paid or None, "blend_buy_locked", ("escrow_seller_attributed",), seller=seller,
                        buyer=buyer, prio=3, side="listing")
            elif t0 in (T_NFTX_BUY, T_NFTX_SELL):
                w = words(data)
                cnt, eth = w_int(w[0]), w_int(w[1])
                if cnt <= 0:
                    continue
                for tid, p in path.items():
                    lab = L.labels().get(p["seller"] if t0 == T_NFTX_BUY else p["buyer"], {})
                    if lab.get("protocol") == "nftx":
                        add(tid, eth // cnt, "nftx", ["amm"], prio=3, side="pool")
            elif t0 in (T_SUDO_OUT, T_SUDO_IN):
                w = words(data)
                if len(w) < 3:
                    continue
                amt = w_int(w[0])
                ids_n = w_int(w[2]) if len(w) > 2 else 0
                ids = [w_int(x) for x in w[3:3 + ids_n]]
                for tid in ids:
                    p = path.get(tid)
                    if p and a in (p["seller"], p["buyer"]):
                        add(tid, amt // max(1, len(ids)), "sudoswap_v2", ["amm"], prio=3, side="pool")
        except Exception:  # noqa — malformed / unexpected layout: skip this log
            continue

    out = []
    for tid, p in path.items():
        seller, buyer = p["seller"], p["buyer"]
        flags = set()
        if n_tokens > 1:
            flags.add("multi_nft_tx")
        if p["hops"] > 1:
            flags.add("multi_hop")
        if not status_ok:
            flags.add("failed_tx")
        c = cand.get(tid)
        typ, price, method, side = None, None, "", ""
        if seller == ZERO:
            typ = "mint"
        elif c is not None and c[1].endswith("_swap"):
            typ, method = "nft_swap_no_price", c[1]
            flags |= c[2]
        elif c is not None:
            typ, price, method, side = "sale", c[0], c[1], c[6]
            flags |= c[2]
            if c[3]:
                seller = c[3]
            if c[4]:
                buyer = c[4]
        else:
            # fallback value-flow
            loan_leg = "lending" in (L.category(seller), L.category(buyer)) or txto == BLEND
            # NFTX vault legs without a zap Buy/Sell event are redeems/swaps paying a vault fee, not sales
            loan_leg = loan_leg or "nftx" in (L.protocol(seller), L.protocol(buyer)) or \
                L.protocol(txto) == "nftx"
            pay = 0 if loan_leg else sum(x[3] for x in erc20 if x[2] == seller and x[1] in (buyer, txfrom)
                                         and x[1] != ZERO)
            same_buyer = sum(1 for q in path.values() if q["buyer"] == buyer)
            if pay > 0:
                typ, price, method = "sale", pay // same_buyer, "fallback_erc20_flow"
                flags.add("price_from_fallback")
            elif value > 0 and not loan_leg and txfrom == buyer and buyer != seller and buyer not in DEAD:
                typ, price, method = "sale", value // same_buyer, "fallback_tx_value"
                flags.add("price_from_fallback")
        if typ == "sale" and price is not None and price <= 10 ** 15:
            typ = "zero_price_trade"
            flags.add("zero_or_dust_price")
        if typ == "sale":
            # escrow attribution: a token sold OUT of a lending escrow is attributed to the borrower; a token bought
            # straight INTO a lending escrow (buy-to-borrow / buy-now-pay-later) is attributed to the borrower.
            inner = p["addrs"][1:-1]
            if L.category(seller) == "lending" and not (c and c[3]):
                w = [a for a in inner if L.category(a) in L.WALLET_CATS]
                if w:
                    seller = w[0]
                elif txfrom and txfrom != buyer and L.category(txfrom) in L.WALLET_CATS:
                    seller = txfrom
                flags.add("escrow_seller_attributed")
            if L.category(buyer) == "lending" and not (c and c[4]):
                w = [a for a in inner if L.category(a) in L.WALLET_CATS]
                if buyer == BLEND and tid in blend_loan_tokens:
                    buyer = blend_loan_tokens[tid]
                elif w:
                    buyer = w[-1]
                elif txfrom and L.category(txfrom) in L.WALLET_CATS:
                    buyer = txfrom
                flags.add("blend_buy_to_borrow" if p["buyer"] == BLEND else "lending_buy_to_borrow")
        if typ is None:
            if buyer in DEAD:
                typ = "burn"
            else:
                cs, cb = L.category(seller), L.category(buyer)
                if cb == "lending":
                    typ = "lending_lock"
                elif cs == "lending":
                    typ = "lending_release"
                elif cb in ("amm_pool", "strategy_vault", "fractional_vault", "staking", "bridge_wrapper"):
                    typ = f"deposit_{cb}"
                elif cs in ("amm_pool", "strategy_vault", "fractional_vault", "staking", "bridge_wrapper"):
                    typ = f"withdraw_{cs}"
                elif cs in L.WALLET_CATS and cb in L.WALLET_CATS:
                    typ = "wallet_transfer"
                else:
                    typ = "other_transfer"
        out.append({"id": tid, "seller": seller, "buyer": buyer, "type": typ,
                    "price_eth": (price / 1e18) if (price is not None and price >= 0) else None,
                    "method": method, "side": side, "flags": ";".join(sorted(flags)), "n_tokens_tx": n_tokens,
                    "tx_from": txfrom, "tx_to": txto})
    return out


def erc20_all(logs):
    res = []
    for a, tp, data, li in logs:
        if tp and tp[0] == T_TRANSFER and len(tp) == 3 and a in (WETH, BLUR_POOL):
            res.append((a, w_addr(tp[1]), w_addr(tp[2]), int(data, 16)))
    return res


def run(key):
    contract = COLLECTIONS[key][0]
    rp = os.path.join(RAW_ON, "receipts", f"{key}.jsonl")
    recs = {}
    with open(rp) as f:
        for line in f:
            try:
                r = json.loads(line)
                recs[r["tx"]] = r
            except Exception:  # noqa
                pass
    df = L.load_transfers(key)
    df = df[df["tx"].isin(recs)]
    rows = []
    for tx, g in df.groupby("tx", sort=False):
        moves = g.sort_values("li").to_dict("records")
        res = classify_tx(key, contract, recs[tx], moves)
        b, t = int(g["b"].iloc[0]), int(g["t"].iloc[0])
        for r in res:
            r.update({"block": b, "ts": pd.Timestamp(t, unit="s", tz="UTC"), "tx": tx})
            rows.append(r)
    mv = pd.DataFrame(rows).sort_values(["block", "tx", "id"])
    cols = ["block", "ts", "tx", "id", "seller", "buyer", "type", "price_eth", "method", "side", "flags", "n_tokens_tx",
            "tx_from", "tx_to"]
    mv = mv[cols].rename(columns={"id": "tokenId"})
    L.write_csv(mv, f"movements_{key}.csv")
    sales = mv[mv["type"] == "sale"].drop(columns=["type"])
    L.write_csv(sales, f"sales_{key}.csv")
    print(key, "movements", len(mv), "sales", len(sales), "priced", sales["price_eth"].notna().sum())
    print(mv["type"].value_counts().to_string())
    print(sales["method"].value_counts().to_string())
    return mv


if __name__ == "__main__":
    for k in (sys.argv[1:] or list(COLLECTIONS)):
        if os.path.exists(os.path.join(RAW_ON, "receipts", f"{k}.jsonl")):
            run(k)
