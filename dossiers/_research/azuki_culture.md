# Azuki: cultural durability and catalyst history

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[I]** = interpretation or inference by this workstream; **UNVERIFIED** = could not confirm. Dated events are in `data/processed/catalysts/azuki.csv`._
_Investor context: owns one Azuki and may replace it._

**Snapshot (2026-10-13):**
- **Price.** Floor is 0.49 ETH (OpenSea), about $1,229 or 0.0147 BTC.
  - This is the lowest value in the NFTPriceFloor 3-day series that starts in May 2022.
  - The floor is 97.8% below the series maximum of 22.69 ETH (2022-05-07 bar) and 99.1% below in BTC terms. The true peak of April 2022 is before the series starts and is UNVERIFIED.
  - Over one year the floor fell 65% in ETH and 71% in BTC. Over two years it fell 90% in ETH (screen_metrics).
- **Holders and activity.** OpenSea counts 4,354 owners for 10,000 tokens and 336 sales in the last 30 days.
- **ANIME token.** Closed at $0.00303 on Binance on 2026-10-13, 96.6% below its first-day close.

---

## 1. Identity & provenance

- **[F] Contract and mint.** The contract is `0xed5af388653567af2f388e6224dc7c4b3241c544`, with a supply of 10,000.
  - It was created 2022-01-10 05:19 UTC (block 13,975,838). The first mint was 2022-01-12 04:17 UTC (block 13,988,541), confirmed on-chain using the method in pudgy_culture.md §1.
  - 8,700 tokens went in a public Dutch auction. It started at 1 ETH and sold out within about 3–4 minutes at 1 ETH [S1].
- **[F] Creator.** Chiru Labs (Los Angeles) made Azuki. The pseudonymous founder Zagabond is Alex Q. Xu, who now calls himself "CEO of Azuki Labs" [S2]. The operating entity now appears in trade press as "Azuki Labs, Inc." [S3]. **[I]** Chiru Labs appears to have rebranded as Azuki Labs; no formal announcement of the rename was found.
- **[F] Companion collections.**
  - **BEANZ** (`0x306b1ea3…f949`, 19,950): created and first minted on-chain on 2022-03-31 at 05:29 and 05:32 UTC, airdropped to Azuki holders.
  - **Azuki Elementals** (`0xb6a37b5d…786e`): first mint on-chain 2023-06-27 18:39 UTC. 20,000 were issued: 10,000 sold and 10,000 airdropped [S8]. Blockscout now reports a total supply of 17,766; the reason for the lower figure is UNVERIFIED.
  - Bobu (a fractionalized Azuki) and the Golden Skateboard also exist; both were eligible for ANIME [S11].
- **[F] Metadata.** On-chain `tokenURI(1)` returns `ipfs://QmZcH4…/1`, and `owner()` is `0x2ae6b0630ebb4d155c6e04fcb16840ffa77760aa` (queried 2026-10-13 ~22:00 UTC, Tenderly RPC). **[I]** The art survives on IPFS without the company, as long as someone pins it. Whether the metadata is frozen is UNVERIFIED.
- **[F] Holder IP rights.** Azuki's founders said the NFTs embed commercial rights [S4]. The license text at azuki.com/license was **not retrieved**, so any revenue cap is UNVERIFIED.

## 2. Narrative timeline (condensed)

| Date | Event | Floor context (NPF 3-day bars) |
|---|---|---|
| 2022-01-12 | Mint, 1 ETH, sold out in minutes [S1] | n/a (series starts May 2022) |
| 2022-03-31 | BEANZ airdrop, 19,950 (on-chain) | n/a |
| 2022-05-09/10 | Zagabond admits he was behind abandoned projects (CryptoPhunks, Tendies, CryptoZunks): "no product-market fit" [S5] | ~19 → 10.9 ETH (Decrypt). NPF: 22.69 (05-07) → 6.99 (05-13). The Terra/LUNA crash hit the same week |
| 2022-09 | Reported $30M Series A at a $300–400M valuation [S6] | Never confirmed by the company. UNVERIFIED that it closed |
| 2023-06-27 | **Elementals mint.** 10,000 sold at 2 ETH (Dutch auction) to Azuki/BEANZ holders within ~15 minutes, raising ~20,000 ETH (~$38M), and 10,000 airdropped to Azuki holders. Art seen as diluting the originals [S7][S8] | 17 → 6 ETH (The Block). NPF: 16.25 (06-22) → 5.32 (07-04) |
| 2023-06-28/29 | Azuki statement: "This time, we missed the mark" [S9] | Exact date UNVERIFIED (Blockworks returned 403) |
| 2024-03 | Animecoin Foundation and Azuki choose Arbitrum for AnimeChain [S10] | ~3.7 ETH |
| 2024-04-30 | *Enter the Garden* ep. 1 (with Dentsu; producer Goro Taniguchi) on YouTube [S12] | ~4.2 ETH |
| 2024-09 | Anime.com waitlist opens [S13] | ~4.7 ETH |
| 2025-01-13 | ANIME token announced [S10] | +9% to 13.67 ETH (NPF ~12 ETH) |
| 2025-01-23 | **ANIME TGE** on Ethereum and Arbitrum. 37.5% of 10B to the Azuki community via "Collector's Status". Upbit lists it the same day; Binance, OKX and Bybit too [S11][S14] | 12.2 (01-15) → 9.93 (01-21) → **4.70 (01-24)** → **2.75 (01-30)** |
| 2025-02-27 | *Enter the Garden* ep. 2 premieres on Anime.com [S12] | ~2.8 ETH |
| 2025-03-09 | ANIME claim window (45 days) closes; unclaimed tokens go back to the community pool [S11] | ~2.6 ETH |
| 2025-03-27 → 04-03 | Holder-only "Alpha Starter Decks" sale ($95 in ANIME, limited by status tier) [S15] | ~2.5 ETH |
| 2025-07-01 | **Studio Azuki** joint venture (COMISMA, Xenotoon) plus strategic partnership with Will and Jada Pinkett Smith's Westbrook [S16] | ~1.9 ETH |
| 2025-10-10 | Market-wide liquidation crash | 1.46 (09-30) → 0.84 (11-05) |
| 2026-01-21 | Zagabond's 2026 roadmap: "Azuki is an IP company"; manga and TCG are the core [S17] | 0.74 → 0.77 ETH |
| 2026-01-23 | ANIME team and company 1-year cliffs end (derived from [S11]) | ~0.7 ETH |
| 2026-02 | Paris Fashion Week: 424 × Azuki, plus an H. Moser piece (per zagabond.com news list; weak) | ~0.7 ETH |
| 2026-06-17 | AZUKI manga announced (Arnold Tsang, ex-Overwatch character art director); Anime Expo July 2–5; free on Azuki.com from 2026-09-17 [S18] | ~0.75–0.83 ETH |
| 2026-06-26 | **Azuki TCG "Gates Awakened"** launches at US retail: >$1M pre-sale, 800k packs [S19] | ~0.83 ETH |
| 2026-09-30 | Second TCG set "Fractured Domains" announced for 2026-11-20. Organized play: Nationals 2027, Worlds 2028 [S3] | ~0.64 ETH |
| 2026-10-12/13 | Blur/Blend wind-down announced (per STATE.md). Floor at series low | **0.49 ETH** |

## 3. Founder/team dependence and company status (Oct 2026)

- **[F] Leadership.** Zagabond (Alex Xu) remains CEO [S2]. Pseudonymous co-founder "location tba" was quoted on the ANIME claim in 2025 [S14]. No departures or layoffs were found (searched The Block, CoinDesk and general web for "Azuki Labs/Chiru Labs layoffs 2025–2026"): **UNVERIFIED either way**.
- **[F] The company is actively shipping in 2026:**
  - A physical TCG with retail distribution and an organized-play ladder to 2028 [S3][S19].
  - An original manga [S18].
  - Studio Azuki (anime) [S16].
  - Fashion collaborations.
- **[F] Funding and treasury.**
  - Elementals primary sales brought in about 20,000 ETH in 2023 [S8].
  - The company holds 7.44% of ANIME, and team/advisors hold 15.62%, with a 1-year cliff and then 3-year vesting from 2025-01-23. That unlock runs to about January 2029 [S11].
  - The Animecoin Foundation holds 24.44%, unlocked at launch [S11].
  - No disclosed revenue figures exist beyond the TCG's ">$1M pre-sale" [S19].
- **[I] Business direction.** The company has moved from an NFT-first brand to a TCG, manga and anime IP company (Zagabond: "Azuki is an IP company, with the TCG being one of the core products"). The TCG and manga are free or for sale to the general public. Holder perks were limited to things like priority access to starter decks [S15].
- **[I] Holder economics.** No mechanism routes TCG or anime revenue to NFT holders. The NFT's tie to company success is reputational and optional: future perks or airdrops.

## 4. Tokens, airdrops, companion collections and their price effects

**[F] BEANZ (March 2022).** A free airdrop. Its effect cannot be measured because the NPF series starts in May 2022.

**[F] Elementals (June 2023)** was the defining dilution event:
- 10,000 new PFPs went to existing holders, plus 10,000 sold at 2 ETH. **[I]** Effectively a ~$38M raise from the community, in a style close to the original art.
- Azuki's floor fell from about 16.25 to 5.32 ETH (−67%) within about 12 days, with 2,500 sales in one bar.
- The Elementals themselves opened at 1.6 ETH and fell to 0.84 ETH, below the 2 ETH mint price [S7].

**[F] ANIME (January 2025):**
- Supply 10B; about 77% circulating at TGE.
- Allocation:

| Bucket | Share | Vesting |
|---|---|---|
| Azuki community (Azuki, Elementals, BEANZ, Bobu, Golden Skateboard) | 37.5% | Fully unlocked |
| Animecoin Foundation | 24.44% | Unlocked at launch |
| Team and advisors | 15.62% | 1-year cliff, then 3-year vest |
| Community cultivation (AnimeDAO) | 13% | n/a |
| Azuki company | 7.44% | 1-year cliff, then 3-year vest |
| Partner communities | 2% | n/a |

- Allocation was **per NFT**, weighted by "Collector's Status", a points system based on holding time and rarity [S11][S14].
- **The per-Azuki amount is UNVERIFIED.** No outlet published it. Tried Decrypt, The Defiant, NFT Evening and NiftyNoon.
- Binance first-day close was $0.0887 and the intraday high $0.107 (Binance); The Block cites an all-time high of $0.1861 on another venue [S14].
- The community pool was worth ≈$333M at the first close (3.75B × $0.0887), against an FDV of just under $1B [S20].
- Path (Binance closes): $0.0170 on 2025-03-31, $0.0182 on 2025-07-28, $0.0053 on 2025-12-17, an all-time-low close of $0.00237 on 2026-08-18, and $0.00303 on 2026-10-13.

**[F data, I interpretation] Measured effect:**
- Announcement: +9% (1 day) [S10].
- Across the TGE, the floor fell from 12.2 ETH (Jan 15 bar) to 2.75 ETH (Jan 30 bar), −77%, with 2,150 sales in the Jan 24 bar.
- **[I]** As with PENGU, the claim was tied to the NFT, so the floor priced in the expected allocation and collapsed once it was claimed. Unlike Pudgy, Azuki **never recovered**. It kept falling every quarter afterward: 2.2 ETH in March 2025, 1.46 ETH in September 2025, 0.84 ETH in November 2025, and 0.49 ETH now.
- 3-day-bar correlation from March 2025 to October 2026 (n = 192):
  - USD-floor returns versus ANIME returns: 0.45.
  - USD-floor returns versus ETH: 0.74.
  - ETH-denominated floor versus ANIME's ETH-relative return: about 0.04.
- **[I]** After the airdrop, the NFT does not trade as an ANIME proxy.

**[F] Post-TGE distributions to Azuki holders:** none identified. Holder-only purchase rights for the TCG starter decks were the only holder-gated item found [S15].

## 5. Controversies & reputation

- **[F] 2022, serial-founder disclosure.** Zagabond admitted to three earlier projects he abandoned or wound down, and the floor fell about 43% on the news [S5]. He later pledged to hand contract control to those communities (secondary sources).
- **[F] 2023, the Elementals mint.** The sale was effectively holder-only and raised ~$38M. The art was criticised as too similar to the originals and the floor collapsed. The team admitted "we missed the mark" [S7][S8][S9].
- **[F] 2025, ANIME.** The FDV launched below Hyperliquid pre-market expectations [S20]. The token is down about 97% since. **[I]** Many holders associate the token with value extraction.
- **[I] Net reputation.** For crypto-native collectors, Azuki now has the weakest "trust" record of the three brands: two value-extracting events plus a disappointing token. Its *art* reputation is still strong; the anime-PFP aesthetic was widely imitated. Its mainstream anime/TCG reputation is being built separately, under the "Azuki" name, by the company.

## 6. Community continuity through downturns (evidence)

- **[F] Recovered after 2022, but did not survive 2025.** After the 2022 controversy the floor recovered to about 17 ETH by June 2023. It then had three step-down events (Elementals, the ANIME TGE, and October 2025) with no recovery after the last two.
- **[F] Breadth and liquidity today.**

| Metric (OpenSea / NPF) | Azuki | Pudgy Penguins |
|---|---|---|
| Owners per supply | 0.435 | 0.56 |
| Sales, last 30 days | 336 | 1,087 |
| Sales, last 365 days (NPF) | 5,121 | 6,695 |

  NPF's 3-day sales counts in 2026 often run in the teens to twenties.
- **[F] The floor kept falling while the company executed:**
  - TCG retail launch (2026-06-26): ~0.83 → ~0.68 ETH by September.
  - Manga (2026-09-17 public): no visible lift.
  - **[I]** This is the strongest evidence that company execution is *not* currently reaching NFT demand.
- **[I]** Discord and social metrics: **unavailable** (no paid tools).

## 7. Competitive threats / displacement

- **[I] Azuki's own cheaper editions.** Elementals and BEANZ give cheaper exposure to the same aesthetic, and Elementals in particular diluted the "Azuki look".
- **[I] Free and non-NFT channels.** The company's own TCG, manga and anime carry the Azuki name to fans with no NFT involved. The NFT is no longer the gateway to the IP. ANIME is the liquid, crypto-native proxy for the "anime + crypto" narrative.
- **[I] Other anime-styled and culture collections.** Milady-sphere and Pudgy compete for the same "culture" bid, and Pudgy has far better liquidity.
- **[I] Mainstream TCG incumbents.** Pokémon, One Piece and Lorcana. Azuki's TCG may fail commercially. If it succeeds, its value goes to the company.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?" (the investor's key question)

**[I] Some demand would remain, but evidence suggests the current bid is already mostly "orphan-PFP" demand plus a small option on company largesse.**

- **Arguments for residual demand:**
  - The art is on IPFS.
  - Azuki was a top-3 PFP in 2022, and its aesthetic is culturally recognised.
  - About 4,350 owners remain.
  - The brand name will keep circulating through any surviving TCG, manga or anime, even if the company is sold.
- **Arguments against:**
  1. The NFT has fallen 96% from its January 2025 level even while the team executed. Execution supports the *company*, not the floor.
  2. The two largest holder "events" (Elementals and ANIME) were monetization or distribution events, and both were followed by permanent re-ratings lower.
  3. Liquidity is thin. A $1–1.5k holding is fine to keep, but the market cannot absorb larger exits without moving the price.
  4. With no team, the "airdrop optionality" part of the bid would disappear.
- **Founder-independence: low.** It is also low for the opposite reason to Pudgy: the company is executing, but not *for* NFT holders.
- **Decision note (not a recommendation).** At 0.49 ETH (≈0.0147 BTC) the position is small. Selling realises a loss near the series low. Keeping it is mostly a bet that the company issues more holder-tied value: TCG perks, a future token, or IP-linked rewards. That is a manufactured-catalyst thesis, not a cultural-durability one.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

**[I]** These are speculative.
- Holder-gated TCG products or promos around "Fractured Domains" (2026-11-20) and the 2027 Nationals.
- An anime series greenlit through Studio Azuki and Westbrook. Nothing specific has been announced [S16].
- A further ANIME or other token distribution to NFT holders. The Community Cultivation pool (13%) and reclaimed unclaimed tokens are a possible source; nothing is announced.
- A corporate sale or partnership of Azuki Labs.

**Negative scheduled items:**
- ANIME team and company vesting continues to about January 2029.
- The Blur/Blend wind-down on 2026-11-12. Azuki loan exposure is for the coordinator's Blend workstream.

## 10. Strongest bull and bear theses

**Bull [I]:**
- The company is one of the few NFT-born brands shipping real non-crypto products: a retail TCG with an organized-play roadmap to 2028, a manga by a recognized artist, an anime studio JV backed by Westbrook, and Paris fashion collaborations.
- The floor sits at an all-time low of 0.49 ETH, about $1.2k. If the TCG or anime becomes a hit and the company chooses to reward OG holders, a small Azuki is cheap optionality.
- Art quality and 2022 cultural status provide some floor.

**Bear [I]:**
- Holders have repeatedly funded or absorbed the company's monetization (Elementals ~$38M; ANIME, where the team and company took 23% plus the Foundation's 24%) and then suffered permanent re-ratings.
- The IP strategy deliberately bypasses the NFT.
- Liquidity is thin, the trend has been negative quarter after quarter, and ANIME is down 97% with insider unlocks through 2029.
- In BTC terms the floor is down 99% from its 2022 high, with no sign of a base.
- Of the three brands, Azuki has the most founder-dependent upside and the least evidence that execution helps holders.

## 11. Sources (publisher, date; accessed 2026-10-13)

- S1 NFT Now, "The ultimate guide to Azuki NFTs" (undated): https://nftnow.com/guides/the-ultimate-guide-to-azuki-nfts-everything-you-need-to-know/ ; DappRadar blog: https://dappradar.com/blog/azuki-nfts (secondary)
- S2 zagabond.com, personal site of Alex Q. Xu ("CEO of Azuki Labs"; no post dates): https://www.zagabond.com/
- S3 ICv2, Milton Griepp, "Azuki Labs Announces Second Azuki TCG Set" (2026-10-02): https://icv2.com/articles/news/view/63522/azuki-labs-announces-second-azuki-tcg-set
- S4 Forbes Japan interview with Chris Xu (date not captured): https://forbesjapan.com/articles/detail/45891 (via search snippet)
- S5 Decrypt, Kate Irwin, "Twitter Declares 'Death' of Azuki NFT Collection Following 45% Price Drop" (2022-05-10): https://decrypt.co/99869/twitter-declares-death-azuki-nft-collection-following-price-drop
- S6 The Block, "Azuki creator closes in on $30 million fundraise: sources" (2022-09): https://www.theblock.co/post/171617/chiru-labs-azuki-creator-30-million-series-a-fundraise
- S7 The Block, Tim Copeland, "Azuki floor price crumbles, with holders down $21,500 per NFT" (2023-07-03): https://www.theblock.co/post/237484/azuki-floor-price-crumbles-with-holders-down-21500-per-nft
- S8 Decrypt, Andrew Hayward, "Azuki Elementals NFT Drop Yields $38 Million in Just 15 Minutes" (2023-06-27): https://decrypt.co/146426/azuki-elementals-nft-drop-yields-38-million-in-just-15-minutes ; The Block (2023-06-27): https://www.theblock.co/post/236681/azuki-nft-collections-ends-elemental-mint-with-37-5-million-before-it-was-ever-open-to-the-public
- S9 Blockworks, "Azuki admits it 'missed the mark' on Elementals mint" (late June 2023; page returned 403, quote via search snippet): https://blockworks.com/news/azuki-missed-the-mark-on-elementals
- S10 Decrypt, Logan Hitchcock, "Azuki-Linked ANIME Token Launching on Ethereum This Month" (2025-01-13): https://decrypt.co/300647/azuki-linked-anime-token-ethereum
- S11 Decrypt, Hitchcock, "ANIME: Everything You Need to Know…" (2025-01-16; updated 2025-01-23): https://decrypt.co/301080/anime-azuki-ethereum-token-airdrop-tokenomics
- S12 Anitrendz, "Enter The Garden … 'The Waiting Man' on April 30" (2024-04-11): https://www.anitrendz.com/news/2024/04/11/enter-the-garden-anime-anthology-series-launches-1st-part-the-waiting-man-on-april-30 ; Dentsu press release: https://www.dentsu.com/news-releases/dentsu-partners-with-azuki-to-create-three-part-anime-series ; episode 2 per Anitrendz (2024-10-22 teaser) and search snippet
- S13 The Block, "Arbitrum, Azuki-backed Animecoin unveils tokenomics" (Jan 2025; Anime.com waitlist Sept 2024 per summary): https://www.theblock.co/post/334203/arbitrum-azuki-backed-animecoin-unveils-tokenomics
- S14 The Block, "Azuki's ANIME token surpasses $350 million market capitalization one day after launch" (2025-01-24): https://www.theblock.co/post/336746/azukis-anime-token-surpasses-350-million-market-capitalization-one-day-after-launch ; The Defiant on the claim going live: https://thedefiant.io/news/nfts-and-web3/azuki-linked-animecoin-airdrop-goes-live
- S15 Blockworks, "Azuki's upcoming game gets pricey card packs" (late March 2025): https://blockworks.co/news/azuki-trading-card-game-packs-nft
- S16 Cartoon Brew, Jamie Lang, "New Anime Studio Azuki Partners With … Westbrook" (2025-07-03): https://www.cartoonbrew.com/anime/will-smith-jada-pinkett-smith-westbrook-inc-studio-azuki-248220.html ; Anitrendz (2025-07-02): https://www.anitrendz.com/news/2025/07/02/web3-company-azuki-sets-up-us-anime-studio-with-comisma-and-xenotoon
- S17 Inside Bitcoins, Dominic Kimani, "NFT Firm Azuki Releases Its 2026 Roadmap, Including A Manga" (2026-01-22): https://insidebitcoins.com/news/nft-firm-azuki-unveils-its-2026-roadmap-including-a-manga (secondary; cites Zagabond's blog of 2026-01-21)
- S18 Press release via AI Journal, "Former Overwatch Character Art Director Arnold Tsang Unveils AZUKI" (2026-06-17), and the 2026-09-08 launch release: https://aijourn.com/former-overwatch-character-art-director-arnold-tsang-unveils-azuki-a-new-original-manga-series/
- S19 CardGamer, Jason Brown, "Gates Awakened, First Set For TCG Azuki, Heads To Retail" (2026-06-22): https://cardgamer.com/games/tcgs/gates-awakened-first-set-for-tcg-azuki-heads-to-retail/
- S20 NiftyNoon, "Azuki's $ANIME Coin is Finally Here" (2025-01-23): https://niftynoon.substack.com/p/niftynoon-azukis-anime-coin-is-finally
- Data: `data/processed/npf_series/azuki.csv` (NFTPriceFloor); `data/processed/token_prices_daily.csv` (Binance ANIMEUSDT, from `scripts/fetch_token_klines.py`); `data/processed/screen_metrics.csv` (OpenSea); on-chain contract creation, first-mint and tokenURI checks via the Tenderly public RPC (2026-10-13).
