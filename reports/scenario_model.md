# Scenario model (v2, post-critic): BTC-relative outcomes for the finalists

_Code: `scripts/scenario_model.py`. Outputs:_
- _`data/processed/scenario_params_v2.csv` (every derived parameter)_
- _`scenarios.csv` (returns by scenario × exit rule)_
- _`breakeven.csv`_
- _`expected_illustrative.csv`_

_The draft v1 used hand-set parameters (`scripts/*_v1_draft.py`, `data/processed/scenarios_v1_draft.csv`). It was
rejected by the critic: the anchors were inconsistent, the exit assumption didn't match the stated rules, and the
Azuki basis was wrong (`reports/critic_review.md` #1, #5–8)._

## 1. What the model is (and is not)

- It is a **conditional** model: "if the world looks like S, what does each position return vs simply holding
  BTC?" It assigns **no probabilities**.
- For decision support it reports the **break-even weight**: how much weight on the favourable scenarios the investor
  must hold for the expected BTC-relative return to be zero.
- Every parameter comes from **one rule applied to every collection**, computed from data. Differences between
  collections smaller than ~10 percentage points in break-even are **not meaningful** given the parameter
  uncertainty, and are not used for ranking.

## 2. Scenarios (explicit assumptions, not forecasts)

| Scenario | ETH/BTC | BTC (USD) | ETH (USD) | Narrative |
|---|---|---|---|---|
| S1 weak | 0.024 | 70,000 | 1,680 | NFT weakness continues; crypto chop or bear; ETH underperforms BTC. ETH/BTC 0.024 is roughly the historical *median* 18-month outcome (0.79× from today); the Apr-2025 low was 0.018 |
| S2 moderate | 0.032 | 110,000 | 3,520 | Moderate crypto recovery; no project-specific catalysts |
| S3 strong | 0.040 | 135,000 | 5,400 | BTC and ETH revisit or exceed ATHs (the investor's working scenario); an NFT rotation like Aug-2025 |
| S4 mania | 0.050 | 160,000 | 8,000 | Speculative mania with renewed leverage and incentives (tokens, points, airdrops) |

From 2017–2025 start dates, the 18-month forward ETH/BTC ratio had a median of 0.79×, a 75th percentile of 1.27× and
a 90th percentile of 2.49×. Since 2021 the 90th percentile is 1.31×. S3 (1.33×) and S4 (1.66×) are therefore
upper-decile ETH/BTC outcomes by recent history.

## 3. Parameter rules (ETH terms; NFTPriceFloor 3-day floors, cleaned; 2022-06 → 2026-10)

| Parameter | Rule | Rationale |
|---|---|---|
| **S1 end multiple** | Mean of: the sector's 18-month decay (0.55, from the equal-weight index at ~−33%/yr in ETH terms), and the collection's own 1-, 2- and 3-year ETH-terms trends each extrapolated to 18 months and capped at 1.0. Bounded to [0.30, 0.90] | Uses each name's record without letting a trough start-date produce a "weak" scenario that rises |
| **S2 end multiple** | 0.90 for every collection | Outside rallies, sector floors have drifted down in ETH terms since 2023. No basis to differentiate |
| **S3 peak multiple** | The collection's own Aug-2025 rally trough→peak ETH multiple | The most recent rally. It was driven by the ETH-treasury bid, not by tokens or Blur farming, whose mechanisms are gone (critic #13). No ETH/BTC scaling: the ETH-terms elasticity of floors to ETH/BTC is only β−1 ≈ 0.1–0.4 |
| **S4 peak multiple** | The collection's best trough→peak ETH multiple of the 2023, 2024 and 2025 rallies | A mania repeats the best of the last three cycles. Some of those (PENGU, ANIME, CULT, Blur) were incentive-driven, which is what S4 assumes returns |
| **Cap on S3/S4 peaks** | ≤ the collection's own 2024–25 cycle-high floor ÷ current floor | No new highs above the last cycle's peak. This binds for CryptoDickbutts (3.49×) and V1 (2.61×) |
| **Hold-through retention (RET365)** | Own mean floor 365 days after the 2024 and 2025 rally peaks ÷ the peak | An 18-month horizon can end long after the peak. 180-day retention would overstate hold-through (critic #7) |
| **Entry slippage e** | 1 + half of the instant-book average-cost premium over floor for a ~$7.5k position (assumes patient bid-side accumulation) | Multi-item positions cost more than floor × n. **Azuki (held):** e = net sell-now bid ÷ ask = (0.466 × 0.99)/0.548 = 0.842, so hold outcomes are measured against selling today (critic #8) |
| **Exit haircut h** | S1 = instant bid gap for the position + seller fee. S2/S3 = half the gap + fee. S4 = fee + 2% | Fees come from OpenSea consideration items: 1%, except Squiggle at 8.5% (7.5% enforced royalty, a venue policy) and wrapped V1 at 0% |

### Derived parameters

| Collection | S1 | S3 peak | S4 peak | Cap | RET365 | e | h S1 / S2 / S4 |
|---|---|---|---|---|---|---|---|
| Milady | 0.47 | 1.56 | 4.37 | 8.52 | 0.25 | 1.045 | 0.09 / 0.05 / 0.03 |
| Remilio | 0.45 | 1.70 | 6.50 | 15.90 | 0.18 | 1.122 | 0.12 / 0.06 / 0.03 |
| CryptoDickbutts | 0.68 | 3.49 (capped) | 3.49 (capped) | 3.49 | 0.52 | 1.143 | 0.24 / 0.13 / 0.03 |
| Pudgy | 0.45 | 1.82 | 3.34 | 10.74 | 0.22 | 1.000 | 0.08 / 0.04 / 0.03 |
| Azuki (held) | 0.32 | 1.11 | 3.40 | 24.90 | 0.22 | 0.842 | 0.17 / 0.09 / 0.03 |
| Chromie Squiggle | 0.66 | 1.44 | 1.86 | 3.21 | 0.45 | 1.000 | 0.31 / 0.20 / 0.11 |
| Terraforms | 0.67 | 1.49 | 3.46 | 6.67 | 0.33 | 1.048 | 0.21 / 0.11 / 0.03 |
| V1 Punks | 0.70 | 2.11 | 2.61 (capped) | 2.61 | 0.50 | 1.000 | 0.12 / 0.06 / 0.02 |

## 4. Exit rules (all executable with a single item)

| Rule | Definition | Comment |
|---|---|---|
| **HOLD** | Hold to the horizon end | Collector behaviour |
| **A** | Sell everything when the BTC-terms floor reaches 2.0× entry; otherwise hold | Caps upside; never fires in S3 for names whose S3 peak is <2× in BTC terms |
| **B** | Once the BTC-terms floor is ≥1.5× entry, sell on a 30% drawdown from the post-entry peak (no cap) | **Recommended discipline.** Lets manias run and locks in about 70% of the peak. On history it beat HOLD and A for most names (`exit_rule_backtest.csv`) |
| TOP | Discretionary sale capturing 75% of the peak gain | Optimistic bound only; not a rule anyone can commit to (the v1 draft's assumption) |

## 5. Results: return vs BTC over ~18 months

**Rule B (disciplined, executable)**

| Collection | S1 weak | S2 moderate | S3 strong | S4 mania |
|:--|--:|--:|--:|--:|
| **ETH (benchmark)** | **−20%** | **+6%** | **+33%** | **+66%** |
| V1 Punks | −51% | −10% | +84% | +197% |
| Milady | −67% | −13% | +32% | +372% |
| Pudgy | −67% | −8% | +62% | +277% |
| CryptoDickbutts | −64% | −27% | +149% | +245% |
| Remilio | −72% | −20% | +32% | +553% |
| Terraforms | −60% | −19% | +18% | +272% |
| Chromie Squiggle | −64% | −23% | +8% | +93% |
| Azuki (hold vs sell now) | −75% | +3% | +12% | +355% |

**HOLD (no exit discipline)**

| Collection | S1 | S2 | S3 | S4 |
|:--|--:|--:|--:|--:|
| ETH | −20% | +6% | +33% | +66% |
| V1 Punks | −51% | −10% | +31% | +111% |
| CryptoDickbutts | −64% | −27% | +83% | +154% |
| Milady | −67% | −13% | −54% | +65% |
| Pudgy | −67% | −8% | −50% | +16% |
| Terraforms | −60% | −19% | −44% | +76% |
| Chromie Squiggle | −64% | −23% | −31% | +24% |
| Remilio | −72% | −20% | −66% | +67% |
| Azuki | −75% | +3% | −64% | +45% |

**Reading the tables.** Without exit discipline, most NFTs lose to BTC *even in the strong scenario*, because the
rally fades within the horizon. With rule B they beat ETH only in S3/S4, and they lose 3–4× more than ETH in S1.

## 6. Break-even weight on the favourable scenarios

Base mix: S1:S2 = 50:50 and S3:S4 = 2:1. Ranges cover S1-heavy 60:40 and S3-heavy 3:1. "Never" means the
favourable block is itself negative.

| Collection | Rule B | HOLD | Rule A |
|:--|--:|--:|--:|
| **ETH** | **14%** (14–18%) | 14% | 14% |
| Remilio | 18% (18–22%) | never | 34% |
| V1 Punks | 20% (20–22%) | **34%** (34–37%) | 25% |
| CryptoDickbutts | 20% (20–21%) | 30% (30–32%) | 36% |
| Milady | 22% (22–26%) | never | never |
| Pudgy | 22% (22–25%) | never | 29% |
| Azuki (hold vs sell) | 22% (22–27%) | never | never |
| Terraforms | 28% (28–32%) | never | 95% |
| Chromie Squiggle | **55%** (55–60%) | never | 88% |

**Interpretation**
1. **ETH needs the least conviction** to beat BTC, with a quarter to a third of the NFT downside in S1.
2. Among NFTs, rule-B break-evens of 18–22% are indistinguishable from each other, except Terraforms (28%) and Squiggle
   (55%), which are clearly worse.
3. **Only V1 and CryptoDickbutts have attainable hold-through break-evens.** Their S1 losses are smaller, and their
   rallies have retained more.
4. Illustrative expected values (`expected_illustrative.csv`, weights chosen only to show sensitivity):
   - Neutral weights (S1 .35, S2 .35, S3 .20, S4 .10), rule B: V1 +15%, Milady +15%, Pudgy +14%, Azuki +13%,
     CDB +22%, Remilio +29%, Terraforms +3%, Squiggle −20%. ETH is +8%.
   - Under HOLD, every NFT except CDB is negative (V1 −4%).
   - **The rule-B advantage over ETH is concentrated in S4.** The mania branch supplies about 90% of the positive
     expected contribution for Remilio, about 85% for Milady and about 70% for Pudgy. That makes the case only as strong as one's confidence in a mania
     *and* in executing the trailing stop.

## 7. Known weaknesses of the model

- S3 and S4 peaks are perfect-timing trough→peak multiples from rallies that started at troughs. Today's floors are
  near (not at) 2026 lows, so the peaks are upper-end.
- Rule B assumes the stop fills at 70% of the peak. Floors gap; 3-day bars hide intra-bar moves; illiquid names
  (Squiggle, CDB, Terraforms) may not fill near the floor.
- Haircuts come from one OpenSea snapshot (2026-10-13). The post-Blur venue structure from 2026-11-12 is untested,
  and 52–58% of Pudgy and Azuki trailing-year sales were on Blur or Blend.
- Royalties and fees are venue policy and may change. Without its 7.5% royalty Squiggle's break-even would be materially
  lower; the critic estimated 21% vs 27% under the v1 parameters (critic #18).
- The rally base rates come from survivors and from incentive mechanisms that are partly gone.
- Not modelled: BTC→ETH conversion spread, gas, taxes on selling BTC, wallet-security risk.
