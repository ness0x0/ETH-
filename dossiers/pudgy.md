# Pudgy Penguins (and Lil Pudgys) — dossier

Contract `0xbd3531da5cf5857e7cfaa92426877b022e612cf8` (Lil Pudgys: `0x524cab2ec69124574082676e6f654a18df49a048`).
The full research with sources is in [`_research/pudgy_culture.md`](_research/pudgy_culture.md). Catalysts are in
`data/processed/catalysts/pudgy.csv`. Chart: `reports/charts/pudgy_history.png`.

<!-- VERDICT -->

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 2.310 / 2.430 ETH ≈ $5,795 ≈ 0.0695 BTC | OpenSea API |
| Supply / holders / holders per item | 8,888 / 4,997 / 0.56 | on-chain |
| Floor-implied cap | $51.5M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -73% / -80% / -76% / -94% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 2.97× / 3.30× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.22 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 1.43; 117% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 9.3% / 19.0% |
| Supply untouched 12m / 24m | 72% / 48% |
| EOA holders from 24m ago still holding | 57% |
| Median token age | 676 days |
| Lending escrow (all protocols) | 259 tokens (2.9%) — blur_blend:194; gondi:61; paraspace:4 |
| Trailing-12m sales / unique buyers / dealer-churn share | 8,884 / 2,177 / 75% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 5.9 |
| Purchases by first-time wallets (t12m) | 19% |
| Top-10 buyers' share of purchases (t12m) | 17% |
| Pre-2024 holders' net change (t12m) | -652 tokens |
| Wash-type flags (share of t12m sales) | 4.4% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 1 | 2.430 ETH | 2.247 ETH | 7.5% | 93% | 5 / 12 | 1.0% |

### BTC-relative scenarios (18-month horizon; `reports/scenario_model.md`)

| Scenario | ETH/BTC | Floor multiple (ETH) | Return vs BTC | Return in ETH | Return in USD |
|---|---|---|---|---|---|
| S1 weak | 0.024 | 0.45× | -67% | -59% | -73% |
| S2 moderate | 0.032 | 0.85× | -14% | -19% | +13% |
| S3 strong (disciplined) | 0.040 | 1.60× | +104% | +54% | +231% |
| S3 strong (hold-through) | 0.040 | 0.59× | -24% | -43% | +23% |
| S4 mania (disciplined) | 0.050 | 3.25× | +424% | +215% | +905% |
| S4 mania (hold-through) | 0.050 | 1.12× | +81% | +9% | +247% |

For comparison, plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.

## 1. Cultural durability thesis

- **The only ETH PFP whose brand reached mass retail:** Walmart, Target, Walgreens, GIPHY, the Sphere, and a TCG
  through Orange Cap Games. The penguin is the most recognisable crypto mascot.
- **The brand's value does not belong to NFT holders:**
  - Licensing revenue goes to Pudgy Penguins Inc./Igloo. Holders earn a royalty only if their own penguin is picked
    for a product.
  - The token (PENGU, 2024-12-17) moved holder value into a liquid coin, which ~29% insider supply unlocks into
    through ~Dec 2028.
  - Lil Pudgys metadata is served from an Igloo server.
- **The founder-vanishes test: fails** (low to moderate independence). Without Igloo, the NFT would likely trade like
  other orphaned 2021 PFPs. Today those sit at 0.09–0.5 ETH (Cool Cats, Doodles, Azuki).
- **Corporate state (verified):**
  - Igloo announced on 2026-10-06 that its Abstract L2 will shut on 2026-12-15, after losses in the "tens of millions".
  - The Canary PENGU ETF rule filing was withdrawn on 2026-01-23.
  - The Pudgy Party game was wound down in June 2026.
  - Igloo says it is now refocusing all resources on Pudgy and PENGU.

## 2. Historical valuation & catalysts

- **2022–23: genuine brand-building re-ratings.** After the toys announcement and the Walmart deal, the floor rose
  +109% vs BTC within 90 days of the Sept-2023 Walmart rollout. Pudgy outperformed the sector index ~20–30× from
  mid-2022 to 2025.
- **Dec 2024: PENGU airdrop.** The floor ran 13.7 → 25.2 ETH into the TGE (CoinGecko intraday ATH 36.3), then fell
  −79% vs BTC within 90 days. No snapshot was taken, so the claim value travelled with the NFT until claimed.
- **Jul 2025: ETF hype.** +121% vs BTC in 30 days, then −33% at 180.
- **2025–26: retail expansion with no floor effect.** Target, Walgreens, Pengu Card and Kung Fu Tea coincided with a
  ~75% decline in ETH terms.
- **Oct 2026: shock.** 3.18 → 2.35 ETH over Oct 1–13 (Abstract shutdown, Blur/Blend shutdown).

## 3. Collector behaviour

- **The broadest ownership** among the PFPs: top-10 hold 9.3%; 4,997 holders.
- **Weak retention:** 48% of supply untouched for 24 months. 75% of trailing-year sales were dealer churn. Organic
  turnover is ~5.9/day.
- **Distribution.** Pre-2024 holders net sold 652 in the last year. One three-wallet entity sold 161 Pudgies plus 94
  Lil Pudgys.
- **Absorption.** One entity (`0xb972…2f97` → Safe `0x250d…55e7`) bought **131 Pudgies (~371 ETH) between 6 and 12
  Oct 2026**, 80 of them in the 11-Oct sell-off. That is real, concentrated support at ~2.5–3 ETH.
- **Lending overhang.** 259 tokens (2.9%): Blend 194, Gondi 61. That is down from 7.4% in Sep-2025, and 119 left
  Blend on 13 Oct alone.

## 4. Liquidity

The best of all finalists:
- Best bid is 93% of floor. 61 unique bidders. Fees are 1%. The instant round trip loses ~7.5% for a whole-budget,
  single-token position.
- Lil Pudgys is divisible (~12 items for the budget) with a ~11% round trip and 10.9 organic sales/day, but even more
  team-dependent and the weakest retention.

## 5. Failure mechanisms

- Igloo runs out of money or sells the IP. The NFT is orphaned.
- PENGU unlocks and price weakness drag the "ecosystem" narrative.
- A second token or airdrop pulls value forward again (pump then dump).
- Blend defaults and lender sales before or after 2026-11-12. The overhang is falling but not zero.
- The trademark suit (PEI Licensing, S.D. Fla., pending) or another corporate legal event.

## 6. Bull thesis / bear thesis

- **Bull.** The most liquid, most widely held, highest-β (1.43 to ETH/BTC) ETH PFP, now at a BTC-terms cycle low
  (0.069 BTC, −94% from peak) after a capitulation week that a large buyer absorbed. Igloo has cut its distractions to
  focus on Pudgy. In any NFT risk-on phase it is the first PFP institutions and retail rotate into, and since Jul-2022
  it has roughly matched BTC (0.94×), unlike almost everything else.
- **Bear.**
  - Every big move came from company-manufactured catalysts (toys, PENGU, ETF hype). The airdrop is spent.
  - Brand success now accrues to equity and PENGU, not to the NFT.
  - The company just wrote off an L2, lost its ETF and closed a game.
  - Insiders unlock PENGU through the whole horizon.
  - −73% vs BTC in a year.

## 7. Entry conditions & what would change the view

- **Entry.** Treat it as a trade, not a collectible:
  - Bid at ≤~2.25–2.3 ETH, the current best-bid level.
  - Or wait until after 2026-11-12, once the Blend unwind is visible in escrow counts.
  - Sell into strength. Its rallies retained only 22–33% of peak after 180 days.
- **Upgrade if:**
  - A credible holder-value mechanism appears, such as revenue share or IP rights for holders.
  - Igloo announces an IPO with holder participation.
  - Organic sales rise without token catalysts.
- **Downgrade if:**
  - Igloo announces further retrenchment or funding stress.
  - The 131-token absorber starts distributing.
