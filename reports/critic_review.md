# Independent critic review of `DRAFT_conclusions_for_critic.md`

_Critic workstream, 2026-10-13 (UTC). I followed `sources/RESEARCH_STANDARDS.md`. Every challenge cites a repo path
(file:line), a recomputation or a live source. Scratch code is reproduced in Appendix A; I wrote no other repo files.
Market inputs: BTC $83,350, ETH $2,508.69, ETH/BTC 0.0301 (2026-10-13)._

---

## 1. Verdict on the draft headline: **MODIFY substantially. "No NFT purchase" should be the headline.**

| Headline item (DRAFT line) | Verdict | Reason |
|---|---|---|
| 1. No structural case for ETH NFTs beating BTC (14–16) | **Accept, with wording fixes** | Replicated: 1/2/3-year BTC-relative losses match `historical_analysis.md` §4 within ±1 pp (§3.6). "−90%" is a geometric mean. A buy-and-hold equal-weight basket lost 70% and the median collection lost 89% (challenge 19). |
| 2. Upside real but transient (17–19) | **Accept, with caveats** | Direction is robust. The token-airdrop statistic is 7 independent tokens, not 22 events (challenge 12). "Durable re-ratings" is wrong (challenge 11). |
| 3. Break-evens 16–27% if the investor sells into the rally; S4 +211% to +470% (20–24) | **Reject as stated** | These numbers come from a "capture 75% of the peak" assumption, not from the draft's own exit rules. Under the literal rules (sell 50% at 2× BTC, then the rest at 3× or on a 30% trailing stop), S4 caps at +120% to +143%. The S3 rally never reaches the 2× trigger for Squiggle, Terraforms or Azuki. Break-evens rise to 25–86% against 14% for ETH (challenge 1). |
| 4. Staged position of half to two-thirds, sell-into-strength (25–28) | **Reject** | It cannot be executed for the top-3 picks. One Squiggle (88% of budget), one Pudgy (81%) or one V1 (57%) cannot be bought in tranches or half-sold at 2× (challenge 2). Its premise (item 3) is also overstated. |

**Recommended headline.** "No NFT purchase now.

- If the investor holds the ETH/BTC-recovery view, ETH expresses it with a lower break-even: 14%, against 16–27% for the NFTs on the draft's own optimistic exit assumption and 25–86% under the stated exit rules. ETH also has about a quarter of the weak-scenario loss (−20% vs −59% to −79% vs BTC).
- If the investor does not hold that view, stay in BTC.
- No finalist meets the 'mania exposure *without relying on one*' requirement. Every NFT loses 7–35% vs BTC even in the moderate scenario (S2)."

A single-item NFT may still be bought as an explicitly speculative or collecting decision. It must not be presented as a BTC-beating investment (§4).

---

## 2. Challenges

Severity: **C** = critical (changes the recommendation), **M** = major (changes the ranking or a material number), **m** = minor.

### Critical

**1 (C). The exit rules and the scenario model describe different strategies.**
- *Claim:* S3/S4 "disciplined" outcomes, break-evens of 16–27%, and S4 of "+211% to +470% vs BTC" (DRAFT:20–24). The exit rules are "sell 50% at 2× BTC; remainder on a 30% drawdown from peak, or at 3×" (DRAFT:106–107).
- *Evidence:*
  - The model sets M = 1 + 0.75 × (peak − 1) (`scripts/scenario_params.py:3–4,20–21`). That is a discretionary near-top sale.
  - Gross S3 peaks in BTC terms are p3 × (0.040/0.0301)/e: Squiggle ×1.99, Terraforms ×1.90, Azuki ×1.86. The 2× trigger never fires for these three, so the holder rides the rally back down.
  - For every name, the 3× rule caps the S4 payoff at 2.5 × (1 − h) − 1, i.e. +120% (Squiggle) to +143% (Pudgy), not +211% to +470%.
  - Recomputed break-evens with the literal rules (§3.3): Squiggle 27→46%, Terraforms 22→57%, Azuki 25→86%, Pudgy 16→29%, Milady 19→33%, Remilio 22→39%, CDB 21→34%, V1 17→25%. ETH stays at 14%.
  - Break-even against ETH rather than BTC: V1 31%, Pudgy 38%, Squiggle 94%. Terraforms and Azuki never beat ETH.
- *Required change:* Pick one of two options:
  - (a) restate headline item 3 using the literal rules; or
  - (b) re-specify rules that actually deliver the modelled capture, backtest them, and publish the result.

  Either way, drop "+211% to +470%" unless a rule can deliver it.

**2 (C). The recommended position cannot be executed for the #1–#3 picks.**
- *Claim:* "Half to two-thirds of the allocation… first tranche after 2026-11-12" (DRAFT:26–28). "Pre-commit: sell 50% at 2×" (DRAFT:106).
- *Evidence:* `data/processed/liquidity_position.csv` gives `items_for_budget` = 1 for Squiggle (2.642 ETH, 88%), Pudgy (2.43 ETH, 81%) and V1 (1.70 ETH, 57%).
  - One item cannot be split into tranches or half-sold.
  - Half to two-thirds of 2.99 ETH (1.5–2.0 ETH) fits only one V1.
  - Partial exits are possible only in Milady (3), Terraforms (9), Remilio (20) and CDB (5). `reports/liquidity.md:81–82` already notes this.
- *Required change:* Write an executable plan per collection: item count, the exact sale trigger for a single item, and what the rest of the allocation does.

**3 (C). Squiggle at #1 contradicts the team's own quantitative evidence.**
- *Claim:* Chromie Squiggle is #1 for "best survivability" (DRAFT:31–44).
- *Evidence:*
  - It ranks **last (8/8)** on the draft's own disciplined break-even (27%; `scenario_model.py` output) and 6–8th under every variant I ran (§3.3). Its break-even against ETH is 35%, the worst except Azuki.
  - In my 18-month window backtest (§3.5, 350 start dates, 2022-06 → 2025-04):
    - floor ≥2× BTC at any point in only **11%** of windows, the lowest;
    - hold beat BTC in **2%** and ETH in **2%**;
    - the stated exit rule beat BTC in **11%** (mean 0.43× vs ETH 0.70×).
  - The timing backtest gives a terminal multiple of 0.002–0.045 for trend-following Squiggle against 0.111 for holding (`data/processed/timing_backtest.csv`). With a 25% round trip, trading destroys value.
  - `reports/liquidity.md:76–78` calls Squiggle "a buy-and-hold asset by construction… holding has not beaten BTC". The headline (DRAFT:21) says NFTs work only with sell-into-strength. These two positions are mutually inconsistent.
  - The dossier itself says museum and cultural evidence "has **not** protected the floor in BTC terms" (`dossiers/_research/chromie_squiggle_culture.md:13,134,154`).
- *Required change:* Either:
  - (a) drop Squiggle from #1 in an *investment* ranking; or
  - (b) keep it only as "the most durable *collectible*, expected to under-perform BTC and ETH, bought for ownership rather than return", with one item and no trading plan.

**4 (C). "No purchase / ETH instead" should be the headline, not a footnote.**
- *Claim:* A staged NFT position is "defensible" with conviction (DRAFT:25–28).
- *Evidence:*
  - The team's own numbers:
    - ETH break-even is 14% against 16–27% for the NFTs, or 25–86% under the literal rules.
    - In S1 the NFTs lose −59% to −79% vs BTC; ETH loses −20%.
    - In S2 every NFT loses 7–35% vs BTC; ETH gains 6%.
    - (`data/processed/scenarios.csv`; §3.)
  - I computed expected values under explicit probabilities (§3.4). With a neutral vector (S1 .35 / S2 .35 / S3 .20 / S4 .10) and the literal exit rules, only V1 (+7%), ETH (+8%) and Pudgy (+1%) are ≥0 vs BTC. Squiggle is −14%.
  - The mandate asks for exposure "without relying on" a mania. Only ETH comes close.
- *Required change:* Lead with no purchase. Present ETH as the clean vehicle for the macro view, and any NFT as an explicitly speculative exception.

### Major

**5 (M). Scenario parameters are hand-set, inconsistently anchored and undocumented.**
- *Evidence:*
  - The docstrings say "Every number is explained in reports/scenario_model.md" (`scripts/scenario_params.py:1`, `scenario_model.py:17,34`, `sources/METHODOLOGY.md:18`). **That file does not exist** (`ls reports/`).
  - The stated S4 rule is "a fraction (25–60%) of the 2024–25 cycle ETH-terms peak" (`scenario_params.py:16`). Recomputed against NPF peaks, the fractions are: Squiggle **78%**, V1 **107%**, CDB **115%**, Azuki **13%**, Milady 47%, Pudgy 39%, Remilio 31%, Terraforms 53%.
  - The Squiggle, Terraforms and V1 "2024–25 peaks" are actually Jan-2024 bars (2023–24 cycle).
  - Azuki's S3 peak of 1.4 exceeds its own Aug-2025 multiple of 1.11 (`scenario_params.py:44`).
  - Squiggle's S1 of 0.65 is gentler than its own 3-year ETH trend over 18 months (0.53).
  - Taken together, the art names get a generous S4 under one anchor, and the PFPs under another. The break-even gaps between finalists (16–27%) are of the same size as these anchor choices.
- *Required change:* Write `reports/scenario_model.md`. Apply one documented rule per parameter. Publish the sensitivity table (§3.3). Do not rank on break-even differences smaller than ~10 pp.

**6 (M). S3 combines incompatible inputs.**
- *Evidence:*
  - S3 takes each collection's Aug-2025 ETH-terms rally multiple (`scenario_params.py:15`). That rally came with ETH/BTC moving 0.018 → 0.040 (×2.2; `historical_analysis.md:35`).
  - S3 assumes ETH/BTC 0.030 → 0.040 (×1.33; `scenario_model.py:30`).
  - Weekly β of BTC-terms floors to ETH/BTC is 1.07–1.43 (`rally_analysis.csv`). That implies an ETH-terms elasticity of 0.07–0.43, so part of the Aug-2025 ETH-terms move rode on the larger ETH/BTC move.
- *Required change:* Scale S3 to the scenario's ETH/BTC move, or justify not doing so. This mainly affects the high-β names (Pudgy, Remilio, Azuki).

**7 (M). Hold-through retention, the S3:S4 mix and the S1:S2 weights are not evidence-based.**
- *Evidence:*
  - RET is retention 180 days after the peak (`scenario_params.py:5–8`; `rally_analysis.py` `retain180`). An 18-month horizon can end ~15 months after an early peak, so hold-through outcomes are overstated.
  - The "2:1 observed relative frequency" of S3:S4 (`scenario_model.py:15`) has no supporting data in the repo.
  - S1 and S2 are weighted equally (`scenario_model.py:59–66`). With 60:40, every break-even rises 2–3 pp (ETH 18%, Squiggle 30%, V1 19%; §3.3).
- *Required change:* Document or replace these weights, and show the break-evens under alternatives.

**8 (M). The Azuki calculation uses the wrong basis, and "fails on every criterion" is overstated.**
- *Claim:* Azuki "fails on every criterion"; replace it (DRAFT:88–96).
- *Evidence:*
  - `scenario_params.py:43` says Azuki is "valued from today's bid 0.466 (sell-now alternative); multiples applied to 0.548 ask-equivalent". But `scenario_model.py:42–46` computes returns relative to the 0.548 ask (e = 1).
  - For an incumbent, the alternative is selling at 0.466 × 0.99 = 0.461 ETH. Every hold outcome is therefore understated by 0.548/0.461 = **1.188×**.
  - Corrected (§3.2):

    | Measure | Draft | Corrected |
    |---|---|---|
    | S1 vs BTC | −71% | −65% |
    | S2 vs BTC | −23% | −9% |
    | S3 (disciplined) | +59% | +89% |
    | Disciplined break-even | 25% | **17%** (≈ Pudgy 16%, V1 17%) |
    | Hold-through break-even | unattainable | still unattainable |

  - Selling now means paying a ~15% bid–ask gap (0.466 vs 0.548; `liquidity_orderbook.csv`) during a forced-selling window. Blend holds 182 and BendDAO 158 Azuki (`onchain/lending_escrow_current.csv`), about 70 days of the 30-day organic pace (4.8/day; `onchain_collector_analysis.md:103`).
  - The Azuki dossier says "A $1–1.5k holding is fine to keep" (`dossiers/_research/azuki_culture.md:158`).
  - Founder dependence and the IP strategy bypassing the NFT remain valid negatives (`azuki_culture.md:160,184`).
- *Required change:*
  - Fix the basis.
  - Replace "fails on every criterion" with "founder-dependent; small position; do not hit the bid during the Blend/BendDAO unwind".
  - Decide at portfolio level. If no NFT is bought, list near floor after the overhang clears, or keep it as the existing (already paid-for) mania ticket with a written exit trigger.
  - Treat "−99% from ATH" as irrelevant to the forward decision (ATH anchoring).

**9 (M). Holder metrics for Squiggle are misread as demand.**
- *Claim:* "Stickiest holders (84% untouched 24 months)" and "Most organic new demand (45%… first-time wallets; 20% churn)" (DRAFT:35–36).
- *Evidence:*
  - **The "untouched" figure includes concentrated dormant supply.** It includes one minter entity holding 1,314 tokens (13.1%), 990 of them in the minting wallet since 2020–21 (`onchain_collector_analysis.md:187`), plus Safes at 10.5% (`:90`).
  - **"Most" is a share, not a level.** Squiggle had 402 unique t12m buyers (≈281 new) against Pudgy's 2,177 (≈1,459 new) and Milady's 2,001 (`:98`). Net absorption by new wallets was +540 against +1,643 for Pudgy (`:107`).
  - **Low churn reflects missing dealers.** Of 675 t12m Squiggle sales, 671 were Seaport and 0 were Blur (`onchain/sales_enriched_chromie_squiggle.csv`). With 8.5% seller fees, dealer flipping is uneconomic, so the first-time share is high mechanically.
- *Required change:* Report levels alongside shares. Describe untouched supply as "dormant/illiquid", not "sticky demand".

**10 (M). Supply overhangs are treated inconsistently, and V1 holder metrics cover only half the supply.**
- *Evidence:* Similar-sized overhangs, very different weighting in the draft:

  | Collection | Overhang | Turnover equivalent | Draft treatment |
  |---|---|---|---|
  | Terraforms | 1,193-token latent owner mint (verified on-chain, §6), controlled by a single EOA (`terraforms_culture.md:30`) | ≈1.3 years of organic turnover | Key negative |
  | Squiggle | 1,314-token minter entity | ≈2 years of *all* t12m sales | Footnote |
  | V1 | Four non-wrapper wallets hold **2,790 V1 (27.9%)**, including the 1,084-V1 Safe (`v1punks_culture.md:43–48`) | ≈4 years of V1 organic turnover (1.9/day) | Partial |

  - On-chain V1 metrics (top-10 48%, retention 72%) cover only the 5,125 wrapped tokens (`onchain_collector_analysis.md:23,201–203`).
  - V1's OpenSea vs on-chain 30-day sales (30 vs 117) are unreconciled (`:203`).
- *Required change:* Use one overhang table for all names. Caveat that V1 metrics cover only the wrapped float.

**11 (M). "Durable re-ratings from structural events" is false at today's prices** (`historical_analysis.md:94–100`; cited in DRAFT:49).
- *Evidence:* BTC-terms floor before each event vs now (pre-event bars from `event_study.csv`, ETH/BTC from `prices_daily.csv`):

  | Event | Before | Now | Change |
  |---|---|---|---|
  | Terraforms on-chain libraries | 0.0405 | 0.0090 | −78% |
  | Pudgy Walmart | 0.2525 | 0.0707 | −72% |
  | V1 NODE IP sale | 0.0476 | 0.0477 | flat |
  | V1 PunksMarket | 0.0468 | 0.0477 | +2% |
  | Moonbirds OCG | 0.0077 | 0.0135 | +75% (the only gain) |

  - "NODE: V1 +109% at 90 days" was market beta: abnormal +13%, 180-day +6% (`event_study.csv`, 2025-05-13). Squiggle moved +88% on the same date with abnormal +1%.
  - The largest re-ratings (Moonbirds, Pudgy) were operator-driven. That conflicts with the founder-independence preference: founder-independent names have no catalyst channel, so their upside is pure beta.
- *Required change:* Remove "durable" and state the reversals. Drop "Legitimacy optionality (PunksMarket)" as a strength (DRAFT:49).

**12 (M). The event-study method overstates the evidence.**
- *Evidence:*
  - **Overlapping events.** Token airdrop "n = 22" (`historical_analysis.md:72`) is 7 tokens: CULT contributes 9 events, BIRB 4, ANIME 3, PENGU 3, plus gooch and LADYS.
    - Two CULT rows are placeholder "scheduled Manipulation Rounds" (2025-06-30, 2026-06-30) that the Milady dossier says were **not evidenced** (`milady_culture.md:105,140`).
    - *send/receive* is an art airdrop misfiled as a token.
  - **Clustering.** Four of 7 TGEs fall in Dec 2024–Jan 2025, at the sector top.
  - **TGE-only medians:** −68% BTC at 90 days, abnormal −49% (n = 7). The direction is robust; "destroyed value" (DRAFT:18) is causal language the design cannot support.
  - **Benchmark.** The abnormal-return benchmark includes the same collections: 36–38 names, of which 4 were the token-season movers (`sector_index.py:21–35`).
  - **No dispersion.** No CIs or IQRs are reported. The standard deviation of 90-day abnormal returns ranges 0.15–2.59 by category, so "~0 effect" means "indistinguishable from 0 within roughly ±10–30 pp".
  - **Counts.** The report says 177 events and 38 collections; the files give 173 events with 90-day data and n = 36 at the index start.
- *Required change:* Deduplicate by episode. Report n_independent and the IQR. Remove the placeholder rows and fix the classification.

**13 (M). The rally base rates rest on incentive mechanisms that no longer exist, and on survivors.**
- *Evidence:* The three rallies that set S3/S4 were driven by:
  - 2023: Blur airdrop farming (`historical_analysis.md:33`). Blur is closing (verified, §6).
  - 2024: PENGU/CULT/ANIME TGEs, already spent for Pudgy, Azuki and Milady.
  - 2025: the ETH-treasury bid.

  The universe was selected in 2026 from survivors (`METHODOLOGY.md:31–32`). Trough→peak multiples are perfect-timing upper bounds (`:34–35`).
- *Required change:* State that two of three rally mechanisms are gone, and down-weight S3/S4 accordingly.

**14 (M). The post-Blur liquidity regime is untested.**
- *Evidence:* Share of t12m sales via Blur v2 + Blend `BuyLocked` (`onchain/sales_enriched_*.csv`):
  - Pudgy 58% (4,306 + 875 of 8,884)
  - Azuki 52% (3,025 + 498 of 6,720)
  - V1 30% (424 of 1,424)
  - Squiggle 0%

  The PFP churn, depth and stress statistics come from a two-venue market that ends 2026-11-12.
- *Required change:* Caveat Pudgy's "best exit liquidity". Re-snapshot OpenSea depth after 2026-11-12 before any PFP entry.

**15 (M). Pudgy's #3 ranking conflicts with the mandate.**
- *Claim:* Pudgy is "the tactical, liquid beta vehicle" (DRAFT:57–67).
- *Evidence:*
  - Founder-independence is rated "low to moderate" and dependence "high" (`pudgy_culture.md:173,93`).
  - PENGU insider unlocks run to ~Dec 2028 (`:186`). Abstract shuts 2026-12-15 (verified, §6), and the ETF filing was withdrawn (`:51`).
  - Pudgy's #1 break-even and the only positive exit-rule backtest (§3.5) both come from operator catalysts (Walmart, PENGU, ETF hype) that have since reversed.
  - "Nearly matched BTC since Jul-2022 (0.94×)" is a start-date artefact. Jul-2022 was Pudgy's post-acquisition trough (~1.0–1.25 ETH; `npf_series/pudgy-penguins.csv`), and 0.94 is after an 8% cost.
  - "A whale absorbed 131" is dependence on one bidder, not a strength.
  - One item (81% of budget) cannot be staged.
- *Required change:* Move Pudgy to a labelled "mandate exception — tactical only" bucket outside the ranking.

**16 (M). The entry and exit rules are invented, and the timing backtest is misreported.**
- *Evidence:*
  - **Exit rule backtest.** I backtested the stated exit rule (§3.5) over NPF 3-day BTC-terms floors with S2 exit costs. The rule beat BTC in 11% (Squiggle), 21% (Terraforms), 26% (V1), 31% (Azuki), 45–48% (CDB, Milady, Remilio) and 76% (Pudgy) of 18-month windows. Only the meme/brand PFPs (Pudgy, Milady, Remilio, CDB) beat ETH on average. Squiggle, V1, Terraforms and Azuki did not.
  - **Trend-filter misreport.** The draft says the ETH/BTC trend filter "does not help single collections" (DRAFT:11,103). Yet it *doubled to tripled* the sector outcome (0.083 → 0.17–0.25) and improved Azuki in all three lookbacks (`timing_backtest.csv`).
  - **Entry limits.** The limits (Squiggle ≤2.3 ETH, V1 ≤1.5 ETH) are ≈87% and 88% of the current ask. They are sensible as patience limits but are not derived from evidence.
- *Required change:* Label the rules as heuristics, or replace them with backtested rules. Report the sector-level trend-filter result.

### Minor

**17 (m). The Squiggle 7.5% royalty is modelled correctly, but its status is a venue policy.**
- All 89 OpenSea listings and all 50 offers carry 7.5% to `0xb8e8e5c518a8a2f2a3f29cafc3dd5234e1cb478f` plus 1% to `0x0000a26b00c1f0df003000390027140000faa719` (`data/raw/opensea_book/chromie-squiggle-by-snowfro_*.json`, 22:32Z).
- The 2020 Art Blocks V0 contract has no royalty getter on-chain: `projectIdToSecondaryMarketRoyaltyPercentage(0)` reverted (§6). Enforcement is therefore an OpenSea policy that could change.
- Wrapped-V1 orders carry no fee item (132/132 listings), so "0% fees" is confirmed as of today only.

**18 (m). The Squiggle haircut comes from a single snapshot.**
- t12m Squiggle bid fills cleared at a median 0.91× of the NPF floor (q25 0.85; trait bids inflate this). The 0.78 snapshot may overstate the S2–S4 haircut.
- Without the royalty, Squiggle's break-even would be 21%, so the fee is the largest single driver of its poor score.

**19 (m). The sector number needs precise wording.** The −90% is the geometric mean of relatives (`sector_index.py:38`). Buy-and-hold EW basket: 0.30× (−70%); median 0.11×. Only 3 of 38 beat BTC since Jun-2022: Lil Pudgys 2.40×, Milady 1.81×, Pudgy 1.44× — all founder-driven.

**20 (m). Floors don't reconcile within an hour.**
- OpenSea stats/NPF vs order-book ask: Azuki 0.49 vs 0.548 (+12%), V1 1.585 vs 1.70 (+7%), Pudgy 2.31/2.349 vs 2.43 (`screen_metrics.csv`, `liquidity_orderbook.csv`).
- NPF sales are 22–47% below on-chain counts (`onchain_collector_analysis.md:247`).
- Entry anchors therefore carry ±5–12% uncertainty.

**21 (m). Milady wording.**
- "CULT is spent" (DRAFT:73): 53.1B CULT (53% of supply) still sits in the contract (`milady_culture.md:103`). That is both an overhang and an undelivered distribution.
- "Vitalik and EF adoption": the EF Mandate used a Milady-*inspired design*, and was followed by −25% BTC at 90 days (`event_study.csv`, 2026-03-13).

**22 (m). Costs and risks the team missed.**
- Costs of the funding leg: BTC→ETH conversion spread, gas, and possible capital-gains tax on selling BTC.
- Wallet-security risk for a new NFT signer: zero-price signature-drain pattern observed in these collections (`onchain_collector_analysis.md:80,260`).
- S1 is not a tail: ETH/BTC was 0.018 in Apr-2025, against S1's 0.024.

**23 (m). The 1-year window date is mislabelled.** `historical_analysis.md:118` says it starts 2025-10-06. The figures replicate with a 2025-10-13 base (ETH/BTC 0.0368).

---

## 3. Recomputations

All scenario math was re-implemented independently (Appendix A). Identity: R_btc = (M/e) × (1 − h) × (ETHBTC_s / 0.0301) − 1, with ETH/BTC ratios S1 0.7973, S2 1.0631, S3 1.3289, S4 1.6611.

### 3.1 Hand checks (match `scenarios.csv` to ±0.1 pp)

| Collection | S1 | S2 | S3 (disc.) | S4 (disc.) | down = (S1+S2)/2 | up = (2·S3+S4)/3 | Break-even = −down/(up−down) |
|---|---|---|---|---|---|---|---|
| Squiggle | 0.65 × 0.69 × 0.7973 − 1 = **−64.2%** | 1.0 × 0.81 × 1.0631 − 1 = **−13.9%** | 1.375 × 0.83 × 1.3289 − 1 = **+51.7%** | 2.125 × 0.88 × 1.6611 − 1 = **+210.6%** | −0.3906 | 1.0465 | **27.2%** |
| V1 | 0.60 × 0.86 × 0.7973 − 1 = **−58.9%** | 0.95 × 0.92 × 1.0631 − 1 = **−7.1%** | 1.75 × 0.94 × 1.3289 − 1 = **+118.6%** | 2.2 × 0.96 × 1.6611 − 1 = **+250.8%** | −0.3297 | 1.6268 | **16.9%** |
| Pudgy | 0.45 × 0.91 × 0.7973 − 1 = **−67.3%** | 0.85 × 0.95 × 1.0631 − 1 = **−14.2%** | 1.6 × 0.96 × 1.3289 − 1 = **+104.1%** | 3.25 × 0.97 × 1.6611 − 1 = **+423.7%** | −0.4074 | 2.1064 | **16.2%** |
| ETH | −20.3% | +6.3% | +32.9% | +66.1% | −0.0699 | 0.4396 | **13.7%** |

Squiggle hold-through: S3 = 0.99 × 0.83 × 1.3289 − 1 = +9.2%; S4 = 1.4025 × 0.88 × 1.6611 − 1 = +105%; break-even **48.7%** (draft 49%). Remilio (135%) and Azuki (678%) hold break-evens exceed 100%: the "up" average is negative, so they are **never attainable**. They should be printed as "n/a", not as percentages.

### 3.2 Azuki incumbent correction (basis factor 0.548 / (0.466 × 0.99) = 1.188)

| | S1 | S2 | S3 disc. | S4 disc. | S3 hold | S4 hold | Break-even (disc.) | Break-even (hold) |
|---|---|---|---|---|---|---|---|---|
| Draft | −70.6% | −23.5% | +58.9% | +298.7% | −58.9% | −2.4% | 25% | never |
| Corrected | −65.1% | −9.1% | +88.8% | +373.6% | −51.2% | +15.9% | **17%** | never |
| Corrected, literal exit rule | −65.1% | −9.1% | +63.2% | +140.0% | | | 29% | — |

### 3.3 Sensitivity of break-even weights on S3/S4 (2:1 mix)

| Collection | Draft | Literal rule | Capture 50% | S4 = Aug-25 high | S1 = own 3y trend | S1:S2 = 60:40 | **vs ETH** (draft) | vs ETH (literal) |
|---|---|---|---|---|---|---|---|---|
| Pudgy | 16% | 29% | 21% | 12% | 13% | 18% | 17% | 38% |
| V1 | 17% | **25%** | 21% | 17% | 15% | 19% | 18% | **31%** |
| Milady | 19% | 33% | 25% | 19% | 17% | 21% | 21% | 45% |
| CDB | 21% | 34% | 28% | 23% | 18% | 22% | 23% | 45% |
| Remilio | 22% | 39% | 28% | 21% | 19% | 23% | 24% | 54% |
| Terraforms | 22% | 57% | 28% | 32% | 23% | 24% | 25% | never |
| Azuki (draft basis) | 25% | 86% | 31% | 21% | 27% | 27% | 30% | never |
| Squiggle | **27%** | **46%** | 34% | 30% | 29% | 30% | **35%** | **94%** |
| ETH | 14% | 14% | 14% | 14% | 14% | 18% | — | — |

- **Squiggle never ranks above 6th.**
- Pudgy and V1 are top-2 in every variant.
- V1's rank is partly an artefact of S1/S2 and S3 inputs:
  - with PFP-like S1/S2 (0.45/0.85), V1's break-even is 21%;
  - with that plus an art-like S3 peak of 1.5, it is 25%;

  It stays in the top three either way.

### 3.4 Expected BTC-relative return under explicit weights (S1/S2/S3/S4)

| | Bearish .45/.35/.13/.07 | Neutral .35/.35/.20/.10 | Constructive .25/.35/.27/.13 |
|---|---|---|---|
| ETH | +2% | +8% | +15% |
| V1, draft exit / literal rule | +4% / −9% | +26% / **+7%** | +47% / +23% |
| Pudgy, draft / literal | +8% / −15% | +35% / +1% | +61% / +17% |
| Milady, draft / literal | 0% / −20% | +24% / −4% | +49% / +12% |
| Squiggle, draft / literal | −12% / −24% | +4% / **−14%** | +20% / **−3%** |
| Terraforms, draft / literal | −6% / −29% | +15% / −20% | +36% / −11% |
| Azuki, draft basis: draft / literal | −11% / −38% | +9% / −31% | +29% / −24% |

Under the rules the draft actually proposes, only V1 (+23%) and Pudgy (+17%) beat ETH (+15%), and only under the constructive weights.

### 3.5 Empirical 18-month windows (NPF 3-day BTC-terms floors; starts 2022-06-03 → 2025-04-15, n = 350, overlapping, so ≈3 independent observations; S2 exit costs and entry slippage applied)

| Collection | P(hold > BTC) | P(hold > ETH) | P(max ≥ 2× BTC) | Mean hold | Mean literal rule | P(rule > BTC) |
|---|---|---|---|---|---|---|
| Pudgy | 41% | 54% | 76% | 1.46 | 1.79 | 76% |
| Milady | 31% | 51% | 46% | 1.63 | 1.13 | 47% |
| Remilio | 26% | 41% | 48% | 3.16* | 1.01 | 48% |
| CDB | 30% | 39% | 41% | 0.72 | 0.95 | 45% |
| V1 | 10% | 12% | 24% | 0.49 | 0.74 | 26% |
| Azuki | 1% | 3% | 29% | 0.24 | 0.57 | 31% |
| Terraforms | 12% | 12% | 21% | 0.45 | 0.56 | 21% |
| **Squiggle** | **2%** | **2%** | **11%** | 0.34 | 0.43 | 11% |
| ETH (same windows) | — | — | — | 0.70 | — | — |

\*Remilio's mean is skewed by early NPF bars.

Caveats: the sample is bear-dominated and start-level dependent (Pudgy starts at its 2022 trough, Squiggle at ~5–12 ETH). For the most recent starts (2024-06 and 2024-12), hold multiples were: Squiggle 0.29/0.34, V1 0.59/0.91, Pudgy 0.30/0.23, Milady 0.13/0.15.

### 3.6 BTC-relative history replicated (NPF floor × ETH/BTC; base dates 2025/2024/2023-10-13)

| Collection | 1y | 2y | 3y |
|---|---|---|---|
| Squiggle | −36% | −38% | −86% |
| V1 | −41% | −30% | −74% |
| Pudgy | −73% | −80% | −75% |
| Azuki | −71% | −93% | −94% |
| Terraforms | −12% | −58% | −87% |
| Milady | −59% | −82% | −79% |
| ETH vs BTC | −18% | −23% | −48% |

These match `historical_analysis.md:106–116` to ±1 pp. Every finalist except Terraforms (1y) **also lost to ETH** in every window.

### 3.7 Discrepancies found

| Item | Draft / report says | Files show |
|---|---|---|
| Rule-consistent S4 payoff | +211% to +470% | +120% to +143% |
| Azuki hold vs sell-now | Uses the ask basis | Should use the net bid (+18.8%) |
| S4 anchor rule | 25–60% | 13–115% |
| `reports/scenario_model.md` | Cited 4× | Missing |
| Token-airdrop n | 22 | 7 independent; 2 placeholder rows |
| Event count / index n | 177 / 38 | 173 / 36 at index start |
| Trend filter | "Doesn't help" | Helped the sector 2–3× and Azuki |
| 1y base date | 2025-10-06 | 2025-10-13 |
| V1 30-day sales | OpenSea 30 | 117 on-chain (unreconciled) |

---

## 4. Independent ranking

**Headline: no purchase.** If the investor holds the ETH/BTC-recovery view, ETH is the better instrument. Otherwise, stay in BTC.

If the investor still wants one NFT, explicitly as a speculative or collecting decision:

1. **V1 CryptoPunks (one item, ~1.6–1.7 ETH, ~57% of budget).**
   - *For:* among founder-independent finalists, the best result on every quantitative test I ran (break-even 15–25%; vs ETH 16–31%; recent-window hold 0.59–0.91×). Only Pudgy scores better, and Pudgy fails the mandate. 0% fees; no founder to fail.
   - *Against:* adverse legitimacy (artists disowned it, NODE is silent, DMCA precedent); 27.9% of supply in four dormant wallets, including the 1,084-V1 Safe; 4-year compression of the V1/V2 ratio; one buyer took 12.9% of t12m purchases.
   - *Execution:* bid ≤1.5 ETH. Sell the single item on a 2× BTC move or on a written discretionary trigger.
2. **Chromie Squiggle, as a collectible only.**
   - *For:* the strongest cultural-durability case (locked on-chain script, project #0, institutional gifts).
   - *Against:* expected to under-perform both BTC and ETH (worst break-even; 11% historical chance of a 2× window); 29% instant round trip.
   - *Fit:* buy only if owning the object is itself the goal.
3. **Milady (mandate exception).**
   - *For:* divisible, so the stated exit rule is executable; mid-pack numbers (break-even 19–33%).
   - *Against:* fails founder-independence; 53% of CULT supply undelivered.

**Excluded:**
- Pudgy: mandate (founder dependence) and indivisible.
- Terraforms: EOA-controlled latent mint, bid concentration, 28% round trip; never beats ETH under the literal rules.
- CDB: 41% round trip.
- Remilio: derivative with total founder dependence.

**Azuki (held).** Do not hit the 0.466 bid during the Blend/BendDAO unwind. Either:
- keep it as the already-paid-for PFP-beta ticket, with a written exit at 2× BTC; or
- list near the floor after the post-2026-11-12 overhang clears.

Its corrected disciplined break-even (17%) is no worse than Pudgy's. Hold-through is never attainable.

**Evidence that would change this ranking:**
- ETH/BTC holding above its 30-week average, together with a sustained recovery in sector participation (quarterly volume well above Q3-2026's $67M and rising organic sales).
- OpenSea bid depth after 2026-11-12 at ≥90% of floor for V1 or Squiggle.
- An exit rule that beats ETH out-of-sample.
- For V1: NODE or a museum acknowledging V1, or the 1,084-V1 Safe being burned or donated (a sale or DMCA would be the reverse).
- For Squiggle: a lower or unenforced royalty, or museum *purchases* rather than donations.
- For Pudgy: an independent revenue link from the brand to NFT holders.

---

## 5. Misleading wording (with replacements)

| Location | Current wording | Problem | Suggested wording |
|---|---|---|---|
| DRAFT:21–24 | "S4 disciplined: +211% to +470%" | Not achievable under the stated rules | "+120% to +143% under the stated 2×/3× rules; higher only with discretionary top-selling" |
| DRAFT:31–34 | "Founder-independent… MoMA, LACMA and Toledo holdings" | Art yes, narrative no. MoMA = donated and coordinated with the founder; LACMA #9999 = founder pledge; Toledo ≈2 tokens inferred (`chromie_squiggle_culture.md:88,95,120`) | "Artwork is founder-independent. Institutional holdings are mainly gifts coordinated by the founder and holders." |
| DRAFT:35–36 | "Stickiest holders… most organic new demand" | Dormancy and fee artefact; highest share but lowest level | "Highest share of first-time buyers and least dealer churn, partly because 8.5% fees deter dealers. Lowest absolute buyer count of the large names." |
| DRAFT:46–49 | "Anchored to V2 Punks, the most resilient asset… legitimacy optionality (PunksMarket)" | Punks lost 44% vs BTC over 1y (`universe.csv`). PunksMarket is third-party plumbing, and V1 is back at its pre-event BTC level. | "A levered derivative of V2 Punks; PunksMarket improved tradability but did not change legitimacy." |
| DRAFT:62 | "A whale absorbed 131… Nearly matched BTC since Jul-2022 (0.94×)" | Single-bidder dependence; start-date artefact | "One entity bought 131 in the sell-off (bid concentration). Since its mid-2022 trough Pudgy roughly matched BTC; since the 2024 peak it is −94%." |
| DRAFT:18 | "Token airdrops destroyed value after the TGE" | Causal; 7 independent tokens; clustered at the cycle top | "After 7 TGEs, floors fell a median 68% vs BTC in 90 days (abnormal −49%). TGEs have marked local tops." |
| historical_analysis.md:94 | "The largest durable re-ratings came from structural events" | 4 of 5 are fully reversed | "The largest re-ratings came from structural events; all but Moonbirds have since been fully reversed in BTC terms." |
| DRAFT:14 | "sector lost ~90% vs BTC" | Geometric mean | "The median collection lost 89% vs BTC; an equal-weight buy-and-hold basket lost 70%. Only 3 of 38 beat BTC, all founder-driven." |
| DRAFT:89 | Azuki "fails on every criterion" | Basis error; liquidity is mid-pack | "Fails founder-independence. The scenario case is similar to Pudgy's once valued from the sell-now bid." |
| DRAFT:11, 103 | "Trend filter does not help single collections" | Omits the sector result | "It hurt 4 of 7 collections and helped the sector index 2–3×. Results are dominated by round-trip costs." |
| DRAFT:73 | "CULT is spent" | 53% of supply undistributed | "CULT TGE has passed; 53% of supply is undistributed (overhang)." |
| DRAFT:69 | "Vitalik and EF adoption" | EF used a Milady-inspired design, not adoption | "Vitalik holds two Miladys; the EF Mandate used Milady-inspired design." |

---

## 6. Live and on-chain verification log

| Claim | Result | Source |
|---|---|---|
| Blur frontend closes; Blend stops new loans; borrowers repay or default | **Verified.** Blend stops matching new loans 2026-11-12; borrowers have until then to repay or default; a withdrawal tool follows; contracts stay live. CoinDesk: website closes Nov 12. | The Block, 2026-10-12, https://www.theblock.co/news/ecosystems/2026-10-12-blur-nft-marketplace-shutting-down-frontend-blend-418363 ; CoinDesk, 2026-10-13, https://www.coindesk.com/tech/2026/10/13/once-largest-ethereum-nft-marketplace-blur-is-shutting-down-after-volumes-collapse-99 (both fetched 2026-10-13) |
| MoMA Squiggle donation | **Verified:** 8 Squiggles + 8 Punks **donated, not purchased**, Dec 2025; Squiggles coordinated by 1OF1 with SquiggleDAO. No official MoMA page surfaced in search. | The Block, https://www.theblock.co/post/383446/moma-adds-cryptopunks-and-chromie-squiggles-nfts-to-permanent-collection-following-coordinated-donation |
| Abstract shutdown | **Verified (secondary):** announced 2026-10-06, shutdown 2026-12-15, Igloo losses "tens of millions". | Protos, https://protos.com/pudgy-penguins-parent-firm-shuts-down-its-own-blockchain/ ; BeInCrypto, https://beincrypto.com/abstract-shutdown-pudgy-penguins-nft-floor/ |
| CULT TGE | **Verified:** 2024-12-09 (date per URL; the search snippet's weekday was inconsistent). | The Block, https://www.theblock.co/news/markets/2024-12-09-cult-memecoin-from-milady-nft-creators-goes-live-at-over-600-million-fdv-329935 |
| Squiggle 7.5% royalty | **Verified in the order book:** 89/89 listings and 50/50 offers carry the 7.5% item. No on-chain royalty getter in the V0 contract (call reverted). | `data/raw/opensea_book/chromie-squiggle-by-snowfro_*.json` (22:32:43Z); eth_call below |
| Terraforms 1,193 latent mint | **Verified on-chain:** `totalSupply` = `tokenCounter` = 9,911; `MAX_SUPPLY` 11,104; `SUPPLY` 9,904; `OWNER_ALLOTMENT` 1,200; `owner()` = EOA `0x7a822bce7b9fadd3ed4a533b48eb04eb22696405`. Remaining = 1,193. | eth_call, `0x4e1f41613c9084fdb9e34e11fae9412427480e56` |
| V1 Yuga-linked holdings | **Balances verified; attribution still inference.** Safe `0xa858ddc0445d8131dac4d1de01f834ffcba52ef1` (3-of-9 Safe) holds **1,084 V1** and **414 V2**, plus 1 WPV1. The WPV1 wrapper holds 5,130 V1 against a `totalSupply` of 5,125. NFT Now (secondary) reports Yuga kept 414 Punks; its own 423 − 5 arithmetic does not reconcile. | eth_call `balanceOf` on V1 `0x6ba6…db8d`, V2 `0xb47e…3bbb`, WPV1 `0x282b…8c5d`; https://nftnow.com/newsletter/cryptopunks-ip-20-million-yuga-labs-node-foundation/ |

On-chain method:
- Endpoint: Tenderly public gateway (`https://gateway.tenderly.co/public/mainnet`) via `scripts/common.py` `RPC`.
- Block: 26,186,875. Query time: 2026-10-13T23:32:10Z.
- Calls: single eth_calls (Safe `getThreshold`/`getOwners`; ERC-721/punk `balanceOf`; Terraforms getters).
- Art Blocks V0 `0x059edd72cd353df5106d2b9cc5ab83a52287ac3a`: `projectIdToSecondaryMarketRoyaltyPercentage(0)` reverted; `artblocksPercentage()` = 10.

Not verified: identity of the Safe's signers; current OpenSea royalty policy documentation.

---

## Appendix A. Reproduction code (scratch, not committed)

```python
# Scenario identity, literal exit rule, break-even (critic re-implementation)
E0=0.0301; r={"S1":.024/E0,"S2":.032/E0,"S3":.040/E0,"S4":.050/E0}
def outcomes(p, capture=0.75, rule=False, basis=1.0, s4peak=None, s1=None):
    m1,m2,p3,p4,h1,h2,h3,h4,ret,e = p; p4 = s4peak or p4; m1 = s1 or m1; k = basis/e
    o={"S1":m1*k*(1-h1)*r["S1"]-1,"S2":m2*k*(1-h2)*r["S2"]-1}
    for s,pk,h,hold in (("S3",p3,h3,p3*ret),("S4",p4,h4,p4*ret*.85)):
        if not rule: o[s]=(1+capture*(pk-1))*k*(1-h)*r[s]-1
        else:
            P=pk*k*r[s]                                   # gross BTC-terms peak multiple
            o[s]= hold*k*(1-h)*r[s]-1 if P<2 else ((.5*2+.5*.7*P)*(1-h)-1 if P<3 else 2.5*(1-h)-1)
        o[s+"hold"]=hold*k*(1-h)*r[s]-1
    return o
def be(o, bench=None):
    down=(o["S1"]+o["S2"])/2; up=(2*o["S3"]+o["S4"])/3
    if bench: down-=(bench["S1"]+bench["S2"])/2; up-=(2*bench["S3"]+bench["S4"])/3
    return float("inf") if up<=0 else -down/(up-down)
# PARAMS tuples typed from scripts/scenario_params.py; Azuki basis = 0.548/(0.466*0.99)
```

```python
# 18-month window backtest of the draft exit rule on NPF BTC-terms floors
s = load_series(slug)["floorBtc"]          # scripts/npf_utils.py
for t0 in s.loc["2022-06-01":"2025-04-15"].index:
    rel = s.loc[t0:t0+pd.Timedelta(days=546)]/s.loc[t0]/e     # e = entry slippage
    pos,cash,peak,half=1.0,0.0,0.0,False
    for v in rel:
        peak=max(peak,v)
        if not half and v>=2: cash+=.5*v*(1-h); pos=.5; half=True
        if pos and v>=3: cash+=pos*v*(1-h); pos=0; break
        if pos and half and v<=.7*peak: cash+=pos*v*(1-h); pos=0; break
    rule = cash+pos*rel.iloc[-1]*(1-h); hold = rel.iloc[-1]*(1-h)   # h = S2 haircut
```
