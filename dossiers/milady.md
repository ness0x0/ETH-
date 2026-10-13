# Milady Maker — dossier

Contract `0x5af0d9827e0c53e4799bb226655a1de152a425a5` (Remilia Corporation). The full research with sources is in
[`_research/milady_culture.md`](_research/milady_culture.md). Catalysts are in `data/processed/catalysts/milady.csv`.
Quiet-window returns: `data/processed/culture/quiet_window_returns.csv`. Chart: `reports/charts/milady_history.png`.

> **Verdict: conditional shortlist #2 — a mandate exception.** It has the strongest living culture of any affordable ETH PFP, is divisible (3 items) and is liquid, but it fails the founder-independence test: its price has been driven by Remilia and celebrity events that fully retraced, and every quiet window since the CULT TGE lost 28–59% in ETH terms. Own it only with rule-B exit discipline.

### Snapshot (2026-10-13)

| Metric | Value | Source |
|---|---|---|
| Floor (OpenSea stats / live ask) | 0.744 / 0.745 ETH ≈ $1,866 ≈ 0.0224 BTC | OpenSea API |
| Supply / holders / holders per item | 9,976 / 5,129 / 0.51 | on-chain |
| Floor-implied cap | $18.6M | floor × supply |
| vs BTC: 1y / 2y / 3y / from BTC-terms ATH | -59% / -82% / -79% / -92% | NPF + Binance |
| Rally trough→peak vs BTC (2024 / 2025) | 2.40× / 2.32× | rally_analysis.csv |
| Share of 2025 peak kept 180d later (BTC terms) | 0.30 | rally_analysis.csv |
| β of BTC-terms floor to ETH/BTC; annualised vol | 0.76; 137% | weekly, 2022–26 |

### Collector behaviour (on-chain, head 2026-10-13)

| Metric | Value |
|---|---|
| Top-10 / top-50 holder share | 11.2% / 24.2% |
| Supply untouched 12m / 24m | 75% / 53% |
| EOA holders from 24m ago still holding | 58% |
| Median token age | 847 days |
| Lending escrow (all protocols) | 200 tokens (2.0%) — blur_blend:136; gondi:63; other_lending:1 |
| Trailing-12m sales / unique buyers / dealer-churn share | 7,437 / 2,001 / 74% |
| Organic sales per day (365d, ex-churn, ex-flagged) | 5.3 |
| Purchases by first-time wallets (t12m) | 21% |
| Top-10 buyers' share of purchases (t12m) | 15% |
| Pre-2024 holders' net change (t12m) | -506 tokens |
| Wash-type flags (share of t12m sales) | 3.4% |

### Liquidity for a ~$7.5k position (OpenSea book, 2026-10-13 22:30 UTC)

| Items | Entry cost | Instant exit (after fees) | Round-trip loss | Best bid / floor | Funded bids ≥90% / ≥80% of floor | Seller fees |
|---|---|---|---|---|---|---|
| 3 | 2.435 ETH | 2.036 ETH | 16.4% | 92% | 7 / 10 | 1.0% |

### BTC-relative scenarios, ~18 months (v2 rule-based model; `reports/scenario_model.md`)

| Scenario (ETH/BTC) | Floor peak / end (ETH multiple) | Return vs BTC: hold | Return vs BTC: rule B | Return in USD: rule B |
|---|---|---|---|---|
| S1 weak (0.024) | 0.47× / 0.47× | -67% | -67% | -78% |
| S2 moderate (0.032) | 0.90× / 0.90× | -13% | -13% | +22% |
| S3 strong (0.040) | 1.56× / 0.38× | -54% | +32% | +185% |
| S4 mania (0.050) | 4.37× / 1.07× | +65% | +372% | +1404% |

Plain ETH vs BTC: S1 -20%, S2 +6%, S3 +33%, S4 +66%.
Break-even weight on S3+S4 (base mix): rule B 22%, hold never (ETH: 14%). Rule B = once ≥1.5× vs BTC, sell on a 30% drawdown from peak.
History (350 overlapping 18-month windows, 2022-06→2025-04 starts): beat BTC in 31% of windows holding, 41% with rule B; median multiple vs BTC 0.50× / 0.83× (`exit_rule_backtest.csv`).

## 1. Cultural durability thesis

- **The most culturally "load-bearing" Ethereum PFP after CryptoPunks:**
  - It is the counter-culture/"network spirituality" icon of 2021–26.
  - It survived a founder-scandal crash (−82%, May 2022) and a coup (Sept 2023).
  - IRL raves have run every year since 2021.
  - It was adopted by **Vitalik**: `vitalik.eth` received #9286 on 2025-01-18 and #595 on 2025-04-13 and still holds
    both. We verified this on-chain.
  - The **Ethereum Foundation's 2026 Mandate** used Milady-*inspired* design. This was not an adoption, and it was
    followed by −25% vs BTC at 90 days.
- **The founder-vanishes test: fails on price, passes on culture:**
  - Every positive price event since 2023 was Remilia-manufactured (Bonkler, CULT) or a celebrity gesture (Musk,
    Vitalik ×2).
  - Every major negative non-macro event was a Remilia governance shock: Miya 2022, the Bonkler coup 2023, the
    treasury drain 2024, and the CULT sell-the-news in 2024.
  - The founder (Charlotte Fang) is the brand, and is re-monetising the scandal persona in 2026 (the Miya book).
- **The meme is free to copy** (Viral Public License; PFP-without-owning is encouraged). Cultural reach does not
  require buying the NFT, and fungible proxies (CULT, LADYS) compete for the same speculative capital.

## 2. Historical valuation & catalysts

- **Musk post (2023-05-10).** Spiked intraday (+50–57%) and was −5% in ETH terms at 30 days. The often-quoted "Milady
  meme for everything" wording is not verified; the post said "There is no meme. I love you."
- **CULT airdrop (TGE 2024-12-09 00:04 UTC, on-chain).** The floor peaked at 6.34 ETH just before (NPF; CoinGecko
  intraday 7.35). Afterwards: −49% vs BTC at 30 days, −70% at 90.
  - CULT itself is −98% in USD since launch (on-chain pool prices; FDV ~$11.7M).
  - 53.1B CULT (53%) sits untouched in the token contract. The scheduled holder "Manipulation Rounds" are not
    evidenced.
- **Vitalik's purchase and PFP (2025-01-18).** +49% within a week, ~0 at 30 days, −54% at 90.
- **Vitalik's "Milady is back" (2026-01-01).** +71% from the bar low, fully reversed in 5 weeks.
- **Quiet windows since the CULT TGE** are all strongly negative: −59% ETH (Feb–Sep 2025), −48% (Sep–Dec 2025), −28%
  (Mar–Oct 2026).

## 3. Collector behaviour

- **A retail-heavy book:** 81% of holders own 1 token; top-10 hold 11%; holder count is flat at ~5,100 for a year.
- **Retention:** 53% of supply untouched for 24 months; 58% of holders retained. Churn is 74% of sales. Organic
  turnover is ~5.3/day.
- **Distribution.** Pre-2024 holders net sold 506 in the last year. Wallets new in the last 12 months absorbed 1,587
  (16% of supply; some are re-addressed owners).
- **Lending overhang:** 200 (2.0%; Blend 136, Gondi 63), down from 7.8% at the Feb-2024 peak.
- **Programmatic support:** "MiladyStrategy"-type contracts bought 32 in the last 12 months.

## 4. Liquidity

- Best bid is 92% of floor. A budget-sized position is 3 tokens, and the instant round trip loses ~16%.
- It is divisible, so a holder can scale out across a rally.
- In stress, liquidity breaks: on 2024-03-18 the floor fell 3.69 → 2.04 ETH on 1,139 sales during the treasury drain.

## 5. Failure mechanisms

- A new Remilia/Fang scandal, legal outcome or treasury event. This is a standing tail risk; the 2023 suits remain
  unresolved.
- The CULT overhang (53B contract-held) is reactivated as sell pressure or as another dilutive "round".
- Cultural migration to fungible meme vehicles. Elite adoption has been tradeable but not durable.
- Liquidity decay: 2026 YTD volume is ~3% of 2023's.

## 6. Bull thesis / bear thesis

- **Bull.**
  - The cultural moat is the deepest of any affordable PFP. Ethereum's founder holds two and twice used one as his
    avatar, and EF material borrowed its aesthetic.
  - At 0.744 ETH it is back at its 2022 post-scandal range (−88% from the ETH peak), with the CULT overhang now tiny
    in dollars.
  - Its β to ETH/BTC is the lowest of the finalists (0.76), with high idiosyncratic convexity.
  - It is divisible, and it is the most likely beneficiary of any "Ethereum culture" revival, or of a Vitalik-style
    moment, in 2027–28.
- **Bear.**
  - Its price is a function of Remilia- or celebrity-driven events that fully retrace.
  - Quiet periods bleed.
  - The founder is the brand and the recurring source of shocks.
  - It is −59% vs BTC in a year and −92% from its BTC-terms peak.

## 7. Entry conditions & what would change the view

- **Entry.** Bid at ≤~0.69 ETH (current best bid), or wait until after 2026-11-12. Scale in over weeks rather than
  sweeping the thin ask stack (the 3rd-cheapest listing is already ~20% above floor).
- **Upgrade if:**
  - A catalyst-free window shows stable or rising floors.
  - CULT supply is burned or a credible distribution mechanism appears.
  - Remilia's governance is resolved (the suits settle).
- **Downgrade if:** a new Remilia scandal or legal loss, or reactivation of the CULT contract balance.
