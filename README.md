# Ethereum NFT Investment Research (Oct 2026)

**Objective.** Identify Ethereum-native NFT collections offering asymmetric, BTC-denominated upside over 6–24 months
(to 2028–29) for a ~$7–8k allocation. The investor is BTC-primary and currently owns one Azuki. The brief allowed a
"no purchase" conclusion if the evidence did not justify one.

**Status: complete (2026-10-13/14).** Start with the **[Executive memo](reports/EXECUTIVE_MEMO.md)**.

**Conclusion in one line:** no NFT purchase now. ETH is the cleaner vehicle for an ETH/on-chain-recovery view.
Exit the Azuki patiently after the 2026-11-12 Blend deadline. If a speculative ticket is still wanted once the entry
gates are met, buy one V1 CryptoPunk by bid with a pre-committed trailing-stop exit.

## Deliverables

| # | Deliverable | Path |
|---|---|---|
| 1 | Executive investment memo | [`reports/EXECUTIVE_MEMO.md`](reports/EXECUTIVE_MEMO.md) |
| 2 | Ranked shortlist (conditional), entry gates, overhang table | [`reports/shortlist.md`](reports/shortlist.md) |
| 3 | Collection dossiers (8 finalists) and underlying culture/catalyst research (10 files) | [`dossiers/`](dossiers/), [`dossiers/_research/`](dossiers/_research/) |
| 4 | Comparative dataset (47 collections) | [`universe.csv`](universe.csv) |
| 5 | Historical charts (ETH/BTC-denominated, relative-to-sector, sales, catalyst markers; sector index; scenarios) | [`reports/charts/`](reports/charts/) |
| 6 | Source & methodology archive | [`sources/METHODOLOGY.md`](sources/METHODOLOGY.md), [`sources/SOURCES.md`](sources/SOURCES.md), [`sources/RESEARCH_STANDARDS.md`](sources/RESEARCH_STANDARDS.md), [`scripts/`](scripts/) |
| 7 | Independent critical review and our response | [`reports/critic_review.md`](reports/critic_review.md), [`reports/critic_response.md`](reports/critic_response.md) |
| 8 | Outstanding uncertainties | [`reports/uncertainties.md`](reports/uncertainties.md) |

**Supporting analyses**
- [`reports/historical_analysis.md`](reports/historical_analysis.md): base rates, rally anatomy, catalyst event study,
  exit-rule and timing backtests.
- [`reports/onchain_collector_analysis.md`](reports/onchain_collector_analysis.md): holders, retention, lending escrow,
  sales vs transfers, dealer churn, wash flags.
- [`reports/liquidity.md`](reports/liquidity.md): order-book depth and round-trip costs.
- [`reports/scenario_model.md`](reports/scenario_model.md): rule-based BTC-relative scenarios and break-evens.
- [`reports/cycle_analysis.md`](reports/cycle_analysis.md): buy at the cycle low, sell into the euphoria. Tested on
  the 2024–25 cycle (primary analog) and 2022–25, with forward odds vs BTC by ETH/BTC. Section E covers the 4–10× vs
  BTC question: how often it happened, the winners' profile, baskets, catalyst triggers and new mints.

## Repository map

| Path | Contents |
|---|---|
| `STATE.md` | Final state and how to refresh |
| `data/raw/` | Raw API responses, each wrapped with `fetched_at_utc` (on-chain dumps are git-ignored and regenerable) |
| `data/processed/` | Derived datasets: prices, NPF series, screening, sector index, rallies, event study, liquidity, on-chain tables, scenarios |
| `scripts/` | Reproducible pipeline (`python3 scripts/<name>.py`; order in `sources/METHODOLOGY.md`) |
| `reports/archive/` | Pre-critic draft conclusions (audit trail) |

## Data sources (verified reachable 2026-10-13)

- Ethereum archive logs via the Tenderly public gateway and a NodeReal public endpoint.
- Blockscout.
- OpenSea API v2: keyless stats, plus a free self-serve key for the order book.
- NFTPriceFloor 3-day history.
- Binance public market data.
- CoinGecko (free).
- Web and news sources, cited per claim.

Unavailable without paid or authenticated access: Reservoir (shut down 2025-10), Dune, Etherscan, Blur bids,
CoinGecko NFT history, BigQuery.
