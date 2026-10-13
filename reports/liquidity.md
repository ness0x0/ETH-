# Liquidity & exitability (finalists)

_Snapshot: OpenSea API v2 order book, 2026-10-13 22:29–22:33 UTC (free key, `scripts/liquidity_orderbook.py`).
On-chain sales classification for the trailing 12 months comes from `reports/onchain_collector_analysis.md`.
Position maths: `scripts/liquidity_position.py`._

## 1. Can a ~$7.5k position (≈2.99 ETH) be entered and exited?

| Collection | Floor ask (ETH) | Items for budget | Entry cost (ETH) | Instant exit into funded bids, after seller fees (ETH) | Instant round-trip loss | Seller fees | Organic sales/day (365d, ex-churn) |
|---|---|---|---|---|---|---|---|
| Pudgy Penguins | 2.430 | 1 | 2.430 | 2.247 | **7.5%** | 1% | 5.9 |
| Lil Pudgys | 0.231 | 12 | 2.905 | 2.579 | 11.2% | 1% | 10.9 |
| V1 Punks (wrapped) | 1.700 | 1 | 1.700 | 1.500 | 11.8% | 0% | 1.9 |
| Milady | 0.745 | 3 | 2.435 | 2.036 | 16.4% | 1% | 5.3 |
| Azuki | 0.548 | 5 | 2.747 | 2.280 | 17.0% | 1% | 4.8 |
| Terraforms | 0.300 | 9 | 2.961 | 2.142 | 27.6% | 1% | 2.5 |
| Chromie Squiggle | 2.642 | 1 | 2.642 | 1.876 | **29.0%** | **8.5%** (7.5% enforced royalty) | 1.5 |
| Remilio | 0.118 | 20 | 2.942 | 2.086 | 29.1% | 1% | 5.3 |
| CryptoDickbutts | 0.473 | 5 | 3.040 | 1.798 | **40.9%** | 1% | 1.1 |

**Reading the table**
- The instant round-trip loss is the worst case: lift the cheapest asks today and dump into today's bids at once.
  A patient seller who lists near the floor recovers much of the bid gap, but not the fees.
- Fees come from the consideration items in the OpenSea listings: 1% marketplace fee on most collections, plus a 7.5%
  creator fee that is enforced on Chromie Squiggle (8.5% total). Wrapped V1 listings carried no fee.
- Multi-item positions cost more than floor × n, because the book is thin above the floor. Remilio's 20 items average
  1.24× floor; CryptoDickbutts' 5 items average 1.29×.

## 2. Bid depth (OpenSea collection offers, funding-checked against WETH balances)

| Collection | Best bid / floor | Unique bidders | Funded bids ≥90% of floor | ≥80% | ≥50% | Distinct tokens listed within 5% / 25% of floor |
|---|---|---|---|---|---|---|
| Pudgy | 93% | 61 | 5 | 12 | 20 | 2 / 14 |
| Lil Pudgys | 96% | 66 | 15 | 32 | 60 | 4 / 39 |
| Milady | 92% | 32 | 7 | 10 | 21 | 1 / 6 |
| Remilio | 93% | 37 | 7 | 22 | 51 | 6 / 10 |
| Terraforms | 90% | 30 | 4 | 4 | 24 | 3 / 11 |
| V1 Punks | 88% | 26 | 0 | 1 | 11 | 5 / 13 |
| Azuki | 85% | 49 | 0 | 9 | 23 | 5 / 18 |
| CryptoDickbutts | 84% | 21 | 0 | 3 | 11 | 1 / 2 |
| Chromie Squiggle | **78%** | 28 | 0 | 0 | 5 | 9 / 19 |

**Caveats**
- These are OpenSea collection offers only. Blur bids aren't observable without wallet login, and Blur's frontend
  closes 2026-11-12.
- Many offers are bot bids with ~15-minute expiry that refresh continuously.
- A bidder's WETH balance backs offers across many collections, so funded depth is an upper bound.
- **Correction:** an earlier draft reported 140+ token "supply walls" in Remilio and Terraforms. Those were duplicate
  orders on the same token (one Remilio token was re-listed 90 times). Listings are now de-duplicated per token, and
  on-chain checks confirmed the wallets held only 1–6 tokens.

## 3. Organic vs headline liquidity

- **68–82% of trailing-year PFP sales are dealer churn**: bid-hit-and-relist on Blur and OpenSea. Raw volume
  overstates real exit liquidity by ~3–6×.
- **Organic turnover is ~5–6 sales/day** for Pudgy, Milady, Remilio and Azuki, and 1–2.5/day for the art names.
- Chromie Squiggle (20% churn) and Terraforms (43%) have the most genuine turnover per sale. Their absolute
  throughput is still low: the median gap between organic Squiggle sales is ~9–11 hours.
- **Dealer liquidity is fragile.** It depends on marketplace incentives and the bot ecosystem. Blur's frontend
  closure may reduce it, though Blur's contracts stay live and OpenSea already aggregates most bids.

## 4. Liquidity in stress and in rallies (history)

- **Stress.** One-bar crashes with heavy volume show what happens when someone sells size into thin bids:
  - Milady, 2024-03-18: floor 3.69 → 2.04 ETH on 1,139 sales in 3 days (treasury-drain liquidation).
  - Pudgy, 2026-10-11: 324 sales in a day at a 2.50 ETH median, against ~3.2 a week earlier. One entity absorbed 131.
- **Rallies.** Sales counts rise 2–5× around rally peaks (`reports/charts/*_history.png`). Exits are easiest exactly
  when a disciplined seller wants to sell.
- **Worst 90-day organic pace in the last two years** (`liquidity_activity.csv`, NPF-based): Squiggle ~1 sale/day,
  CryptoDickbutts ~1.2, Terraforms ~2.5.

## 5. Implications

1. **Pudgy is the only finalist where a whole-budget position can be exited quickly at ≤~8% cost.** That makes it the
   natural vehicle for a tactical, sell-into-strength trade.
2. **Chromie Squiggle's 8.5% fees plus a ~22% bid gap make it a buy-and-hold asset by construction.** It needs a
   large move before a sale makes sense. That works against its role as a "survivability" pick, because survivability
   matters most to a holder who doesn't trade, and holding has not beaten BTC.
3. **CryptoDickbutts is slow to exit at size:** a ~41% instant round trip (mostly from a thin ask stack above the floor)
   and 11-hour organic sale gaps. Single items do clear near the floor: the on-chain median sale is 1.02× the floor.
4. **Divisible positions (Milady 3–4 items, Lil Pudgys ~12) allow scaling out,** which suits disciplined exits better
   than a single high-priced item.
