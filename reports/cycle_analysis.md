# Cycle-timing analysis: buy near the NFT cycle low, sell into the euphoria — does it beat BTC?

_Prepared 2026-10-14 in response to the investor's framing. Scripts: `scripts/cycle_2024.py`,
`cycle_tail.py`, `cycle_analysis.py`, `cycle_forward.py`, `cycle_a_sales_sampler.py`, `cycle_a_analysis.py`,
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

## E. Can anything plausibly do 4–10× against BTC? (follow-up, 2026-10-14)

_Script: `scripts/cycle_tail.py`. Outputs: `data/processed/cycle_tail_{counts,profile,buckets,baskets,watchlist}.csv`,
`recent_launches.csv`._

The bar moved from "beat BTC" to "plausibly 4–10× against a BTC 2×". There are two readings:
- **4–10× in USD while BTC does ~2×**, which is roughly 2–5× vs BTC.
- **4–10× relative to BTC**, which is roughly 8–20× in USD.

**Short answer.** Among established ETH NFTs, neither has been a projectable outcome. It has been a tail: about
5–8% of collections per cycle, even with hindsight-generous exit timing. It came from collections no one could have
singled out at the low.

### E1. How often it happened

The table counts collections at each threshold. All tiers except the last use rough timing and deduct 10% costs. The
rough exit is centred on each collection's actual peak, so these counts are upper bounds on what a real seller gets.

| Cycle | n | ≥4× USD | ≥2× vs BTC | **≥4× vs BTC** | ≥10× vs BTC | ≥4× vs BTC, perfect timing |
|---|---|---|---|---|---|---|
| **2024–25** (BTC ~2.1×) | 44 | 2 | 7 | **2**: Moonbirds 6.6×, CryptoDickbutts 4.7× | 0 | 8 |
| 2022–25 (full cycle; BTC ~3.9× to the NFT exits) | 37 | 11 | 3 | **3**: Lil Pudgys 10.9×, Pudgy 6.5×, Milady 4.8× | 1 | 5 |
| 2021 (12 sampled survivors, post-mint lows) | 12 | 9 | 10 | **8** | 4 | 10 |

- **The 2024–25 near-misses gave it all back.** Five collections did 2.0–2.4× vs BTC (3.4–4.0× USD): Cool Cats,
  Sappy Seals, Doodles, Rektguy and Sproto Gremlins. All five now trade at 17–74% of their 2024 lows.
- **2021 is the only regime where ≥4× vs BTC was common.** It was a launch mania, with ETH/BTC going from 0.031 to
  0.080, measured on survivors picked in hindsight. You have ruled it out as an analog.

### E2. What the winners had in common

| Winner | Cycle | Floor cap at the low | Below prior peak at the low | What moved it | Knowable at the low? |
|---|---|---|---|---|---|
| Moonbirds | 2024–25 | $5.0M | −98% | Orange Cap Games bought the IP from Yuga (2025-05-30), then a Jul–Aug 2025 revival; ETH/BTC +67% in the same window | No: came 10 months after the low |
| CryptoDickbutts | 2024–25 | $1.8M | −94% | No dated project catalyst found. Coincided with an unaffiliated DICKBUTT memecoin (Oct-2024) and the 2025 meme and ETH rallies. The community/Weitsman takeover was announced in Nov-2025, after the peak, with no positive reaction | No |
| Pudgy Penguins | 2022–25 | $9.5M | −82% (vs the Aug-2021 sampled peak) | New owner (Netz, Apr-2022), toys (2022–23), PENGU (Dec-2024) | Partly: the owner change came 2½ months before the low |
| Lil Pudgys | 2022–25 | $1.2M | n/a (no 2021 data) | As Pudgy, plus a PENGU allocation | Partly |
| Milady | 2022–25 | $2.75M | −71% (vs the Apr-2022 sampled peak) | Musk meme post (May-2023), LADYS, CULT (Dec-2024) | No |

**Pattern.**
- **All five were PFPs.** All had a floor cap of $10M or less at the low, and all were deeply drawn down.
- **Something new and unpriced moved them:** an owner, a celebrity moment, a token. The move took 10–30 months.
- **Cap mattered.** No collection with a floor cap above $15M at the low reached 4× vs BTC in either cycle (0 of 29).
  The 2022–25 median vs BTC fell with size: 1.24× under $5M; 0.75× at $5–15M; 0.63× at $15–50M; 0.39× above $50M.
- **The profile is common; the catalyst is rare.** In 2024–25, 17 collections were under $5M at the low and 2 did
  ≥4× vs BTC (12%).
- **Today 17 PFPs fit the pre-catalyst profile:** floor cap ≤$10M, ≥85% below their ATH in BTC, and at least one sale
  a day. In cap order: Captainz, Sproto Gremlins, DeGods, Sappy Seals, World of Women, Wassies, Cool Cats, Hashmasks,
  Rektguy, Remilio, Chimpers, mfers, CrypToadz, Doodles, CryptoDickbutts, Clone X, MoonCats
  (`cycle_tail_watchlist.csv`). This is a watchlist for catalysts, not a buy list.

### E3. Diversifying raises the odds of holding a winner, not of the position doing 4×

Equal-weight baskets, testing every combination drawn from the 2024–25 collections under $5M at the low (n=17; rough
timing):

| Picks | P(position ≥2× vs BTC) | **P(position ≥4× vs BTC)** | P(holds at least one ≥4× name) | Median position |
|---|---|---|---|---|
| 1 | 29% | **12%** | 12% | 1.56× |
| 3 | 35% | **2%** | 33% | 1.68× |
| 5 | 45% | **0%** | 52% | 1.88× |

- **2022–25 small caps (n=11)** gave 18% for one pick, 27% for three and 1% for five. That cycle had one 10.9×
  outlier, Lil Pudgys.
- **To get the whole position to 4× you need one concentrated name.** Historically that worked about 1 time in 8 to 1
  in 6. That assumes you already knew to fish in the small-cap pond, and that you sold near the peak.

### E4. Buying after the catalyst: the one version with a defined trigger

- **Moonbirds 2025.** Buying on the first bar after the Orange Cap Games announcement would still have returned 7.1×
  vs BTC (perfect exit; ~5.4× rough, after costs). By then the floor had already jumped 2.5×: entry 0.0176 BTC on
  2025-06-05, exit 0.125 BTC on 2025-08-25. The floor then sat at 0.013–0.018 BTC for six weeks, so the entry was
  available. In ETH terms the move was 4.3×; ETH/BTC rising from 0.024 to 0.040 supplied the rest.
- **Pudgy.** The new owner arrived before the 2022 low.
- **The trigger usually fails.** Moonbirds-OCG is 1 of 5 measurable ownership or operator changes in our event file.
  The other four, with 90-day returns vs the sector:

  | Event | 90-day result vs the sector |
  |---|---|
  | Yuga buys Moonbirds (Feb-2024) | −1%: a spike (floor 1.07 → 1.77 ETH) reversed within three weeks; −46% at 180 days |
  | CryptoDickbutts Series 4 control "twist" (2023) | −44% |
  | Penus DAO/Weitsman takeover (Nov-2025) | −23% |
  | Infinite Node buys the Punks IP (May-2025) | +13% (for V1) |

  The sample is too small to call this an edge.

### E5. New mints: the tail lives here, and so does the wreckage

This covers the fresh launches in our universe since 2023 (two contract migrations excluded). Multiples are in BTC,
against each collection's first-month floor.

| Launch | Peak ÷ first month | Today ÷ first month | Today vs peak | Days to peak |
|---|---|---|---|---|
| Opepen Edition (Jan-2023, free open edition) | 39× | 1.26× | −97% | 147 |
| Sproto Gremlins (May-2023) | 11.5× | 0.44× | −96% | 507 |
| Good Vibes Club (Mar-2025) | 6.1× | 1.33× | −78% | 321 |
| NORMIES (Feb-2026) | 2.4× | 1.26× | −47% | 33 |
| The Captainz (Jan-2023) | 2.1× | 0.002× | −99.9% | 150 |
| Checks VV Originals (Feb-2023) | 1.3× | 0.08× | −94% | 18 |

- **Half peaked at ≥4× vs BTC from their first month. Held to today, none is above 1.33×.** The gain existed only
  for someone who sold into the hype.
- **These six are already the notable survivors.** Across all launches:
  - A Sept-2023 dappGambl study found 69,795 of 73,257 collections (~95%) at zero market cap
    ([The Fader, 2023-09-21](https://thefader.com/2023/09/21/95-percent-of-nfts-worthless-study-finds)).
  - An NFT Evening study classed 96% of 5,000 collections as "dead"
    ([ForkLog, 2024-09-04](https://forklog.com/en/?p=16686)).
- **"Impossible to project" is the right description.** Nothing in this dataset identifies the winning launch in
  advance.

### E6. What this means for the recommendation

1. **A 4–10× vs BTC cannot be underwritten in ETH NFTs.** It has been a ~5–12%-per-name outcome, and only with
   timing generous to the point of hindsight. It cannot be identified at the low. The base answer stays: **stay in
   BTC**.
2. **If you want lottery exposure anyway,** the data supports only this structure:
   - **Size.** An amount you expect to lose.
   - **Entry.** Not at a forecast. Start from the E2 watchlist and wait for a dated trigger: a funded new owner or
     operator, or a credible IP or token deal. Buy within weeks of it.
   - **Concentration.** One name per trigger, since baskets dilute the multiple. Accept roughly a 1-in-5 hit rate.
   - **Exit.** Pre-commit to selling into the euphoria and rotating into BTC; the 2024–25 near-misses show the cost
     of holding.
3. **New mints are a separate game.** Their survivors show the 4–10×, but their base rate is roughly 95% mortality,
   and this data offers no way to pick one. If played, it is a mint-and-sell-into-hype trade, sized as a total loss.
4. **This does not raise the case for the 2024–25 cycle trade in section D.** That trade's realistic outcome is "beat
   BTC" (median 1.3–1.6× vs BTC), not 4×. By your new bar it does not justify the risk, and the "stay in BTC"
   conclusion now applies to it too.

_The 2021 cycle (CryptoPunks on-chain; sampled OpenSea sales, `cycleA_summary.csv`) is kept only as context.
Category-creation multiples are not a usable analog:_
- _CryptoPunks: ~0.3 → ~94 ETH (2019 → Nov-2021), 555× vs BTC (rough)._
- _Chromie Squiggle: ~0.08 → ~10 ETH (Jan → Oct 2021), 110× vs BTC._
- _2021 mints from their post-mint lows: BAYC 77×, Milady 25×, MAYC 6.7×, CryptoDickbutts 6.2×, Cool Cats 4.9×,
  Meebits 4.8× vs BTC._
