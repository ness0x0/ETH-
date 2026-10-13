# On-chain collector analysis: 9 finalist collections

_Analysis date 2026-10-13. Head block **26,186,366** (2026-10-13 21:49:23 UTC). Data was pulled 2026-10-13 21:55–23:15 UTC.
Author: on-chain collector analyst workstream. Everything below comes from Ethereum event logs and receipts unless a line
says otherwise. Interpretation is labelled **[interp]**._

## 1. Method (summary)

| Step | Source / endpoint | Method | Script |
|---|---|---|---|
| Transfer history | `eth_getLogs` Transfer topic0 per contract, blocks 11,000,000 → 26,186,366. Tenderly public gateway, with NodeReal as fallback. | Adaptive ranges that follow Tenderly's 20k-result hint. Checkpointed and resumable. Each log carries its own `blockTimestamp`, so **timestamps are exact and nothing is interpolated**. Replaying ownership gave **0 chain breaks** in 1.36 M logs (every `from` matched the replayed owner). | `scripts/onchain_fetch_transfers.py` |
| EOA vs contract | Deployless `eth_call` that returns `EXTCODESIZE` and the code prefix for 700 addresses per call, at the head block. | 153,486 addresses checked: 3,432 contracts. **13,186 are EIP-7702-delegated EOAs**; their code starts `0xef0100` and they are counted as EOAs. | `scripts/onchain_codes.py` |
| Contract labels | Blockscout API v2 `/addresses/<a>` (verified name, proxy implementation, ENS, tags). For unnamed contracts: `eth_getCode` clone/EIP-1967 implementation, plus probes (Sudoswap `nft()`/`pairVariant()`, Safe `getThreshold()`, NFTX `assetAddress()`). | Keyword rules plus a short manual list. Covers 3,424 contracts that ever held a token and the top-60 holders of each collection. 1,044 contracts (mostly tiny or historical) stay `contract_unlabelled`. | `scripts/onchain_labels.py` → `address_labels.csv` |
| Holders, escrow, retention | Replayed Transfer logs | Monthly snapshots (state at 00:00 UTC on the 1st) plus the head block. | `scripts/onchain_holders.py` |
| Sales vs transfers | `eth_getTransactionReceipt` + `eth_getTransactionByHash` for **every tx that moved a token** in the windows: 122,953 txs. Throttled single calls fanned out over 6 public endpoints. | Decoders for Blur v1/v2, Seaport 1.1–1.6, LooksRare v2, Payment Processor, NFTX zap, Sudoswap v2 and Blend `BuyLocked`, then a value-flow fallback (§5). **Receipt validation:** dRPC returned another tx's logs for 82 of ~31k receipts (0.26%). Every receipt was checked against the independent Transfer logs, the bad ones were re-fetched, and dRPC was dropped. | `scripts/onchain_fetch_receipts.py`, `onchain_validate_receipts.py`, `onchain_sales.py` |
| Buyer behaviour, wash flags, liquidity, reconciliation | Classified sales; NFTPriceFloor 3-day bars (`data/raw/nftpricefloor/charts_<slug>.json`); OpenSea stats API cache | §5–§8 | `scripts/onchain_buyers.py`, `onchain_summary_table.py` |

Windows:
- **t12m** = 2025-10-13 00:00Z → head, for all 9 collections (Lil Pudgys included).
- **Milady** 2023-04-15 → 2023-07-15.
- **Pudgy** 2024-11-01 → 2025-02-15.

Chromie Squiggle uses the Art Blocks V1 contract filtered to tokenId < 1,000,000. V1 Punks covers only the official wrapper.

**Validation of the holder layer.** On-chain holder counts match the OpenSea `num_owners` fetched the same evening to within 0–4 addresses: Milady 5,129 vs 5,129; Chromie 2,939 vs 2,939; Terraforms 1,971 vs 1,971; CDB 2,131 vs 2,131; V1 1,169 vs 1,169; Pudgy 4,997 vs 5,001.

## 2. Decision-relevant takeaways

1. **Most trailing-year volume is dealer churn, not new ownership.** For Milady, Pudgy, Azuki, Remilio and Lil Pudgys, 68–82% of sales are on tokens that traded ≥3 times within 30 days, or that the buyer resold within 7 days. That is Blur/OpenSea bid-hit-and-relist arbitrage. Stripping it out and the flagged trades leaves this organic turnover:

   | Collection | Organic turnover (sales/day, trailing 365d) |
   |---|---|
   | Pudgy | 5.9 |
   | Milady | 5.3 |
   | Remilio | 5.3 |
   | Azuki | 4.8 |
   | Terraforms | 2.5 |
   | V1 | 1.9 |
   | Chromie | 1.5 |
   | CDB | 1.1 |

   Chromie (20% churn) and Terraforms (43%) have the most "real" turnover per sale. **[interp]** For the Blur-traded PFPs, raw sales counts overstate organic exit liquidity by roughly 3–6× (365-day all vs organic sales/day).
2. **Long-held supply is highest in the art names.**

   | Collection | Supply untouched 24 months | EOA holders from 24 months ago still holding |
   |---|---|---|
   | Chromie | 84% | 79% |
   | Terraforms | 74% | 78% |
   | V1 | 72% | 69% |
   | CDB | 61% | 71% |
   | Milady | 53% | 58% |
   | Remilio | 57% | 57% |
   | Azuki | 49% | 65% |
   | Pudgy | 48% | 57% |
   | Lil Pudgys | 44% | 59% |

3. **Every collection was distributed from existing holders to new wallets over the last 12 months.** Wallets holding ≥20 at the start, wallets holding 5–19, and holders whose first receipt was before 2024 were **net sellers in all 9**. Wallets that held nothing on 2025-10-13 absorbed 5–18% of supply (Milady +1,587, Pudgy +1,643, Remilio +1,358). Some of these "new" wallets are existing owners who moved to a fresh address (wallet ≠ person).
4. **Concentrated support exists in a few names, and it is real accumulation rather than wash.**
   - **Terraforms:** one entity (bid wallet `0x0506…37ba` forwarding to `0x3f51…d4f9`) took **13.5% of all t12m purchases**, 174 of them by filling floor bids, and went from 105 to 234 tokens.
   - **V1 Punks:** `beautifulnfts.eth` (`0x696e…354b`, with feeder `0xf45e…4a95`) took **12.9% of purchases** and went from 43 to 148.
   - **Pudgy:** `0xb972…2f97` swept **131 Pudgies (~371 ETH) between 6 and 12 Oct 2026**, 80 of them on the 11 Oct sell-off, and parked 130 in Safe `0x250d…55e7`.
   - **Remilio:** four wallets each added 84–115 tokens.
   - **[interp]** A single buyer pausing would visibly thin bids in Terraforms and V1.
5. **Lending escrow overhang is small and falling.** Total lending escrow at head, with Blend shown separately:

   | Collection | Total lending escrow | % of supply | of which Blend | Year-ago total | Peak Blend |
   |---|---|---|---|---|---|
   | Azuki | 363 | 3.6% | 182 | 616 | 815 (Jan-2025) |
   | Pudgy | 259 | 2.9% | 194 | 411 | 641 (Aug-2025) |
   | Milady | 200 | 2.0% | 136 | 306 | 592 (Feb-2024) |
   | V1 | 74 | 1.4% | 0 | 18 | — |
   | Lil Pudgys | 290 | 1.3% | 253 | 504 | 766 (Jan-2024) |
   | Remilio | 118 | 1.2% | 100 | 221 | 778 (Jan-2024) |
   | Chromie | 103 | 1.0% | 0 | 250 | — |
   | Terraforms | 58 | 0.6% | 0 | 80 | — |
   | CDB | 5 | 0.1% | 0 | 19 | — |

   - Azuki also has BendDAO 158 and Gondi 22. Pudgy has Gondi 61. Milady has Gondi 63. All of V1's escrow is Gondi, and 74 is an all-time high. Chromie is Gondi 82 plus NFTfi 18. Terraforms is all Gondi.
   - Gross Blend outflows jumped on 13 Oct: 119 Pudgy, 68 Azuki, 55 Lil and 25 Milady tokens left Blend that day. That is consistent with borrowers unwinding after the Blur wind-down news. The 2026-11-12 deadline comes from project STATE.md and was **not re-verified here**.
6. **Wash-type flags are modest (1.5–10.5% of sales)** and are dominated by "linked wallets" (buyer and seller swapped tokens off-market at some point). Terraforms is highest at 10.5%, because its holders often shuffle between their own wallets. No collection shows a large self-trade or round-trip ring. Separately, a **zero-price Payment Processor pattern** (`0x71cf…fe33` collecting NFTs for 0 ETH from up to 37 distinct wallets per collection through its own unverified contract) is consistent with signature-phishing drains (**UNVERIFIED**). These movements are excluded from sales.

## 3. Comparison table (head 2026-10-13; t12m = trailing 12 months)

| Metric | Milady | Remilio | CDB | Pudgy | Azuki | Terraforms | Chromie | V1 Punks | Lil Pudgys |
|---|---|---|---|---|---|---|---|---|---|
| Live supply | 9,976 | 9,995 | 5,198 | 8,888 | 10,000 | 9,911 | 10,000 | 5,125 (wrapped) | 21,931 |
| Holders (addresses) | 5,129 | 4,165 | 2,131 | 4,997 | 4,355 | 1,971 | 2,939 | 1,169 | 10,211 |
| % holders with 1 token | 81% | 78% | 67% | 78% | 72% | 55% | 76% | 67% | 72% |
| Top-10 / top-50 share | 11.2 / 24.2% | 15.6 / 32.2% | 12.2 / 29.1% | 9.3 / 19.0% | 13.1 / 25.1% | 17.5 / 42.0% | 36.4 / 52.0% | 48.3 / 62.9% | 5.6 / 14.3% |
| Contract or protocol share (Safes incl.) | 6.9% | 3.6% | 4.2% | 8.8% | 6.7% | 13.4% (Safes 12.7%) | 12.1% (Safes 10.5%) | 3.4% | 5.0% |
| Lending escrow: tokens (% supply) | 200 (2.0%) | 118 (1.2%) | 5 (0.1%) | 259 (2.9%) | 363 (3.6%) | 58 (0.6%) | 103 (1.0%) | 74 (1.4%) | 290 (1.3%) |
| of which Blend | 136 | 100 | 0 | 194 | 182 | 0 | 0 | 0 | 253 |
| Lending escrow, 2025-10 month-end | 306 | 221 | 19 | 411 | 616 | 80 | 250 | 18 | 504 |
| Supply untouched >12m / >24m | 75 / 53% | 77 / 57% | 86 / 61% | 72 / 48% | 79 / 49% | 88 / 74% | 92 / 84% | 86 / 72% | 74 / 44% |
| EOA holders retained, 12m / 24m | 83 / 58% | 84 / 57% | 91 / 71% | 80 / 57% | 86 / 65% | 90 / 78% | 92 / 79% | 86 / 69% | 82 / 59% |
| Supply held by 12m / 24m-ago EOA holders | 78 / 59% | 83 / 68% | 88 / 67% | 75 / 56% | 80 / 60% | 82 / 74% | 83 / 77% | 89 / 79% | 78 / 53% |
| t12m sales (on-chain) | 7,437 | 6,234 | 1,033 | 8,884 | 6,720 | 1,805 | 675 | 1,424 | 22,395 |
| t12m unique buyers / % new wallets | 2,001 / 69% | 1,416 / 65% | 358 / 51% | 2,177 / 67% | 1,874 / 63% | 354 / 54% | 402 / 70% | 463 / 60% | 4,817 / 64% |
| % of sales to first-time wallets | 21% | 16% | 18% | 19% | 18% | 13% | 45% | 20% | 15% |
| Top-10 buyers' share of purchases | 15% | 18% | 24% | 17% | 15% | 33% | 19% | 27% | 11% |
| Churn share (hot token or 7-day flip) | 74% | 68% | 58% | 75% | 73% | 43% | 20% | 49% | 82% |
| Suspect (wash/affiliated) share | 3.4% | 3.6% | 5.4% | 4.4% | 4.2% | 10.5% | 1.5% | 6.2% | 6.5% |
| Sales/day, 30d: all / organic | 14.7 / 5.4 | 13.4 / 6.9 | 1.9 / 1.2 | 40.6 / 18.1 | 12.4 / 4.8 | 6.3 / 3.9 | 1.8 / 1.5 | 3.9 / 2.4 | 75.2 / 26.0 |
| Sales/day, 365d: all / organic | 20.3 / 5.3 | 17.0 / 5.3 | 2.8 / 1.1 | 24.1 / 5.9 | 18.4 / 4.8 | 4.9 / 2.5 | 1.8 / 1.5 | 3.9 / 1.9 | 60.7 / 10.9 |
| Median gap between sales, 90d: all / organic (h) | 0.36 / 1.95 | 0.39 / 1.34 | 5.4 / 11.1 | 0.20 / 0.57 | 0.64 / 2.7 | 0.66 / 2.9 | 6.2 / 10.7 | 1.7 / 2.7 | 0.10 / 0.42 |
| t12m median price (ETH) / ÷ NPF floor | 1.09 / 1.05 | 0.172 / 1.02 | 0.70 / 1.02 | 4.44 / 1.04 | 0.86 / 1.07 | 0.251 / 1.09 | 2.65 / 1.06 | 2.00 / 1.18 | 0.514 / 1.05 |
| Net change, wallets empty at start / ≥20 at start | +1,587 / −191 | +1,358 / −584 | +398 / −140 | +1,643 / −294 | +1,268 / −346 | +468 / −87 | +540 / −100 | +430 / −136 | +3,880 / −1,276 |
| Net change, holders since before 2024 | −506 | −503 | −327 | −652 | −665 | −306 | −220 | −377 | −1,149 |
| Buys by "Strategy" auto-buy contracts | 32 | 4 | 17 | 16 | 1 | 5 | 1 | 0 | 0 |
| On-chain sales vs NPF (bar correlation) | +47% (0.98) | +41% (0.97) | +10% (0.59) | +40% (0.95) | +33% (0.95) | +24% (0.96) | +22% (0.96) | +28% (0.93) | +31% (0.98) |

Notes on the table:
- **Organic** sales exclude both churn and suspect trades.
- **Contract or protocol share** also includes two Flooring Protocol EOA vaults identified by their `*.liquidity.flooringlab.eth` ENS names.
- **EOA holders retained** answers: of the EOAs that held ≥1 token 12 or 24 months ago, what % still hold ≥1 now.
- **Supply held by 12m / 24m-ago EOA holders** is a share of all live supply; the denominator of EOA-held supply only is in `retention.csv`.
- **Net change** rows are escrow-adjusted (lending-escrow tokens are attributed to the borrower). Full detail is in `cohort_flows.csv`.
- **NPF** is the NFTPriceFloor 3-day series; see §6 for the reconciliation.

Source files: `data/processed/onchain/collector_comparison.csv`, `holders_summary.csv`, `retention.csv`, `buyers_summary.csv`, `liquidity_summary.csv`, `cohort_flows.csv`, `reconciliation.csv`.

## 4. Per-collection findings

**Milady (`0x5af0…a5a5`)**
- **Holders.** 5,129 holders, flat for a year (peak 5,326 in Apr-2025). The book is very retail: 81% of holders own 1 token and the top-10 hold 11.2%.
- **Largest holders.** An EOA with 150 tokens, held since 2022. Blend with 136. Safe `0x673a…` with 131, consolidated in t12m with no market buys. `imnotuncertain.eth` with 104, bought in t12m for ~103 ETH.
- **Escrow and strategy contracts.**
  - Lending escrow: 200 tokens (2.0%; Blend 136, Gondi 63). It peaked at 777 in Feb-2024 (7.8%).
  - "MiladyStrategy"-type contracts bought 32 in t12m and hold ~0.3%.
- **Trailing 12 months.**
  - 7,437 sales, but 74% is churn. Organic turnover is ~5 sales/day.
  - 2,001 buyers, 69% of them wallets new to Milady, taking 21% of purchases.
  - Holders since before 2024 net sold 506.
- **2023-04-15 → 07-15 window.** 14,280 sales at a 3.45 ETH median with 90% churn (Blur farming era). Organic sales over the 3 months were 1,368, a pace similar to today's ~5/day.

**Remilio (`0xd3d9…abab`)**
- **Holders.** 4,165 holders, down from a 4,570 peak in Jun-2024.
- **Largest holders.** Concentration is higher than Milady (top-10 15.6%). Several 140–285-token EOAs have been accumulating since early 2024. The NFTX vault holds 171 (1.7%).
- **Escrow.** 1.2% (Blend 100). Blend peaked at 778 (7.8%) in Jan-2024.
- **Trailing 12 months.**
  - 6,234 sales, 68% churn, at a 0.172 ETH median.
  - Four entities each added 84–115 tokens, while three large wallets each sold 88–110 (about 15 ETH apiece).
  - **[interp]** This is a low-price handover between whales.
- **Floor walls.** See §9 for the coordinator's question about OpenSea listing walls.

**CryptoDickbutts (`0x4206…1cdb`)**
- **Holders.** 2,131 holders; median token age 1,168 days; 86% of supply untouched for 12 months.
- **Escrow and strategy contracts.**
  - Lending escrow is negligible: 5 tokens.
  - The "DickStrategy" contract holds 78 (1.5%) and bought 17 in t12m. **[interp]** It is a programmatic floor bid.
- **Trailing 12 months.**
  - 1,033 sales: 58% churn, 1.1 organic sales/day, 11 hours median gap between organic sales.
  - Lowest new-wallet share (51%), and the top-10 buyers took 24%.
  - `cdb-otc.eth` was a net buyer of 33.
  - The NPF reconciliation is weakest here (bar correlation 0.59). Volume is thin and lumpy.

**Pudgy Penguins (`0xbd35…2cf8`)**
- **Holders.** 4,997 holders; top-10 hold only 9.3%, the lowest concentration among the PFPs.
- **Escrow and protocol holders.**
  - Lending escrow: 2.9% (Blend 194, Gondi 61), down from 7.4% (Sep-2025).
  - The Flooring Protocol vault EOA holds 84; "PudgyStrategy" contracts hold 58.
- **Trailing 12 months.**
  - 8,884 sales and 41.7k ETH, 75% churn, ~5.9 organic sales/day over 365d.
  - The last 30 days are elevated: 18/day organic, driven by the 10–13 Oct sell-off (324 sales on 11 Oct, median 2.50 ETH vs ~3.2 a week earlier).
  - A single entity (`0xb972…2f97` → Safe `0x250d…55e7`) bought 131 that week. Separately, a three-wallet entity (`0x3f22…5ea2`) sold 161 Pudgies (~693 ETH) plus 94 Lil Pudgys over the year.
- **2024-11-01 → 2025-02-15 window.** 6,752 sales at a 17.0 ETH median, 76% churn, 21% of sales to first-time wallets (similar to today's 19%).

**Azuki (`0xed5a…c544`)**
- **Holders.** 4,355 holders (5,514 peak in Mar-2022), but rising since 2024-09 (4,062).
- **Escrow.** Highest lending escrow of the nine: 363 tokens (3.6%) = Blend 182 + BendDAO BNFT 158 + Gondi 22. Year-ago escrow was 616, and Blend peaked at 815 (8.2%) in Jan-2025.
- **Flooring Protocol.** The vault EOA `chirulabs.liquidity.flooringlab.eth` holds 155 (1.6%).
- **Trailing 12 months.** 6,720 sales, 73% churn, ~4.8 organic sales/day.
- **Largest distributors.** `dingaling.eth` (120 → 22, mostly via non-sale transfers) and an entity that sold 74.
- **Note.** The largest t12m "accumulator" is the zero-price drain pattern (54 tokens received for 0 ETH; §7).

**Terraforms (`0x4e1f…0e56`)**
- **Holders.** 1,971 holders, at 5.0 tokens per holder (the PFPs sit at ~1.8–2.4). Top-50 hold 42%; Safes hold 12.7% (two Safes with 333 and 268).
- **Retention.** Excellent: 88% of supply untouched for 12 months, 74% for 24 months; 90% of EOAs from 12 months ago are still holders.
- **Trailing 12 months.**
  - 1,805 sales, only 43% churn, ~2.5 organic sales/day, 0.251 ETH median.
  - Bid concentration is the risk: one entity bought 243 and sold 115 (net +129, 13.5% of purchases), mostly by filling floor bids from Nov-2025 to Jun-2026.
  - A large holder, `0x5f29…20ae`, sold 107 (215 → 108).
- **Lending.** Gondi only: 58 tokens.

**Chromie Squiggle (Art Blocks V1, project 0)**
- **Holders.** 2,939 holders. The most concentrated and stickiest book: median token age 1,848 days; 92% / 84% of supply untouched for 12 / 24 months.
- **Largest holder.** One minter (`0xd110…e588`) minted 1,007 Squiggles in Nov-2020–Jan-2021 and still holds 990 (9.9%). Linked to three other wallets, the entity holds 1,314 (13.1%); identity UNVERIFIED. The top-10 hold 36.4%.
- **Trailing 12 months.**
  - Lowest churn (20%), so almost all of its 675 sales (1.8/day) are real ownership changes.
  - 45% of purchases went to first-time wallets, the highest of the nine.
  - The median gap between sales is ~6 hours. **[interp]** Exit liquidity for size is thin.
- **Lending.** Gondi 82 + NFTfi 18.

**V1 CryptoPunks, official wrapper (`0x282b…2c5d`)**
- **Holders.** 1,169 holders of 5,125 wrapped tokens. Extreme concentration: top-1 holds 11.9% (612), top-2 22%, top-10 48%.
- **Possible single entity.** Three wallets (388 / 365 / 174) share the same first-receipt date (2024-04-08) and the same token age. **[interp]** Possibly one entity holding ~18%.
- **Trailing 12 months.**
  - 1,424 sales, 49% churn, 1.9 organic sales/day.
  - The `beautifulnfts.eth` entity was 12.9% of buying (+105); the top holder sold 56.
- **Lending.** Gondi escrow is at an all-time high: 74 (1.4%), up from 18 a year ago.
- **Coverage gaps.**
  - Unwrapped V1 punks on the original V1 contract are not covered.
  - The OpenSea 30-day count (30 sales) is far below the on-chain count (117), unexplained; for the other collections on-chain is 3–31% higher.

**Lil Pudgys (`0x524c…a048`; sales included)**
- **Holders.** 10,211 holders, near the all-time high of 10,553 (Jun-2026); the least concentrated (top-10 5.6%).
- **Escrow and bridge.** Blend holds 253; the `LilPudgysProxyONFT` bridge adapter (ONFT, a LayerZero-style standard) holds 181.
- **Trailing 12 months.**
  - The highest churn (82%): 60 sales/day headline vs 10.9/day organic.
  - Wallets holding ≥20 at the start net sold 1,276.
- **Retention.** Weakest 24-month retention of the nine: only 44% of supply untouched.

## 5. Sales vs transfers: heuristic and failure modes

Per tx, each token's collection Transfer logs are collapsed into one movement (first `from` → last `to`), so router hops disappear. Price candidates, in priority order:

1. **Blur v2** `Execution721*Packed`. The tokenId is `word>>168`; the price is bits 160–247; the top byte is the side (1 = bid filled). Verified against Blur Pool flows in sample txs.
2. **Blur v1** `OrdersMatched`, using the sell order's price.
3. **Seaport** `OrderFulfilled`. The price is the currency items on the other side of the order (ETH, WETH or Blur Pool) divided by the number of NFTs in the order. This is the gross price, fees included. When matched or counter orders overlap, the maximum is kept.
4. **LooksRare v2**, Payment Processor, **NFTX** zap `Buy`/`Sell`, and **Sudoswap v2** pair events.
5. **Blend `BuyLocked`.** The price is what the buyer paid in Blur Pool/WETH; the seller is the borrower.
6. **Fallback.** WETH or Blur Pool paid by the recipient to the sender, or `tx.value` when the recipient sent the tx. Disabled for lending and NFTX legs.

Escrow attribution:
- Tokens sold out of lending escrow are credited to the borrower.
- Buy-to-borrow purchases (Blend `LoanOfferTaken`, Gondi buy-with-loan) are credited to the borrower.
- Movements with price ≤0.001 ETH become `zero_price_trade` (non-sale).

Coverage in the t12m window:
- 97.5–100% of sales are priced by marketplace events; the fallback prices ≤0.6% except CDB (1.5%) and V1 (2.5%).
- Unpriced (non-ETH currency) sales: 0–13.
- Multi-NFT txs are 8–30% of sales. True bundles where the price was split equally are ≤5%.

Non-sale movements are typed in `movements_<key>.csv`. They are mint, burn, `lending_lock`/`lending_release`, AMM/vault deposit or withdrawal, `wallet_transfer`, `nft_swap_no_price` and `other_transfer`. They make up 31–70% of t12m movements: lending legs alone are 22–35% for Milady, Pudgy and Azuki.

Failure modes:
- OTC deals settled in a separate tx look like gifts.
- NFT-for-NFT swaps have no price.
- Mixed bundles are split equally.
- Fallback flows can misattribute an unrelated WETH payment.
- Blend refinance or auction mechanics are not modelled; this was not a loan-book reconstruction.
- The wallet clustering behind "entities" is heuristic: ≥2 non-sale transfers between wallets in the window.

## 6. Reconciliation with NFTPriceFloor (3-day bars) and OpenSea

- **NPF bar alignment.** An NPF bar dated T covers [T−72h, T). This alignment gave the highest bar-level correlation in a grid search over offsets and lengths: 0.93–0.98 for 8 collections, 0.59 for CDB.
- **Level gap.** NPF's `salesCount` and `volumeNative` are consistently **22–47% below** on-chain counts and volume (CDB +10%). The ratio drifts month to month (Milady 0.52–0.81) and does not match any single excluded marketplace or category in a regression. NPF's filtering methodology is undisclosed, so treat **on-chain counts as the upper bound and NPF as a filtered lower bound**.
- **OpenSea 30-day counts** (API fetched 21:33Z) are close to on-chain counts for 8 collections (on-chain is 3–31% higher). The exception is V1 (30 vs 117).

Files: `reconciliation.csv`, `reconciliation_bars_<key>.csv`.

## 7. Wash-trading and affiliated-support indicators (flags, not proof)

`wash_flags.csv` lists every flagged sale; `wash_summary.csv` has the counts.

- **Suspect** = round trip A→B→A within 30 days, self-trade, or linked wallets (buyer and seller swapped tokens of the collection off-market at some point). This is 1.5–6.5% of t12m sales, and 10.5% for Terraforms. Round-trip sales in t12m: Lil 901, Pudgy 187, Milady 145, Azuki 132, Remilio 117, Terraforms 40, V1 22, CDB 11, Chromie 4. Self-trades: Pudgy 5, Lil 2.
- **Price outliers** (>3× or <0.5× the trailing 30-day median) are rare. They are mostly genuine rare-token sales: Terraforms up to 11 ETH vs a 0.3 median, Chromie 30 ETH, V1 62.9 ETH.
- **Bid clusters** (one wallet taking ≥25% of a month's bid fills) appear in Terraforms (121 fills, `0x0506…37ba`), V1 (53 fills in 3 days, Aug-2026, `0xf45e…4a95` → `beautifulnfts.eth`) and CDB (11). The monthly top-2 bidder share of bid fills has a median of 13–29% by collection, peaking at 54% (Terraforms, Nov-2025).
- **Funding links** (buyer funding seller via ETH) were **not measured**. Only NFT-transfer links are used.
- **Zero-price pattern.** `0x71cf…fe33` (an EIP-7702 EOA) and its unverified contract `0x415f…0b1a` received 84 Azuki, 77 Lil Pudgys, 94 CDB, 11 Milady and 9 Pudgy via 0-ETH Payment Processor offers from many wallets, then sold some on. This is consistent with phishing drains (**UNVERIFIED**). It is excluded from sales but appears as holder churn.

## 8. Blend and lending-escrow overhang

`blend_escrow_monthly.csv` gives, per month since May-2023: month-end, daily max and daily min for Blend; the total across lending protocols; and per protocol (Gondi, NFTfi, Arcade, BendDAO, ParaSpace, Drops/compound-fork, JPEG'd, Cyan, MetaStreet, X2Y2, Astaria). Current positions by contract are in `lending_escrow_current.csv`.

Blend now holds 136 Milady, 100 Remilio, 194 Pudgy, 182 Azuki and 253 Lil Pudgys, which is 1.0–2.2% of supply. That is down 67–87% from each collection's peak. No Blend exposure exists for Terraforms, Chromie, V1 or CDB.

**[interp]** Suppose every remaining Blend loan defaulted to lenders at the Blur wind-down (deadline per STATE.md, unverified here). The forced supply would be about 11–25 days of organic turnover for Milady, Pudgy and Remilio at 30-day organic rates (136 / 5.4 per day ≈ 25 days; 194 / 18.1 ≈ 11; 100 / 6.9 ≈ 14). That is meaningful but not a cliff.

This is not a loan-book reconstruction; a separate team owns that.

## 9. Coordinator request: OpenSea "floor walls" (Remilio, Terraforms)

`scripts/onchain_wallet_provenance.py` → `wallet_provenance.csv`, `wallet_provenance_summary.csv`.

| Wallet | Collection | Held at head | Lifetime tokens received |
|---|---|---|---|
| `0x54c6…4cfa` | Remilio | 1 | 4 |
| `0x163a…2094` | Remilio | 1 | 1 |
| `0x0033…3059` | Terraforms | 2 | 5 |
| `0xcd8c…a1ca` | Terraforms | 6 | 12 |

Blockscout confirms these holdings. **The walls of 90 / 52 / 46 / 27 listings cannot be backed by tokens in these wallets.**
- None of the held tokens came from Blend or other lending escrow, or from mint. All were marketplace purchases:
  - Remilio: 0.111 and 0.114 ETH in Oct-2026.
  - Terraforms `0x0033…`: 0.29 and 0.26 ETH in Oct-2026.
  - Terraforms `0xcd8c…`: six tokens at 1.18–1.32 ETH in Mar–Apr 2024.
- `0x54c6…` and `0x0033…` hold the same spam NFTs, so they are possibly one operator.

**[interp]** The order-book attribution should be re-checked: wrong maker field, stale listings, or a different contract. On-chain, there is no evidence that these walls are lender liquidations.

## 10. Data quality and known limitations

- **Wallet ≠ individual.** Holder counts, "new buyers" and cohorts are address-level. Wallet migrations inflate "new" wallets. Entity clustering is heuristic and partial.
- **Contract status is taken at the head block** and applied to all history. Safes, smart wallets and EIP-7702 EOAs are treated as wallets for cohorts, but retention metrics (b) and (c) **exclude every contract, Safes included**. An escrow-adjusted variant that credits Blend/Gondi collateral to the borrower is in `retention.csv`; it adds ≤0.5 pp.
- **Labels** are keyword rules on Blockscout names. 1,044 small contracts are unlabelled. Arcade "AssetVault"s are counted as lending although some may hold NFTs with no loan. Flooring Protocol EOA vaults were detected only among top-60 holders.
- **Sales detection is heuristic** (§5). On-chain counts exceed NPF by 22–47%; the cause is unresolved.
- **"Churn"** is a behavioural classification (dealer or arbitrage turnover), not wrongdoing. **"Suspect"** flags are indicators only.
- **Not measured:**
  - ETH funding links between buyers and sellers.
  - Unwrapped V1 punks.
  - Blur off-chain bid depth.
  - Sales outside the stated windows (full history is available for holders, but not for price).
  - Lil Pudgys key windows.
- **Endpoint risk.** One public RPC (dRPC) returned wrong receipt logs in 0.26% of calls; all were detected and re-fetched. Re-runs must use `onchain_validate_receipts.py`.

## 11. Files

**Scripts** (`scripts/`):
- `onchain_config.py`, `onchain_lib.py`
- `onchain_fetch_transfers.py`, `onchain_codes.py`, `onchain_labels.py`, `onchain_holders.py`
- `onchain_fetch_receipts.py`, `onchain_validate_receipts.py`, `onchain_sales.py`, `onchain_buyers.py`
- `onchain_wallet_provenance.py`, `onchain_summary_table.py`
- `common.py` was extended with `iter_logs`, `rpc_multi` and `RECEIPT_RPCS`.

**Raw data** (`data/raw/onchain/`):
- `<key>_transfers.jsonl` plus checkpoints
- `receipts/<key>.jsonl` and `validation.json`
- `codesize.json`
- `blockscout/addresses.jsonl` and `probes.json`
- `logs/`

**Processed data** (`data/processed/onchain/`):
- Holders: `holders_summary.csv`, `holders_monthly_<key>.csv`, `top_holders_<key>.csv`, `retention.csv`, `address_labels.csv`
- Escrow: `blend_escrow_monthly.csv`, `lending_escrow_current.csv`
- Sales: `sales_<key>.csv` (tx-level: block, ts, tx, tokenId, seller, buyer, price_eth, method, side, flags), `sales_enriched_<key>.csv` (adds wash/churn flags and cohorts), `movements_<key>.csv`
- Buyers: `buyers_monthly_<key>.csv`, `buyers_summary.csv`, `cohort_flows.csv`, `entity_accumulators_t12m.csv`
- Wash and liquidity: `wash_flags.csv`, `wash_summary.csv`, `liquidity_summary.csv`
- Reconciliation: `reconciliation.csv`, `reconciliation_bars_<key>.csv`
- Summary and coordinator request: `collector_comparison.csv`, `wallet_provenance*.csv`

Pipeline order:

```
fetch_transfers → codes → labels → holders → fetch_receipts → validate_receipts → sales → buyers → summary_table
```
