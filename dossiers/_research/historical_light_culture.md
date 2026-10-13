# Historical collections, lighter coverage: Curio Cards, MoonCats, Autoglyphs (reference)

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[OC]** = verified on-chain by this workstream; **[I]** = interpretation; **UNVERIFIED** = could not confirm. No catalyst CSVs were requested for these three; key dates are inline._
_Budget reference: $7,000 ≈ 2.79 ETH and $8,000 ≈ 3.19 ETH at ETH $2,508.69 (2026-10-13 Binance close)._

## Summary table (2026-10-13)

| | Curio Cards (wrapped) | MoonCats (Acclimated) | Autoglyphs |
|---|---|---|---|
| Launch | 2017-05-09 | 2017-08-09 | 2019-04 |
| Supply | 30 cards (+17b), 111–2,154 copies each; 29,700 total, ~4k est. lost | 25,440; **20,953 acclimated** [OC] | 512 |
| Floor (OpenSea/NPF) | 0.049 ETH (cheapest card) | 0.124 ETH (~$311) | 59.69 ETH (~$149.7k; 1.80 BTC) |
| Owners (OpenSea) | 4,953 | 5,438 | 171 |
| 30d sales / vol | 213 / 29.7 ETH | 253 / 33.1 ETH | 0 / 0 |
| 1y floor chg ETH / BTC | −23% / −36% | −28% / −40% | −29% / −41% |
| Drawdown from NPF-era peak, BTC | −93% | −87% | −93% (3y −82%) |
| Issuer today | None (community docs/site) | MoonCatRescue LLC team, active on-chain Sept 2026 [OC] | Larva Labs (dormant project) |
| Institutional / auction anchor | Christie's full set, 393 ETH, 2021-10-01 | none found | Centre Pompidou (#25, 2023) |

Floors, owners and sales are from `data/raw/opensea/*` and `data/processed/screen_metrics.csv`.

---

## A. Curio Cards

**Identity & provenance**
- **[F] Origins.** Launched **2017-05-09** as an "online gallery" of 30 card designs by seven artists: Cryptograffiti, Cryptopop, Daniel Friedman, Marisol Vengas, Phneep, Robek World, Thoros of Myr [S1][S2][S3].
  - Cards sold for $0.50–$1, with proceeds to artists [S1].
  - Developed by Travis Uhrig and Thomas Hunt, with Rhett Creighton on the smart contract [S1][S2].
- **[F] Supply structure.** Each card is a separate 2017 ERC-20 "vending machine" token with fixed supply between 111 and 2,154; the total is 29,700 and an estimated ~4,000 are lost or destroyed [S3].
  - **17b misprint.** A contract error led to cards 17–19 being reissued. The original #17 became the "17b" misprint, needed for a "complete" 31-card set [S1][S2].
- **[F] Rediscovery and wrapper.** Rediscovered in **March 2021**: @DieAping found the vending-machine contracts on GitHub [S2].
  - **[OC]** The canonical ERC-1155 wrapper `CurioERC1155Wrapper` `0x73da73ef3a6982109c4d5bdb0db9dd3e3783f313` was created **2021-03-28 17:58 UTC** (Blockscout). It is backed 1:1 and reversible to the 2017 ERC-20s.
  - **[F]** An earlier rushed OpenSea wrapper had a bug that "permawrapped" some cards, making #26 the rarest in tradeable form (~105 per a 2022 account) [S2].
  - 17b has its own wrapper flow (wrap.curio.cards/17b) [S3].

**Timeline (key dates)**
- 2017-05-09: launch.
- 2021-03 (rediscovery); 2021-03-28: wrapper deployed [OC].
- **2021-10-01: Christie's** "Post-War to Present" (New York) sells a complete set including 17b for **393 ETH (~$1.27M)**.
  - Described as the first Christie's auction with bidding solely in ETH [S1].
  - The buyer is named by one account as early Ethereum contributor Taylor Gerring [S2] (UNVERIFIED independently).
- 2025-10-22: revised edition of Robert Alice's *On NFTs*, which the Wikipedia article cites, keeps Curio in the canonical NFT-history literature [S1].

**Team dependence and status**
- **[I] There is no active issuer.** The project survives as immutable 2017 contracts plus community-run site, docs and supply tracker (curio.cards, docs.curio.cards, ccsupply.xyz) [S3].
- **[OC]** The wrapper owner `0x5af3e047…bf36` has no recent transactions visible on Blockscout.
- Founder reputation is mixed: Rhett Creighton is associated with abandoned coins such as ZClassic and Whalecoin [S2].
- **[I]** "If the team vanished" is moot. Durability rests on the "first art NFTs on Ethereum" claim, which is colloquial and contested by others, plus the Christie's sale.

**What ~$7k buys (card-by-card pricing)**
- **[OC] Method.** All Seaport `OrderFulfilled` events in transactions that moved wrapper tokens (TransferSingle logs), blocks 24,886,487–26,186,487 (~180 days), decoded per token. Queried 2026-10-13 22:13 UTC via Tenderly/NodeReal; output saved at `data/raw/onchain_culture/curio_sales_180d.json`.
  - Some trades emit two OrderFulfilled events, so medians are used. Rare-card figures rest on 1–4 trades each and are indicative only.
- **90-day median unit prices (ETH):**
  - **Commons (cards 2, 3, 7–13, 20, 30):** ~0.046–0.069.
  - **Cards 14, 16, 17, 27, 28:** ~0.08–0.13.
  - **Cards 1, 4, 5, 6, 15, 18, 19:** ~0.13–0.25. Card 1 "Apples" ~0.25.
  - **Card 29:** ~0.60.
  - **Rares (cards 21–26):** 26 ~1.09; 23 ~1.4–2.0; 24 ~1.5–5 (wide); 25 ~3.8; 21 ~4.2 (single trade); 22 ~5.0–5.3.
  - **17b:** not measured (separate contract).
- **Implications:**
  - A full 30-card set (ex-17b) costs ≈ **22 ETH (~$55k)**, out of budget.
  - **$7k (~2.8 ETH)** buys either:
    - (a) **all 24 non-rare cards** (1–20, 27–30) for ≈2.3 ETH (~$5.8k) plus one more mid card; or
    - (b) one rare (card 26 or 23) plus ~10–15 commons.
  - **[I]** Commons have 1,000–2,000+ copies each and track the collection floor. Cultural value concentrates in complete sets, 17b, and the low-supply cards 21–26.

**Bull/bear (compact) [I]**
- **Bull.** Genuinely 2017, artist-made, Christie's-validated. A "near-complete set" is achievable within budget. The collection floor of 0.049 ETH ($123) is near its NPF-era low.
- **Bear.**
  - No museum acquisition found and no steward.
  - Liquidity is ~1 ETH/day across 30 SKUs, and the commons are abundant.
  - The floor is −93% vs BTC from its 2022 high.
  - Set-completion demand has not re-emerged since 2021–22.

## B. MoonCats (MoonCatRescue)

**Identity & provenance**
- **[OC]** `MoonCatRescue` `0x60cd862c9C687A9dE49aecdC3A99b74A4fc54aB6` was created **2017-08-09 04:36 UTC** by `0xA97F8fFC…` (Blockscout).
- **[F]** 25,440 cats (96 black-and-white Genesis plus 25,344 Rescue), made by the two-person team Ponderware [S4]. Contract development hit a bug that made sale funds inaccessible, and the project went dormant with most cats unrescued [S5].
- **[F] Rediscovery.** Thread by "ETHoard" at **07:00 UTC on 2021-03-12**. All remaining cats were rescued within hours; the floor reached ~0.8 ETH within a day [S6]. Bots dominated the rescue rush [S7].
- **[OC]** `MoonCatAcclimator` (ERC-721/998 wrapper) `0xc3f733ca98e0dad0386979eb96fb1722a1a05e69` was created **2021-04-22**.
  - `totalSupply` is **20,953** at 2026-10-13 22:00 UTC, i.e. 82% of cats acclimated.
  - Owner `team.mooncatrescue.eth` (`0xdf2e60af…ce27`).

**Team state**
- **[F] Ownership changed on 2022-09-06.** IP and ownership passed internally from Ponderware to pseudonymous members MidnightLightning (lead dev) and Paws (community) as MoonCatRescue LLC. Ponderware became a separate consulting/creative entity.
  - Development was paused for a period after the sale, which drew community criticism [S4].
  - Holders have **limited commercial rights**; MoonCatRescue LLC owns the IP [S4].
- **[OC] The team is still operating:** `team.mooncatrescue.eth` called `setBaseURI` on the Acclimator (**2026-08-23**) and set accessory prices on MoonCatAccessories (**2026-09-04**).
  - **[I]** The team controls the Acclimator metadata base URI, so display metadata depends on the team. Whether images are fully derivable on-chain from cat IDs is UNVERIFIED.
- **[F] Name collision.** An unrelated 2025 "MOONCAT" brand (Lady Rocket / Unstoppable Domains `.MOONCAT`) exists and may confuse search and press [S8].

**[I] Assessment.**
- **Positives.** Strong "2017 digital archaeology" story, a large holder base (5,438), an active small team, and cheap entry (~$311/cat; $7k ≈ 22 floor cats, or a few higher-tier cats). Genesis-cat pricing is UNVERIFIED.
- **Negatives.** No institutional anchor found, team-controlled metadata and IP, and a −87% drawdown vs BTC. Fits "historical curiosity" more than "museum provenance".

## C. Autoglyphs (reference only; unaffordable)

- **[F] Identity.** Larva Labs, April 2019, 512 glyphs, described as the first entirely on-chain generative art project [S9].
- **[F] Institutional anchor.** **Centre Pompidou** acquired Autoglyph #25, donated by Larva Labs, alongside CryptoPunk #110.
  - Larva Labs announced it on 2023-02-10 [S10][S11]. NODE's timeline lists it under Apr 2023, presumably the exhibition date [S9].
  - Autoglyphs were also on view in Toledo's *Infinite Images* (2025-07-12 to 11-30) per Toledo's exhibition text [S12].
- **[F] Market.** Floor 59.69 ETH (~$149.7k; 1.80 BTC), 171 owners, no sales in 30 days (OpenSea). The largest "clean" art sale in Sept 2026 was an Autoglyph at **55 ETH**, below the current listed floor [S13].
  - **[I]** The quoted floor is ask-driven.
- **[I] Why it matters here.** Autoglyphs and V2 Punks are the benchmark for what "institutional, fully on-chain, low-founder-dependence" looks like. Neither is buyable with $7–8k. Squiggles are the closest affordable analogue; Terraforms and V1 Punks are further away.

## Sources

| # | URL | Publisher | Date | Accessed |
|---|---|---|---|---|
| S1 | https://en.wikipedia.org/wiki/Curio_Cards | Wikipedia (cites Observer/Christie's coverage 2021-09/10) | last edited 2026-02-16 | 2026-10-13 |
| S2 | https://amycastor.com/2022/06/04/the-early-history-of-nfts-curio-cards/ | Amy Castor & David Gerard (blog) | 2022-06-04 | 2026-10-13 |
| S3 | https://docs.curio.cards/ ; https://ccsupply.xyz/ ; https://curio.cards/ | Curio community docs/tools | n/a | 2026-10-13 |
| S4 | https://www.coindesk.com/learn/what-are-mooncats-the-legacy-nft-project-revived-by-its-community/ | CoinDesk | 2023-03-13 | 2026-10-13 |
| S5 | https://decrypt.co/61316/an-ancient-nft-project-called-mooncats-is-eating-up-ethereum | Decrypt | 2021-03 | 2026-10-13 |
| S6 | https://cointelegraph.com/news/digital-archeology-long-dormant-mooncats-project-rides-nft-mania-to-the-moon | Cointelegraph (Andrew Thurman) | 2021-03-13 | 2026-10-13 |
| S7 | https://decrypt.co/62231/bots-are-ruining-mooncats-one-of-ethereums-oldest-nft-projects | Decrypt | 2021-03 | 2026-10-13 |
| S8 | https://www.globenewswire.com/news-release/2025/08/28/3140968/0/en/Lady-Rocket-Foundation-and-Unstoppable-Domains-Announce-Launch-of-MOONCAT-to-Support-Cat-Rescue-and-Onchain-Identity.html | GlobeNewswire (unrelated brand) | 2025-08-28 | 2026-10-13 |
| S9 | https://nodefoundation.com/cryptopunks | Infinite Node Foundation | accessed 2026-10-13 | 2026-10-13 |
| S10 | https://decrypt.co/137094/quite-surprise-seeing-cryptopunks-nft-pompidou-larva-labs-co-founder | Decrypt | 2023 | 2026-10-13 |
| S11 | https://www.centrepompidou.fr/en/ressources/oeuvre/WX3xkvI | Centre Pompidou (Autoglyph #25 record: "Don de Larva Labs, 2023") | n/a | 2026-10-13 |
| S12 | https://infiniteimages.toledomuseum.org/collection/chromie-squiggle | Toledo Museum of Art | 2025 | 2026-10-13 |
| S13 | https://grailcap.substack.com/p/digital-art-market-on-blockchains-2e3 | Grail Capital newsletter (secondary) | Sept/Oct 2026 | 2026-10-13 |
| OC | Tenderly/NodeReal RPC via `scripts/common.py`; Blockscout API v2 (creation txs; tx list of `team.mooncatrescue.eth`; wrapper owner). Queries 2026-10-13 21:53–22:30 UTC. | — | — | — |

**Could not verify:**
- Per-card circulating supply (ccsupply.xyz table did not render).
- 17b price.
- Curio art hosting (IPFS vs centralized).
- MoonCat Genesis-cat prices.
- Whether MoonCat images are fully on-chain-derivable.
- Any MoonCats/Curio museum holdings.
