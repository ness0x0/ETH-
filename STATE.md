# STATE (operational)

_Last updated: 2026-10-14 (UTC)_

## Phase: COMPLETE
1. Infrastructure + universe screening (47 collections) — done
2. Finalist deep research (culture ×3 agents, on-chain agent, liquidity, history) — done
3. Scenario/valuation model — v2 rule-based (post-critic) — done
4. Independent critic review — done; 22/23 challenges accepted in full, 1 in part
5. Final package — done (memo, shortlist, dossiers, dataset, charts, methodology, sources, critic record, uncertainties)

## Conclusion
- No NFT purchase now.
  - ETH is the cleaner vehicle for the macro view: break-even 14% vs 18–22% for the best NFTs under rule B.
  - In S1, ETH loses 20% vs BTC; the NFTs lose 51–75%.
- Azuki: exit patiently after the 2026-11-12 Blend deadline; don't hit the forced-selling bid.
- Conditional shortlist, only if gates G1–G3 pass: V1 Punks > Milady (exception) > CryptoDickbutts (small) >
  Chromie Squiggle (collectible only). Pudgy is not ranked (outside the mandate).

## Follow-up (2026-10-14): cycle-timing framing
- Investor asked: buy near the NFT cycle low, sell into the euphoria. Does it beat BTC going 2.16–2.52× to its top?
  The 2024–25 leg is the primary analog (BTC ~2.1× from the Sep-2024 low to the Oct-2025 top).
- Result: 75% of 44 collections beat BTC (rough timing, rotating into BTC). Applied to today: 77–91% beat BTC at
  ETH/BTC 0.025–0.035, and roughly 1-in-3 to 1-in-2 double BTC's result. Upper bound: one cycle; 59% of collections
  now sit below their 2024 lows; tokens spent; survivors only. Full 2022–25 cycle: ~41%.
- Files: `reports/cycle_analysis.md`, `scripts/cycle_2024.py`, `cycle_analysis.py`, `cycle_forward.py`,
  `chart_cycles.py`; memo addendum.
- 2021 context only: Punks on-chain floor (`punks_onchain_floor.py`); OpenSea sampled 2020–22 sales
  (`cycle_a_sales_sampler.py`, complete; `cycle_a_analysis.py` → `cycleA_summary.csv`).
- Second follow-up: the bar is "4× in dollars while BTC does 2×", i.e. 2× vs BTC (`scripts/cycle_tail.py`; report
  section E; memo addendum 2).
  - With a pre-set sell at 2× vs BTC in 2024–25: 32% of all collections hit it, 8 of 12 small PFPs, and 21% of names
    above $15M. In 2022–25 small PFPs hit it 25–50% of the time.
  - 10× in dollars is a tail (5–17%).
  - The quality finalists peaked at 1.5–1.9× vs BTC, so the candidates for this bar are the small-cap watchlist.
  - Still no buy before the entry gates.
- Buy-and-hold from a cycle low fails: from the Oct-2023 low, 0 of 44 beat BTC over three years; from the 2024 low,
  41% beat BTC by its Oct-2025 top and 5% to today (report E7).
- Third follow-up, the halving-cycle hold (`scripts/halving_cycle.py`; report section F; memo addendum 3).
  - Bought Oct-2022 and sold in thirds into the 2024–25 euphorias, 4 of 39 beat BTC.
  - The small-cap basket returned 1.8× vs BTC (2.5–3.5× applied today if ETH/BTC is 0.025–0.035). It was carried by
    Remilia's collections, and dead names are missing from the data. Large caps: 0.31×.

## Market context (verified)
- 2026-10-13 closes: BTC $83,350; ETH $2,508.69; ETH/BTC 0.0301. BTC close ATH $124,659 (2025-10-06).
- Blur (announced 2026-10-12): frontend closes 2026-11-12; Blend stops new loans; borrowers repay or default by then.
- Abstract L2 (Igloo) shuts 2026-12-15. PENGU ETF rule filing withdrawn 2026-01-23.

## How to refresh (e.g., after 2026-11-12)
1. `python3 scripts/fetch_prices.py && python3 scripts/screen_universe.py --refresh`
2. Get a free OpenSea key (`POST https://api.opensea.io/api/v2/auth/keys`) into
   `/root/.config/ethnft/opensea_key.json`, then run `python3 scripts/liquidity_orderbook.py` and
   `python3 scripts/liquidity_position.py`. This is gate G1.
3. Re-run the on-chain pipeline (`scripts/onchain_*.py`) to see where the Blend-escrowed tokens went.
4. Run `python3 scripts/scenario_model.py`, `python3 scripts/build_dossiers.py` and `python3 scripts/sector_activity.py`
   (gate G2 volume test).

## Open items
- Integrate the Codex Blend loan-book reconstruction when available (not present in the repo as of 2026-10-14).
- OpenSea SEA token launch status is unverified.
- No draft PR: the repository has no base branch other than this work branch.
