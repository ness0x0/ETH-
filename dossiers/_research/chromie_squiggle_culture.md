# Chromie Squiggle (Snowfro / Art Blocks #0): cultural durability and catalyst history

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[OC]** = verified on-chain by this workstream (method in §1); **[I]** = interpretation or inference by this workstream; **UNVERIFIED** = could not confirm. Dated events are in `data/processed/catalysts/chromie_squiggle.csv`._
_Investor context: a BTC-primary investor with ~$7–8k to deploy for 6–24 months, judging returns against BTC._

**Snapshot (2026-10-13):**
- **Price.** Floor is 2.642 ETH (OpenSea and NPF), about $6,628 or 0.0795 BTC.
  - In ETH, the floor is down 22% over 1y, 19% over 2y, 72% over 3y, and 84% from the series peak of 16.4 ETH (2023-01-11 bar).
  - In BTC, it is down 35% over 1y, 37% over 2y, 86% over 3y, and **94% from peak** (`data/processed/screen_metrics.csv`).
- **Holders and activity.** OpenSea counts 2,939 owners for 10,000 tokens (29% unique ratio). Last 30 days: 42 sales, 87 ETH.
- **Royalty.** OpenSea enforces a **7.5% creator royalty** plus a 1% marketplace fee. That adds roughly 8.5% to the round-trip cost (`data/raw/opensea/collection_chromie-squiggle-by-snowfro.json`).
- **[I] One-line verdict.** Squiggles have the strongest institutional and cultural evidence of any affordable gen-art token: MoMA, LACMA, Toledo, Sotheby's, and an immutable, fully on-chain script. That evidence has **not** protected the floor in BTC terms. Museums collect type-sets and grails; the floor (a "Normal" Squiggle) rides ETH beta and NFT-market liquidity.

---

## 1. Identity & provenance

- **[OC] Contract.** Art Blocks "GenArt721" V0 contract `0x059edd72cd353df5106d2b9cc5ab83a52287ac3a`.
  - Created 2020-11-27 05:59 UTC by `0x96dC73c8…7660` (Blockscout API). Project 0 = Chromie Squiggle, tokenIds 0–9999.
  - `projectTokenInfo(0)` returns invocations **10,000 / maxInvocations 10,000**.
  - `projectScriptInfo(0)` returns script type `p5js` v1.0.0 with **locked = true**, so the artist/admin can no longer change the script.
  - Query: eth_call at block 26,186,384, 2026-10-13 21:53–22:38 UTC, via `scripts/common.py` RPC (Tenderly public gateway / NodeReal public endpoint).
- **[OC] Mint history.** Method: Transfer logs from `0x0` on the contract, blocks 11,300,000–26,186,000, queried 2026-10-13 21:54 UTC; 10,000 Squiggle mints found.
  - **First mint:** 2020-11-27 16:12 UTC (block 11,341,538).
  - **Pace:** 5,501 minted by ~2021-01-06; 9,110 by ~2021-03-08; 9,247 by 2022-01-01.
  - **Reserve:** the last **753** were released in batches from 2022-01-07 to 2023-08-29. Batches included 310 on 2022-05-09, plus 30–66 per batch April–August 2023.
  - **Final two:** #9998 was minted 2024-07-23 to `0x9b917686…3f80`, a contract labeled "Relic" that is also listed as an editor of the OpenSea Squiggle collection. #9999 was minted **2024-08-21** for LACMA.
  - **[F]** A Jan 2023 newsletter said the then ~266 unminted Squiggles "will be hand-picked by Snowfro over time" [S12]. **[I]** Supply has been fully fixed since 2024-08-21; no further dilution is possible.
- **[F] Origin.** Snowfro (Erick Calderon) wrote the Squiggle as a proof of concept / demo for Art Blocks. Friends persuaded him to make it "project zero" [S2][S3]. Art Blocks itself was funded by Calderon's CryptoPunk sales, per NODE's official Punks timeline [S20].
- **Rarity tiers: what the floor represents.**
  - **[F] Type shares** (NADA 2022 dealer texts [S14]): Normal ≈60%, Slinky ≈11%, Ribbed <8%, Bold <5%, Pipe <2%. Fuzzy is also a type.
  - **[F] Color-spread attributes** sit on top of type: HyperRainbow, Full Spectrum (42 minted as of Jan 2023), Perfect Spectrum (~20–22) [S12][S15]. Special subtypes such as "Ghost/Harmonic Ribbed" (~35) are also traded [S12].
  - **[I] The floor is a common Normal Squiggle.** Museum and auction demand (Perfect Spectrum #1780 sold for $635k at Sotheby's in 2023 [S10]) concentrates in rare types and complete type-sets.
- **[F] Record sale.** About 945 ETH (~$2.8M) in September 2021, for a Squiggle minted 9 months earlier [S12]. Identified elsewhere as #4697 (secondary source).
  - **[OC]** #4697 moved to `0x55faf0e5…2d` on 2021-09-26 and has not moved since.

## 2. Narrative timeline (condensed; full list in CSV)

| Date | Event | Floor context (NPF 3-day bars, ETH) |
|---|---|---|
| 2020-11-27 | Art Blocks launch; Squiggle minting starts [OC] | n/a (series starts May 2022) |
| 2021-08/09 | Art Blocks mania; 945 ETH record Squiggle (Sept 2021) [S12] | n/a |
| 2022-03-29 | Venus Over Manhattan announces Venus Digital; first show is a Snowfro solo (June 2022) [S16] | n/a |
| 2022-09-27 | Art Blocks winds down numbered Curated Series and starts "Art Blocks 2.0" rebrand [S17][S18] | ~10.0 |
| 2022-10-26/27 | Friendship Bracelets (Snowfro × Alexis André): free claim for AB holders, snapshot 10-26, claim to 2023-01-10 [S19] | 10.5 → 15.9 by 11-09 bar. Confounded by the FTX collapse week |
| 2022-12 → 2023-01-11 | Gen-art rotation; Squiggle series peak **16.4 ETH (2023-01-11 bar)**. Terraforms peaked the same bar. Cause UNVERIFIED | 12.9 → 16.4 |
| 2023-02-13 | LACMA announces Cozomo donation; Snowfro pledges the final Squiggle to LACMA [S6] | ~13 |
| 2023-03-29 | Art Blocks launches its own marketplace (Seaport, no platform fee, royalties honored) [S21] | ~9.5 |
| 2023-06-15 | Sotheby's "Grails Part II" (3AC estate): Perfect Spectrum #1780 sells for $635k incl. premium; #9071 for $30.5k [S10][S11] | ~10.4 |
| 2023-04-08 → 2023-08-29 | Final ~264 reserve Squiggles minted; 10 to Flamingo DAO announced 2023-07-17 [OC][S10] | 9.0 → 9.4 |
| 2024-01-31 | Art Blocks acquires Sansa marketplace [S22] | ~7.5 |
| 2024-03-08 | Art Blocks enters a "focus period", pausing new releases (aggregator report) [S23] | 6.5 → 5.0 by 03-21 |
| 2024-08-21 | #9999 minted for LACMA; supply complete [OC][S7] | ~3.2 |
| 2024-11-24 | LACMA *Digital Witness* opens with Squiggle #9999 [S7] | ~3.9 |
| 2024-11-27 | Art Blocks: ~90% of works viewable from Ethereum alone (on-chain generator) [S24] | ~3.9 |
| 2025-03-12 | Squiggle #1458 moves into the wallet holding Toledo Museum's CryptoPunk #9833 [OC][S8][S20] | ~3.9 |
| 2025-05-13 | NODE buys CryptoPunks IP; Snowfro joins its advisory council [S25] | ~4.4 |
| 2025-07-12 | Toledo *Infinite Images* opens (to 2025-11-30) with 9 Squiggles under accession 2025.18 [S8] | ~3.75 |
| 2025-08-06 | "Art Blocks 500" announced: curated program to end, 500-project "glass case" [S4][S5] | ~5.0 (Aug: ETH ATH) |
| 2025-09-09 | Christie's closes its digital art department [S26] | ~4.2 |
| 2025-10-09 | Larva Labs' *Quine*: final Art Blocks Curated release [S27] | ~3.5 |
| 2025-11-27 | Art Blocks 5-year anniversary; "Mint Zero Day" for the final three AB500 projects [S28] | 2.2–2.5 |
| 2025-12-15 | Snowfro's *send/receive* launches; airdrop to Squiggle Type-Set / Full-Set achievement holders (snapshot 11-23) [S28] | ~2.4 |
| 2025-12-21 | **MoMA acquires 8 Squiggles** (complete type set) plus 8 CryptoPunks, by coordinated donation incl. SquiggleDAO [S1][S9] | 2.38 → 3.25 (12-29 bar) |
| 2026-09-09 | Art Blocks: 100% of AB500 renderable via on-chain generator [S29] | ~2.1–2.6 |
| 2026-10-12 | Blur announces frontend shutdown on 2026-11-12; Blend stops new loans [S30] | 2.64 |
| 2026-10-22–25 | Marfa Weekend 2026 (scheduled) [S31] | upcoming |

## 3. Founder/team dependence and company status (as of Oct 2026)

- **[F] The company is alive but has shrunk its ambition.**
  - **Curation ended.** In Aug 2025 Art Blocks declared its first 500 projects a finite canon ("Art Blocks 500") and ended its role as curated publisher. The final Curated release was *Quine* (Oct 2025); the final three Explorations (Snowfro, DCA, Jeff Davis) launched Dec 2025 [S2][S4][S27][S28].
  - **New focus.** "Preservation and elevation", Studio (artists self-publish on their own contracts), and Engine (partner platforms) [S2][S4].
  - **Recent signals of operation.**
    - Art Basel HK "Zero 10" activation (Mar 2026) [S32].
    - An MCP server for AI agents (mid-March 2026). Jordan Lyall is named **Chief Product Officer**; Calderon is described as "Founder" [S33].
    - "True Onchain Art" update (2026-09-09): 100% of AB500 renderable from Ethereum [S29].
    - Marfa Weekend 2026 is scheduled for Oct 22–25 [S31].
- **Layoffs: UNVERIFIED.**
  - **Searches.** I searched The Block, CoinDesk, Decrypt, NFT Now, Right Click Save, and general web for Art Blocks layoffs or restructuring 2023–2026; no report was found.
  - **Hardship quote.** A Now Media interview (date UNVERIFIED; page body would not load) is quoted in search snippets with Snowfro saying "The last couple of years have been excruciatingly tough" and that the market was "at its absolute worst" when the AB500 decision was made [S34]. Treat it as a secondary quote.
  - **Other signals.** An aggregator cites headcount 29 (UNVERIFIED). An aggregator reported a March 2024 "focus period" pausing new releases [S23]; I could not find the primary post.
- **[F] Snowfro's role beyond Art Blocks.**
  - Advisory council of the Infinite Node Foundation (NODE, CryptoPunks IP owner since 2025-05-13) [S25].
  - Co-donor (with Mara Calderon) of CryptoPunk #2786 to MoMA [S1].
  - Toledo Museum of Art has a page for "Snowfro" under `/about/leadership/` (role UNVERIFIED; page returned 403) [S35].
  - **[I]** He is now a museum-world figure. That raises the odds of further institutional placements of Squiggles. It also means Squiggle institutional events are partly *founder-coordinated* (MoMA gift coordinated with 1OF1/Ryan Zurrer and SquiggleDAO) rather than organic museum purchases.
- **Dependence by layer:**
  - **Artwork survival: low.** The script is on-chain and **locked** [OC]. Art Blocks' on-chain generator and dependency registry render AB500 works from Ethereum alone [S24][S29].
  - **Metadata/marketplace: moderate.**
    - The Art Blocks marketplace (launched 2023) aggregated listings via Reservoir, which shut down 2025-10-15 [S21][S36]. Whether Art Blocks migrated is UNVERIFIED.
    - Blur, a liquidity venue, closes its frontend 2026-11-12 [S30].
    - OpenSea remains the main venue.
  - **Narrative and liquidity: high.** Floor demand historically tracked Art Blocks' platform cycles (2021 mania, 2023 rotation) and the ETH/NFT macro, not Snowfro's output.

## 4. Tokens, airdrops, companion collections, incentives — and their effects

- **[F] No Art Blocks token.** No points program specific to Squiggles was found. OpenSea's SEA token TGE (planned 2026-03-30) was postponed indefinitely [S37]; it is a general marketplace incentive.
- **[F] Friendship Bracelets** (Explorations #1). Free claim, 2 per AB-holding address. Snapshot 2022-10-26, claim from 2022-10-27 until 2023-01-10; ~38.5k minted [S19].
  - **[I]** It was a goodwill airdrop, not a Squiggle-specific benefit. The Squiggle floor rose ~50% within two weeks, but in the FTX-collapse week, so it cannot be attributed.
- **[F] *send/receive*** (Snowfro's final AB500 project). Launched 2025-12-15. Pre-launch airdrop to holders of "Chromie Squiggle Type Set" and "Full Set" achievements (snapshot 2025-11-23) [S28].
  - **[I]** It rewards *set* holders, not floor holders, so the effect on the floor is negligible. The floor was flat at 2.2–2.5 ETH through December until the MoMA news.
- **[OC] Artist reserve (2022–2024).** 753 Squiggles came from Snowfro's reserve over 2.5 years.
  - Distribution was via gifts and programs, e.g., 10 to Flamingo DAO (2023-07-17 per SquiggleDAO Times [S10]). The 310 minted 2022-05-09 were not analyzed by recipient.
  - **[I]** This was a slow supply drip during the 2022–23 bear market. It is finished now.
- **[F] Lending.** SquiggleDAO passed proposals for an "Art Blocks Curated Lending Program" (SDIP-38) and an "Arcade Lending Program" (SDIP-39) in Feb 2023 [S13].
  - Loan-book exposure of Squiggles (NFTfi/Arcade/Gondi/Blend) was **not measured**. The coordinator's Blend reconstruction may cover it.

## 5. Controversies & reputation

- **[I] No scandal of the type that hit PFP projects** (rugs, founder deception, token dumps).
- **Points of friction:**
  - **Supply drip.** 753 Squiggles released from the artist reserve in 2022–2024 [OC]. It was disclosed ("hand-picked by Snowfro over time" [S12]) but diluted supply during a drawdown.
  - **High royalty.** 7.5% creator royalty is enforced on OpenSea, which taxes trading in a low-liquidity market.
  - **Museum provenance needs care.**
    - Toledo's exhibition page lists 9 Squiggles under a purchase credit line (accession 2025.18) [S8].
    - **[OC]** Only #1458 and #7884 sit in the wallet that also holds Toledo's on-chain-purchased CryptoPunk #9833 (`0x63c2645b…8bec`).
    - **[OC]** Seven of the nine exhibited token IDs (incl. #4697, #7583) remain in two private wallets (`0x55faf0e5…`, `0x95b9f6e9…`).
    - **[I]** Most exhibited Squiggles were probably loans. "Toledo bought 9 Squiggles" would overstate it; Toledo appears to have acquired ~2 (UNVERIFIED which exactly).
  - **Company retrenchment.** Ending curation in 2025 was framed as completion ("glass case"). It also reflects a weak market (Snowfro quote [S34]).

## 6. Community continuity through downturns (evidence)

- **[F] Institutional accumulation** (2023–2025, across the bear market):
  - LACMA: pledge Feb 2023; #9999 minted Aug 2024; exhibited from Nov 2024 [S6][S7].
  - Toledo: purchase in 2025 with Libbey Endowment funds [S8].
  - MoMA: 8-Squiggle type set, Dec 2025 [S1][S9].
  - **[I]** Few NFT collections outside CryptoPunks and Autoglyphs have this. It persisted while the floor fell ~85% in BTC.
- **[F] Collector organization.** SquiggleDAO was active in 2023 (bi-weekly town halls, lending programs, newsletter) [S13], and was a named MoMA donor in Dec 2025 [S1].
- **[F] Recurring physical events.** Art Blocks Marfa Weekend has run annually since 2021: 5th edition Oct 2025, 2026 edition scheduled Oct 22–25 [S31][S38].
- **[F] Holders and activity.** 2,939 owners (OpenSea, 2026-10-13). 552 sales / 1,575 ETH in the last 365 days (NPF via screen_metrics).
  - **[I]** Thin but continuous. A $6.6k floor token with ~1.5 sales/day means exit is feasible at or near floor, but not in size.
- **[I] The counter-evidence is price.** Cultural continuity has not translated into floor resilience: 0.43 BTC (May 2022 bar) → 1.12 BTC (Jan 2023) → 0.08 BTC now.

## 7. Competitive threats / displacement

- **[I] CryptoPunks absorb the "museum NFT" bid.** Punks are ~42% of NFT market cap per a Sept 2026 newsletter [S39]. NODE runs a museum-partnership program with the IP [S25], and MoMA paired Punks with Squiggles [S1].
  - Squiggles benefit from the pairing, but any marginal institutional dollar goes to Punks first.
- **[I] Within generative art, the grails are elsewhere.** In Sept 2026, Fidenza led ETH-terms gains (+40%) and took seven of the top ten art sales; the largest clean art sale was an Autoglyph at 55 ETH [S39]. The Squiggle floor is a mass-edition item by comparison.
- **[I] New long-form generative platforms and AI-generated art** dilute "first generative NFT" novelty. Squiggle's moat is being **first** (project #0) and founder-as-artist, which is not reproducible.
- **[I] Venue risk.** Christie's closed its digital department (Sept 2025) [S26]; Blur closes 2026-11-12 [S30]; Reservoir is gone [S36]. Fewer venues means thinner liquidity for the floor.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

- **[I] Yes, more than almost any other affordable ETH NFT.**
  - **The art doesn't need the company.** The script is immutable (locked) and renders from Ethereum via the on-chain generator [OC][S29].
  - **Canonical status is externally anchored.** MoMA, LACMA and Toledo collections, and Sotheby's sales history, would survive Art Blocks' disappearance.
  - **Snowfro's legacy as Art Blocks founder is fixed history.**
- **What would be lost:**
  - Art Blocks' marketplace and events (Marfa) as demand-generators.
  - Royalty-funded promotion.
  - The coordinating role that produced the MoMA gift.
- **[I] Net effect.** The *cultural* asset is durable. Whether the *floor* is durable in BTC terms depends on aggregate NFT liquidity and ETH/BTC, which the team does not control.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

- **[I] Speculative list.** None are announced except where marked.
  - **Marfa Weekend 2026** (2026-10-22–25, scheduled) [S31]. Historically a sentiment event; no measurable floor effect isolated.
  - **Further museum gifts.** Snowfro, 1OF1 and NODE run explicit museum-placement programs. Another type-set donation is plausible [S1][S25].
  - **Snowfro releases with Squiggle-holder allowlists/airdrops**, as with *send/receive*. Effect has been negligible.
  - **Sotheby's/Phillips generative sales** featuring rare Squiggles (2025 Digital Art Day lots existed [S11]). These affect rare-type comps more than the floor.
  - **Marketplace incentives.** An OpenSea SEA TGE (postponed indefinitely) could create wash-volume incentives [S37]. Not Squiggle-specific.
  - **ETH/BTC and NFT beta.** The dominant driver historically (e.g., Jul–Aug 2025: floor 4.2 → 5.75 ETH alongside the ETH ATH).

## 10. Strongest bull thesis & strongest bear thesis

- **Bull [I]:**
  - Squiggle is the "first page" of on-chain long-form generative art. It is now in **MoMA, LACMA and Toledo**, with a locked, fully on-chain script and fixed supply since 2024-08-21.
  - The floor is ~0.08 BTC, 94% below its 2023 peak, while institutional recognition has only grown since.
  - The "glass case" AB500 framing turns Art Blocks' first five years into a closed canon, and Squiggle is item #0.
  - If NFTs re-rate with ETH (ETH/BTC at 0.030 is near cycle lows), Squiggles are one of the few names with both liquidity (~550 sales/yr) and museum-grade provenance at a ~$6.6k entry.
- **Bear [I]:**
  - Museum validation is already public and **has not stopped a 35% one-year BTC-denominated decline**.
  - The floor is the most common type (~60% Normal). Institutions buy sets and grails, not floors.
  - Art Blocks is in retrenchment (curation ended; aggregator-reported release pause; "excruciatingly tough" years).
  - Liquidity venues are closing (Blur, Reservoir, Christie's digital department).
  - The 7.5% royalty plus 1% fee makes round trips costly.
  - With 10,000 units and ~2,900 holders, a few motivated sellers can cap any rebound. The floor behaves as high-beta ETH, a poor fit for a BTC-denominated mandate unless one has a view on ETH/BTC.

## 11. Sources

| # | URL | Publisher | Date | Accessed |
|---|---|---|---|---|
| S1 | https://www.theblock.co/post/383446/moma-adds-cryptopunks-and-chromie-squiggles-nfts-to-permanent-collection-following-coordinated-donation | The Block (Zack Abrams) | 2025-12-21 | 2026-10-13 |
| S2 | https://opensea.io/blog/articles/in-conversation-with-erick-calderon | OpenSea (Hannah Vanek) | 2025-08-28 | 2026-10-13 |
| S3 | https://nftevening.com/snowfro-speaks-the-art-blocks-founder-on-his-journey-as-a-web3-artist/ | NFT Evening | dated 2026-01-29 (internal date inconsistency noted) | 2026-10-13 |
| S4 | https://www.artblocks.io/articles/art-blocks-500-complete-collection | Art Blocks (Erick Calderon) | 2025-08-06 | 2026-10-13 |
| S5 | https://www.bankless.com/read/art-blocks-evolves | Bankless | 2025-08-09 | 2026-10-13 |
| S6 | https://decrypt.co/121238/lacma-art-museum-nft-donation-cryptopunk-art-blocks | Decrypt | 2023-02-14 | 2026-10-13 |
| S7 | https://unframed.lacma.org/node/3729 | LACMA Unframed | 2024 (mint 2024-08-21; exhibition 2024-11-24) | 2026-10-13 |
| S8 | https://infiniteimages.toledomuseum.org/collection/chromie-squiggle ; https://infiniteimages.toledomuseum.org/artwork/chromie-squiggle-7583 | Toledo Museum of Art | 2025 (exhibition 2025-07-12 to 11-30) | 2026-10-13 |
| S9 | https://www.rightclicksave.com/article/digital-art-acquisitions-in-2025-moma-whitney-centre-pompidou | Right Click Save | 2025-12-29 | 2026-10-13 |
| S10 | https://squiggledao1.substack.com/p/the-squiggledao-times-009 | SquiggleDAO Times (fan newsletter) | 2023-07-11 | 2026-10-13 |
| S11 | https://sothebys.com/en/buy/auction/2023/grails-part-ii/chromie-squiggle-1780 ; https://sothebys.com/en/buy/auction/2025/digital-art-day-auction/chromie-squiggle-9871 | Sotheby's (lot pages; results behind login) | 2023-06-15; 2025-02-19 | 2026-10-13 |
| S12 | https://corporatetrash.beehiiv.com/p/five-things-know-chromie-squiggles | Corporate Trash (newsletter; secondary) | 2023-01-11 | 2026-10-13 |
| S13 | https://squiggledao1.substack.com/p/the-squiggledao-times-001 | SquiggleDAO Times | 2023-02-15 | 2026-10-13 |
| S14 | https://www.newartdealers.org/fairs/nada-miami-2022/artworks/8141 (and /8143, /8142, /8144) | NADA / Venus Over Manhattan | 2022-12 | 2026-10-13 |
| S15 | https://threadreaderapp.com/thread/1439332605263032327.html | 6529 thread (secondary) | 2021-09 | 2026-10-13 |
| S16 | https://venusovermanhattan.com/news/ocula | Venus Over Manhattan | 2022-03-29 | 2026-10-13 |
| S17 | https://www.theblock.co/post/172991/art-blocks-nft-platform-winds-down-curated-series-plans-branding-refresh | The Block | 2022-09-27 | 2026-10-13 |
| S18 | https://metaversal.banklesshq.com/p/art-blocks-20 | Bankless Metaversal (W. Peaster) | 2022-10-04 | 2026-10-13 |
| S19 | https://www.theblock.co/post/179636/art-blocks-founder-announces-friendship-bracelet-nft-airdrop | The Block | 2022-10-27 | 2026-10-13 |
| S20 | https://nodefoundation.com/cryptopunks | Infinite Node Foundation (official timeline) | accessed 2026-10-13 | 2026-10-13 |
| S21 | https://decrypt.co/124848/art-blocks-nft-marketplace-enforced-creator-royalties | Decrypt | 2023-03-29 | 2026-10-13 |
| S22 | https://decrypt.co/214715/art-blocks-acquires-nft-marketplace-sansa | Decrypt (sponsored post by Art Blocks) | 2024-01-31 | 2026-10-13 |
| S23 | https://www.bitget.com/news/detail/12560603924492 | Bitget/Cointime (aggregator; last resort) | 2024-03-08 | 2026-10-13 |
| S24 | https://decrypt.co/293720/art-blocks-nft-project-major-leap-ethereum | Decrypt (Sander Lutz) | 2024-11-27 | 2026-10-13 |
| S25 | https://www.theblock.co/post/354114/yuga-labs-sells-cryptopunks-ip-to-nonprofit-infinite-node-foundation | The Block (Daniel Kuhn) | 2025-05-13 | 2026-10-13 |
| S26 | https://cointelegraph.com/news/auction-christies-shuts-digital-art-nft-division | Cointelegraph | 2025-09-09 | 2026-10-13 |
| S27 | https://www.rightclicksave.com/article/larva-labs-to-release-final-art-blocks-curated-project-quine-news | Right Click Save | 2025 (release 2025-10-09) | 2026-10-13 |
| S28 | https://www.artblocks.io/articles/the-final-three-ab500-comes-full-circle | Art Blocks | 2025-11-24 | 2026-10-13 |
| S29 | https://www.artblocks.io/articles/true-onchain-art | Art Blocks | 2026-09-09 | 2026-10-13 |
| S30 | https://www.theblock.co/news/ecosystems/2026-10-12-blur-nft-marketplace-shutting-down-frontend-blend-418363 ; https://www.coindesk.com/tech/2026/10/13/once-largest-ethereum-nft-marketplace-blur-is-shutting-down-after-volumes-collapse-99 | The Block; CoinDesk | 2026-10-12; 2026-10-13 | 2026-10-13 |
| S31 | https://dev.artblocks.io/marfa-weekend | Art Blocks (event page) | 2026 | 2026-10-13 |
| S32 | https://www.artblocks.io/articles/art-basel-hk-2026-recap | Art Blocks | 2026-04-02 | 2026-10-13 |
| S33 | https://www.rightclicksave.com/article/art-blocks-embraces-ai-agents-jordan-lyall-interview | Right Click Save (Louis Jebb) | 2026-04-13 | 2026-10-13 |
| S34 | https://nowmedia.co/posts/art-blocks-500-snowfro-generative-art-interview | Now Media (body not retrievable; quotes via search snippet only) | UNVERIFIED (2025) | 2026-10-13 |
| S35 | https://toledomuseum.org/about/leadership/snowfro | Toledo Museum of Art (403) | n/a | 2026-10-13 |
| S36 | https://apis.io/providers/reservoir/ (Reservoir sunset 2025-10-15; announced 2025-04-24) | apis.io / secondary | 2025 | 2026-10-13 |
| S37 | https://whale-alert.io/stories/ea98012535090c/OpenSea-delays-SEA-token-launch-indefinitely-last-Treasure-rewards-wave-refunds-offered-forfeiting-Treasure-and-0-OS2-trading-fees-for-60-days | Whale Alert (secondary) | 2026-03 | 2026-10-13 |
| S38 | https://bigbendsentinel.com/2025/10/16/5th-annual-art-blocks-weekend-to-bring-hundreds-of-visitors/ | Big Bend Sentinel | 2025-10-16 | 2026-10-13 |
| S39 | https://grailcap.substack.com/p/digital-art-market-on-blockchains-2e3 | Grail Capital newsletter (secondary) | Sept/Oct 2026 | 2026-10-13 |
| OC | On-chain: Tenderly public gateway / NodeReal public RPC via `scripts/common.py`; Blockscout API v2 (`eth.blockscout.com/api/v2/addresses/...`). Queries 2026-10-13 21:53–22:39 UTC; blocks noted inline. | — | — | — |

**Could not verify:**
- Art Blocks layoffs/headcount.
- Snowfro's formal title in 2026 and his Toledo role.
- Exact Sotheby's 2025 hammer prices.
- Which Squiggles Toledo actually owns beyond the two in its inferred wallet.
- Whether Squiggles appear in MoA+L *EMULATION* (2026-03-04 to 08-16).
- Cause of the Dec 2022–Jan 2023 rally.
