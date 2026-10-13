# CryptoDickbutts — dossier

Contract `0x42069abfe407c60cf4ae4112bedead391dba1cdb`. The full research with sources is in
[`_research/cryptodickbutts_culture.md`](_research/cryptodickbutts_culture.md). Catalysts are in
`data/processed/catalysts/cryptodickbutts.csv`. Chart: `reports/charts/cryptodickbutts_history.png`.

> **Verdict: conditional shortlist #3 — small, patient, bid-side only.** It is the only finalist that has already passed the 'team vanished' test (handover 2023), with strong holder retention and an attainable hold-through break-even. But exit liquidity at size is poor (~1.1 organic sales/day, best bid 84% of floor) and its meme IP is contested.

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 0.472 / 0.473 ETH ≈ $1,184 ≈ 0.0142 BTC | OpenSea API |
| Supply / holders / holders per item | 5,198 / 2,131 / 0.41 | on-chain |
| Floor-implied cap | $6.2M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -66% / +47% / -59% / -94% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 6.39× / 7.90× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.33 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 0.87; 138% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 12.2% / 29.1% |
| Supply untouched 12m / 24m | 86% / 61% |
| EOA holders from 24m ago still holding | 71% |
| Median token age | 1,168 days |
| Lending escrow (all protocols) | 5 tokens (0.1%) — gondi:4; compound_fork_nft:1 |
| Trailing-12m sales / unique buyers / dealer-churn share | 1,033 / 358 / 58% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 1.1 |
| Purchases by first-time wallets (t12m) | 18% |
| Top-10 buyers' share of purchases (t12m) | 24% |
| Pre-2024 holders' net change (t12m) | -327 tokens |
| Wash-type flags (share of t12m sales) | 5.4% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 5 | 3.040 ETH | 1.798 ETH | 40.9% | 84% | 0 / 3 | 1.0% |

### BTC-relative scenarios, ~18 months (v2 rule-based model; `reports/scenario_model.md`)

| Scenario (ETH/BTC) | Floor peak / end (ETH multiple) | Return vs BTC: hold | Return vs BTC: rule B | Return in USD: rule B |
|---|---|---|---|---|
| S1 weak (0.024) | 0.68× / 0.68× | -64% | -64% | -76% |
| S2 moderate (0.032) | 0.90× / 0.90× | -27% | -27% | +3% |
| S3 strong (0.040) | 3.49× / 1.80× | +83% | +149% | +435% |
| S4 mania (0.050) | 3.49× / 1.80× | +154% | +245% | +1000% |

Plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.
Break-even weight on S3+S4 (base mix): rule B 20%, hold 30% (ETH: 14%). Rule B = once ≥1.5× vs BTC, sell on a 30% drawdown from peak.
History (350 overlapping 18-month windows, 2022-06→2025-04 starts): beat BTC in 31% of windows holding, 34% with rule B; median multiple vs BTC 0.45× / 0.78× (`exit_rule_backtest.csv`).

## 1. Cultural durability thesis

- **A CC0 2021 collection built on a ~20-year-old internet meme**, with CryptoPunks-adjacent OG status. 5,200 supply.
- **The founder-vanishes test: already passed.** The founders handed control to the largest holder in Aug 2023. Since
  2025-11-03 a holder DAO ("Penus DAO") and collector Adam Weitsman have run it. Owners stayed at ~2.1k, and the
  floor rallied ~8× in BTC terms in 2025 without a team.
- **Provenance is contested.** There is no licence from K.C. Green, the meme's creator, who has disavowed the meme.
  The mass meme audience has moved to an unaffiliated fungible memecoin.

## 2. Historical valuation & catalysts

- **The $gooch token snapshot (May 2023)** did not lift it: −33% at 90 days.
- **The team-exit announcements (Jul–Aug 2023)** marked the start of the capitulation: −87% in ETH terms to Jul 2024.
- **The 2025 rally** (BTC-terms floor 0.0078 → 0.0616, Apr–Aug 2025) coincided with the ETH/BTC recovery and an
  unaffiliated DICKBUTT memecoin wave. No source documents the cause, so treat it as beta from a deep base.
- **Since then:** −66% vs BTC over 12 months and −41% in 2026.

## 3. Collector behaviour

- **Strong holding:** 86% of supply untouched for 12 months; median token age 1,168 days; negligible lending (0.1%).
- **Thin and lumpy trading:** 1,033 sales in 12 months, 1.1 organic sales/day, an 11-hour median organic gap.
  NPF's bar correlation with on-chain sales is weak (0.59).
- A "DickStrategy" programmatic bidder holds 1.5%. `cdb-otc.eth` was a net buyer of 33.

## 4. Liquidity: the disqualifier

- Best bid is 84% of floor, with zero funded bids at ≥90%.
- A 5-item position costs ~29% above floor on the instant book, and the instant round trip loses ~41%.
- Correction: an earlier draft cited NPF data implying sales at ~0.64× floor. On-chain sales show a trailing-12m
  median sale price of 1.02× the NPF floor, so the floor is executable for single items. The problem is bid depth and
  turnover at the investor's size.

## 5. Bull thesis / bear thesis

- **Bull.**
  - Genuinely founder-independent.
  - A deep meme with a committed whale and DAO.
  - The highest convexity in the set in 2025 (+690% vs BTC trough to peak).
- **Bear.**
  - Slow to exit at size: ~1.1 organic sales/day, and the best bid is 84% of floor.
  - Contested IP.
  - Governance concentrated in one whale.
  - No catalyst in its history created lasting value.

## 6. Verdict rationale

It passes the founder test, and its rule-based scenario profile is comparable to V1's: rule-B break-even 20%,
hold-through break-even 30%. But it fails the exit-liquidity test at the investor's ticket size and has contested
IP. A patient, bid-side accumulation of 1–2 items is the only sensible way to own it.
