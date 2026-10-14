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

## A. Primary analog: the 2024–25 leg

**Why this cycle.** It is the most recent, and its BTC move matches your hurdle: BTC went from ~$58k at the
Aug–Sep 2024 low ($54k on 2024-09-06) to $124.7k on 2025-10-06, about **2.1×**, against your 2.16–2.52× from here. It
had two NFT euphorias:
- **Dec 2024:** post-election, plus the PENGU/CULT/ANIME token season. ETH ≈ $4.0k, ETH/BTC 0.038.
- **Aug 2025:** ETH all-time high. ETH ≈ $4.8k, ETH/BTC 0.041.

The entry low was in Aug–Oct 2024: ETH ≈ $2.2–2.6k, ETH/BTC 0.044.

`scripts/cycle_2024.py` → `data/processed/cycle2024*.csv`; chart `reports/charts/cycle2024_low_to_high_vs_btc.png`.

### A1. What happened: 44 collections, entry near the 2024 low, exit in the euphoric month (rough timing, −10% costs)

| Exit | Median NFT gain (USD) | BTC from entry to its Oct-2025 top | Beat BTC if proceeds rotate into BTC at the NFT exit | Beat BTC holding cash to BTC's top | NFT gain ≥2.5× (USD) | Median NFT÷ETH |
|---|---|---|---|---|---|---|
| Dec-2024 euphoria only | 1.86× | 2.08× | **73%** | 36% | 25% | 1.45 |
| Best euphoria before BTC's top (Dec-24 or Aug-25) | 2.40× | 2.08× | **75%** | 64% | 45% | 1.70 |

| Sub-group (best exit) | n | Beat BTC (rotate) | Median NFT÷ETH |
|---|---|---|---|
| PFPs | 25 | 76% | 1.90 |
| Art / historical | 19 | 74% | 1.45 |
| Token-airdrop names (Pudgy, Lil Pudgys, Milady, Remilio, Azuki, Doodles) | 6 | 100% (Dec-24 exit) | 1.79 |
| Excluding token names | 38 | 71% | 1.67 |
| Finalists | 8 | 88% | 1.54 |

**Finalists in the 2024–25 leg** (rough timing; "rotate" means NFT÷BTC between entry and exit):

| Collection | 2024 low → peak | NFT gain (USD) | NFT÷BTC (rotate) | vs BTC held to its top | NFT÷ETH |
|---|---|---|---|---|---|
| CryptoDickbutts | Aug-24 → Oct-25 | 8.86× | **4.70×** | 4.24× | 5.94 |
| Azuki (ANIME) | Aug-24 → Jan-25 | 3.03× | 1.88× | 1.45× | 2.53 |
| V1 Punks | Aug-24 → Aug-25 | 2.86× | 1.57× | 1.39× | 1.89 |
| Pudgy (PENGU) | Aug-24 → Dec-24 | 2.14× | 1.31× | 1.03× | 1.67 |
| Milady (CULT) | Oct-24 → Dec-24 | 1.99× | 1.30× | 0.99× | 1.41 |
| Chromie Squiggle | Oct-24 → Aug-25 | 2.34× | 1.30× | 1.17× | 1.39 |
| Remilio (CULT) | Oct-24 → Dec-24 | 1.86× | 1.21× | 0.92× | 1.31 |
| Terraforms | Aug-24 → Dec-24 | 1.54× | 0.96× | 0.74× | 1.22 |

**Reading it**
- In the most recent cycle, buying near the 2024 low and selling into the euphoria **beat BTC for about three
  quarters of collections**. That held even though ETH/BTC *fell* (0.044 → ~0.04), because NFT floors outran ETH by a
  median 1.7×.
- Rotating back into BTC at the NFT exit matters. Most PFPs peaked in Dec 2024, ten months before BTC's top. Sitting
  in cash after that would have lost to BTC for most of them.
- The biggest winners were neglected names that received a new catalyst: Moonbirds (new owner, 6.6×) and
  CryptoDickbutts (DAO/whale takeover, 4.7×). The token-airdrop names won on the run-up but crashed after (see the
  event study).

### A2. Applying the 2024–25 swing to today

Each collection's own 2024–25 NFT÷ETH swing (rough timing) is applied from today's price. Cells show the share of
collections that would beat BTC, by where ETH/BTC is at the next NFT euphoria. `data/processed/cycle2024_forward.csv`.

| ETH/BTC at the next NFT euphoria (ETH at BTC $200k) | Beat BTC: all 44 | PFPs | Art / historical | Finalists | Chance of ≥2× BTC (all / PFPs) |
|---|---|---|---|---|---|
| 0.025 ($5,000) | 77% | 80% | 74% | 8 of 8 | 16% / 28% |
| **0.030 ($6,000; today)** | **84%** | **80%** | **89%** | 8 of 8 | **32% / 40%** |
| 0.035 ($7,000) | 91% | 88% | 95% | 8 of 8 | 50% / 56% |
| 0.040 ($8,000) | 93% | 88% | 100% | 8 of 8 | 55% / 60% |

In USD at BTC $200k and ETH/BTC 0.03, the median 2024-type swing (1.7× vs ETH) is a ~4× NFT against 2.4× for BTC.

### A3. Why these odds are an upper bound

1. **It is one cycle.** The 44 outcomes are cross-sectional results of a single macro episode: post-election
   risk-on, memecoin season, then the ETH-treasury bid. They are not 44 independent trials. The real uncertainty is
   whether the next cycle has a comparable NFT euphoria at all. You rightly call 2021 a special macro environment;
   2024–25 also had special drivers, though milder ones.
2. **Today's starting point is different.** 59% of collections are *below their 2024 low* in USD. PFPs sit at a median
   0.49× of their 2024 low, and the token-airdrop PFPs at 0.23×:
   - Pudgy 0.35×, Milady 0.29×, Azuki 0.15×, Remilio 0.17×.

   Art/historical names are around or above their 2024 lows (median 1.22×):
   - Squiggle 0.93×, V1 1.67×, CryptoDickbutts 3.4×.

   The PFP lows of 2024 were later undercut by 50–85% after their token catalysts were spent. Today is a *lower* low
   for them, which may mean a bigger rebound or continued secular decline.
3. **Token catalysts are spent.** Six of the Dec-2024 winners were airdrop-driven, and post-TGE every one of them fell
   (median −64% vs BTC at 90 days). Excluding them barely changes the odds (71% vs 75%), but the same names won't get
   the same catalyst twice.
4. **Survivorship and timing.** Survivors only, and "rough" timing assumes you buy within ~6 weeks of the low and sell
   within ~2 weeks of the peak. Blind entry (buying anywhere in the low period) gave similar results in this cycle
   (73% rotate), because the 2024 lows were broad and flat.

## B. Context and robustness

### B1. All NFT euphorias since 2021

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



### B2. The full 2022–25 cycle (2022 low → best euphoria): a harder test

#### Cycle low (Jun-2022 → Oct-2023) to the best euphoria (Nov-2023 → Oct-2025)

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

#### Each low → the next euphoria (swing trades)

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

### B3. Forward view using the full 2022–25 cycle (more conservative than A2)

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

## C. What these numbers do not capture

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

## D. Implications for the recommendation

1. **The unconditional answer is unchanged.** If you are unsure about the macro, the weak scenarios dominate and
   "no purchase / ETH instead" stands (`reports/EXECUTIVE_MEMO.md`).
2. **Conditional on your view** (BTC $180–210k this cycle, i.e. a repeat of the ~2.1× 2024→2025 leg) **and a
   cycle-trade discipline** (buy near the low, sell into the euphoria, rotate into BTC), the most recent cycle is
   clearly favourable:
   - In 2024–25, about **3 in 4 collections beat BTC**.
   - Applying each collection's 2024–25 swing from today gives **~77–91%** odds of beating BTC and **~1-in-3 to
     1-in-2** odds of doubling BTC's result, for ETH/BTC between 0.025 and 0.035 at the euphoria.
   - The harder full-cycle test (2022 low → 2023–25 euphorias) gives ~2 in 5.

   This is the strongest case in the package for a capped speculative position.
3. **What decides it is not the collection.** In 2024–25 both PFPs and art beat BTC at similar rates (76% vs 74%).
   Three things decide it:
   - **(a) Being near the low.** Today's PFP floors are 50–85% *below* their 2024 lows; the art names sit near theirs.
   - **(b) Selling into the euphoria and rotating into BTC.** Holding cash after a Dec-2024 exit would have cut the
     win rate from 73% to 36%.
   - **(c) ETH/BTC not collapsing** before the euphoria.
4. **If you run it, prefer names that combine 2024–25 performance, exitability and no spent-catalyst overhang:**

   | Name | 2024–25 vs BTC | Position | Notes |
   |---|---|---|---|
   | **V1 Punks** | 1.57× | One item, ~57% of budget | 0% fees; no team. Legitimacy and concentration risks as in the dossier |
   | **Milady** | 1.30× | 2–3 items | Divisible, liquid, culture beta. Founder risk; 53% of CULT still undistributed |
   | **CryptoDickbutts** | 4.70× | Small, by bids only | Best 2024–25 swing, but it started from a deep 2024 trough and now sits 3.4× above that low. Illiquid at size |
   | Pudgy | 1.31× | One item | Most liquid alternative. Igloo/PENGU operator risk |

   Squiggle (1.30×) works only if you accept its 8.5% sale fees. **Terraforms** (0.96×) was the one finalist that
   lagged even in 2024–25.
5. **Execution:**
   - *Tranches.* The first tranche after the 2026-11-12 Blend deadline. Add more as evidence of a low accumulates:
     ETH/BTC making a higher low; NFT volume rising off its series lows (> $35M/month); the post-Blend supply absorbed.
   - *Exit into the euphoria.* The 2024–25 tells were sector volume spikes, ETH/BTC breakouts and token-airdrop
     announcements; sell before any TGE. Rotate the proceeds into BTC immediately. Most NFT peaks came 2–10 months
     before BTC's.
   - *Size.* Only what you can lose entirely. It is one cycle's evidence, on survivors.

_The 2021 cycle (CryptoPunks on-chain; sampled OpenSea sales) is kept only as context: category-creation multiples
(Punks ~0.3 → ~94 ETH, 2019 → Nov-2021; Squiggle ~0.08 → ~10 ETH, Jan → Oct 2021) are not a usable analog._
