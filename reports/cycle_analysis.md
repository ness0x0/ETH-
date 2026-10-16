# Cycle-timing analysis: buy near the NFT cycle low, sell into the euphoria — does it beat BTC?

_Prepared 2026-10-14 in response to the investor's framing. Scripts: `scripts/cycle_2024.py`,
`cycle_tail.py`, `halving_cycle.py`, `cycle_analysis.py`, `cycle_forward.py`, `cycle_a_sales_sampler.py`, `cycle_a_analysis.py`,
`punks_onchain_floor.py`, `chart_cycles.py`.
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

_This section answers "beat BTC". For the investor's later bar, 4× in dollars while BTC does 2×, see E6: it
changes which names fit._

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

## E. Can anything do 4–10× in dollars while BTC does 2×? (follow-ups, 2026-10-14)

_Script: `scripts/cycle_tail.py`. Outputs: `data/processed/cycle_tail_*.csv` and `recent_launches.csv`._

**The bar, translated.** Assume you rotate the NFT proceeds into BTC when you sell. Then ending with 4× in dollars
while BTC does 2× means the NFT must **double against BTC** between your buy and your sell. 10× in dollars means 5×
against BTC.

_An earlier draft of this section answered a harder reading, 4–10× *against* BTC. Its material is kept in E5 for the
10× end._

**Short answer.**
- **4× in dollars.** In the 2024–25 analog this was common among *small* collections: about half of those under a
  $5M floor cap at the low hit it with a sell order placed in advance, and 8 of 12 small PFPs. Among the larger
  "quality" names it was rare.
- **10× in dollars.** Only 5% of all collections got there (12–17% of small ones). That is a tail, not a plan.

### E1. A sell rule that needs no hindsight

**The rule.**
- **Buy** near the 2024 low.
- **Place a sell listing** at 2.22× the entry price in BTC terms, which is 2× after 10% costs. It fills the first time
  the floor reaches it.
- **When it fills,** rotate the proceeds into BTC.
- **If it never fills,** hold to BTC's top (2025-10-06).

**Entry tiers.**
- *Rough:* the average floor ±45 days around the low.
- *Blind:* the median floor of the whole low period.

**2024–25 analog.** Cells show rough timing, with blind timing in brackets where they differ.

| Sample | n | Hit 2× vs BTC (= 4× $) | Hit 5× vs BTC (= 10× $) | Lost to BTC | Average outcome vs BTC |
|---|---|---|---|---|---|
| All collections | 44 | 32% (36%) | 5% | 45% (43%) | 1.19× (1.24×) |
| PFPs (incl. historical and artist PFPs) | 31 | 42% (48%) | 6% | 35% (32%) | 1.29× (1.37×) |
| **Under $5M floor cap at the low** | 17 | **53%** | 12% | 18% | 1.53× (1.55×) |
| **Small PFPs** | 12 | **67%** (8 of 12) | 17% | 8% | 1.68× (1.69×) |
| $15M or more at the low | 14 | 21% (29%) | 0% | 64% | 0.95× (1.01×) |

- **Would the order have filled?** 13 of the 14 hits held at or above the target for at least two consecutive 3-day
  readings, mostly for 9–33 days. World of Women touched it once. Excluding it, small PFPs drop to 7 of 12.
- **When.**
  - 10 of 14 hits came by 31 Dec 2024, inside two months of the euphoria starting and 3–5 months after the lows.
  - The other four came in Jul–Aug 2025, during ETH's all-time-high run.
- **Token dependence.**
  - Three hits belonged to token-airdrop collections, a catalyst now spent: Azuki, Lil Pudgys and Doodles.
  - None of the small-cap hits did. They were beta to the euphoria.
- **The quality names mostly missed.** Of the eight finalists, only Azuki (2.14×) and CryptoDickbutts reached 2×. The
  rest peaked at:

  | Finalist | Peak vs BTC in 2024–25 |
  |---|---|
  | Pudgy | 1.90× |
  | V1 Punks | 1.90× |
  | Milady | 1.65× |
  | Remilio | 1.62× |
  | Squiggle | 1.54× |
  | Terraforms | 1.14× |

- **If the order never filled,** the median collection ended at 0.76× vs BTC (small caps 1.17×).
- **The ones that hit and weren't sold gave it back.** Cool Cats, Sappy Seals, Doodles and Sproto Gremlins all hit 2×.
  They now trade at 17–49% of their 2024 lows.

**A harsher check: the full 2022–25 cycle.** Low window Jun-2022 → Oct-2023; sell window Nov-2023 → Oct-2025.
Cells show rough / blind.

| Sample | n | Hit 2× | Hit 5× | Lost to BTC |
|---|---|---|---|---|
| All collections | 44 | 25% / 11% | 14% / 5% | 66% / 89% |
| Under $5M at the low | 11 | 36% / 18% | 18% / 9% | 45% / 82% |
| Small PFPs | 8 | 50% / 25% | 25% / 12% | 38% / 75% |

- **Entry timing decided this cycle.** The 2022–23 bottom was a 16-month slide, so buying anywhere but near the end
  lost.
- **What mattered was size at the low, not the name.** Pudgy, Lil Pudgys, Milady and Remilio did it from the 2022 low
  while they were small. By the 2024 low they were $17–150M, and none repeated.

### E2. Applied to today

This applies each collection's 2024–25 swing in ETH terms to an entry at today's ETH/BTC (0.0301), with ETH/BTC at the
level shown when the euphoria hits.

| Probability of hitting 2× vs BTC (= 4× $) | ETH/BTC 0.020 | 0.025 | 0.030 | 0.035 |
|---|---|---|---|---|
| All collections | 16% | 34% | 52% | 64% |
| Under $5M at the low | 24% | 53% | 76% | 82% |

- **5× vs BTC (= 10× $)** comes out at 5% for all collections and 12% for small ones at ETH/BTC 0.025–0.035.
- **These are upper bounds,** for the reasons in A3: one cycle, survivors only, spent tokens.
- **They assume you buy near a fresh low, not today.** 59% of collections are below their 2024 lows, and the next low
  may be lower still.
- **The small-cap result is the most exposed to survivorship.** The universe was chosen in 2026, so small collections
  that died after 2024 are missing from it.

### E3. One name or a basket

This uses the 2× sell rule on the 2024–25 collections under $5M at the low, testing every combination.

| Names held | Position ≥2× vs BTC (= 4× $) | Position ≥1.5× | Position lost to BTC | Median position |
|---|---|---|---|---|
| 1 | 53% | 59% | 18% | 2.0× |
| 3 | 12% | 53% | 7% | 1.52× |
| 5 | 2% | 56% | 1% | 1.54× |

- **A basket trades the 4×-in-dollars outcome for reliability.** It rarely lost to BTC, but it almost never doubled
  vs BTC as a whole, because some names miss.
- **Getting the whole position to 4× in dollars** means holding one or two names and accepting the higher loss rate.

### E4. Today's candidates

These are the PFPs that fit the small-cap profile today (`cycle_tail_watchlist.csv`):
- floor cap of $10M or less;
- at least 85% below their ATH in BTC;
- at least one sale a day.

Prices are as of 2026-10-13. Nine of the 17 hit 2× in 2024–25, but that does not predict a repeat: what mattered was
being small and drawn down at the low.

| Collection | Floor cap | Floor (ETH) | Sales/day (30d) | 2024–25 peak vs BTC (2× hit?) |
|---|---|---|---|---|
| The Captainz | $0.6M | 0.023 | 14.7 | 0.79× (no; $43M at the 2024 low) |
| Sproto Gremlins | $1.2M | 0.141 | 4.2 | 2.60× (yes) |
| DeGods (ETH) | $1.3M | 0.162 | 2.2 | 0.79× (no) |
| Sappy Seals | $1.5M | 0.060 | 16.2 | 2.85× (yes) |
| World of Women | $1.8M | 0.074 | 6.9 | 2.02× (one reading only) |
| Wassies | $2.1M | 0.087 | 1.1 | 1.23× (no) |
| Cool Cats | $2.3M | 0.091 | 10.7 | 3.45× (yes) |
| Hashmasks | $2.6M | 0.064 | 10.2 | 1.66× (no) |
| Rektguy | $2.9M | 0.132 | 11.2 | 2.56× (yes) |
| Redacted Remilio Babies | $3.0M | 0.118 | 13.0 | 1.62× (no; $17M at the 2024 low) |
| Chimpers | $3.2M | 0.319 | 3.0 | 2.42× (yes) |
| mfers | $3.2M | 0.128 | 12.2 | 1.66× (no) |
| CrypToadz | $4.4M | 0.247 | 3.3 | 1.68× (no) |
| Doodles | $5.4M | 0.214 | 15.1 | 2.83× (yes; token) |
| CryptoDickbutts | $6.2M | 0.472 | 1.8 | 6.30× (yes) |
| Clone X | $6.2M | 0.125 | 16.3 | 0.72× (no) |
| MoonCats | $6.5M | 0.124 | 8.4 | 2.29× (yes) |

- **The misses were not far off.** The eight that missed peaked at 0.7–1.7× vs BTC.
- **Size check.** $1,500 buys 1–26 floor items in these collections. In the names with 10 or more sales a day other
  than Captainz, that is under a day's volume.

### E5. The 10× end (5× vs BTC) is a tail

Peak-centred rough timing (section A's method) gives the same picture as the sell rule.

| Cycle | n | ≥4× vs BTC | ≥10× vs BTC |
|---|---|---|---|
| 2024–25 | 44 | 2: Moonbirds 6.6×, CryptoDickbutts 4.7× | 0 |
| 2022–25 | 37 | 3: Lil Pudgys 10.9×, Pudgy 6.5×, Milady 4.8× | 1 |
| 2021 (12 sampled survivors, post-mint lows; the launch mania you ruled out) | 12 | 8 | 4 |

**What the big winners had in common:**
- PFPs with a floor cap of $10M or less at the low, 70–98% below their prior peak.
- Each was moved, 10–30 months later, by something new and unpriced:

  | Winner | What moved it |
  |---|---|
  | Moonbirds | New owner (Orange Cap Games, 2025-05-30) |
  | Milady | Musk meme post (May-2023), then the LADYS and CULT tokens |
  | Pudgy | New owner (Netz, Apr-2022), toys, then the PENGU token |
  | CryptoDickbutts | No dated catalyst; the holder takeover came after its peak, in Nov-2025 |

- **No collection above a $15M cap at the low did it** (0 of 29).

**Buying after a catalyst.**
- *The case that worked:* buying Moonbirds on the first reading after the Orange Cap Games announcement still
  returned 7.1× vs BTC (~5.4× with rough timing after costs). In ETH terms that was 4.3×; ETH/BTC rising from 0.024
  to 0.040 did the rest.
- *The usual outcome:* that was 1 of 5 measurable ownership changes. The other four, vs the sector at 90 days:

  | Event | 90 days vs the sector |
  |---|---|
  | Yuga buys Moonbirds (Feb-2024) | −1% (the spike reversed within three weeks); −46% at 180 days |
  | CryptoDickbutts Series 4 "control twist" | −44% |
  | CryptoDickbutts Penus DAO/Weitsman takeover | −23% |
  | Infinite Node buys the Punks IP (V1s) | +13% |

**New mints.** Of six notable launches since 2023, three peaked at ≥4× vs BTC from their first month: Opepen 39×,
Sproto 11.5×, Good Vibes Club 6.1×.
- Held to today, none is above 1.33×. Captainz is at 0.002× and Checks VV at 0.08×.
- Across all launches about 95% die:
  - A Sept-2023 dappGambl study found 69,795 of 73,257 collections at zero market cap
    ([The Fader](https://thefader.com/2023/09/21/95-percent-of-nfts-worthless-study-finds)).
  - An NFT Evening study classed 96% of 5,000 collections as "dead"
    ([ForkLog, 2024-09-04](https://forklog.com/en/?p=16686)).
- This data cannot pick the winner in advance (`recent_launches.csv`).

### E6. What this means for the recommendation

1. **On your bar, the cycle trade is plausible, but only in small, high-beta PFPs.**
   - In the 2024–25 analog, half to two-thirds of small names hit 4× in dollars with a sell order set in advance.
   - In the harsher 2022–25 test, a quarter to half did, and most lost to BTC when the entry was mistimed.
   - The evidence base is about a dozen small PFPs over one or two cycles.
2. **This changes the shortlist for this objective.** The earlier finalists (V1, Milady, Pudgy, Squiggle) peaked at
   1.5–1.9× vs BTC in 2024–25. That is good enough to beat BTC, not to reach 4× in dollars. The candidates are the
   E4 list.
3. **How to run it, if you do:**
   - **Entry gate, unchanged.** Not before 2026-11-12. Then wait for evidence of a low: ETH/BTC making a higher low
     and NFT volume rising off its lows. Entry timing decided the 2022–25 result.
   - **Size.** Only what you can lose. Hold 1–2 names for a real shot at 4× in dollars on the whole position, or 3–5
     for a likely ~1.5× vs BTC with a low chance of losing to BTC.
   - **Exit, set on day one.** List each name for sale at 2.2× its entry in BTC terms, repricing the ETH listing as
     ETH/BTC moves. Optionally put half at ~5.5× for the 10× tail. Rotate fills into BTC.
   - **Don't hold past the euphoria.** It came 3–5 months after the 2024 lows, and the names that weren't sold gave
     it back.
4. **10× in dollars is a tail (5–17%).** New mints are an unprojectable gamble.
5. **Not a buy today.** "No purchase before the entry gates" still holds. Once they are met, and with your BTC view, a
   small-cap sleeve with pre-set sells is the one version of this trade that has historically reached your bar.

### E7. Buy at the low and hold? (the original "hold to 2028–29" idea)

This uses rough entry near each low and deducts 10% costs (`cycle_tail_hold.csv`).

| Bought near the… | Beat BTC, held to BTC's top (Oct-2025) | Median vs BTC at the top | ≥2× vs BTC at the top | Beat BTC, held to today | Median vs BTC today |
|---|---|---|---|---|---|
| 2024 low | 41% | 0.82× | 9% | 5% | 0.36× |
| Aug–Nov 2023 low | 18% | 0.37× | 0% | **0%** | 0.14× |
| 2022–23 low | 23% | 0.38× | 7% | 2% | 0.18× |

**Buying the low did not rescue a hold.**
- Even held only to BTC's top, most collections lost to BTC.
- Bought at the Oct-2023 low and held three years, none of 44 did.
- The cycle trade works only because of the sell (E1). For legacy collections, buy-and-hold to 2028–29 is the idea
  the data argues against most clearly.

## F. Halving-cycle hold: buy in the bear, sell into the halving and post-halving euphoria (follow-up, 2026-10-14)

_Script: `scripts/halving_cycle.py`. Outputs: `data/processed/halving_cycle.csv`, `halving_cycle_summary.csv`,
`halving_cycle_forward.csv`._

**The strategy.**
- Buy about 18 months before the halving, which is where we are now (the next halving is expected in Apr-2028).
- Hold through the quiet stretch.
- Sell into the on-chain euphorias of the halving and post-halving years, and rotate the proceeds into BTC.

**The phase-matched test.** Buy in **Oct-2022**, 18 months before the Apr-2024 halving. Sell into the three euphorias
that followed:
- Feb–Mar 2024 (ETF);
- Nov 2024 – Jan 2025 (tokens);
- Jul–Sep 2025 (ETH all-time high).

Each sale uses the window's average floor, i.e. scaling out without knowing the peak day. "Ladder" means selling a
third in each window. Costs are 10%.

### F1. Results (39 collections with history, vs BTC)

| Bought Oct-2022, sold… | Beat BTC | ≥2× vs BTC (= 4× $ at BTC 2×) | Median vs BTC |
|---|---|---|---|
| All in the Feb–Mar 2024 euphoria | 15% | 10% | 0.36× |
| **Ladder (a third in each euphoria)** | **10%** | 10% | 0.26× |
| Best window (hindsight) | 15% | 10% | 0.39× |
| Pre-set 2× target, else in Jul–Sep 2025 | 13% | 13% | 0.18× |

| Ladder, by size at entry | n | Beat BTC | Median | **Equal-weight basket** |
|---|---|---|---|---|
| All | 39 | 4 (10%) | 0.26× | 0.81× |
| Under $10M floor cap | 13 | 3 (23%): Remilio 9.7×, Milady 5.0×, Lil Pudgys 4.7× | 0.54× | **1.82×** |
| $10M or more | 25 | 1 (4%): Pudgy 2.7× | 0.19× | 0.31× |
| Art / historical | 11 | 0 | 0.30× | — |

**The shape is binary.**
- **Small caps.** The three that won returned 4.7–9.7× vs BTC; the other ten lost 18–89%. The equal-weight basket
  still finished at 1.8× vs BTC.
- **Large and legacy names.** These lost: CryptoPunks 0.38×, Squiggle 0.25×, BAYC 0.11×, Azuki 0.26×.
- **Catching the actual low helped.** Buying at each collection's own 2022–23 low gave a ladder that beat BTC 21% of
  the time, with a 1.19× basket. That takes timing skill.

### F2. Why holding from 18 months out was hard

There were two headwinds during the 16–35-month hold:
- **ETH/BTC halved,** from 0.070 in Oct-2022 to 0.054, 0.036 and 0.034 at the three euphorias.
- **The median collection also lost 53–64% against ETH.**

**Oct-2022 was not the NFT low.** After an Oct-2022 entry, the median collection fell to 0.14× its entry in BTC terms
before recovering, bottoming around Aug-2024. The lows that worked came 6 months before the halving (Oct-2023) and 4
months after it (Aug-2024).

### F3. Applied to today

This applies each collection's NFT÷ETH path from the Oct-2022 entry to today's ETH/BTC of 0.0301, with ETH/BTC at the
level shown during the euphorias.

| ETH/BTC at the euphorias | 0.025 | 0.030 | 0.035 |
|---|---|---|---|
| All: beat BTC / basket | 13% / 1.12× | 15% / 1.35× | 21% / 1.57× |
| Under $10M: beat BTC / basket | 31% / 2.54× | 38% / 3.05× | 54% / 3.55× |
| ≥2× vs BTC (all / under $10M) | 10% / 23% | 10% / 23% | 10% / 23% |

These numbers improve on F1 only because they assume ETH/BTC does not halve again.

### F4. Read with care

- **One project carried the small-cap basket.** Remilia's two collections, Milady and Remilio, did 5.0× and 9.7×.
  Without them, the other 11 small caps averaged 0.82× vs BTC.
- **Survivorship is worst here.** The universe was picked in 2026, so collections that were small in 2022 and later
  died are missing. Each missing dead name pulls the basket toward zero.
- **This is one cycle with broad data.** The 2018–21 cycle is where this strategy produced the outliers people
  remember. CryptoPunks bought in Nov-2018 (~0.13 ETH, 18 months before the May-2020 halving) and sold into the 2021
  euphoria returned ~600× in ETH and ~1,200× vs BTC. That was a brand-new category on a tiny base, with ETH/BTC
  tripling.
- **Today's market is much quieter than at the analog entry:** universe volume was $67M in Q3-2026, against $857M in
  Q4-2022. It may be nearer a low, or further into decline.

### F5. What this means

1. **A single legacy or large name, bought now and sold in 2028–29, is not supported.** Only 1 of 25 beat BTC, and the
   equal-weight basket finished at 0.31×.
2. **One version has a positive record:** a venture-style basket.
   - **Composition:** many tiny culture PFPs, equal weight, each sized to zero.
   - **Exit:** sell in thirds into the halving and post-halving euphorias, rotating into BTC.
   - **Record:** about 1.8× vs BTC last cycle, or 2.5–3.5× applied to today if ETH/BTC holds at 0.025–0.035.
   - **Expect:** three in four names to lose, and the result to hinge on one or two.
   - **Fragility:** it rests on one project's run and on data that leaves out the dead.
3. **Timing:** buying 18 months early cost a further ~86% median drawdown before the euphoria. Staggering purchases
   through 2027 into mid-2028 would follow the last cycle's pattern of lows (6 months before and 4 months after the
   halving). That is one cycle's evidence.

## G. Midterm years (follow-up, 2026-10-16; `scripts/midterm_check.py`)

**In the two US-midterm years with data, on-chain euphoria appeared only as a carryover from the prior year's mania,
early in the year.**
- **2018:** BTC −50% in Q1 and −44% in Q4. The low was $3,212 on 2018-12-15.
- **2022:** 9 of the 13 sampled 2021-era collections peaked Jan–Apr 2022 (BAYC last, on Apr-23). BTC then fell 56% in
  Q2. The low was $15,781 on 2022-11-21.
- **Neither year started a fresh euphoria.**

**Heat returned the following year.**
- **2019:** BTC +164% in Q2, with no alt season.
- **2023:** BTC +72% in Q1. ETH-NFT universe volume went from $0.86B in Q4-2022 to $2.29B in Q1-2023 (Blur airdrop
  farming, partly wash). Memecoins/BRC-20 followed in the spring and the Ordinals boom late in the year.

**2026 so far fits the pattern.**
- BTC −22% in Q1, −14% in Q2, and a low of $58,625 on 2026-06-30, then +43% in Q3.
- NFT universe volume fell every quarter: $111M → $86M → $67M. On-chain activity did not follow the bounce.

**Limits.** This is two cycles, and 2014 predates the data. Earlier midterm-year lows came in Q4. On Ethereum, NFT
lows kept coming after BTC's low, in Oct-2023 and Aug-2024.

_The 2021 cycle (CryptoPunks on-chain; sampled OpenSea sales, `cycleA_summary.csv`) is kept only as context.
Category-creation multiples are not a usable analog:_
- _CryptoPunks: ~0.3 → ~94 ETH (2019 → Nov-2021), 555× vs BTC (rough)._
- _Chromie Squiggle: ~0.08 → ~10 ETH (Jan → Oct 2021), 110× vs BTC._
- _2021 mints from their post-mint lows: BAYC 77×, Milady 25×, MAYC 6.7×, CryptoDickbutts 6.2×, Cool Cats 4.9×,
  Meebits 4.8× vs BTC._
