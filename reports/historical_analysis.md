# Historical analysis: base rates, rally anatomy, catalyst event study

_Data as of 2026-10-13. Sources: NFTPriceFloor 3-day floor bars (secondary; see `sources/METHODOLOGY.md` for
caveats), Binance ETHBTC/BTCUSDT daily closes, catalyst dates from `data/processed/catalysts/*.csv` (each row
cited). Scripts: `sector_index.py`, `sector_activity.py`, `rally_analysis.py`, `event_study.py`._

## 1. Base rate: ETH NFTs vs BTC since mid-2022

Equal-weight floor index of the 38 universe collections with history from 2022-06-01
(`reports/charts/sector_index_btc.png`):

| Date | EW floor (ETH terms) | EW floor (BTC terms) | ETH/BTC (rebased) |
|---|---|---|---|
| 2022-06-01 | 1.00 | 1.00 | 1.00 |
| 2023-05-31 | 0.78 | 0.88 | 1.13 |
| 2024-05-29 | 0.39 | 0.35 | 0.91 |
| 2025-05-28 | 0.40 | 0.16 | 0.41 |
| 2026-10-07 | 0.20 | 0.10 | 0.51 |

- The index is a geometric mean of floor relatives. **Measured as a portfolio:**
  - An equal-weight buy-and-hold basket of the same 38 collections fell to **0.25×** in BTC terms (−75%) from the
    first bar after 2022-06-01.
  - The **median collection fell to 0.11× (−89%)**.
  - Only **3 of 38 beat BTC**, and all three are founder- or company-driven: Lil Pudgys 1.74×, Pudgy 1.19×,
    Milady 1.07×. These multiples are sensitive to the start bar.
- In BTC terms, the index lost value in **every calendar year**: 2023 −62%, 2024 −40%, 2025 −62%, 2026 YTD −17%.
- About half of the BTC-terms loss is ETH/BTC (−49%). The rest is NFT floors falling in ETH terms (−80%).
- **Survivorship bias makes this a flattering number.** Collections that died before 2026 are excluded.
- **Participation has collapsed.** Universe-wide traded volume was $67M in Q3 2026, against $2.29B in Q1 2023
  (wash-inflated) and $1.83B in Q1 2024. Sales count was about 30k in Q3 2026, against 360k in Q1 2023
  (`reports/charts/sector_activity.png`).

**Implication.** There is no structural tailwind. Owning a basket of "established" ETH NFTs has been a reliable way
to lose against BTC. Any recommendation has to rest on a specific mispricing or a cyclical trade, not on owning the
sector.

## 2. Rally anatomy: the upside is real but transient

Three sector rallies stand out: Jan–Mar 2023 (Blur airdrop farming plus a generative-art bid), Nov 2024–Jan 2025
(the post-election run and the PENGU/CULT/ANIME token season) and Jul–Sep 2025 (the ETH-treasury run, with ETH/BTC
going from 0.018 to 0.040). Trough-to-peak multiples are best case by construction.

| Median across universe | 2023 | 2024 | 2025 |
|---|---|---|---|
| Trough→peak, BTC terms | 1.60× | 2.29× | 2.85× |
| Floor 90d after peak ÷ peak | — | 0.34 | 0.40 |
| Floor 180d after peak ÷ peak | 0.37 | 0.39 | 0.33 |

Finalists:

| Collection | 2023 ×BTC | 2024 ×BTC | 2024 retained 180d | 2025 ×BTC | 2025 retained 90d | 2025 retained 180d | β to ETH/BTC | Ann. vol (BTC) |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Milady | 4.15 | 2.40 | 0.23 | 2.32 | 0.34 | 0.30 | 0.76 | 137% |
| Remilio | 6.37 | 2.35 | 0.16 | 2.50 | 0.27 | 0.22 | 1.35 | 200% |
| CryptoDickbutts | 1.73 | 6.39 | 0.86 | 7.90 | 0.42 | 0.33 | 0.87 | 138% |
| Pudgy Penguins | 3.02 | 2.97 | 0.23 | 3.30 | 0.33 | 0.22 | 1.43 | 117% |
| Azuki | 1.61 | 2.74 | 0.10 | 1.86 | 0.33 | 0.26 | 1.20 | 122% |
| Chromie Squiggle | 1.62 | 2.04 | 0.49 | 2.93 | 0.36 | 0.35 | 1.07 | 85% |
| Terraforms | 3.58 | 1.95 | 0.37 | 2.61 | 0.32 | 0.28 | 1.11 | 116% |
| V1 Punks | 1.56 | 3.16 | 0.42 | 4.44 | 0.32 | 0.28 | 1.16 | 105% |
| CryptoPunks (ref) | 1.19 | 1.94 | 0.64 | 2.71 | 0.54 | 0.42 | 0.88 | 62% |

**Implications.**
1. Positive convexity exists. A 2–8× BTC-terms move inside a few months has happened in each recent cycle for every
   finalist.
2. Roughly 60–80% of the peak is given back within 3–6 months. **A holder who doesn't sell into the rally keeps
   almost none of it.** The opportunity is a trade with exit discipline, not a buy-and-hold collectible thesis.
3. Floors in BTC terms carry ~1× beta to ETH/BTC, with low correlation (ρ≈0.2–0.5) and 85–200% annualised
   volatility. **Buying ETH NFTs is first a leveraged, noisy bet on ETH/BTC.**

## 3. Catalyst event study (251 dated rows, 9 collections; 151 independent events with 90-day data)

**Method**
- Floor change after each event vs the last bar before it, in BTC terms.
- "Abnormal" means relative to the sector index. The index includes the same collections, so abnormal returns are
  understated for big movers.
- "Max up within 90d" is the best exit available to a perfectly timed seller.
- **Revised after critic review (challenge 12):**
  - 11 placeholder rows are excluded. These are scheduled or unverified events, e.g. CULT "Manipulation Rounds" that
    were never evidenced.
  - Events are de-duplicated: within a collection × category, an event is kept only if it falls ≥45 days after the
    previous kept one.
  - IQRs are reported.
  - *send/receive* is reclassified as an art airdrop.
  - Cross-collection clustering remains. Three of the six token TGEs (PENGU, CULT, ANIME) fell in Dec 2024 – Jan 2025 — see note below.

| Category | n (independent) | 30d | 90d | 90d IQR | 180d | Abnormal 90d | Max up within 90d |
|---|---|---|---|---|---|---|---|
| **Token airdrop / TGE** | 13 | **−22%** | **−53%** | −58% … −41% | **−59%** | **−27%** | +13% |
| Celebrity / influencer | 9 | −1% | −7% | −24% … +15% | −37% | +9% | +42% |
| Companion collection | 9 | +4% | −8% | −42% … 0% | −34% | −9% | +45% |
| Controversy | 6 | −11% | −18% | −30% … +9% | −18% | −14% | +12% |
| Partnership / product | 28 | +5% | −7% | −30% … +21% | −20% | +1% | +21% |
| Founder announcement | 18 | +3% | −8% | −41% … +15% | −3% | +1% | +29% |
| Cultural moment (museum, auction, exhibition) | 19 | +4% | −14% | −26% … −3% | −19% | −1% | +19% |
| Market / macro | 20 | +8% | −34% | −49% … +17% | −49% | −6% | +41% |

(Medians. `data/processed/event_study_summary.csv`, `event_study.csv`.)

- **One row per token TGE (6 tokens: PENGU, CULT, ANIME, BIRB, $gooch, LADYS):** median **−64% vs BTC at 90 days,
  abnormal −47%**.
- These TGEs cluster near local market tops, so this is an association: **TGEs have marked local tops**. The design
  cannot prove that the token caused the decline.
- Category IQRs of ±20–30 pp mean "~0 abnormal effect" should be read as "indistinguishable from zero".

**Findings**
- **After token TGEs, floors fell.** Pudgy (PENGU): −79% BTC in 90 days. Azuki (ANIME): −85%. Milady (CULT): −68%.
  Moonbirds (BIRB): −60%.
  - The profitable window was the run-up *before* the TGE (Pudgy +84% into it).
  - Pudgy, Azuki and Milady have had their airdrops. Milady's CULT still has 53% of supply undistributed in the
    contract, which is an overhang rather than a spent catalyst.
- **Brand execution does not reach the floor.** Pudgy's retail run from 2025–26 (Target, Walgreens, Sphere, Pengu
  Card) and Azuki's TCG, manga and anime show ~0 abnormal return. Value accrues to company equity and tokens.
- **Museum validation does not reach the floor either.** MoMA (2025-12-21): Squiggle +18% at 30 days, −5% at 90.
  LACMA: −36% BTC at 90 days. Toledo: +114% at 30 days, then reversed alongside the macro move.
- **Celebrity moments are tradeable spikes, not re-ratings.** Musk (2023-05-10), Vitalik's purchase (2025-01-18)
  and Vitalik's "Milady is back" (2026-01-01) each produced a 1–3 week spike that fully reversed.
- **The largest re-ratings came from structural events, but all except Moonbirds have since been fully reversed in BTC
  terms** (critic challenge 11):
  - Moonbirds' sale to Orange Cap Games (2025-05-30): +1,412% (≈15×) in 90 days, mostly given back by 2026.
  - Terraforms putting its JS libraries on-chain (2022-09-15): +243% at 90 days.
  - The NODE Punks-IP transfer (2025-05-13): V1 +109% at 90 days, but that was mostly market beta (abnormal +13%).
    V1 is back at its pre-event BTC level.
  - PunksMarket enabling native V1 trading (2026-05-18): +34% at 90 days, then back to the pre-event BTC level.
  - Pudgy's Walmart and Pudgy World news in late 2023: +109% and +66% at 90 days. Those were early-stage brand
    milestones, not repeated since. Pudgy's BTC-terms floor is now 72% below its pre-Walmart level.
  - Terraforms is 78% below its pre-event BTC level.
- **Founder-independent names have no catalyst channel.** The largest re-ratings were operator-driven (Moonbirds,
  Pudgy). For founder-independent collections, upside is essentially sector and ETH beta.
- **Quiet periods since 2025 are negative.** Milady's catalyst-free windows: −59% ETH (Feb–Sep 2025) and −28%
  (Mar–Oct 2026). See `data/processed/culture/quiet_window_returns.csv`.

## 4. BTC-relative record of finalists (OpenSea live floor vs NPF history)

| Collection | 1y vs BTC | 2y vs BTC | 3y vs BTC | From BTC-terms ATH |
|:--|--:|--:|--:|--:|
| Milady | −59% | −82% | −79% | −92% |
| Remilio | −53% | −89% | −81% | −96% |
| CryptoDickbutts | −66% | +47% | −59% | −94% |
| Pudgy Penguins | −73% | −80% | −76% | −94% |
| Azuki | −71% | −93% | −94% | −99% |
| Chromie Squiggle | −35% | −37% | −86% | −94% |
| Terraforms | −11% | −58% | −87% | −97% |
| V1 Punks | −40% | −30% | −74% | −91% |
| CryptoPunks (ref) | −44% | −12% | −64% | −84% |

The 1-year window base is 2025-10-13 (ETH/BTC 0.0368), a week after the BTC price peak (2025-10-06). Every finalist has lost to BTC over every window
except CryptoDickbutts' 2-year window, which starts from its 2024 trough.

## 5. Exit rules and timing on history (in-sample)

**Exit rules** (`scripts/exit_rule_backtest.py`, `data/processed/exit_rule_backtest.csv`):
- Method: 350 start dates (2022-06 → 2025-04), 18-month windows, BTC-terms floors, patient-exit costs. The windows
  overlap, so there are ≈3 independent periods, and the sample is bear-dominated.
- Rule B (once ≥1.5× vs BTC, sell on a 30% drawdown from the peak) beat BTC in this share of windows:
  Pudgy 80%, Milady 41%, CDB 34%, V1 32%, Remilio 27%, Terraforms 27%, Squiggle 13%, Azuki 7%.
- Median outcomes were below 1× BTC for every collection except Pudgy (1.51×). Pudgy's figure reflects its
  operator-driven 2022–24 run.
- ETH averaged 0.70× BTC over the same windows.

**ETH/BTC trend filter** (`timing_backtest.py`; critic challenge 16):
- A filter that holds only when ETH/BTC is above its 10/20/30-week average **improved the sector index 2–3×** (0.08 →
  0.17–0.25 vs BTC). It improved Azuki and V1 (30w).
- **It hurt Milady, Pudgy, Squiggle and CDB in every lookback, with mixed results for Terraforms**, once 8–25%
  round-trip costs per switch are charged.
- It is useful as a one-time **entry gate**, not as a switching strategy for a single illiquid NFT.

## 6. What the history supports and what it doesn't

**Supported**
- High-beta, short-lived upside in crypto risk-on phases.
- Pre-TGE run-ups.
- Structural re-ratings, though these too have mostly reversed.
- Collections that already crashed early (CDB 2024, Moonbirds 2025) showing the largest rebounds off depressed
  bases.

**Not supported**
- Buy-and-hold outperformance vs BTC.
- Recovery to 2021–2024 all-time highs: each cycle peak has been lower in BTC terms for most collections.
- Durable effects from brand news, museum validation or celebrity endorsement.
- Organic demand growth: trading participation is at series lows.

Charts: `reports/charts/sector_index_btc.png`, `sector_activity.png`, `finalists_btc_rebased.png`, and
`<collection>_history.png` (floor in ETH and BTC, relative-to-sector, sales, numbered catalyst markers).
