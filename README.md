# Ethereum NFT Investment Research (Oct 2026)

**Objective.** Identify Ethereum-native NFT collections offering asymmetric, BTC-denominated upside over 6–24 months
(to 2028–29) for a ~$7–8k allocation, held by a BTC-primary investor who currently owns one Azuki.
Conclude "no purchase" if evidence does not justify one.

**Status.** See [STATE.md](STATE.md).

## Navigation

| Path | Contents |
|---|---|
| `STATE.md` | Current phase, completed work, next actions, blockers |
| `universe.csv` | Screened universe (~47 collections) with valuation/liquidity metrics and include/reject reasons |
| `reports/` | Executive memo, ranked shortlist, scenario model, critic review, uncertainties |
| `reports/charts/` | Historical ETH/BTC-denominated charts with catalyst annotations |
| `dossiers/` | One file per finalist |
| `data/raw/` | Raw API responses (each wrapped with `fetched_at_utc`) |
| `data/processed/` | Derived datasets (price series, screening metrics, on-chain holder/sales tables) |
| `scripts/` | Reproducible fetch + analysis code (`python3 scripts/<name>.py`) |
| `sources/` | Source registry, data-quality notes, methodology |

## Data sources (verified reachable 2026-10-13)

- **On-chain**: Ethereum archive logs via Tenderly public gateway (`gateway.tenderly.co/public/mainnet`) and
  NodeReal public endpoint — Transfer events, marketplace receipts.
- **OpenSea API v2** (keyless endpoints): collection stats & metadata.
- **NFTPriceFloor** (`api-bff.nftpricefloor.com`): 3-day floor/volume/sales history since ~May 2022.
- **Binance public market data** (`data-api.binance.vision`): daily ETHBTC/BTCUSDT/ETHUSDT since 2017.
- **Blockscout** (`eth.blockscout.com`): holder counts.
- Web/news sources for catalysts and culture (cited in dossiers).

Unavailable without paid/authenticated access: Reservoir (shut down), Dune, Etherscan, OpenSea events/orders
endpoints (need key), CoinGecko NFT history (Pro), BigQuery (no credentials).
