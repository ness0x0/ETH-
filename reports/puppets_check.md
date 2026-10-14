# Bitcoin Puppets: does a $180k BTC imply a $5k+ Puppet? (quick check, 2026-10-14)

_Outside the Ethereum mandate. Script: `scripts/puppets_check.py`. Data:_
- _NFTPriceFloor 3-day floors. The feed is live Jan-2024 → Apr-2025, then frozen with zero sales, so frozen bars are
  dropped._
- _The CoinGecko NFT endpoint, for today's floor in BTC and its 1-year change. CoinGecko's own USD figure uses a stale
  BTC price, so USD is recomputed at BTC $83,350._

Puppets are priced in BTC, so the floor in dollars = floor in BTC × BTC price. The question is whether the floor holds
**in BTC**.

| Date | Floor (BTC) | Floor (USD) | Context |
|---|---|---|---|
| Jan-2024 (launch month) | 0.020 | ~$860 | |
| 2024-04-14 (peak, halving month) | 0.397 (3-day bar) | ~$27.9k | |
| Aug-2024 | 0.077 | ~$4.5k | BTC low ~$58k |
| Dec-2024 | 0.139 | ~$13.6k | Post-election euphoria |
| Apr-2025 | 0.034 | ~$2.9k | |
| ~Oct-2025 (from CoinGecko's −74% 1-year change) | ~0.040 | ~$4.5k | BTC near its $124.7k top |
| 2026-10-14 | 0.0102 | ~$850 | 10,001 supply → ~$8.5M floor cap; ~1 sale a day |

## Readings

- **Last cycle's leg: BTC 2.1×, Puppets flat in dollars.** From the Aug–Sep 2024 BTC low to BTC's Oct-2025 top, the
  Puppets floor roughly halved in BTC terms (0.08 → 0.04). In dollars it ended about where it started (~$4.5k).
- **The only gain went to sellers.** The Dec-2024 spike made 1.8× vs BTC (3× in dollars).
- **Each peak was lower in BTC terms:** 0.40 → 0.14 → ~0.04. In the year since, the floor fell another 74% in BTC
  while BTC fell ~26%.
- **What a $5k Puppet at BTC $180–210k requires:**
  - Flat in BTC terms, today's floor becomes $1.8–2.2k at BTC $180k.
  - $5k needs 2.3–2.7× vs BTC from 0.0102 BTC, or 2.0–2.3× from a $1k (0.012 BTC) entry.
  - That is the same "2× vs BTC" bar tested in `cycle_analysis.md` section E. It is achievable in a strong euphoria,
    and Puppets fit the profile that hit it (a culture PFP with a ~$10M floor cap, down ~97% from its peak vs BTC).
    But it is not implied by BTC's price, and last cycle it was not held.
