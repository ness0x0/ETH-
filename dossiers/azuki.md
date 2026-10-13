# Azuki (the investor's incumbent position) — dossier

Contract `0xed5af388653567af2f388e6224dc7c4b3241c544` (Chiru Labs / Azuki Labs). The full research with sources is in
[`_research/azuki_culture.md`](_research/azuki_culture.md). Catalysts are in `data/processed/catalysts/azuki.csv`.
Chart: `reports/charts/azuki_history.png`.

> **Verdict on the held Azuki: exit patiently; do not sell into the current forced-selling bid.** It fails the mandate (founder-dependent; the company's IP strategy bypasses the NFT; −75% vs BTC in the weak scenario; beat BTC in 1% of historical 18-month windows held and 7% with rule B). Measured against selling at today's net bid (0.461 ETH), its rule-B scenario case is similar to the other PFPs, so there is no urgency. List near the prevailing floor after the 2026-11-12 Blend deadline clears (182 Blend + 158 BendDAO tokens in escrow), or on any rebound. If you want to keep one NFT as a mania ticket, V1 is the better ticket on every mandate criterion.

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 0.490 / 0.548 ETH ≈ $1,229 ≈ 0.0147 BTC | OpenSea API |
| Supply / holders / holders per item | 10,000 / 4,355 / 0.44 | on-chain |
| Floor-implied cap | $12.3M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -71% / -93% / -94% / -99% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 2.74× / 1.86× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.26 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 1.20; 122% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 13.1% / 25.1% |
| Supply untouched 12m / 24m | 79% / 49% |
| EOA holders from 24m ago still holding | 65% |
| Median token age | 668 days |
| Lending escrow (all protocols) | 363 tokens (3.6%) — blur_blend:182; benddao:158; gondi:22; arcade:1 |
| Trailing-12m sales / unique buyers / dealer-churn share | 6,720 / 1,874 / 73% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 4.8 |
| Purchases by first-time wallets (t12m) | 18% |
| Top-10 buyers' share of purchases (t12m) | 15% |
| Pre-2024 holders' net change (t12m) | -665 tokens |
| Wash-type flags (share of t12m sales) | 4.2% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 5 | 2.747 ETH | 2.280 ETH | 17.0% | 85% | 0 / 9 | 1.0% |

### BTC-relative scenarios, ~18 months (v2 rule-based model; `reports/scenario_model.md`)

| Scenario (ETH/BTC) | Floor peak / end (ETH multiple) | Return vs BTC: hold | Return vs BTC: rule B | Return in USD: rule B |
|---|---|---|---|---|
| S1 weak (0.024) | 0.32× / 0.32× | -75% | -75% | -83% |
| S2 moderate (0.032) | 0.90× / 0.90× | +3% | +3% | +45% |
| S3 strong (0.040) | 1.11× / 0.25× | -64% | +12% | +141% |
| S4 mania (0.050) | 3.40× / 0.76× | +45% | +355% | +1352% |

Plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.
Break-even weight on S3+S4 (base mix): rule B 22%, hold never (ETH: 14%). Rule B = once ≥1.5× vs BTC, sell on a 30% drawdown from peak.
History (350 overlapping 18-month windows, 2022-06→2025-04 starts): beat BTC in 1% of windows holding, 7% with rule B; median multiple vs BTC 0.19× / 0.64× (`exit_rule_backtest.csv`).

## 1. Cultural durability thesis

- Azuki was a top-3 PFP in 2022 with a recognisable anime aesthetic. The art is on IPFS. About 4,350 owners remain,
  and the holder count has been rising since Sept 2024 (4,062).
- **The company is executing, but not for NFT holders.** It has a retail TCG ("Gates Awakened", 2026-06), a manga
  (Arnold Tsang), Studio Azuki (a JV with Westbrook) and fashion collaborations. Nothing routes value to the NFT.
  The 2026 roadmap describes Azuki as an IP company.
- **The founder-vanishes test: fails.** The remaining bid is mostly "orphan PFP" demand plus an option on company
  largesse.

## 2. Historical valuation & catalysts

- **Two permanent re-ratings lower, both company monetisation events:**
  - **Elementals mint (2023-06-27):** −74% vs BTC at 90 days. The company raised ~$38M from holders.
  - **ANIME token (TGE 2025-01-23):** −85% vs BTC at 90 days. Team, company and foundation took ~47%.
- **The Zagabond controversy (May 2022)** also preceded the long decline.
- **Product news since then shows ~0 abnormal effect**: the anime episodes, the Studio Azuki JV, the TCG launch and
  the manga.
- **Current level.** 0.49–0.55 ETH, the lowest since May 2022. −99% vs BTC from its ATH.

## 3. Collector behaviour

- 4,355 holders; top-10 hold 13.1%. 49% of supply untouched for 24 months; 65% of holders retained.
- 73% of sales are dealer churn. Organic turnover is ~4.8/day.
- **The highest lending escrow of the finalists:** 363 tokens (3.6%) — Blend 182, **BendDAO 158**, Gondi 22. BendDAO
  is a pooled lender with liquidation auctions, a separate forced-sale channel from Blend.
- **Flooring Protocol vault:** 155 tokens (1.6%), held by the vault EOA `chirulabs.liquidity.flooringlab.eth`.
- **Probable phishing drains:** a zero-price collection pattern (`0x71cf…fe33`) pulled tokens from dozens of wallets
  (unverified). These are excluded from sales.

## 4. Liquidity

- Best bid is 85% of floor. 49 unique bidders.
- **Selling one Azuki now realises ~0.466 ETH × 0.99 ≈ 0.461 ETH (~$1,157).**
- Organic turnover is ~4.8/day, so exiting one item is easy. The question is price, not access.

## 5. Failure mechanisms (for continuing to hold)

- Further monetisation, such as another token or companion collection, follows the Elementals/ANIME pattern.
- BendDAO and Blend liquidations during the Blur wind-down add near-term supply.
- ANIME insider vesting runs to ~Jan 2029, and the token is down ~97%.
- Company pivot or sale with no holder rights.

## 6. Bull thesis / bear thesis

- **Bull.** It sits at an all-time-low floor with a company that ships real products. A hit TCG or anime plus a
  holder reward would re-rate it. A ~$1.2k position is cheap optionality.
- **Bear.**
  - Holders have repeatedly funded the company's monetisation and then absorbed permanent re-ratings.
  - The IP strategy bypasses the NFT.
  - Lending escrow is the highest of the set, the trend is negative quarter after quarter, and there is no evidence
    of a base.
  - Of all finalists it has the most founder-dependent upside and the least evidence that execution helps holders.

## 7. Hold or replace?

The decision is small in dollars (~$1.2k) but should be made on the same criteria as any new purchase. Azuki fails
every criterion in the mandate: cultural durability without the team, low founder dependence, organic demand, and
BTC-relative evidence.

**Timing nuance.** Part of today's price may be temporary Blur/Blend and BendDAO forced selling:
- 68 tokens left Blend on 13 Oct.
- The floor fell 0.63 → 0.49 ETH over Oct 7–13.
- The Blend repay-or-default deadline is 2026-11-12.

A seller who believes that pressure is temporary can list near the prevailing floor through November rather than hit
today's bid (~85% of floor). There is no evidence of a durable rebound to wait for.
