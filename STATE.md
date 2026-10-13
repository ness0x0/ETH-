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
- Workspace skeleton; prices; universe screening (47 collections) → `universe.csv` (8 finalists, 9 watchlist,
  7 reference, 23 reject).
- Base rates: EW sector floor index −90% vs BTC (Jun-2022→Oct-2026), negative vs BTC every calendar year;
  sector rallies (2023/2024/2025) median trough→peak 1.6×/2.3×/2.9× in BTC terms, ~35–40% of peak retained 90–180d
  later. Sector quarterly volume $67M (Q3-2026) vs $2.3B (Q1-2023).
- Recent shock: Pudgy/Azuki/Milady/BAYC floors fell sharply over Oct 10–13 (Blur shutdown) on top of an Aug–Oct
  downtrend; art collections (Squiggle, Terraforms) and Punks did not.
- Finalists: Milady, Remilio, CryptoDickbutts, Pudgy, Azuki (incumbent), Chromie Squiggle, Terraforms, V1 Punks.
- Charts: sector index, finalists BTC-rebased, per-finalist history (catalyst annotations pending).
- Methodology & data-quality notes (`sources/METHODOLOGY.md`); scenario engine scaffold.

## Active (background agents)
- Culture/catalyst research ×3 (Milady/Remilio/CDB; Pudgy/Azuki/Moonbirds; Squiggle/Terraforms/V1 + Curio/MoonCats).
- On-chain collector analyst (holders, retention, lending escrow incl. Blend + Gondi, sales classification).
- OpenSea free-key retry loop (key creation rate-limited) → then `liquidity_orderbook.py`.

## Next
- Integrate agent outputs → event study, annotated charts, dossiers.
- Scenario parameters (`scripts/scenario_params.py`) → `scenario_model.py`.
- Independent critic agent → revisions → memo, shortlist, uncertainties; commit, push, draft PR.

## Open flags
- CryptoDickbutts avg sale ≈0.64× floor (90d) → floor may not be executable; verify on-chain.
- Quirkies rise looks concentrated/leveraged (Gondi escrow ~10%) → rejected.
- OpenSea SEA token launch status unverified (possible marketplace-incentive catalyst).
- Codex Blend loan-book findings not yet available (remote has no other branches as of 22:05 UTC).

## Blockers
- None requiring the user.
