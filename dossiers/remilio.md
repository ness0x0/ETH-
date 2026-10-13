# Redacted Remilio Babies — dossier

Contract `0xd3d9ddd0cf0a5f0bfb8f7fceae075df687eaebab` (Remilia). The full research with sources is in
[`_research/remilio_culture.md`](_research/remilio_culture.md). Catalysts are in `data/processed/catalysts/remilio.csv`.
Chart: `reports/charts/remilio_history.png`.

<!-- VERDICT -->

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 0.118 / 0.118 ETH ≈ $297 ≈ 0.0036 BTC | OpenSea API |
| Supply / holders / holders per item | 9,995 / 4,165 / 0.42 | on-chain |
| Floor-implied cap | $3.0M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -53% / -89% / -81% / -96% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 2.35× / 2.50× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.22 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 1.35; 200% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 15.6% / 32.2% |
| Supply untouched 12m / 24m | 77% / 57% |
| EOA holders from 24m ago still holding | 57% |
| Median token age | 896 days |
| Lending escrow (all protocols) | 118 tokens (1.2%) — blur_blend:100; gondi:18 |
| Trailing-12m sales / unique buyers / dealer-churn share | 6,234 / 1,416 / 68% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 5.3 |
| Purchases by first-time wallets (t12m) | 16% |
| Top-10 buyers' share of purchases (t12m) | 18% |
| Pre-2024 holders' net change (t12m) | -503 tokens |
| Wash-type flags (share of t12m sales) | 3.6% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 20 | 2.942 ETH | 2.086 ETH | 29.1% | 93% | 7 / 22 | 1.0% |

### BTC-relative scenarios (18-month horizon; `reports/scenario_model.md`)

| Scenario | ETH/BTC | Floor multiple (ETH) | Return vs BTC | Return in ETH | Return in USD |
|---|---|---|---|---|---|
| S1 weak | 0.024 | 0.31× | -79% | -73% | -82% |
| S2 moderate | 0.032 | 0.67× | -35% | -38% | -14% |
| S3 strong (disciplined) | 0.040 | 1.36× | +70% | +28% | +176% |
| S3 strong (hold-through) | 0.040 | 0.39× | -51% | -63% | -20% |
| S4 mania (disciplined) | 0.050 | 3.57× | +470% | +243% | +993% |
| S4 mania (hold-through) | 0.050 | 0.99× | +57% | -5% | +202% |

For comparison, plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.

## 1. Thesis in one paragraph

Remilio is Remilia's second collection (Aug 2022, minted at 0.125 ETH). It trades as a ~1.3× beta on Milady over
30-day windows and is below its mint price. Its identity is "the cheaper Milady". Without Remilia's events, airdrops
and Milady spillover there is little to anchor it, so on the founder-independence criterion it is the weakest
finalist.

Its history shows the highest convexity in good times:
- +504% vs BTC within 30 days of the Apr-2023 Bonkler/Tokyo announcement.
- The Oct-2023 → Mar-2024 rally.

It also shows the steepest falls on Remilia shocks: −69% in the Sept-2023 coup, and −76% vs BTC at 90 days after the
CULT TGE.

## 2. Collector behaviour and liquidity

- 4,165 holders, down from 4,570 in Jun-2024. Top-10 hold 15.6%.
- Several 140–285-token EOAs have accumulated since early 2024. Four entities each added 84–115 tokens in the last
  year while three large wallets sold ~100 each: a low-price handover between whales.
- Lending is 1.2% (Blend 100). The NFTX vault holds 171.
- Best bid is 93% of floor, but the ask side is thin above the floor. A 20-item position costs ~24% above floor on the
  instant book, and the instant round trip loses ~29%.
- **Correction:** the apparent 140-item floor "walls" in an earlier draft were duplicate OpenSea orders on two tokens.

## 3. Verdict rationale

It is a pure derivative of a founder-dependent parent, with weaker cultural standing, higher shock sensitivity and
worse round-trip costs at the investor's size. Anyone who wants Remilia exposure should prefer Milady itself.
