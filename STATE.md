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
