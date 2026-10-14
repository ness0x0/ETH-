# Cycle-timing analysis: buy near the NFT cycle low, sell into the euphoria — does it beat BTC?

_Prepared 2026-10-14 in response to the investor's framing. Scripts: `scripts/cycle_analysis.py`,
`cycle_forward.py`, `cycle_a_sales_sampler.py`, `cycle_a_analysis.py`, `punks_onchain_floor.py`, `chart_cycles.py`.
Data: NFTPriceFloor 3-day floors (2022-06 →); OpenSea sampled sales (weekly 48-hour windows, 2020-12 → 2022-06);
CryptoPunks on-chain PunkBought events (2017 →); Binance prices._

## The question, made precise

- **Your hurdle.** BTC goes from $83,350 to its cycle top at $180–210k, i.e. 2.16–2.52×.
- **The NFT trade.** Buy near the NFT cycle low and sell into the next on-chain euphoria. If the NFT is sold and the
  proceeds go back into BTC (or the NFT peak coincides with BTC's), the trade beats BTC exactly when the NFT's
  **multiple measured in BTC** between entry and exit is above 1.
- **Decomposition.** NFT÷BTC = (NFT÷ETH) × (ETH/BTC change). The NFT trade is therefore a bet on two things: the
  NFT's swing measured in ETH, and where ETH/BTC is when the euphoria hits. Your BTC target changes the USD numbers,
  not who wins.

**Timing tiers** used throughout. All non-perfect tiers deduct 10% round-trip costs.

| Tier | Entry | Exit |
|---|---|---|
| Perfect | The exact lowest bar | The exact highest bar |
| **Rough** (your premise) | Average floor ±45 days around the low | Average floor ±15 days around the peak (selling in the euphoric month) |
| Blind | Median floor of the whole low period (no idea where the bottom is) | Same as rough |

## 1. The euphorias and the lows

| Euphoria | Window | ETH/BTC (mean) | BTC (mean) | Preceding NFT low |
|---|---|---|---|---|
| 2021 OG/PFP mania | Aug–Oct 2021 | 0.069 | $49.9k | 2019–early 2021 (OG); post-mint lulls (2021 launches) |
| 2022 blue-chip peak | Jan–Apr 2022 | 0.072 | $41.3k | — (no deep low in between) |
| Blur season | Jan–Mar 2023 | 0.071 | $21.8k | Sep–Dec 2022 |
| ETF season | Feb–Mar 2024 | 0.054 | $59.1k | Aug–Nov 2023 |
| Token season | Nov 2024 – Jan 2025 | 0.036 | $96.9k | Jun–Oct 2024 |
| ETH-ATH season | Jul–Sep 2025 | 0.036 | $115.2k | Mar–Jun 2025 |

`reports/charts/cycles_overview.png` shows the pattern. Since 2022, **every euphoria took the NFT sector back to
roughly the same USD level** (1.55–1.65× its June-2022 value). Meanwhile BTC rose ~7× and each NFT low was lower than
the last. CryptoPunks has traded around $100k in USD since late 2021, while BTC went from $16k to $125k and back to
$83k. NFTs have behaved like a range-bound, decaying oscillator, not a trending asset.

<!-- CYCLE_A -->

## 3. Cycle B (2022 → 2025): the realistic analog

### 3a. Full cycle — cycle low (Jun-2022 → Oct-2023) to the best euphoria (Nov-2023 → Oct-2025)

37 collections with history. BTC rose 3.9× (median) between the same dates.

| Tier | Median NFT gain in USD | Median NFT÷BTC | Share beating BTC | Share beating BTC by ≥1.5× |
|---|---|---|---|---|
| Perfect | 5.39× | 1.38× | 65% | 49% |
| **Rough** | **2.53×** | **0.71×** | **41%** (15 of 37) | 19% |
| Blind | 1.54× | 0.40× | 14% | 8% |

`reports/charts/cycleB_low_to_high_vs_btc.png` ranks every collection.
- **Winners** were culture and brand PFPs that were cheap at the 2022 low: Lil Pudgys 10.9× BTC, Pudgy 6.5×,
  Milady 4.8×, Doodles 2.0×, Wassies 1.8×. Terraforms (1.7×) is the one art name.
- **Losers** were mostly the historical / art blue chips: Chromie Squiggle 0.30×, V1 Punks 0.36×, CryptoPunks 0.38×,
  Fidenza 0.40×, Meebits 0.42×, Autoglyphs 0.74×. BAYC came in at 0.32×.

| Group (Cycle B, rough timing) | n | Median NFT÷ETH | Median NFT÷BTC | Share beating BTC |
|---|---|---|---|---|
| Meme / culture PFPs | 5 | 1.77 | 1.10 | 60% |
| Other PFPs | 5 | 1.51 | 1.15 | 60% |
| Brand PFPs (operator-run) | 10 | 1.28 | 0.93 | 50% |
| Historical / art | 17 | 0.85 | 0.59 | 24% |

### 3b. Each low → the next euphoria (swing trades)

Medians; rough timing, net of 10% costs.

| Episode | BTC over window | ETH/BTC change | NFT gain in USD | NFT÷BTC | Share beating BTC (rough) | Share beating BTC (perfect) |
|---|---|---|---|---|---|---|
| Blur 2023 | 1.35× | 0.96× | 1.16× | 0.93× | 46% | 92% |
| ETF 2024 | 2.25× | 0.94× | 1.74× | 0.97× | 39% | 75% |
| Tokens 2024–25 | 1.74× | 0.86× | 1.86× | 1.20× | 73% | 100% |
| ETH-ATH 2025 | 1.38× | **1.91×** | 2.18× | **1.69×** | **100%** | 100% |

**Takeaway.**
- With rough timing, the swing beat BTC about half the time when ETH/BTC was flat or falling, and every time when ETH
  led (2025).
- Holding from the cycle low to the cycle's best euphoria beat BTC for 41% of collections. It did so only because a
  handful of culture PFPs exploded; the blue-chip art names lost even to ETH.

## 4. Forward view under your assumptions

Assumptions: BTC to $180–210k at the top; NFTs bought near today's level, treated as the low; sold in the euphoric
month; rough timing; survivors only. Cells show the share of Cycle-B observations (cycle low → best euphoria) that
beat BTC, by where ETH/BTC is at the NFT euphoria. `data/processed/cycle_forward.csv`.

| ETH/BTC at the NFT euphoria (ETH price at BTC $200k) | NFT÷ETH needed to beat BTC | All 37 collections | PFPs (20) | Historical / art (17) | All 37, blind entry | Chance of ≥2× BTC (all / PFPs) |
|---|---|---|---|---|---|---|
| 0.025 ($5,000) | >1.20 | 49% | 65% | 29% | 22% | 14% / 25% |
| **0.030 ($6,000; today's level)** | >1.00 | **57%** | **70%** | **41%** | 30% | 22% / 30% |
| 0.035 ($7,000; level at the last two NFT euphorias) | >0.86 | 62% | 75% | 47% | 38% | 32% / 45% |
| 0.040 ($8,000) | >0.75 | 65% | 75% | 53% | 43% | 38% / 55% |
| 0.050 ($10,000) | >0.60 | 86% | 85% | 88% | 59% | 49% / 65% |

Swing-sample equivalents (171 episodes) are similar: 57% beat BTC at 0.030 and 85% at 0.040.

**How to read this**
- If you are right about BTC, ETH holds its own (ETH/BTC ≥ ~0.03 at the next NFT euphoria), and you really buy near
  the low and sell into the euphoria, history gives a **culture/brand PFP roughly a 65–75% chance of beating BTC**, and
  **roughly a 1-in-3 to 1-in-2 chance of doubling BTC's result**.
- An **art/heritage name is roughly a coin flip or worse.**
- **If you are early (not at the low), odds fall to 22–43%.**

## 5. What these numbers do not capture

1. **Is this the low?** No one can know.
   - *Toward a low:* BTC is ~12 months past its Oct-2025 top (the Nov-2022 low came 12 months after the 2021 top).
     The NFT sector index in BTC and ETH terms is at its all-time low. NFT trading volume is at series lows. Blur's
     shutdown looks like venue capitulation. Lending leverage is down 35–47% year on year, and long-time holders have
     been net sellers for a year.
   - *Against:* in Cycle B, NFT lows kept getting lower for a year *after* BTC bottomed. The USD index fell another
     ~30% from Nov-2022 to Oct-2023. In ETH and BTC terms there has never yet been a higher low. The Blend
     repay-or-default deadline (2026-11-12) can still add supply.
2. **Cycles are shrinking.** Cycle A's low→high was 100–500× vs BTC for OG names (category creation). Cycle B's median
   was 0.7× (rough timing). The amplitude of NFT÷ETH swings has fallen each cycle, and euphoria peaks in ETH terms have
   come in lower each time (sector index 1.49 → 0.87 → 0.70 → 0.56).
3. **Leadership rotates.** Cycle A's giants (CryptoPunks, Chromie Squiggle, BAYC) badly lagged BTC in Cycle B; Cycle B's
   winners were 2021 launches that were cheap at the 2022 low. Last cycle's winners (Pudgy, Milady) now carry operator
   and founder risk, and their token catalysts are spent.
4. **Survivorship.** Every percentage above is computed on collections that still trade in 2026. Some of today's names
   will not survive the next cycle.
5. **Exit liquidity.** Euphorias are when bids are deepest, but Blur, the venue that supplied ~half of PFP liquidity,
   closes on 2026-11-12.

## 6. Implications for the recommendation

- **The earlier "no purchase" headline is the unconditional answer.** It weighted the chance that your macro view is
  wrong or NFTs keep bleeding.
- **Conditional on your view** (BTC $180–210k this cycle) **and a cycle-trade discipline** (buy near the low, sell into
  the euphoria), the evidence is more constructive: a better-than-even chance that a liquid culture PFP beats BTC,
  with meaningful odds of doubling BTC's result. That is a defensible speculative bet for a capped sleeve.
- **It changes what to buy.** For a cycle trade, last cycle rewarded beta, not durability. Liquid culture and brand
  PFPs led, and the durable art/heritage names (Squiggle, V1, Punks) lagged even ETH. Within the finalists:
  - **Milady** is divisible, liquid and a culture PFP. Last cycle 4.8× BTC.
  - **Pudgy, or Lil Pudgys for divisibility,** are the most liquid. Last cycle 6.5× / 10.9× BTC, but
    operator-dependent and post-token.
  - **CryptoDickbutts** had big swings (3.4× and 2.8× BTC in the last two euphorias), but is illiquid at size.
  - **V1, Squiggle and Terraforms** are not cycle-trade vehicles on this evidence. Terraforms did beat BTC in Cycle B,
    but its liquidity is thin.
- **It changes how to buy and sell:**
  - *Entry in tranches.* Today's level carries the "not yet the low" risk. Add on evidence of a low: ETH/BTC making a
    higher low, NFT volume rising off series lows, and the post-Blend supply absorbed after 2026-11-12.
  - *Exit into the euphoria, before the top tick.* Use the signs that marked past euphorias: sector volume spikes,
    ETH/BTC breakouts, and token-airdrop announcements. Sell the run-up before any TGE.
