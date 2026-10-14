# Ranked shortlist (conditional)

**Read this after the [executive memo](EXECUTIVE_MEMO.md).** The headline recommendation is **no NFT purchase now**.
This ranking says what to buy *if* the entry gates below are met **and** you choose to hold a speculative "mania
ticket" anyway. It is not a recommendation to buy today.

Data as of 2026-10-13: ETH $2,508.69, ETH/BTC 0.0301. Prices are OpenSea order-book asks and bids at ~22:30 UTC.
"Rule B" means: once the position is ≥1.5× vs BTC, sell on a 30% drawdown from its post-entry peak.

## Summary

| Rank | Collection | Role | Executable entry | Weak-scenario loss vs BTC (S1) | Rule-B break-even* | Hold-through break-even* | Historical: beat BTC with rule B† | Mandate fit |
|---|---|---|---|---|---|---|---|---|
| — | **ETH** | Clean vehicle for the macro view | Spot | −20% | **14%** | 14% | — | Not an NFT; captures the ETH/BTC part of the thesis |
| 1 | **V1 CryptoPunks** | Founder-independent mania ticket | 1 item, ask 1.70 / bid 1.50 ETH | **−51%** | 20% | **34%** | 32% | No team; legitimacy contested |
| 2 | **Milady Maker** | Culture ticket (mandate exception) | 2–3 items, ask 0.745 / bid 0.686 | −67% | 22% | never | 41% | Founder-dependent |
| 3 | **CryptoDickbutts** | Small founder-independent meme ticket | 1–2 items via bids, ask 0.473 / bid 0.399 | −64% | 20% | 30% | 34% | Team gone since 2023; IP contested |
| 4 | **Chromie Squiggle** | Collectible only | 1 item, ask 2.64 / bid 2.05 | −64% | **55%** | never | 13% | Strongest durability; worst investment case |
| n/r | Pudgy Penguins | Tactical, outside the mandate | 1 item, ask 2.43 / bid 2.27 | −67% | 22% | never | 80% (operator era) | Founder- and company-dependent |
| held | Azuki | Exit patiently | Sell-now net bid 0.461 | −75% | 22% | never | 7% | Founder-dependent |

\* Weight on S3+S4 (2:1 mix vs S1:S2 50:50) at which the expected return vs BTC is zero (`reports/scenario_model.md`).
Gaps under ~10 pp are not meaningful.
† Share of 350 overlapping 18-month windows (2022-06 → 2025-04 starts) in which rule B beat BTC
(`exit_rule_backtest.csv`; in-sample, bear-dominated).

**Not recommended:**
- Terraforms: latent 1,193-token owner mint by a single EOA, single-buyer bid dependence, ~28% round trip.
- Remilio: a derivative of a founder-dependent parent.
- Every watchlist name (`universe.csv`).

## Entry gates (all must hold before any NFT purchase)

| Gate | Test | Status 2026-10-13 |
|---|---|---|
| **G1 Liquidity regime** | After Blur's frontend closes (2026-11-12), re-run `scripts/liquidity_orderbook.py`. The target's best *funded* bid must be within ~15% of its floor, and for PFPs the Blend escrow must be resolved (`data/processed/onchain/blend_escrow_monthly.csv`) | **Not testable until mid-Nov.** Pudgy and Azuki ran 52–58% of trailing-year sales through Blur/Blend |
| **G2 Market regime** | ETH/BTC weekly close above its 30-week average **and** universe traded volume >$35M/month for two consecutive months (`scripts/sector_activity.py`) | **Not met.** ETH/BTC 0.0301 vs 30w MA 0.0295 (marginal pass); volume $16–34M/month in 2026 with no uptrend |
| **G3 Conviction** | Your own weight on S3+S4 is ≥~25% **and** you will follow rule B mechanically. If the conviction is really about ETH/BTC, ETH needs only ~14% | Investor's call |
| **G4 Price** | Bid at or below today's best bid, not the ask: V1 ≤1.5 ETH, Milady ≤0.69, CDB ≤0.40–0.45, Squiggle ≤2.05–2.3 | Patience heuristics, not derived optima |

**Sizing if all gates pass.** One V1 (~1.5 ETH ≈ $3.8k, about half of the allocation), or 2–3 Miladys (~$3.5–5k).
Keep the rest in BTC (or ETH if that is your macro view). Treat the NFT leg as fully losable. Don't buy more than one
ranked name; the budget doesn't diversify, it only adds round-trip costs.

## Supply overhangs (one table, all names)

| Collection | Overhang | Size | ≈ Days of organic turnover |
|---|---|---|---|
| V1 Punks | Four non-wrapper wallets, including the likely-Yuga Safe (1,084 V1, dormant since 2022) | 2,790 V1 (27.9% of all 10,000) | ~1,470 |
| Chromie Squiggle | One original-minter entity (identity unverified) | 1,314 (13.1%) | ~880 |
| Terraforms | Latent `ownerClaim` mint controllable by a single EOA | up to 1,193 new tokens (+12%) | ~480 |
| Azuki | Lending escrow: Blend 182 + BendDAO 158 + Gondi 22; Flooring vault 155 | 363 (3.6%) + 155 | ~76 (escrow only) |
| Pudgy | Lending escrow: Blend 194 + Gondi 61; one absorber Safe holds 130 | 259 (2.9%) | ~44 |
| Milady | Lending escrow: Blend 136 + Gondi 63; **plus 53.1B undistributed CULT (53%)** — a token overhang, not NFT supply | 200 (2.0%) | ~38 |
| Remilio | Lending escrow (Blend 100); NFTX vault 171 | 118 (1.2%) | ~22 |
| CryptoDickbutts | Whale and DAO concentration; programmatic bidder (DickStrategy) holds 78 | lending 5 (0.1%) | ~5 |

---

## 1. V1 CryptoPunks — conditional #1

- **Current executable valuation:**
  - Ask 1.70 ETH (≈$4.26k ≈ 0.051 BTC); best funded bid 1.50 ETH.
  - 0% seller fees on wrapped listings. Instant round trip ~12%.
  - Floor-implied cap ~$20M on ~5.1k wrapped tokens. V1 trades at ~5% of the V2 Punk floor (31.3 ETH).
- **Cultural durability thesis:** the first CryptoPunks contract (2017-06-09, Larva Labs, same 10,000 images as V2).
  No team to vanish; the wrapper owner can only change metadata. PunksMarket (2026-05) lets V1s trade natively on the
  original contract.
- **Organic demand evidence:**
  - 72% of wrapped supply untouched for 24 months.
  - 1.9 organic sales/day.
  - 463 unique buyers in the last 12 months (60% new wallets).
  - Buying is concentrated: one entity made 12.9% of purchases.
  - Gondi lending escrow is at an all-time high (1.4%).
- **Historical catalyst dependence:** moves came from Punks-wide events (NODE IP sale, the Jul-2025 Punks rally,
  PunksMarket). All are now back to pre-event BTC levels, and much of the move was market beta. There is no
  token-airdrop history.
- **Future catalysts (speculative):**
  - NODE, a museum or an auction house acknowledging V1.
  - The Yuga-linked Safe burning or donating its 1,084 V1s.
  - Further native V1 sales.
  - Negative: DMCA or other IP enforcement (2022 precedent), or a sale from the Safe.
- **Liquidity:** single-item exit is feasible (bid 88% of floor). Only 1 funded bid sits ≥80% of floor, so size above
  one item is thin. OpenSea counts only ~25% of on-chain sales; the rest happen elsewhere.
- **BTC-relative scenarios:**
  - Rule B: S1 −51%, S2 −10%, S3 +84%, S4 +197%. Hold: S3 +31%, S4 +111%.
  - It has the smallest weak-scenario loss and one of only two attainable hold-through break-evens, because V2 Punks
    anchor the downside.
- **Failure conditions:**
  - IP enforcement.
  - Dormant-wallet distribution.
  - Continued V1/V2 ratio compression (from ~10% in 2022 to ~5% now).
  - A fall in V2 Punks (−44% vs BTC over 1y).
- **Entry:** gates G1–G3. Bid ≤1.5 ETH.
- **Why prefer it over BTC or the Azuki:** it beats BTC only in S3/S4. It is a better *ticket* than the Azuki on
  every mandate axis: no founder dependence, smaller S1 loss (−51% vs −75%), an attainable hold-through break-even,
  and a far better historical rule-B hit rate (32% vs 7%).
- **Strongest bear case:** the creators disowned it, the IP holder and every museum chose V2, and since 2022 the "first
  contract" story has only lost ground. Dossier: [`dossiers/v1punks.md`](../dossiers/v1punks.md).

## 2. Milady Maker — conditional #2 (mandate exception)

- **Current executable valuation:**
  - Ask 0.745 ETH (≈$1.87k ≈ 0.022 BTC); bid 0.686. 1% fees. The 3rd-cheapest listing is already ~20% above floor.
  - Floor cap ~$18.6M.
- **Cultural durability thesis:**
  - The deepest living culture of any affordable ETH PFP: network-spirituality canon, IRL raves since 2021.
  - Vitalik holds two (on-chain verified) and twice adopted one as his avatar.
  - It survived a founder-scandal crash and a coup.
- **Organic demand evidence:**
  - ~5.3 organic sales/day.
  - 2,001 buyers in the last 12 months, 69% new wallets.
  - Holder count is flat at ~5,100.
  - Pre-2024 holders net sold 506.
- **Historical catalyst dependence:** **high.**
  - Every positive move since 2023 was a Remilia or celebrity event that retraced within 1–3 months.
  - The CULT TGE was followed by −68% vs BTC at 90 days.
  - Quiet windows since then lost 28–59% in ETH terms.
- **Future catalysts:**
  - CULT distributions (53% undistributed), RemiliaChat, fashion, another Vitalik moment.
  - Negative: a new Remilia scandal or lawsuit outcome; the Miya book.
- **Liquidity:** best bid 92% of floor; 7 funded bids ≥90%. Divisible, so a holder can scale out.
- **BTC-relative scenarios:**
  - Rule B: S1 −67%, S2 −13%, S3 +32%, S4 +372%. Hold: S3 −54%.
  - About 85% of the positive expected contribution comes from the mania branch.
- **Failure conditions:** a founder or governance shock; CULT reactivation as sell pressure; continued liquidity decay
  (2026 volume is ~3% of 2023's).
- **Entry:** gates G1–G3. Bid ≤0.69. Accumulate over weeks.
- **Why prefer it over the Azuki:** stronger culture (one founder vs a company that monetises holders), better
  historical rule-B hit rate (41% vs 7%), divisibility.
- **Strongest bear case:** the founder *is* the brand, and the price is an event-driven series of spikes that fully
  retrace. Dossier: [`dossiers/milady.md`](../dossiers/milady.md).

## 3. CryptoDickbutts — conditional #3 (small, bid-side only)

- **Current executable valuation:**
  - Ask 0.473 ETH (≈$1.19k); bid 0.399.
  - Single items clear near the floor (on-chain trailing-12m median sale 1.02× floor), but a 5-item sweep costs ~29%
    above floor.
- **Cultural durability thesis:** a 2021 CC0 collection built on a ~20-year-old internet meme. **It has already
  passed the "team vanished" test:** the founders handed over control in 2023; a DAO and a collector have run it
  since 2025-11.
- **Organic demand evidence:**
  - 86% of supply untouched for 12 months; 71% of holders retained over 24 months.
  - ~1.1 organic sales/day.
  - The top-10 buyers took 24% of purchases.
- **Historical catalyst dependence:** low. No catalyst created lasting value, and its rallies tracked ETH/BTC beta from
  deep bases.
- **Future catalysts:** DAO/Weitsman redevelopment, memecoin crossovers (unaffiliated). None are reliable.
- **Liquidity:** the weakest of the ranked names. Best bid 84% of floor; no funded bids ≥90%; 11-hour median gap
  between organic sales.
- **BTC-relative scenarios:** rule B: S1 −64%, S2 −27%, S3 +149%, S4 +245%. Hold: S3 +83%. The S3/S4 peaks are capped
  at its Aug-2025 high.
- **Failure conditions:**
  - The meme audience migrates to fungible tokens.
  - Contested IP: the original artist disowned it.
  - Whale or DAO governance concentration.
  - Liquidity drought.
- **Entry:** bids ≤0.40–0.45 ETH, 1–2 items. Do not sweep.
- **Strongest bear case:** it may simply be unexitable at size when it matters. Dossier:
  [`dossiers/cryptodickbutts.md`](../dossiers/cryptodickbutts.md).

## 4. Chromie Squiggle — conditional #4 (collectible, not investment)

- **Current executable valuation:**
  - Ask 2.642 ETH (≈$6.63k ≈ 0.080 BTC; 88% of budget).
  - Best bid 2.05 (78% of floor).
  - **8.5% seller fees** (7.5% enforced royalty — a venue policy). Instant round trip ~29%.
- **Cultural durability thesis:** the strongest in the universe.
  - Project #0 of Art Blocks; a locked, fully on-chain script; fixed supply.
  - MoMA (donated set), LACMA (#9999), Toledo.
  - The artwork is independent of the company.
- **Organic demand evidence:**
  - 45% of purchases by first-time wallets (~283 first-time buyers in level terms); 20% dealer churn; 1.5 organic sales/day.
  - 84% of supply dormant for 24 months, partly a 13.1% single-entity block.
- **Historical catalyst dependence:** none from tokens. Institutional news has had no durable price effect. Price
  follows ETH/BTC and the sector.
- **Liquidity:** the worst exit economics among the ranked names.
- **BTC-relative scenarios:**
  - Rule B: S1 −64%, S2 −23%, S3 +8%, S4 +93%.
  - Break-even 55% vs 14% for ETH.
  - Beat BTC in 2% of historical 18-month windows held, 13% with rule B.
- **Failure conditions:** generative art stays a closed niche, the 13% entity distributes, the royalty regime
  persists.
- **Entry:** only if owning it is the goal. Bid ≤2.05–2.3 ETH.
- **Strongest bear case:** none of its durability has translated into BTC-relative returns, and the fees tax every
  exit. Dossier: [`dossiers/chromie_squiggle.md`](../dossiers/chromie_squiggle.md).

## Not ranked: Pudgy Penguins (tactical alternative outside the mandate)

- The most liquid finalist: 7.5% instant round trip; whole budget = 1 item.
- Best historical rule-B record: beat BTC in 80% of windows. That record comes from an operator-driven 2022–24 run
  (toys, PENGU, ETF hype) that has since reversed.
- It fails founder-independence. Holders have no claim on IP or revenue. PENGU insiders unlock through ~2028. Abstract
  shuts 2026-12-15. ~58% of trailing-year liquidity ran through Blur/Blend.
- **If you consciously trade outside the mandate,** it is the most exitable PFP. Apply G1 strictly.

Dossier: [`dossiers/pudgy.md`](../dossiers/pudgy.md).

## The held Azuki

- Exit patiently. Don't sell into today's forced-selling bid (0.466 ETH, ~85% of the ask), while 182 Blend and 158
  BendDAO tokens are in escrow ahead of the 2026-11-12 deadline.
- List near the prevailing floor after the deadline, or on any rebound. Proceeds go to BTC.
- Measured from the sell-now bid, its rule-B scenario case is similar to the other PFPs. That is a reason not to
  panic-sell, not a reason to keep it.
- It fails the mandate: the company's IP strategy bypasses the NFT, and it beat BTC in only 1–7% of historical windows.
- If you want to keep exactly one NFT as a mania ticket, V1 is the better one.

Dossier: [`dossiers/azuki.md`](../dossiers/azuki.md).
