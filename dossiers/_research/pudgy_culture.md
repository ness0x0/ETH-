# Pudgy Penguins + Lil Pudgys: cultural durability and catalyst history

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[I]** = interpretation or inference by this workstream; **UNVERIFIED** = could not confirm (what was tried is stated)._
_Dated events are in `data/processed/catalysts/pudgy.csv`. Source numbers [S#] are listed in §11._

**Snapshot (2026-10-13):** Pudgy floor 2.31 ETH and Lil Pudgys floor 0.231 ETH (OpenSea, via `data/processed/screen_metrics.csv`). ETH $2,508.69, BTC $83,350. In BTC terms the Pudgy floor is ≈0.0695 BTC, about 94% below its 3-day-bar peak of 1.143 BTC on 2024-02-20 (NPF series). In ETH terms it is 91% below the 25.23 ETH peak on 2024-12-16. Lil Pudgys is 91% below its 2.65 ETH peak on the same date. OpenSea counts 5,001 owners for 8,888 Pudgy Penguins and 10,213 owners for 21,931 Lil Pudgys. In the last 30 days Pudgy had 1,087 sales and Lil Pudgys had 1,962 (screen_metrics). PENGU closed at $0.00783 on Binance on 2026-10-13 (`data/processed/token_prices_daily.csv`).

---

## 1. Identity & provenance

- **[F] Pudgy Penguins**, contract `0xbd3531da5cf5857e7cfaa92426877b022e612cf8`, supply 8,888. The contract was created 2021-07-22 12:26 UTC (block 12,876,179) and the first mint followed at 12:48 UTC (block 12,876,278). This is on-chain (method below), and it matches Wikipedia's 22 July 2021 date [S1].
- **[F] Lil Pudgys**, contract `0x524cab2ec69124574082676e6f654a18df49a048`, supply 22,222 by design (OpenSea now counts 21,931). The contract was created 2021-12-19 17:09 UTC (block 13,836,867) and the first mint followed at 17:18 UTC. Secondary sources say the first 8,888 were reserved for Pudgy holders and the rest were sold publicly [S2]; the mint split is UNVERIFIED against the original mint documents.
- **[F] Pudgy Rods** were a free-claim "egg" NFT from August 2021. On 2021-12-24 the eggs were revealed as fishing rods, which disappointed holders and fed the leadership turmoil. They later became multipliers for licensing deals and the PENGU airdrop [S2][S3]. Decrypt calls them "Pudgy Rogs" [S3]; The Block calls them "Pudgy Rods" [S4].
- **[F] Founder era.** In January 2022 holders voted founder Cole Villemain ("ColeThereum") out, amid allegations about the treasury and a plan to sell the project. The exact vote date is UNVERIFIED. Luca Netz publicly offered 750 ETH that same January [S5][S6].
- **[F] Acquisition.** Netz Capital's Luca Netz bought the collection and its royalties for 750 ETH (≈$2.5M). The deal was made public on Saturday 2 April 2022; Decrypt's article and Netz's embedded tweet are dated 3 April 2022 [S5]. Wikipedia says the IP went to Netz, Peter Lobanov, Lorenzo Melendez, Vedant Mangaldas and Jennifer McGlone, and that Igloo Inc. was formed that month [S1]. **[I]** The Wikipedia page reads like brand copy, so it is used only for low-stakes dates.
- **[F] Metadata and custody.** Queried on-chain on 2026-10-13: Pudgy `tokenURI(1)` returns an IPFS URI (`ipfs://bafybei…/1`). Lil Pudgys `tokenURI(1)` returns a **centralized URL, `https://api.pudgypenguins.io/lil/1`**. Both contracts report the same `owner()`, `0xf54c9a0e44a5f5afd27c7ac8a176a843b9114f1d`. **[I]** Lil Pudgys art and traits depend on an Igloo-run server, which matters for the "team vanishes" test in §8. Whether either contract's metadata is frozen is UNVERIFIED.
- **[F] Character IP.** The brand's core characters are "Pax Pengu" and "Polly", set in "The Berg"; the community is "The Huddle" [S1]. The characters belong to the company and are not tied to any one NFT.

_On-chain method:_ `scripts/common.py` RPC (Tenderly public gateway `https://gateway.tenderly.co/public/mainnet`, NodeReal as fallback). Creation block was found by binary search on `eth_getCode`; first mint came from `eth_getLogs` (Transfer with `from=0x0`) over the 400k blocks after creation; metadata from `eth_call` to `tokenURI(1)` and `owner()` at `latest` (head ≈ block 26,186,443). Queried 2026-10-13 ~21:55–22:05 UTC. Scratch script: `/tmp/claude-0/.../scratchpad/scripts/first_mint.py`, not committed.

## 2. Narrative timeline (condensed; the CSV has the full list)

| Date | Event | Floor context (NPF 3-day bars) |
|---|---|---|
| 2021-07-22 | Mint, 8,888 [on-chain] | n/a (series starts May 2022) |
| 2021-12-19 / 12-24 | Lil Pudgys mint begins; Pudgy Rods revealed as fishing rods, community upset [S2] | n/a |
| 2022-01 | Founders voted out; Netz offers 750 ETH [S5][S6] | n/a |
| 2022-04-02 | Netz acquisition made public [S5] | Blockmedia: floor recovered from <1 ETH to 3.15 ETH [S6] |
| 2022-08-11 | "Pudgy Toys … licensed directly from the community" announced [S7] | 2.63 ETH, +18% d/d (CoinDesk) |
| 2023-05-09 | $9M seed round led by 1kx [S8] | ~4.1 ETH |
| 2023-05 | Pudgy Toys launch on Amazon [S9][S10] | 3.8–5.1 ETH |
| 2023-09-26 | Walmart, ~2,000 stores [S9] | 4.46 → 4.68 ETH |
| 2023-12-10 | Pudgy World announced at Art Basel [S11] | 6.2 → 10.0 ETH (Dec 2023; NFT market rallied broadly) |
| 2024-01 → 02 | OverpassIP licensing platform (Jan 2024 per [S12]); Walmart grows to 3,100 stores (2024-02-21) [S13] | 10.5 → 19.8 ETH. **BTC-terms all-time high 1.143 BTC (2024-02-20)** |
| 2024-05-12 | Target, nationwide [S10] | ~11 ETH. The NPF 2024-05-11 bar shows 5.74 ETH, a one-bar outlier between 11.0 and 11.3, likely a data artifact |
| 2024-07-23 | Igloo raises $11M+ led by Founders Fund to build the Abstract L2 [S14] | ~10.4 ETH |
| 2024-12-06 | PENGU airdrop announced [S4] | 13.7 ETH (Dec 4 bar) |
| 2024-12-16 | **ETH-terms all-time high: Pudgy 25.23 ETH, Lil 2.65 ETH** (NPF) | |
| 2024-12-17 | PENGU TGE on Solana; Binance/OKX/Bybit list it [S3] | Pudgy 15.08 ETH, Lil 0.915 ETH (Dec 19 bar) |
| 2025-01-27 | Abstract public mainnet [S14] | ~15–19 ETH |
| 2025-01-30 | PENGU claim window cut to five more days [S3] | 23.3 (Jan 18) → 9.5 ETH (Feb 5) |
| 2025-03-13 / 03-20 | Robinhood lists PENGU [S15]; Canary PENGU ETF S-1 filed [S16] | ~8.3–8.8 ETH |
| 2025-06-25 | Cboe BZX files 19b-4 to list the Canary PENGU ETF (PENGU plus some Pudgy NFTs) [S17] | ~8.8 ETH |
| 2025-07-11 → 07-29 | PENGU roughly doubles in a week (ETF hype; Coinbase uses a Pudgy as its X profile picture on 07-11) [S18] | 8.7 → 15.8 ETH |
| 2025-08-29 | Pudgy Party mobile game launches globally (Mythical Games) [S19] | ~9.5 ETH |
| 2025-10-10 | Market-wide liquidation crash, ~$19B [S20] | 9.49 → 6.18 ETH (Oct 6 → Oct 15) |
| 2025-12-17 | PENGU team and company 1-year cliffs end (derived from [S3]) | 4.38 ETH |
| 2025-12-24 | Las Vegas Sphere holiday ads, ~$500k [S21] | ~4.0–4.5 ETH |
| 2026-01-23 | **Cboe withdraws the PENGU ETF rule filing** (SEC page marked "WITHDRAWN 01/23/2026") [S22] | ~4.7 ETH |
| 2026-02 | Pengu Card (Visa/KAST) announced [S23] | ~4.3 ETH |
| 2026-03-04 | PEI Licensing (Original Penguin) sues Pudgy Penguins Inc. for trademark infringement, S.D. Fla. 1:26-cv-21458 [S24] | ~4.3 ETH |
| 2026-03-09 | Pudgy World browser game launches publicly [S25] | Flat in ETH (CoinDesk) |
| 2026-04-17 | ~703M PENGU unlocked (0.79% of supply); monthly unlocks continue [S26] | ~4.0–4.2 ETH |
| 2026-06-13 | Pudgy Party wound down after >1M downloads [S27] | ~4.3 ETH |
| 2026-06-20 | Vibes TCG Series 3 (Pudgy plus Moonbirds) at Target nationwide; 15M cards in circulation [S28] | ~4.4 ETH |
| 2026-08 (late) | PENGU +62% in a week on recycled IPO talk; no new company statement [S29] | ~3.7–4.2 ETH |
| 2026-09-15 | Rice AI (Mint Inc., NASDAQ: MIMI) takes a non-exclusive license for a "Blue Pengu Minibot" [S30] | ~3.2 ETH |
| 2026-10-06 | **Abstract L2 shutdown announced** for 2026-12-15; Igloo lost "tens of millions" [S31][S32] | 2.97 ETH |
| 2026-10-11 | Collector Adam Weitsman buys 117 Pudgy Penguins [S33] | 2.70 ETH |
| 2026-10-12 | Blur says its frontend closes and Blend winds down by 2026-11-12 (per STATE.md, coordinator-verified) | **2.35 ETH, 381 sales in the 10-13 bar** |

## 3. Founder/team dependence and company status (Oct 2026)

**[F] Ownership and leadership.** Igloo Inc. is the parent and Pudgy Penguins Inc. is the operating and licensing entity: an SEC exhibit names "Pudgy Penguins, Inc." as licensor [S30], and the PEI suit names "Pudgy Penguins Inc." [S24]. Luca Netz is CEO. Vedant Mangaldas is chief of strategy and brand [S21]. Jennifer McGlone is reported as Chief Legal Officer [S24 coverage].

**[F] Funding.** Known equity rounds are a $9M seed led by 1kx (2023-05-09) [S8] and $11M+ led by Founders Fund (2024-07-23), which went to Cube Labs to build Abstract [S14]. No later priced round was found. The company holds 11.48% of PENGU supply and the team 17.8%, each with a 1-year cliff and then 3-year vesting from 2024-12-17 [S3]. **[I]** That treasury token is probably Igloo's largest liquid asset, so Igloo's runway is tied to PENGU's price. That is consistent with Netz's "we could have launched a token or pursued an ICO" remark about Abstract [S31].

**[F] Revenue claims.** None of these are audited.
- Netz set a 2025 target of $50M and wants an IPO "by 2027" [S34].
- CoinDesk Research, in a report **commissioned by Pudgy Penguins** [S35], cites over 1M toy units and over $13M in toy retail sales in 2024, a Walgreens presence of ~2,000 doors by June 2025, 65.1B GIPHY views, and a PENGU airdrop to over 6M wallets.
- Netz said in May 2024 that over 1M toys sold in the previous 12 months [S28].
- Orange Cap Games' Pudgy-themed Vibes TCG did ≈$6M in trailing-12-month revenue as of December 2025; that revenue is OCG's, not Igloo's [S36].

Actual 2025 revenue and profitability are **UNVERIFIED**. No filings or audited figures exist. EDGAR full-text search for "Igloo, Inc", "Pudgy Penguins" and "PENGU" (2025-06 → 2026-10) found only third-party mentions [S16].

**[F] Retrenchment in 2026.**
1. Pudgy Party was wound down in June 2026 [S27].
2. Abstract will shut on 2026-12-15 after ~18 months of funding and "8 figures" of losses. Two senior Abstract staff reportedly left in August [S31][S32].
3. The PENGU ETF rule filing was withdrawn on 2026-01-23 [S22].
4. A trademark suit has been open since March 2026. CourtListener still showed the case as not terminated on 2026-10-13 [S24].

No layoff reports were found (searched The Block, CoinDesk and general web): **UNVERIFIED either way**.

**[F] Are NFT holders' economics separate from the company's? Yes.**
- Holders have commercial rights to their own penguin. A reported cap of about $500k a year before a separate license is needed is UNVERIFIED against the official terms [S12].
- Through OverpassIP, holders can submit NFTs to a pool for licensing deals. Holders whose NFTs are selected earn a royalty, typically 5% of net revenue on physical products [S28][S12], though rates are deal-specific (one Toys deal paid 20%, with Rods multipliers).
- Corporate licensing of the brand characters (Pengu/Polly) goes to Pudgy Penguins Inc. The Rice AI license, for example, is between Rice AI and Pudgy Penguins Inc. [S30].
- **NFT holders have no equity, no pro-rata revenue share, and no claim on Igloo's PENGU treasury.**
- A figure of ">$1M royalties returned to community by mid-2025" comes from a low-quality template site and is UNVERIFIED.

**[I] Dependence score: high, but the brand would outlive the company better than most.** The NFT's value premium has come from (a) Igloo's ability to manufacture catalysts (toys, token, ETF, games) and (b) PENGU speculation. The retail brand (Pengu/Polly) is the most mainstream-penetrated PFP IP. But it is owned by the company and only loosely coupled to the 8,888 NFTs.

## 4. Tokens, airdrops, companion collections and their price effects

**PENGU facts [F]** [S3][S4]:
- Total supply 88.88B.
- Allocation: Pudgy community 25.9%; other communities 24.12%; team 17.8% (1-year cliff, 3-year vest); liquidity 12.35%; company 11.48% (1-year cliff, 3-year vest); public good 4%; "proliferation" 4% (including 3% to Binance HODLers); FTT holders 0.35%.
- Announced 2024-12-06. TGE and claims opened 2024-12-17 on Solana.
- **No snapshot:** the right to claim travelled with the NFT until it was claimed.
- The claim window was meant to be 88 days (to 2025-03-15) but was cut on 2025-01-30 to five more days, so it closed about 2025-02-04 (approximate). About 85% had been claimed by then; unclaimed tokens were burned.
- Reported per-NFT amounts: **≈1.7M PENGU per Pudgy Penguin, ≈188K per Lil Pudgy, 105K–195K per Rod.** Decrypt marks these as *estimates from a project graphic* [S3]; The Block said the split was not public [S4]. Official per-NFT figures are UNVERIFIED.

**PENGU price path [F]** (Binance PENGUUSDT daily, `token_prices_daily.csv`):

| Date | Close (USD) | Note |
|---|---|---|
| 2024-12-17 | 0.02865 | First day; intraday high 0.0700 |
| 2025-04-08 | 0.003868 | All-time-low close |
| 2025-07-27 | 0.04313 | All-time-high close |
| 2025-12-17 | 0.00942 | |
| 2026-06-30 | 0.00601 | |
| 2026-10-13 | 0.00783 | −73% vs first close, −82% vs ATH close |

Listings: Binance, OKX and Bybit at launch [S3]; Robinhood 2025-03-13 [S15]; Coinbase by December 2025 [S21].

**ETF [F].**
- Canary filed the S-1 on 2025-03-20. EDGAR shows **no amendments** for CIK 0002059693 as of 2026-10-13 [S16].
- Cboe BZX filed the 19b-4 on 2025-06-25. The SEC instituted proceedings on 2025-09-25 and extended the deadline to 2026-03-11 [S17].
- **The filing was withdrawn on 2026-01-23** [S22]. The fund would have held 80–95% PENGU and 5–15% Pudgy NFTs (secondary report). **No live PENGU ETF exists.**

**Post-TGE distributions to NFT holders:** none found (searched "second PENGU airdrop", 2025–2026). UNVERIFIED that none occurred, but no evidence of any.

**Measured airdrop effect [F data, I interpretation]:**
- Pudgy floor went from 13.74 ETH (Dec 4 bar) to 25.23 ETH (Dec 16 bar), +84% during the announcement-to-TGE window. Lil Pudgys went from 1.275 to 2.65 ETH (+108%).
- On the first bar after TGE (Dec 19), Pudgy fell to 15.08 ETH (−10.2 ETH) and Lil Pudgys to 0.915 ETH (−1.7 ETH). Lil Pudgys printed 4,187 sales in that bar.
- At the first-day close, the reported allocation was worth ≈12.5 ETH per Pudgy and ≈1.38 ETH per Lil Pudgy (1.7M × $0.02865 ÷ ETH $3,893).
- **[I]** The NFT priced in the claim and then went "ex-dividend". The drop roughly equals the airdrop value.
- A second leg followed when the claim window was shortened: Pudgy fell from 23.3 ETH (Jan 18 bar) to 9.5 ETH (Feb 5 bar). **[I]** Because there was no snapshot, unclaimed NFTs still carried PENGU until the window closed, and that residual value then vanished. The PENGU drawdown in late January 2025 and the broader market both contributed, so the attribution is approximate.

**Post-airdrop coupling [F, own calc]:**
- On 3-day bars from 2025-02-10 to 2026-10-13 (n = 203), USD-floor returns correlate 0.76 with ETH and 0.46 with PENGU.
- The ETH-denominated floor is essentially **uncorrelated (ρ ≈ 0.02) with PENGU's ETH-relative return** (Lil Pudgys: 0.09).
- **[I]** Outside episodes such as July 2025, the NFT is not a leveraged PENGU proxy. It behaves as ETH beta plus its own drift, and that drift has been steadily negative since February 2025.

**Lil Pudgys [I].** It behaves as a 2.5× larger, lower-priced version of the same bet. The Lil/Pudgy floor ratio was ~0.10 at both the peak and today. It carries extra centralized-metadata risk (§1).

## 5. Controversies & reputation

- **[F] Founder-era turmoil (2021-12 → 2022-01):** treasury and sell-out allegations, the Rods reveal, and a vote ousting the founders [S5][S6]. **[I]** The turmoil is resolved and now works as a redemption-story asset.
- **[F] Abstract (2025–2026):** Igloo raised money for an L2 that it shut within ~23 months of mainnet. Users have a short withdrawal window, and critics flagged a class-action waiver attached to migration [S31][S37]. **[I]** This is Igloo's most significant reputational hit to date. It shows strategic overreach, and Netz himself framed it as a drain on "the Pudgy Penguins business".
- **[F] PENGU treated as exit liquidity:** analysts flagged "vesting-claim-and-disperse" wallet patterns after unlocks [S26]. PENGU is down about 80–90% from its highs.
- **[F] Legal:** PEI Licensing (Original Penguin apparel) v. Pudgy Penguins Inc., filed 2026-03-04. It seeks to block Pudgy's trademark applications [S24]. **[I]** An adverse outcome would constrain apparel licensing, which is not the toy core.
- **[F] Scams:** fake Pudgy World sites were used for wallet draining [S25 related coverage]. This is a minor brand nuisance.
- **[I] Net:** Among PFP brands, Pudgy's mainstream reputation is the strongest; GIPHY views and retail doors are corroborated by multiple outlets. Its crypto-native reputation in October 2026 is weakening: Abstract has failed, the ETF is gone, Pudgy Party is shut and PENGU is down ~90%.

## 6. Community continuity through downturns (evidence)

- **[F] Survived 2022:** the floor bottomed at 0.8 ETH (2022-06-12, NPF) under new ownership and climbed to about 4 ETH by mid-2023 with no token. It is the only collection in this set that set new ETH highs after 2022 (2024–2025).
- **[F] Holder breadth now:** 5,001 owners for 8,888 tokens (56%) and 10,213 for 21,931 Lil Pudgys (OpenSea). Pudgy had 1,087 sales in 30 days, about 3× Azuki (336) and about 5× Moonbirds (231), and Lil Pudgys had 1,962 (screen_metrics). **[I]** Liquidity is the best in this group, which matters for a $7–8k buyer who may want to exit.
- **[F] Recent stress:** the floor fell 68% in ETH and 73% in BTC over one year (screen_metrics). It slid steadily from ~9.5 ETH (October 2025) to 2.35 ETH, and that slide **continued through positive brand news**: Sphere, Pudgy World, Target expansion, Pengu Card and Kung Fu Tea. The Oct 10–13, 2026 bar shows capitulation-like volume (381 sales) after the Abstract and Blur news.
- **[F] Collector support:** Adam Weitsman's 117-NFT buy (2026-10-11) "to support the collection during a difficult period" [S33]. **[I]** One whale buying is a sentiment signal, not durable demand.
- **[I]** Social and community metrics (Discord, X engagement) were not measured here. They are **unavailable** without paid tools.

## 7. Competitive threats / displacement

- **[I] Brand exposure has moved into liquid substitutes.** PENGU (a ~$0.5B market cap token on Robinhood and Coinbase) gives anyone Pudgy-brand exposure without owning an NFT. Retail Pudgy merchandise satisfies mainstream fans. The NFT's role shrinks to status and identity for crypto-native collectors.
- **[I] Mainstream character-IP competition.** Pop Mart/Labubu-style blind-box collectibles and Pokémon/One Piece TCG compete for the same consumer wallet. OCG's own goal of being a "Pop Mart of web3" [S36] shows where the money is: physical collectibles and TCGs. Those revenues accrue to companies (Igloo, OCG), not to NFT holders.
- **[I] Within NFTs.** Pudgy is no longer the "momentum" PFP. Its floor has fallen below BAYC's again since 2025-12-17 (NPF cross-check). Moonbirds and Azuki share the same token-then-dump pattern, so none of them displaces Pudgy on fundamentals.
- **[F] Infrastructure loss.** Abstract (Igloo's chain) and Blur/Blend (the main NFT-lending venue) are both closing in Q4 2026, which reduces leverage and liquidity venues.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

**[I] Partly, but at a much lower price than the brand's reach suggests.**
- **For:** the art is on IPFS, and the penguin is the most recognizable crypto mascot (GIPHY, retail, Sphere). It has a redemption story and the deepest liquidity in this set.
- **Against:**
  - The IP that consumers know (Pengu/Polly) belongs to Igloo and would end up with whoever buys Igloo's assets, not with holders.
  - Lil Pudgys metadata sits on an Igloo server.
  - The NFT's 2023–2025 premium was produced by company-run catalysts.
  - With no operator, the floor would likely trade like other orphaned "OG" PFPs. Today Cool Cats trades at 0.09 ETH, Doodles at 0.21 ETH and Azuki at 0.49 ETH (OpenSea, screen_metrics).
- **Verdict:** collector demand would survive as a niche historical PFP. The current 2.3 ETH floor implicitly assumes continued operation.
- **Founder-independence rating: low to moderate.** That conflicts with the investor's stated preference.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

**[I]** These are speculative, and none of them gives NFT holders a contractual claim.
1. An Igloo IPO or reverse merger. Netz's stated goal is 2027 [S34]; there is no filing.
2. A new PENGU ETF attempt under generic listing standards.
3. A new airdrop or reward to NFT holders. None has been announced; it would repeat the December 2024 pump-then-dump pattern.
4. Big licensing or media deals (animation, Pudgy World growth). Brand retail news has not lifted NFT floors since 2025.
5. Acquisition of Igloo.
6. Reflexive PENGU rallies. In August 2026 PENGU gained 62% on recycled IPO talk.

**Negative scheduled items:**
- Monthly PENGU team and company unlocks run until about **December 2028** (1-year cliff plus 3-year vest from 2024-12-17), right through the investor's horizon.
- Abstract closes 2026-12-15.
- The Blur/Blend wind-down deadline is 2026-11-12. Forced loan resolution could add NFT supply; the coordinator's Blend workstream should quantify Pudgy exposure.

## 10. Strongest bull and bear theses

**Bull [I]:**
- Pudgy is the only PFP whose brand penetrated mass retail: Walmart, Target, Walgreens, GIPHY and a TCG in Target.
- The company is now refocusing all resources on Pudgy after cutting Abstract and Pudgy Party.
- In BTC terms the floor sits at a cycle low (0.0695 BTC, −94% from peak), after capitulation volume, with a whale buying.
- If Igloo IPOs or relaunches growth, the NFT is the "OG membership" token with the best liquidity among PFPs. A move back to 2025's 9–10 ETH would be about 4×.

**Bear [I]:**
- Every big floor move has come from token or ETF speculation, not from cultural traction:
  - December 2024 airdrop: +84% into the event, then a dump.
  - July 2025 ETF hype.
  - Retail and mainstream news since 2025 has coincided with a 75% ETH-terms decline.
- Brand value accrues to Igloo equity and PENGU (which has ~29% insider supply unlocking through 2028), not to NFTs.
- Igloo just wrote off an L2. It lost its ETF and shut its mobile game, and its treasury is mostly a falling token.
- The airdrop has already been paid out; a second one would likely be smaller or be sold into.
- Floor bids are thin; Blend shutdown flow plus Abstract fallout may not be finished.

## 11. Sources (publisher, date; accessed 2026-10-13)

- S1 Wikipedia, "Pudgy Penguins" (rev. 2026-10-12): https://en.wikipedia.org/wiki/Pudgy_Penguins (low-weight)
- S2 CoinGecko Learn, "What Are Pudgy Penguins?" (undated): https://coingecko.com/learn/what-are-pudgy-penguins-nfts (secondary)
- S3 Decrypt, Hitchcock & Hayward, PENGU tokenomics (2024-12-13; updated 2025-01-31): https://decrypt.co/296507/pengu-pudgy-penguins-solana-token-airdrop-tokenomics
- S4 The Block Research, Arnold Toh, "Rapid Insights: The Pudgy Penguin Airdrop" (2024-12-19): https://www.theblock.co/research/institutional/rapid-insights-the-pudgy-penguin-airdrop-331611
- S5 Decrypt, Kate Irwin, "Pudgy Penguins … Sold to Netz Capital for $2.5 Million" (2022-04-03): https://decrypt.co/96786/pudgy-penguins-ethereum-nft-collection-sold-to-netz-capital-for-2-5-million
- S6 Blockmedia, "Luca Netz Acquires Pudgy Penguins…" (undated): https://www.blockmedia.co.kr/archives/707573 (secondary)
- S7 CoinDesk, Eli Tan, "Pudgy Penguins NFT Prices Surge After Creator Unveils IRL Toys" (2022-08-11): https://coindesk.com/business/2022/08/11/pudgy-penguins-announce-physical-toys-sending-nft-prices-surging/
- S8 Axios, "Pudgy Penguins raise $9M to create an IP brand" (2023-05-09): https://www.axios.com/2023/05/09/pudgy-penguins-nft-ip-brand
- S9 The Block, Yogita Khatri, "Walmart to sell Pudgy Penguins toyline in 2,000 stores" (2023-09-26): https://www.theblock.co/post/252987/walmart-pudgy-penguins-nft-toys
- S10 PR Newswire via Retail IT Insights, Target expansion (2024-05-12): https://www.retailitinsights.com/doc/pudgy-penguins-expands-pudgy-toys-to-second-major-nationwide-retailer-0001
- S11 CoinDesk, "Pudgy Penguins to Launch Webkinz-Like Virtual World in 2024" (2023-12-10): https://www.coindesk.com/tech/2023/12/10/pudgy-penguins-to-launch-webkinz-like-virtual-world-in-2024
- S12 Four Pillars, "Pudgy Penguins will inherit Disney's crown" (OverpassIP launched January 2024): https://4pillars.io/en/issues/pudgy-penguins-will-inherit-disneys-crown ; Forkast on Overpass: https://forkast.news/pudgy-penguins-licensing-nft-revenue-airdrops/ (secondary)
- S13 The Block, Khatri, Walmart expands to 3,100 stores (2024-02-21): https://www.theblock.co/post/278347/walmart-pudgy-penguins-expansion
- S14 The Block, "Founders Fund leads $11 million round for Pudgy Penguins' parent" (2024-07-23): https://www.theblock.co/news/deals/2024-07-23-peter-thiel-founders-fund-pudgy-penguins-igloo-funding-abstract-306955 ; Decrypt: https://decrypt.co/241125/pudgy-penguins-igloo-raises-11-million-ethereum-layer-2
- S15 Cointelegraph, "Robinhood lists PENGU, POPCAT…" (2025-03-13): https://cointelegraph.com/news/robinhood-lists-pengu-popcat-memecoins-crypto-ramp-up
- S16 SEC EDGAR: Canary PENGU ETF S-1 (2025-03-20), CIK 0002059693 submissions (only the S-1): https://data.sec.gov/submissions/CIK0002059693.json ; EDGAR full-text search API (queried 2026-10-13)
- S17 Federal Register notices for SR-CboeBZX-2025-081: 2025-07-14 (filing), 2025-08-28, 2025-09-30 (proceedings), 2026-01-12 (extension to 2026-03-11): https://www.federalregister.gov/api/v1/documents.json?conditions[term]=%22PENGU%22
- S18 Decrypt, Vismaya V, "PENGU doubles in a week amid ETF hype" (2025-07-15): https://decrypt.co/330150/pudgy-penguins-pengu-token-doubles-in-a-week-amid-etf-hype
- S19 Decrypt, "Pudgy Party launches on iOS and Android" (2025-08-29): https://decrypt.co/337273/pudgy-penguins-game-pudgy-party-launches-on-ios-and-android
- S20 CoinDesk, "$16B in longs liquidated…" (2025-10-10): https://www.coindesk.com/markets/2025/10/10/usd16b-in-longs-liquidated-as-wall-street-sell-off-extends-btc-eth-broader-crypto-market-meltdown
- S21 CoinDesk, Helene Braun, "Pudgy Penguins takes over Las Vegas Sphere" (2025-12-13): https://www.coindesk.com/tech/2025/12/12/nft-project-pudgy-penguins-takes-over-las-vegas-sphere-in-holiday-campaign
- S22 SEC, Release 34-104070, page marked "(WITHDRAWN 01/23/2026)": https://www.sec.gov/rule-release/34-104070
- S23 CoinDesk (mentions the Pengu Card with Visa; see S26). Announcement date of 2026-02-11/12 is from aggregator coverage (MEXC news) and is weakly sourced.
- S24 CourtListener docket, PEI Licensing, LLC v. Pudgy Penguins Inc., S.D. Fla. 1:26-cv-21458, filed 2026-03-04, trademark (15:1114): https://www.courtlistener.com/docket/72364956/pei-licensing-llc-v-pudgy-penguins-inc/ ; Invezz coverage (2026-03-06)
- S25 CoinDesk, Shaurya Malwa, "Pudgy Penguins launches its Club Penguin moment" (2026-03-10): https://www.coindesk.com/tech/2026/03/10/pudgy-penguins-launches-its-club-penguin-moment-and-the-game-doesn-t-feel-like-crypto-at-all ; Decrypt on the fake game: https://decrypt.co/361574/pudgy-penguins-launched-a-new-game-crypto-scammers-made-a-fake-version
- S26 CoinDesk, Ashraf & Reynolds, "Pudgy Penguins rally coincides with token unlock…" (2026-04-27): https://www.coindesk.com/markets/2026/04/27/pudgy-penguins-rally-coincides-with-token-unlock-as-analyst-flags-exit-liquidity-risk
- S27 Cointelegraph, Reguerra, "Pudgy Penguins winds down Pudgy Party…" (2026-06-15): https://cointelegraph.com/news/pudgy-penguins-winds-down-pudgy-party-mobile-game
- S28 Cointelegraph, Reguerra, "Pudgy Penguins … Target Card Launch" (2026-06-20): https://cointelegraph.com/news/pudgy-penguins-expands-retail-footprint-with-target-trading-card-rollout
- S29 Crypto Briefing, "PENGU token jumps 62% on IPO speculation" (2026-08-24): https://cryptobriefing.com/pengu-token-jumps-62-percent-ipo-speculation/ (secondary)
- S30 SEC EDGAR, Mint Inc. Ltd 6-K Exhibit 99.1, Rice AI license with Pudgy Penguins, Inc. (2026-09-15): https://www.sec.gov/Archives/edgar/data/1998560/000121390026099901/ea030552101ex99-1.htm ; Bullish 6-K Ex. 99.1, multi-year agreement with Igloo Inc. (2025-09-17): https://www.sec.gov/Archives/edgar/data/1872195/000110465925090870/tm2525633d1_ex99-1.htm
- S31 The Block, Jason Shubnell, "Abstract to shut down after losing 'tens of millions'" (2026-10-06): https://www.theblock.co/news/ecosystems/2026-10-06-abstract-ethereum-layer-2-shutting-down-pudgy-penguins-igloo-417855
- S32 CoinDesk, Shaurya Malwa, "Abstract becomes second Ethereum layer 2 to shut in a week" (2026-10-07): https://www.coindesk.com/tech/2026/10/07/pudgy-penguins-abstract-becomes-second-ethereum-layer-2-to-shut-in-a-week ; BlockchainGamerBiz (2026-10-07): https://www.blockchaingamer.biz/news/43020/abstract-shutting-down/
- S33 crypto.news, Olivia Stephanie, "Pudgy Penguins gets support as billionaire buys 117 NFTs" (2026-10-13): https://crypto.news/pudgy-penguins-gets-support-as-billionaire-buys-117-nfts/
- S34 Phemex news / CoinDesk Research on the $50M target and IPO by 2027 (2025): https://phemex.com/news/article/pudgy-penguins-targets-50-million-revenue-eyes-ipo-by-2027-16063 (aggregator; flagged)
- S35 CoinDesk Research, "Pudgy Penguins: A New Blueprint for Tokenized Culture" (2025-12-30; **commissioned by Pudgy Penguins**): https://www.coindesk.com/research/pudgy-penguins-a-new-blueprint-for-tokenized-culture
- S36 Crypto Briefing, "Moonbirds to launch BIRB token in early Q1 2026" (2025-12-14; Vibes ≈$6M trailing-12-month revenue, "Pop Mart of web3"): https://cryptobriefing.com/moonbirds-birb-token-launch/
- S37 Protos, "Pudgy Penguins parent firm shuts down its own blockchain" (2026-10): https://protos.com/pudgy-penguins-parent-firm-shuts-down-its-own-blockchain/
- Data: `data/processed/npf_series/pudgy-penguins.csv`, `lil-pudgys.csv`, `bored-ape-yacht-club.csv` (NFTPriceFloor); `data/processed/token_prices_daily.csv` (Binance PENGUUSDT, written by `scripts/fetch_token_klines.py`); `data/processed/screen_metrics.csv` (OpenSea).
