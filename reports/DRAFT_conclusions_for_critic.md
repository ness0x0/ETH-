# DRAFT conclusions (pre-critic) — 2026-10-13

_This is the coordinator's draft position, written so the independent critic can attack it. It will be revised._

## Evidence base (paths)
- Screening: `universe.csv` (47 collections). Base rates: `reports/historical_analysis.md`.
- Culture/catalysts: `dossiers/_research/*_culture.md`, `data/processed/catalysts/*.csv`, `data/processed/event_study.csv`.
- On-chain: `reports/onchain_collector_analysis.md`, `data/processed/onchain/*.csv`.
- Liquidity: `data/processed/liquidity_activity.csv`, `liquidity_orderbook.csv`, `liquidity_position.csv`.
- Scenarios: `scripts/scenario_params.py`, `scripts/scenario_model.py` → `data/processed/scenarios.csv`.
- Timing test: `data/processed/timing_backtest.csv` (ETH/BTC trend filter does not help single collections after costs).

## Draft headline
1. **There is no structural case for ETH NFTs beating BTC.** The equal-weight sector lost ~90% vs BTC from Jun-2022
   to Oct-2026 and fell vs BTC in every calendar year. Trading participation is at series lows. Every finalist has
   lost to BTC over 1-, 2- and 3-year windows (except CDB's 2-year window, measured from its trough).
2. **The upside is real but transient.** Each sector rally ran 1.6–2.9× vs BTC (median, trough→peak), then gave
   back 60–80% within 3–6 months. Token airdrops destroyed value after the TGE (median −58% vs BTC at 90 days).
   Brand, museum and celebrity events had ~0 abnormal effect at 90 days.
3. **Under evidence-anchored scenario assumptions**, every finalist matches BTC in expectation only if the investor
   puts ≥16–27% weight on strong-recovery or mania scenarios **and** sells into the rally. Buy-and-hold needs 38% to
   >100%. ETH itself breaks even at 14%, so it is the cleaner vehicle for the macro view. NFTs add convexity only in
   a mania (S4 disciplined: +211% to +470% vs BTC, against +66% for ETH) at the cost of −59% to −79% in the weak
   scenario (−20% for ETH).
4. **Draft recommendation.** Do not deploy the full allocation as a buy-and-hold collectible bet. If the investor
   holds the "ETH and BTC revisit ATH" view with conviction, a staged position is defensible: half to two-thirds of
   the allocation, explicit sell-into-strength rules, bids rather than lifted asks, and the first tranche after the
   2026-11-12 Blend deadline for PFPs.

## Draft ranking (affordable, mandate fit)
1. **Chromie Squiggle** — best survivability.
   - Strengths:
     - Immutable on-chain script; MoMA, LACMA and Toledo holdings.
     - Founder-independent.
     - Stickiest holders (84% of supply untouched 24 months).
     - Most organic new demand (45% of t12m purchases by first-time wallets; 20% churn).
     - No Blend exposure; did not sell off in the Blur shock; 1-year vs BTC −35%, the best large finalist.
   - Weaknesses:
     - Costly exit: 8.5% seller fees including a 7.5% enforced royalty, and the best bid sits at 78% of floor, so
       an instant round trip loses about 29%.
     - Lowest convexity. One item uses about 88% of the budget.
     - One minter entity holds 13%.
     - Museum news did not lift the floor.
   - Scenario break-even: 27% (disciplined), 49% (hold).
2. **V1 CryptoPunks** — best scenario profile under the draft assumptions.
   - Strengths:
     - Anchored to V2 Punks, the most resilient asset.
     - 0% fees.
     - Legitimacy optionality (PunksMarket).
     - Scenario break-even 17% (disciplined), 38% (hold).
   - Weaknesses:
     - Disowned by the artists; the IP holder (NODE) ignores it; every museum chose V2.
     - Concentration: top-10 hold 48%, a possible single entity holds ~18%, and a Yuga-linked block holds 1,084
       unwrapped.
     - The V1/V2 ratio has compressed.
     - DMCA tail risk.
3. **Pudgy Penguins** — the tactical, liquid beta vehicle.
   - Strengths:
     - Best exit liquidity (instant round trip about 7.5%; 5.9 organic sales/day).
     - Least concentrated holders.
     - A whale absorbed 131 in the Oct-11 sell-off.
     - Highest β to ETH/BTC (1.43). Nearly matched BTC since Jul-2022 (0.94×).
   - Weaknesses:
     - Fails founder-independence. Holders have no claim on IP or revenue.
     - PENGU insider unlocks run to 2028. Abstract was written off; the ETF is dead.
     - −73% vs BTC over 1 year.
   - A trade, not a collectible.
4. **Milady Maker** — cultural optionality.
   - Strengths:
     - Vitalik and EF adoption.
     - Divisible (3–4 items), which allows scaling out of the position.
   - Weaknesses:
     - High founder risk. Quiet windows are negative. CULT is spent.
5. **Terraforms** — small speculative.
   - Strengths: on-chain art; sticky holders.
   - Weaknesses:
     - The "living artwork" is founder-dependent.
     - Latent 1,193-token owner mint.
     - One entity made 13.5% of purchases.
     - Instant round trip about 28%.

**Not recommended:**
- CryptoDickbutts: instant round trip about 40%; contested IP.
- Remilio: a derivative with total founder dependence.
- Azuki: see below.
- Watchlist names: none upgraded.

## Azuki (incumbent)
It fails on every criterion:
- Founder-dependent, and the company's IP strategy bypasses the NFT.
- Highest lending escrow (3.6%, including BendDAO).
- −99% vs BTC from its ATH.
- Hold-through break-even is effectively unattainable.

Draft: replace it. Timing is secondary, since the position is about 0.47 ETH. Either sell into any bounce, or after
the Blend deadline if forced selling is judged temporary.

## Draft entry conditions
- Bid, don't lift. Funded bots refill bids at about 92–93% of floor for liquid PFPs.
- Pudgy and Milady: first tranche after 2026-11-12, or bids at ≤90% of floor during the Blend unwind.
- Squiggle: bid ≤2.3 ETH (≤~0.07 BTC).
- V1: bid ≤1.5 ETH.
- No mechanical ETH/BTC trend filter. The backtest shows whipsaw plus round-trip costs hurt single collections.

## Draft exit rules
- Pre-commit: sell 50% at 2× in BTC terms.
- Sell the remainder on a 30% drawdown from the post-entry peak, or at 3×.
- Sell into any pre-TGE token run-up (sell the news).
