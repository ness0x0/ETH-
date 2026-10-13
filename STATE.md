# STATE (operational — keep < 1,000 words)

_Last updated: 2026-10-13 (UTC)_

## Phase
1. Infrastructure + universe screening — **in progress**
2. Finalist deep research (parallel workstreams) — pending
3. Scenario/valuation model — pending
4. Independent critic review — pending
5. Final package — pending

## Market context (verified)
- 2026-10-13 Binance closes: BTC $83,350; ETH $2,508.69; ETH/BTC 0.03010.
  BTC close ATH $124,659 (2025-10-06); ETH close ATH $4,832 (2025-08-22). ETH/BTC low 0.01805 (2025-04-21).
- Blur announced 2026-10-12: blur.io frontend closes **2026-11-12**; Blend stops new loans; borrowers must
  repay or default by that date (collateral to lender). On-chain marketplace contracts remain. (CoinDesk, The Block.)
- Codex agent separately reconstructs Blend loan book — do not duplicate; integrate when available.

## Data access decisions
- Tenderly public RPC = archive logs (≤20k results/query); NodeReal public key (≤50k block range). publicnode
  blocks archive. Batch receipts get rate-limited → throttle single calls.
- NFTPriceFloor 3d series = primary historical floor source (2022→); on-chain for cross-check and 2021.

## Completed
- Workspace skeleton; `scripts/common.py`, `fetch_prices.py` (prices_daily.csv), `universe_config.py` (47 names).

## Active
- `screen_universe.py` fetching OpenSea + NPF for universe.

## Next
- Pick 6–10 finalists → launch: market historian, collector (on-chain) analyst, cultural researcher agents.
- Build scenario model; critic; memo.

## Blockers
- None requiring the user.
