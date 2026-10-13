# V1 CryptoPunks (official wrapper WPV1) — dossier

Wrapper `0x282bdd42f4eb70e7a9d9f40c8fea0825b7f68c5d` around the original 2017 Larva Labs contract
`0x6Ba6f2207e343923BA692e5Cae646Fb0F566DB8D`. The full research with sources is in
[`_research/v1punks_culture.md`](_research/v1punks_culture.md). Catalysts are in `data/processed/catalysts/v1punks.csv`.
Chart: `reports/charts/v1punks_history.png`.

<!-- VERDICT -->

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 1.585 / 1.700 ETH ≈ $3,976 ≈ 0.0477 BTC | OpenSea API |
| Supply / holders / holders per item | 5,125 / 1,169 / 0.23 | on-chain |
| Floor-implied cap | $20.5M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -40% / -30% / -74% / -91% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 3.16× / 4.44× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.28 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 1.16; 105% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 48.3% / 62.9% |
| Supply untouched 12m / 24m | 86% / 72% |
| EOA holders from 24m ago still holding | 69% |
| Median token age | 943 days |
| Lending escrow (all protocols) | 74 tokens (1.4%) — gondi:74 |
| Trailing-12m sales / unique buyers / dealer-churn share | 1,424 / 463 / 49% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 1.9 |
| Purchases by first-time wallets (t12m) | 20% |
| Top-10 buyers' share of purchases (t12m) | 27% |
| Pre-2024 holders' net change (t12m) | -377 tokens |
| Wash-type flags (share of t12m sales) | 6.2% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 1 | 1.700 ETH | 1.500 ETH | 11.8% | 88% | 0 / 1 | 0.0% |

### BTC-relative scenarios (18-month horizon; `reports/scenario_model.md`)

| Scenario | ETH/BTC | Floor multiple (ETH) | Return vs BTC | Return in ETH | Return in USD |
|---|---|---|---|---|---|
| S1 weak | 0.024 | 0.60× | -59% | -48% | -65% |
| S2 moderate | 0.032 | 0.95× | -7% | -13% | +23% |
| S3 strong (disciplined) | 0.040 | 1.75× | +119% | +64% | +254% |
| S3 strong (hold-through) | 0.040 | 1.08× | +35% | +2% | +119% |
| S4 mania (disciplined) | 0.050 | 2.20× | +251% | +111% | +573% |
| S4 mania (hold-through) | 0.050 | 1.19× | +90% | +15% | +265% |

For comparison, plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.

## 1. Cultural durability thesis

- **Provenance is real.** V1 is the first CryptoPunks contract, deployed by Larva Labs on 2017-06-09 with the same
  10,000 images 13 days before V2. A bug in V1's marketplace led Larva Labs to abandon it and airdrop V2.
- **Legitimacy is contested, and that is the whole thesis:**
  - Larva Labs publicly said V1s "are not official" (2022-01-25) and issued a DMCA notice that briefly delisted them.
  - Yuga's license covered V2 only.
  - The current IP holder, the Infinite Node Foundation (NODE, since 2025-05-13), leaves V1 out of its official
    history.
  - **Every museum Punk found is V2** (MoMA 2025, Toledo).
  - V1's value therefore depends on (a) V2 Punks' price, since V1 trades at ~5% of V2, and (b) whether the market or
    institutions ever accept "the original contract" as meaningful.
- **No team to vanish.** The wrapper's owner can only change metadata. Since 2026-05-18, jalil.eth's PunksMarket lets
  unwrapped V1s trade "as intended" on the original contract.

## 2. Historical valuation & catalysts

- **The V1/V2 floor ratio** has compressed from ~7–10% (2022–23) to ~5% today.
- **Re-ratings came from structural Punks events:**
  - NODE's acquisition of Punks IP (2025-05-13): +109% vs BTC at 90 days.
  - The Jul-2025 Punks whale rally.
  - PunksMarket (2026-05-18): +34% at 90 days, floor 1.7 → 3.0 ETH, then faded to 1.585.
- **Wrap waves preceded weak prices** (Dec-2022, Oct-2023). Wrapping means more tradeable supply.

## 3. Collector behaviour

- **Extreme concentration:**
  - Top-10 wallets hold 48% of wrapped supply.
  - Three wallets (388 / 365 / 174) share a first-receipt date and look like one entity (~18%).
  - **A Gnosis Safe holds 1,084 *unwrapped* V1s**, with 414 V2 Punks in the same Safe. It is very likely Yuga, and it
    has been dormant since 2022-03-17.
  - The four largest non-wrapper V1 holders control 27.9% of all 10,000.
- **Retention is good** (72% of wrapped supply untouched for 24 months; 69% of holders retained). Churn is 49%.
- **Buying is concentrated:** `beautifulnfts.eth` made 12.9% of trailing-year purchases (+105 tokens).
- **Gondi lending escrow** is at an all-time high (74 tokens, 1.4%; 18 a year ago). Leverage is growing in a thin
  market.

## 4. Liquidity

- Whole-budget position = 1 token (1.70 ETH ask).
- Best bid is 88% of floor. Wrapped listings carry 0% fees. The instant round trip loses ~12%.
- Organic turnover is ~1.9 sales/day.
- OpenSea's 30-day sales count (30) is far below the on-chain count (117), unexplained. Some trading happens off
  OpenSea (PunksMarket, OTC).

## 5. Failure mechanisms

- NODE or Yuga enforces IP (a DMCA precedent exists) and V1 is delisted again.
- Yuga's 1,084-unit block, or the ~18% entity, is sold into a thin market.
- The V1/V2 ratio keeps compressing toward "derivative" status.
- V2 Punks fall. The V1 thesis is levered to them.

## 6. Bull thesis / bear thesis

- **Bull.** The cheapest exposure to CryptoPunks, the most resilient ETH NFT (−44% vs BTC 1y, against −73% for Pudgy),
  plus an option on legitimacy. Any NODE or museum acknowledgement, or a Yuga burn or donation of its 1,084, would be
  a step change. A return to a 10% ratio doubles the floor even with V2 flat. Scenario losses are the smallest of the
  finalists because the V2 anchor dampens the downside.
- **Bear.** The artists disowned it, and the IP holder and every institution have chosen V2. Ownership is highly
  concentrated with large dormant blocks. The "first contract" story has been told since 2022 and the ratio has only
  compressed. It is a leveraged bet on V2 Punks plus a legitimacy shift that keeps failing to arrive.

## 7. Entry conditions & what would change the view

- **Entry.** Bid ≤ ~1.5 ETH (the current best bid). The 2026 median was ~1.7 ETH, and the post-PunksMarket spike
  faded.
- **Upgrade if:**
  - NODE, a museum or a major auction house presents V1 alongside V2.
  - The Yuga Safe burns or donates its V1s.
  - The V1/V2 ratio rises above ~7% on volume.
- **Downgrade if:**
  - Any IP enforcement.
  - Movement from the Yuga Safe or the ~18% entity toward marketplaces.
  - Gondi escrow keeps rising, which signals leverage.
