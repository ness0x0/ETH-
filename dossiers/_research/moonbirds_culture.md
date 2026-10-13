# Moonbirds: cultural durability and catalyst history (lighter coverage)

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[I]** = interpretation or inference by this workstream; **UNVERIFIED** = could not confirm. Dated events are in `data/processed/catalysts/moonbirds.csv`._

**Snapshot (2026-10-13):** The floor is 0.449 ETH (OpenSea), ≈$1,126 or 0.0135 BTC. That is 98.3% below the NPF peak of 25.99 ETH (2022-07-09 bar) and 99.3% below the BTC-terms peak of 1.83 BTC (2022-07-18). The floor fell 83% in ETH over one year, but over two years it is up 52% in ETH (from 0.295) and 17% in BTC. OpenSea counts 3,341 owners for 9,999 tokens and 231 sales in 30 days (screen_metrics). BIRB, the token, traded at ≈$0.056 on 2026-10-13, giving a market cap of ≈$15.9M and an FDV of ≈$55.8M (CoinGecko page) [S12].

---

## 1. Identity & provenance

- **[F] Contract and mint.** The contract is `0x23581767a106ae21c074b2276d25e5c3e136a68b`, supply 10,000. It was created 2022-04-15 16:38 UTC (block 14,591,056), and the first mint followed at 17:27 UTC (block 14,591,282), on-chain.
  - The public raffle mint was 2022-04-16 at 2.5 ETH. 2,000 tokens went to holders of the PROOF Collective pass, 7,875 to the public, and 125 were reserved [S1].
  - The creator was PROOF (Kevin Rose and team). Moonbirds and its sister collections, Oddities and Mythics, form one ecosystem.
- **[F] The art is fully on-chain.** `tokenURI(1)` returns a `data:application/json` payload with an embedded base64 BMP image. Only the "alternate_image" and "animation_url" point to `proof.xyz` (queried 2026-10-13 ~22:00 UTC, Tenderly RPC). `owner()` is `0x80d154d71f2e1400311c539ef5d08710bd37d044`.
- **[F] CC0 since 2022-08-04.** Kevin Rose moved Moonbirds and Oddities to a Creative Commons Zero license, which ended holders' exclusive commercial rights [S2][S3].
- **[F] Owners of the IP over time:**

| Period | Owner | Source |
|---|---|---|
| 2022-04 → 2024-02 | PROOF | |
| 2024-02-16 → 2025-05-30 | Yuga Labs (reportedly an all-stock deal) | [S4] |
| 2025-05-30 → now | Orange Cap Games (OCG), CEO Spencer Gordon-Sand | [S5] |

## 2. Narrative timeline

| Date | Event | Floor (NPF 3-day bars) |
|---|---|---|
| 2022-04-15/16 | Mint at 2.5 ETH [S1] | ~17–21 ETH in May 2022 |
| 2022-07-09/18 | Peak, 25.99 ETH / 1.83 BTC | |
| 2022-08-04 | CC0 switch; holders call it a "bait and switch"; a Moonbirds DAO for trademark licensing is promised [S2][S3] | 17.5 (08-02) → 15.0 (08-08) → 10.0 ETH (08-20) |
| 2023-07-19 | Mythics launched: holders nest Moonbirds or burn Oddities; reveals run ≥200 days [S6] | 1.54 ETH (NPF). Decrypt's "well below 1 ETH by mid-2023" [S7] conflicts with NPF, which first shows the floor below 1 ETH in March 2024 |
| 2024-02-16 | Yuga Labs acquires PROOF; Rose becomes an advisor [S4] | 1.07 → 1.77 (02-23) → 0.86 ETH (03-09) |
| 2024-08-06 | **Series low, 0.21 ETH**, during Yuga's dormant period | |
| 2025-05-30 | OCG buys the Moonbirds, Mythics and Oddities IP; terms undisclosed [S5] | 0.30 → 0.74 ETH (06-05) |
| ~2025-06 | OCG closes a $3.5M seed led by 1kx and Yuga Labs [S8] | Page dates conflict (2025-06-09 vs 2026-06-06) |
| 2025-07 → 08 | OCG revives the community, pushes the "birb" meme, Beeple post; ETH rallies [S7] | 0.57 (07-14) → 3.15 ETH (08-25) |
| 2025-10-01/02 | BIRB token announced on Solana at the "Birbhalla" side event of Token2049 [S9] | Decrypt: 4 ETH; NPF 2.65 → 3.0 ETH |
| 2025-10-10 | Market-wide liquidation crash | 3.0 → 2.3 ETH |
| 2025-12 (Breakpoint) | OCG confirms BIRB for Q1 2026; "Pop Mart of web3" ambition; Moonbirds to join Vibes TCG [S10] | ~1.24–1.7 ETH |
| 2026-01-27 | BIRB tokenomics published [S11] | Floor drops >30% [S11] |
| 2026-01-28 | **BIRB TGE on Solana** (~$200M FDV) plus Nesting 2.0: NFT holders' BIRB vests monthly over 24 months [S11][S13] | 2.0 (01-25) → **0.77 ETH (01-31)**, −62% |
| 2026-06-18/20 | Vibes TCG Set 3 "Birb & Pengu" launches worldwide; Target rollout [S14] | ~0.68 ETH |
| 2026-10-12/13 | Blur/Blend wind-down announced (per STATE.md) | 0.39–0.45 ETH |

## 3. Founder/team dependence and company status (Oct 2026)

- **[F] OCG profile.** OCG is a young TCG and collectibles company. Its Vibes TCG launched in December 2024 on Pudgy Penguins IP and runs on Abstract [S5][S8]. OCG claims:
  - 4M+ Vibes cards sold across 100+ retailers (June 2026 press release, via search snippet).
  - Vibes revenue of ≈$6M over the trailing 12 months, ≈$8M expected for 2025 and ≈$20M for 2026, as of December 2025 [S10].
  - Distribution partnerships with GTS and Star City Games.
  - **None of these figures are audited.**
- **[I] Dependence on Pudgy and Abstract.** OCG's main business, Vibes, is built on Pudgy Penguins IP and on Igloo's Abstract chain, which shuts on 2026-12-15. How Vibes' on-chain parts will migrate is **UNVERIFIED** (searched; nothing found). Moonbirds' new owner therefore depends partly on Igloo's choices.
- **[F] Kevin Rose** has had no operating role since February 2024 [S4].
- **[I] Dependence score: medium.** The art is on-chain and CC0, so it needs no operator. The 2025 revival, however, was driven entirely by OCG's community work and token. Holders' BIRB vesting through about January 2028 needs OCG's contracts and Solana claim infrastructure to keep working.

## 4. Tokens, airdrops, companion collections and their price effects

**[F] BIRB tokenomics** [S11]:
- Supply 1B.
- 65% "community": 27% holder rewards, 12% ecosystem partners, 10% value-chain incentives, 8% liquidity, 8% "innovation" reserve.
- 10% team; 25% investors and advisors.
- Some outlets put the NFT holders' share at "~25%" [S11b]. The exact NFT-holder share and per-NFT amounts are **UNVERIFIED**; no official per-Moonbird figure was found.

**[F] Distribution mechanism.** Under "Nesting 2.0", nested Moonbirds, Mythics and Oddities each receive a soulbound token (SBT) at launch. BIRB then unlocks monthly on the 28th for 24 months, which runs to about January 2028 [S13]. Holders criticised the small community share and the long vesting [S11].

**[F] BIRB price.**
- CoinGecko page on 2026-10-13: $0.0559, ATH $0.4769 (no date shown), ATL $0.045, circulating ≈285–290M [S12].
- A Coinbase page snapshot dated 2026-02-26 instead showed an ATH of $0.17 on 2026-02-25.
- **The ATH figure and date conflict; UNVERIFIED.**
- Either way, BIRB is down about 67–88% from its highs.
- Binance does not list BIRB. Venues include Coinbase, Bybit, Bitget and Gate.
- A machine-readable price history could not be pulled: CoinGecko's API throttled and Bybit's API is geo-blocked.

**[F data, I interpretation] Measured effects:**

| Event | Floor move | Note |
|---|---|---|
| OCG acquisition | ×2.5 within a week (0.30 → 0.74 ETH) | |
| Meme/revival period | ×4 more by late August 2025 (→ 3.15 ETH) | |
| Token announcement | ≈+10–20% | Confounded by the Oct 10 crash a week later |
| Tokenomics plus TGE | −62% over two bars (2.0 → 0.77 ETH) | **[I]** Same airdrop-then-dump pattern as Pudgy and Azuki |

- **[I]** Unlike the Pudgy and Azuki airdrops, BIRB vests over 24 months *to nested NFTs*. A nested Moonbird therefore still carries a stream of future BIRB claims, which is a small, explicit yield. At $0.056 that stream is probably a small fraction of the floor; this cannot be quantified without per-NFT figures.

**[F] Companion collections:**
- **Oddities:** pixel art, sister collection.
- **Mythics:** launched July 2023 through nesting or burning [S6].
- Both are eligible for BIRB [S13].

## 5. Controversies & reputation

- **[F] CC0 switch (2022).** Community members later called it the project's "biggest mistake", and one holder reportedly lost a six-figure licensing deal [S2][S3].
- **[F] Two changes of ownership** within 3 years, the first followed by a dormant Yuga period [S5][S7].
- **[F] BIRB tokenomics backlash (January 2026)**, aimed at the small holder share and long vesting [S11].
- **[I] Net reputation.** Moonbirds is seen as a "revived orphan". OCG earned credibility in 2025 by reviving the brand without a token. The BIRB launch spent much of that credibility.

## 6. Community continuity through downturns (evidence)

- **[F] An orphan baseline exists.** During Yuga's dormant period (2024-03-10 to 2025-05-30, 150 NPF bars) the floor ranged from **0.21 to 0.90 ETH**. The mean was ≈0.43 ETH, and from mid-2024 it was mostly 0.3–0.5 ETH. The owner count over that period was not measured. **[I]** This is the closest thing in this set to an observed "team-vanished" floor. Today's 0.449 ETH is roughly at that dormant-period mean, so the market already prices Moonbirds near orphan value and gives OCG and BIRB little credit.
- **[F] Liquidity is thin.** 231 sales in 30 days; NPF 3-day sales counts in late 2026 often run in single digits to the 40s.
- **[I]** The community proved able to re-ignite under a motivated operator (the 10× in mid-2025), so dormant does not mean dead. It also fully round-tripped that rally within about 8 months.

## 7. Competitive threats / displacement

- **[I] Token over NFT.** BIRB on Solana gives liquid "birb" exposure without the NFT.
- **[I] CC0 cuts both ways.** Anyone can use the art, including OCG's own products, so the NFT is not needed to use the IP. That helps spread the brand but does not help NFT scarcity value.
- **[I] Pudgy's shadow.** OCG's main IP relationship is with Pudgy; Moonbirds sits in Pudgy-led Vibes sets ("Birb & Pengu").
- **[I]** It competes with every other "revived OG" PFP for a shrinking pool of collector capital.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

**[I] Yes, at about the orphan baseline (0.2–0.5 ETH; the dormant-period mean was ≈0.43 ETH, close to today's floor). Moonbirds is also the most technically resilient of the three.**
- **Resilience:** the art is fully on-chain and CC0. It has a 2022 cultural pedigree (Kevin Rose, PROOF). There is an empirical precedent that the community persists through a dormant owner.
- **What would be lost:** OCG's marketing engine and the BIRB vesting stream, if the claim infrastructure lapsed.
- **Founder-independence: moderate.** The highest of the three on format, the lowest on scale and liquidity.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

**[I]** These are speculative.
- More Vibes sets featuring Moonbirds, and Moonbirds-only physical products. OCG's "Pop Mart of web3" plan [S10].
- BIRB exchange listings or incentive campaigns.
- OCG fundraising or acquisition.
- Integration into Yuga's Otherside, agreed at the 2025 sale [S5].

**Negative scheduled items:**
- Monthly BIRB unlocks to nested NFTs (selling pressure on BIRB) and to the 25% investor/advisor bucket (schedule UNVERIFIED).
- Abstract shutdown (2026-12-15), which may disrupt Vibes' on-chain layer.
- The Blur/Blend wind-down (2026-11-12).

## 10. Strongest bull and bear theses

**Bull [I]:**
- It already trades near its own dormant-period average (≈0.43 ETH), so little operator value is priced in. It is also the most format-durable of the three (on-chain, CC0).
- An operator with real physical-TCG distribution that has already produced a 10× rally once.
- A nested NFT pays a small BIRB stream until about January 2028.
- If the "revived OG" narrative returns in a 2027–28 alt cycle, Moonbirds has shown high beta.

**Bear [I]:**
- The 2025 revival was a meme-and-token cycle that fully reversed. The token is now down ~70–90% and dilutes holders monthly.
- OCG is small and dependent on Pudgy IP and the closing Abstract chain.
- Liquidity is the thinnest of the three.
- CC0 means no IP rent ever accrues to holders.
- In BTC terms the floor has lost 99% from its 2022 peak, and has never set a higher high in BTC.

## 11. Sources (publisher, date; accessed 2026-10-13)

- S1 Fortune (2022-04-18) and Gfinity / Benzinga mint guides (secondary): https://fortune.com/2022/04/18/moonbird-nft-collection-surge/ ; https://www.gfinityesports.com/article/moonbirds-nft-mint-price-where-to-buy
- S2 The Block, "Moonbirds ruffles some holders' feathers with abrupt copyright switch" (2022-08): https://www.theblock.co/post/161819/moonbirds-ruffles-some-holders-feathers-with-abrupt-copyright-switch
- S3 The Defiant, "Moonbirds' Public Flight Sparks Debate About IP Rights" (2022-08): https://thedefiant.io/news/nfts-and-web3/moonbirds-cc0-license-nfts
- S4 The Block, "Bored Apes' creator Yuga Labs acquires Proof…" (2024-02-16): https://www.theblock.co/post/277905/bored-apes-creator-yuga-labs-acquires-proof-takes-over-moonbirds-nft-brand ; NFT Now: https://nftnow.com/news/yuga-labs-acquires-proof/
- S5 Decrypt, Andrew Hayward, "Bored Ape Maker Sells Moonbirds IP to Gaming Startup" (2025-05-30): https://decrypt.co/323189/bored-ape-maker-sells-moonbirds-gaming-startup ; Cointelegraph: https://cointelegraph.com/news/yuga-labs-sells-moonbirds-ip-orange-cap-games
- S6 Decrypt, "Moonbirds Mythics NFTs begin reveal that will last at least 200 days" (2023-07-19): https://decrypt.co/149362/moonbirds-mythics-nfts-begin-reveal-last-least-200-days
- S7 Decrypt via Yahoo Finance, Erika Lee, "Moonbirds NFTs Are Soaring Again" (2025-08-16): https://finance.yahoo.com/news/moonbirds-nfts-soaring-again-whats-160103496.html
- S8 GAMES.GG, "Orange Cap Games Raises $3.5 Million" (metadata conflicts: 2025-06-09 vs 2026-06-06): https://games.gg/news/orange-cap-games-raises-millions/
- S9 Decrypt, Erika Lee, "Moonbirds Token BIRB to Take Flight on Solana…" (2025-10-02): https://decrypt.co/342727/moonbirds-token-birb-take-flight-solana-nft-comeback-continues
- S10 Crypto Briefing, Vivian Nguyen, "Moonbirds to launch BIRB token in early Q1 2026" (2025-12-14): https://cryptobriefing.com/moonbirds-birb-token-launch/
- S11 The Defiant, Denis Omelchenko, "Moonbirds debuts BIRB token TGE" (~2026-01-28; body not loaded, figures via search summary): https://thedefiant.io/news/nfts-and-web3/moonbirds-debuts-birb-token-tge ; S11b Inside Bitcoins, "Moonbirds Unveils $BIRB Tokenomics, Allocates Just 25% to NFTs": https://insidebitcoins.com/news/moonbirds-unveils-birb-tokenomics-allocates-just-25-to-nfts (secondary)
- S12 CoinGecko, Moonbirds (BIRB) coin page (viewed 2026-10-13): https://www.coingecko.com/en/coins/moonbirds ; Coinbase price page: https://www.coinbase.com/price/moonbirds
- S13 KuCoin flash / PANews syndication, "Moonbirds Announces $BIRB Token TGE on January 28" and Nesting 2.0 (2026-01): https://www.kucoin.com/news/flash/moonbirds-announces-birb-token-tge-on-january-28 (aggregator; flagged)
- S14 Cointelegraph, Reguerra, "Pudgy Penguins … Target Card Launch" (2026-06-20): https://cointelegraph.com/news/pudgy-penguins-expands-retail-footprint-with-target-trading-card-rollout
- Data: `data/processed/npf_series/proof-moonbirds.csv` (NFTPriceFloor); `data/processed/screen_metrics.csv` (OpenSea); on-chain creation, first-mint and tokenURI checks via the Tenderly public RPC (2026-10-13).
