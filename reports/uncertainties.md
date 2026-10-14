# Outstanding uncertainties (only those that could change the decision)

| # | Uncertainty | Why it matters | How to resolve | Effect if resolved favourably |
|---|---|---|---|---|
| 1 | **Blend loan book / liquidation pipeline.** The separate Codex reconstruction was not available. We measured only NFTs held in lending escrow (Blend 194 Pudgy, 182 Azuki, 136 Milady, 100 Remilio, 253 Lil Pudgys; BendDAO 158 Azuki) | Defaults transfer collateral to lenders, who may sell before or after 2026-11-12. That determines whether the current PFP weakness is temporary and when the Azuki should be sold | Integrate the Codex output (loan sizes, LTVs, lender identities) and re-run `scripts/onchain_holders.py` after 2026-11-12 to see where escrowed tokens went | A cleaner entry and exit window for PFPs (G1). It does not change the headline |
| 2 | **Post-Blur liquidity regime.** 52–58% of Pudgy and Azuki trailing-year sales ran through Blur or Blend | Every PFP liquidity, churn and haircut number comes from a two-venue market that ends on 2026-11-12 | Re-snapshot OpenSea depth (`scripts/liquidity_orderbook.py`) and churn in late November | Pass or fail of gate G1 for the PFPs |
| 3 | **ETH/BTC direction.** The dominant driver of every NFT outcome (β≈1) | S1 vs S3/S4 is mostly an ETH/BTC question. If ETH/BTC recovers, ETH alone captures most of the benefit | Not resolvable; investor's view | Changes the case for ETH more than for any NFT |
| 4 | **A new incentive regime** (e.g., an OpenSea SEA token rewarding NFT trading or staking; launch status unverified as of 2026-10-13) | Incentives drove the 2023 and 2024 rallies (S4) | Watch OpenSea announcements; verify TGE mechanics and snapshot rules | It would create a tradeable spike (sell into it), not durable value, given the TGE history |
| 5 | **V1 legitimacy and dormant supply.** NODE's stance is unknown; the 1,084-V1 Safe is attributed to Yuga by inference; ~18% may sit with one entity | The #1 conditional pick rests on V1 not being suppressed (DMCA precedent) and dormant supply not being sold | Primary statement from NODE; watch Safe `0xa858…2ef1` and the large wallets on-chain | Acknowledgement or a burn would be a step change; a sale or enforcement would invalidate the pick |
| 6 | **Remilia governance and the CULT overhang** (53.1B CULT, 53% of supply, undistributed; 2023 lawsuits unresolved) | Milady's price has been driven by Remilia events; new shocks are the main tail risk | Court records; on-chain movements of the CULT contract balance | A burn or resolution would upgrade Milady's founder-risk assessment |
| 7 | **Squiggle 13% entity and royalty policy** | The single holder is ~2.4 years of organic turnover. The 7.5% enforced royalty is the largest driver of Squiggle's poor exit economics | Identify the entity; monitor OpenSea creator-fee enforcement | Royalty removal would cut its break-even materially (critic estimate under v1: 27% → 21%), still far above ETH's 14% |
| 8 | **Terraforms latent mint** (1,193 tokens controllable by a single EOA) | ~12% dilution risk that no public source discusses | A team statement or an on-chain renounce/lock | Would lift Terraforms from "not recommended" to the watchlist |
| 9 | **Data limitations.** NPF 3-day bars smooth peaks and undercount sales by 22–47%; the order book is OpenSea-only; wallets ≠ people; the exit-rule backtest is in-sample with ~3 independent periods | Magnitudes, not directions, could change | Paid Dune/Reservoir-successor data; a longer out-of-sample period | Unlikely to change the headline, which rests on several consistent lines of evidence |
| 10 | **Investor-specific costs.** Tax on selling BTC, conversion spreads, operational security | They raise the hurdle for any switch out of BTC | Investor's own circumstances | Higher costs strengthen "no purchase" |

Resolved during the project (no longer uncertain):
- Abstract shutdown (2026-12-15); PENGU ETF withdrawn (2026-01-23); CULT TGE date (2024-12-09).
- MoMA Squiggle donation (donated, not purchased).
- Terraforms latent mint (verified on-chain).
- Squiggle royalty (present in 89/89 listings).
- The Remilio/Terraforms "floor walls" were duplicate orders, not supply.
- CryptoDickbutts sales clear near the floor (on-chain median 1.02×).
