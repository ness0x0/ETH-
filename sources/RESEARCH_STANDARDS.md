# Research standards (all workstreams)

- **Today is 2026-10-13.** Model knowledge after mid-2026 is missing or stale; verify every post-2025 claim with a
  live source. Market context: BTC $83,350, ETH $2,508.69, ETH/BTC 0.0301 (Binance daily close 2026-10-13).
- **Never fabricate** numbers, dates, quotes, holder counts, URLs, or events. If something cannot be verified, write
  `UNVERIFIED` or `unavailable` and say what was tried.
- **Cite every material claim**: URL, publisher, publication date, access date. Prefer primary sources (official
  blogs/X posts/docs, contracts and event logs) and reputable outlets (CoinDesk, The Block, Decrypt, Blockworks,
  Bloomberg, Cointelegraph, NFT Now, Artnet). SEO aggregators (exchange "flash" news, price-prediction sites) only as
  a last resort and flagged as such.
- **Separate fact from interpretation.** Label speculation. Do not accept another agent's unsupported conclusion as
  fact — re-verify or mark as "per <agent>, unverified".
- **On-chain**: always record contract address, block range, RPC endpoint, query time (UTC), and method. Distinguish
  wallets from individuals; classify contracts (marketplaces, lending such as Blur Blend
  `0x29469395eAf6f95920E59F858042f0e28D98a20B`, NFTX vaults, Sudoswap pairs, staking, wrappers, Gnosis Safes).
- **Persist work to files** in the repo (`/home/user/ETH-`); return to the coordinator only a concise handoff
  (≤ 400 words) listing output paths and the most decision-relevant findings, including what could not be verified.
- Do not purchase, sign, connect wallets, create paid accounts, or bypass access controls/CAPTCHAs.
- Do not commit or push git changes; the coordinator handles git.

Helpers: `scripts/common.py` (HTTP with raw-cache, JSON-RPC client using Tenderly public archive gateway
`https://gateway.tenderly.co/public/mainnet` [≤20k logs/query; batch requests get rate-limited — use single,
throttled calls] and NodeReal public endpoint [≤50k-block log ranges]). Price history:
`data/processed/prices_daily.csv` (date, eth_btc, btc_usd, eth_usd). Floor history (3-day bars since ~May 2022):
`data/processed/npf_series/<npf_slug>.csv` (floorNative, floorUsd, salesCount, volumeNative, volumeUsd, eth_btc,
floorBtc) sourced from NFTPriceFloor `api-bff.nftpricefloor.com/projects/<slug>/charts/all`.
