# Terraforms by Mathcastles: cultural durability and catalyst history

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[OC]** = verified on-chain by this workstream (method in §1); **[I]** = interpretation or inference; **UNVERIFIED** = could not confirm. Dated events are in `data/processed/catalysts/terraforms.csv`._

**Snapshot (2026-10-13):**
- **Price.** Floor is 0.2998 ETH (OpenSea and NPF), about $752 or 0.0090 BTC.
  - In ETH: +7% over 1y, −45% over 2y, −75% over 3y, −91% from the series peak of 3.45 ETH (2023-01-11 bar).
  - In BTC: −11% over 1y, −58% over 2y, −87% over 3y, **−96.6% from peak** (`screen_metrics.csv`).
- **Holders and activity.** OpenSea counts 1,971 owners / 9,911 tokens. Last 30 days: 178 sales, 51.5 ETH. Last 365 days: 1,459 sales, 545 ETH.
- **Fees.** No creator royalty is enforced on OpenSea (only the 1% marketplace fee).
- **Data caveat.** NPF 3-day volume figures for 2022 look implausible, e.g. 8,112 ETH on 478 sales in one Oct 2022 bar. Use NPF *floors* only, not 2022 volumes.
- **[I] One-line verdict.** Terraforms is the most technically ambitious fully on-chain artwork in this set and is respected by on-chain-art specialists. However, it has **no institutional acquisitions found**, an **anonymous two-person team that communicates sporadically**, and a **latent owner-mint allowance of up to 1,193 extra tokens**. It is a high-beta, low-liquidity cultural bet, not a provenance asset in the Punks/Squiggle sense.

---

## 1. Identity & provenance

- **[OC] Contract.** `0x4e1f41613c9084fdb9e34e11fae9412427480e56` ("Terraforms", verified source on Blockscout). Query: eth_call at latest block (≈26,186,500), 2026-10-13 22:07 UTC, `scripts/common.py` RPC (Tenderly/NodeReal).

  | Getter | Value |
  |---|---|
  | `totalSupply` / `tokenCounter` | 9,911 |
  | `MAX_SUPPLY` | 11,104 |
  | `SUPPLY` (public cap) | 9,904 |
  | `OWNER_ALLOTMENT` | 1,200 |
  | `PRICE` | 0.16 ETH |
  | `seed` | 10196 |
  | `dreamers` | 1,913 |
  | `owner()` | EOA `0x7a822bce…6405` (not a multisig) |

- **[OC] Mint timeline.** Method: Transfer logs from `0x0`, blocks 13.6M–26.19M, queried 22:07 UTC; 9,911 mints.
  - First mint 2021-12-17 15:21 UTC (block 13,823,383). 99% were minted by 2021-12-18.
  - Five later mints ran from 2022-02-10 to **2023-09-08**. These are owner claims; public minting stopped at 9,904.
  - The contract code gates early mint to **Loot holders or mintpass holders** (Loot contract `0xFF9C1b15…`). Mintpass redemption created "Origin Daydream" tokens.
  - The reveal (`setSeed`) was sent by the owner on 2021-12-18 (Blockscout tx list).
- **[OC] Latent supply.** `ownerClaim(to, n)` requires `tokenCounter >= SUPPLY && tokenCounter <= MAX_SUPPLY − n`.
  - **The owner can still mint up to 11,104 − 9,911 = 1,193 tokens (+12%).** There is no lock or renounce.
  - **[I]** This dilution risk is material and is not discussed in any source found. The team has used only 7 of the 1,200 allotment in ~4.8 years.
- **[OC] Mint proceeds.** About 1,585 ETH (9,904 × 0.16).
  - Withdrawn 2021-12-18 and forwarded from the owner EOA on 2021-12-18–20: ~938 ETH to `0x113d754F…` (vanity prefix matching member "0x113d") and ~697 ETH to `0x90b03aFB…` (Blockscout tx list).
  - **[I]** The team was well funded by the mint and has not needed a token. It also has no visible on-chain treasury earmarked for the project.
- **[F] Creators.** Mathcastles is a studio of two anonymous developers, **0x113d and xaltgeist** [S1][S2]. The license names Mathcastles LLC (contract source).
  - The brief's "Xer0x" could not be matched to any source; treat it as an error.
- **[F] Design.**
  - Each token is a parcel (a 32×32 grid of Unicode characters) in a 20-level "Hypercastle", rendered at runtime from on-chain data [S2][S3][S4].
  - **Modes:** Terrain (default) → Daydream (holder draws; irreversible exit from Terrain) ↔ Terraform (drawing committed on-chain). Mintpass tokens are Origin Daydream / Origin Terraform [S3][S5].
  - Traits include zones (75), biomes (92), chroma, and topography that changes over time [S3].
- **[OC][F] Decay.** The contract's `_yearsOfDecay` returns 0 when `dreamers >= 500`. With 1,913 dreamers the structure does not decay [S3].
- **[OC] Renderer architecture** (`tokenURIAddresses`):

  | Index | Contract | Deployed | Type |
  |---|---|---|---|
  | 0 | `TerraformsData` `0xa5afc9fe…` | 2021-12-17 | plain contract, immutable |
  | 1 | ERC1967 proxy `0xb51a3bb8…` → impl `TerraformsData_v1_0` | 2023-12-24 | upgradeable |
  | 2 | ERC1967 proxy `0x8af860c8…` → impl `TerraformsData_v2_0` | 2023-12-24 | upgradeable |
  | — | Antenna proxy `0x331512a2…` → `TerraformsBeacon_v2_0` | 2023-12-24 | upgradeable |

  - Holders opt each token into a renderer (`setTokenURIAddress`).
  - The community "Antenna info" site describes V0 as the original, V1 as the version meant "to run on the EVM on its own in 50 years", and V2 as "where the party is" (new broadcasts). It describes moving to V2 as irreversible per its guide [S6]. Bankless calls this the "Terraforms 2.0 upgrade" [S3].
  - **[I]** The original art is immutable. The *living* features (Antenna broadcasts, v2) depend on Mathcastles-controlled upgradeable proxies.

## 2. Narrative timeline (condensed; full list in CSV)

| Date | Event | Floor (NPF 3-day bars, ETH) |
|---|---|---|
| 2021-12-17/18 | Mint at 0.16 ETH (Loot/mintpass early access), sold out in ~1 day; seed set 12-18 [OC] | n/a |
| 2022-09 | Mathcastles writes three.js and p5.js into EVM storage as composable on-chain libraries [S2] | ~0.48 |
| 2022-10 | First re-rating: 0.8 → 1.62 ETH in ~2 weeks. Cause **UNVERIFIED** (secondary sources cite "whale buying" [S5][S7]) | 0.8 → 1.6 |
| 2022-12 → 2023-01-11 | Second leg to **3.45 ETH peak (2023-01-11)**, same bar as the Squiggle peak. Coincides with a Mathcastles ZK teaser (2022-12-31) and the Zero "Sunflower One" demo [S8], and a broad gen-art rotation. Cause UNVERIFIED | 1.3 → 3.45 |
| 2023-02/03 | Drift lower; heavy Blur-era trading [S5] | 2.7 → 2.0 |
| 2023-07-26 | Royalty override set on-chain by owner (EIP-2981) [OC] | ~1.5 |
| 2023-08-01 | Glitch Marfa "Every 30 Days" exhibition of *Terraforms Level 7 at {22, 3}* (to 2023-09-01) [S9] | ~1.4 |
| 2023-09-08 | Last owner-claim mint; supply 9,911 [OC] | ~1.3 |
| 2023-12-24 | **Terraforms 2.0 / Antenna contracts deployed** (v1/v2 renderers, beacon) [OC][S3][S6] | ~1.38 (12-25) → 1.15 (12-28) → 1.78 (2024-01-27). Confounded by the Dec 2023 NFT rally |
| 2023-12-28/29 | Mathcastles announces and deploys *Angelus* (Zero Suite, ZK-gated 1/1) [S8][OC] | ~1.2 |
| 2024-03-05 | Two unverified contracts deployed by the Mathcastles deployer [OC] | ~1.3 |
| 2024-06-06 | Bankless "Terraforms Explained: ETH's best onchain art?" [S3] | ~0.5–0.7 |
| 2024-12-09 | Rare "Plague"-chroma Terraform (Level 14 {18,11}) reported sold for 50 ETH (1 of 7) [S10] | 0.82 (12-10) → 0.92 (12-22) |
| 2025-07/08 | NFT/ETH rally (ETH ATH 2025-08-22) | 0.40 → 0.59 |
| 2025-11 → 2026-04 | Series lows | 0.20–0.26 |
| 2026-07-14 | **"TD(R)unes — tDR x Mathcastles" contracts deployed** (UUPS proxy and impl), Blockscout-verified 2026-09-20/25. Content still empty; not signed or locked [OC] | ~0.31 |
| 2026-09 | Newsletter reports Terraforms +32% in ETH terms for September [S11]. **Not confirmed by NPF floors**, which show 0.24 (09-01) → 0.21 (09-13) → 0.23 (10-01) → 0.30 (10-13) | see left |
| 2026-10-12 | Blur frontend shutdown announced (2026-11-12) [S12] | 0.30 |

## 3. Founder/team dependence and team status (as of Oct 2026)

- **[F] Team.** Anonymous duo with no public company announcements found for 2025–2026. The studio website `mathcastles.xyz` shows only a GIF (fetched 2026-10-13).
  - There is a Mathcastles X post dated 2025-03-12 with content not retrievable [S13]. X pages were not readable (paywall/403).
- **[OC] On-chain activity of the Mathcastles deployer** (`0x9f400619…2cFA`; same address listed for Mathcastles on Le Random [S2]):
  - Big Terraforms 2.0 push on **2023-12-24**.
  - *Angelus* (Zero Suite) on **2023-12-29**.
  - Two unverified contracts on **2024-03-05**.
  - Then nothing until **2026-07-14**: deployment of `TD_R_unes`, whose header reads "TD(R)unes™ — tDR x Mathcastles", "Storage for composable text runes", with a `signedByTDR` flag and a quote attributed to "Ian Anderson".
    - Proxy `0xC2C5f8aA…3717`, impl `0xFC9D80EF…441B`.
    - State: `version` "Version 1.0"; `segmentCounter` 1 (no content uploaded); `signedByTDR` false; `locked` false.
  - **[I]** "tDR" is very likely The Designers Republic (Sheffield design studio co-founded by Ian Anderson). **UNVERIFIED**: no public announcement found. If real, it is the first notable outside-brand collaboration and a probable future "broadcast" to Antenna/V2 parcels.
- **Dependence by layer:**
  - **Art: low.** The V0 renderer is immutable and fully on-chain [OC][S4].
  - **Evolving features: high.** Upgradeable proxies are owned by Mathcastles.
  - **Supply: team-controlled.** 1,193 un-minted owner allotment remains.
  - **Narrative: high.** The thesis rests on Mathcastles continuing to "broadcast" new work into the Hypercastle, and they ship rarely.

## 4. Tokens, airdrops, companion collections, incentives — and their effects

- **[F] No token, and none planned** per a third-party report [S5]. No points or staking program found.
- **[F] Companion and related works:**
  - **Zero Suite** (ZK artworks): Sunflower One demo (~Jan 2023, not for sale); *Angelus* (announced 2023-12-28, a single 1/1 whose price must be revealed via ZK proofs); *Necropolis* announced [S8].
  - **"Project 2"**, referenced but undetailed [S3].
  - None were airdropped to Terraforms holders as far as found.
  - **[I]** No measurable floor effect from companion releases.
- **[F] Community derivatives:**
  - Hypercastle Explorers: 1,024 pieces, community-led, "not officially connected" [S14].
  - Thousand Ant's Unity Hypercastle Explorer [S15].
  - terrafans.xyz, terraformexplorer.xyz [S3].
  - **[I]** These are evidence of builder interest, not of price support.
- **[F] Loot linkage.** Early mint was open to Loot holders (contract code). This ties Terraforms culturally to the Aug 2021 "Loot" on-chain primitive movement.

## 5. Controversies & reputation

- **[I] No scandals found.** Reputation among on-chain-art collectors is strong ("ETH's best onchain art?" [S3]; inclusion in the Le Random archive [S2]).
- **[I] Under-discussed risks rather than controversies:**
  1. The owner-mint allowance of up to 1,193 tokens [OC].
  2. Upgradeable v2 proxies controlled by an EOA [OC].
  3. Mint proceeds of ~1,635 ETH paid out to the two members in Dec 2021, with no on-chain treasury [OC]. Normal for artists, but there is no endowment.
  4. Opaque communications (Discord/X only).
- **[F] Third-party data on Terraforms is inconsistent.** Supply is cited as 9,500, 9,905, 11,000, or 11,104. One wiki gives the mint as "Dec 17, 2022" (on-chain shows 2021) [S5][S16]. Expect press coverage to be noisy.

## 6. Community continuity through downturns (evidence)

- **[OC] 1,913 tokens have been converted to dreaming modes** (`dreamers`). That is ~19% of supply where a holder actively interacted with the artwork, an unusually high engagement signal for an NFT.
- **[F] Owners.** 1,971 (OpenSea 2026-10-13) vs 1,917 in Mar 2023 per NFTGo [S5]. Holder count is roughly stable through an ~89% ETH-price drawdown.
- **[F] Trading.** 1,459 sales in the last 365 days (NPF), the most of the three main collections in this workstream. It is cheap per unit, so liquidity in ETH is small (~1.5 ETH/day).
- **[F] Exhibitions.** Glitch Marfa window exhibition (Aug 2023) [S9]. Le Random holds six Terraforms [S2].
- **[F] No museum acquisition found** (searched MoMA/LACMA/Pompidou/Toledo/Whitney coverage; Right Click Save 2025 roundup lists none [S17]).
- **[I] Verdict.** Holder-base continuity is good, the price trend is poor, and institutional anchoring is absent.

## 7. Competitive threats / displacement

- **[I] Competing "fully on-chain art" grails:** Autoglyphs (Larva Labs, 2019; Pompidou) and Art Blocks' on-chain-generator claim (100% of AB500, Sept 2026) [S18]. These erode Terraforms' "most on-chain" distinction.
- **[I] Competing "on-chain worlds / autonomous worlds" narratives**, plus Mathcastles' own newer works (Zero Suite), compete for the same collectors' ETH.
- **[I] Complexity.** Explaining parcels, modes, Antenna and decay is hard. Museums have so far chosen simpler canonical objects (Punks, Squiggles, Autoglyphs).

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

- **[I] Partially.**
  - The V0 artwork is immutable and computable from Ethereum indefinitely. Community explorers exist, and the decay threshold is already met.
  - A core group of on-chain-art collectors (the ~1,900 holders who "dream") would likely keep it.
- **[I] But the investment narrative is "living artwork that keeps receiving broadcasts".** It dies if the team vanishes, and two latent risks would be frozen in place:
  - The 1,193-token owner allotment (if the key were lost, risk disappears; if compromised, risk rises).
  - Upgradeable v2 proxies.
- Expect it to settle as a niche historical piece. Without institutional anchoring, a re-rating would depend on collector rediscovery.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

- **[I] Speculative:**
  - **TD(R)unes reveal** (contract deployed 2026-07-14, verified Sept 2026, empty).
    - A Designers Republic × Mathcastles broadcast to Antenna/V2 parcels would be the first marquee outside-brand event. Probability and timing are UNVERIFIED.
    - Upside for "antenna-on" parcels; possibly the floor.
  - **New Zero Suite / Necropolis releases** with Terraforms-holder access (none historically).
  - **Owner use of the 1,193 allotment** for a sale or airdrop. Negative for the floor. Nothing announced.
  - **Museum placement.** None found; it would be a first.
  - **Market/venue events.** Blur frontend closure 2026-11-12 [S12] and OpenSea incentives [S19].
  - **The "+32% in Sept 2026" figure** (newsletter [S11]) is not confirmed by NPF floor bars (0.24 → 0.23 over September). The early-October rise to 0.30 was not tied to any announcement found. It may be early positioning around TD(R)unes or noise.

## 10. Strongest bull thesis & strongest bear thesis

- **Bull [I]:**
  - Terraforms is a genuinely novel, fully on-chain, interactive world-artwork with a still-active (if quiet) team. On-chain evidence shows an outside-studio collaboration being prepared (TD(R)unes, 2026-07-14).
  - Engagement is real: 19% of tokens dreaming, and owners stable at ~2k.
  - At ~$750 (0.009 BTC, −96.6% from peak in BTC), it is an option-like position. A $7k budget buys ~9 floor parcels or a few rarer ones (e.g., Origin or rare chroma).
  - A broadcast event, renewed on-chain-art cycle, or museum pickup could re-rate a tiny market cap (~3,000 ETH floor value).
- **Bear [I]:**
  - **No institutional anchoring and an anonymous team.** Mathcastles controls upgradeable renderers and can still mint **1,193 more tokens**.
  - **Price.** Down ~97% vs BTC since Jan 2023, with no evidence that team releases (2.0 in Dec 2023, Angelus) produced durable re-ratings.
  - **Liquidity.** ~1.5 ETH/day.
  - **Data and hype risk.** Press and data are noisy. The Oct 2026 bounce is unexplained.
  - **Mandate fit.** For a BTC-benchmarked holder who values low founder dependence, the living-artwork thesis is founder-dependent by design.

## 11. Sources

| # | URL | Publisher | Date | Accessed |
|---|---|---|---|---|
| S1 | https://iq.wiki/wiki/terraforms | IQ.wiki (secondary; contains date errors) | updated 2023-03-28 | 2026-10-13 |
| S2 | https://www.lerandom.art/artists/mathcastles | Le Random | n/a | 2026-10-13 |
| S3 | https://www.bankless.com/terraforms-explained-is-this-ethereums-best-onchain-art | Bankless (W. Peaster; author discloses holding) | 2024-06-06 | 2026-10-13 |
| S4 | https://ilikecalculus.substack.com/p/an-ode-to-terraforms | "i like calculus" Substack | 2022-10-28 | 2026-10-13 |
| S5 | https://www.gate.com/learn/articles/first-class-research-report-terraforms-by-mathcastles/1820 | Gate Learn (exchange research; secondary) | data to 2023-03-27; updated 2026-04-08 | 2026-10-13 |
| S6 | https://www.terraformsantenna.info/ | Community guide (not official) | n/a | 2026-10-13 |
| S7 | https://medium.com/@first.vip/first-vip-project-analysis-terraforms-by-mathcastles-c401dd15a1a6 | First.VIP (403; via search snippet) | 2023 | 2026-10-13 |
| S8 | https://mintorskip.beehiiv.com/p/will-never-buy ; https://mintorskip.beehiiv.com/p/im-smooth-brain | Mint or Skip newsletter | 2024-01-03; 2023-01 | 2026-10-13 |
| S9 | https://www.glitchmarfa.com/e30dgallery/terraforms/ | Glitch Marfa | 2023-08 | 2026-10-13 |
| S10 | https://x.com/RogerDickerman/status/1866125456287683046 | RD / 24 Hours of Art (X post; via search snippet; post time 2024-12-09 from snowflake ID) | 2024-12-09 | 2026-10-13 |
| S11 | https://grailcap.substack.com/p/digital-art-market-on-blockchains-2e3 | Grail Capital newsletter (secondary) | Sept/Oct 2026 | 2026-10-13 |
| S12 | https://www.theblock.co/news/ecosystems/2026-10-12-blur-nft-marketplace-shutting-down-frontend-blend-418363 | The Block | 2026-10-12 | 2026-10-13 |
| S13 | https://x.com/mathcastles | Mathcastles X (not readable) | n/a | 2026-10-13 |
| S14 | https://opensea.io/collection/hypercastle-explorers | OpenSea | n/a | 2026-10-13 |
| S15 | https://thousandant.itch.io/hypercastle-explorer | Thousand Ant | n/a | 2026-10-13 |
| S16 | https://verse.works/series/terraforms-by-mathcastles | VERSE (release 2021-12-17) | n/a | 2026-10-13 |
| S17 | https://www.rightclicksave.com/article/digital-art-acquisitions-in-2025-moma-whitney-centre-pompidou | Right Click Save | 2025-12-29 | 2026-10-13 |
| S18 | https://www.artblocks.io/articles/true-onchain-art | Art Blocks | 2026-09-09 | 2026-10-13 |
| S19 | https://whale-alert.io/stories/ea98012535090c/OpenSea-delays-SEA-token-launch-indefinitely-last-Treasure-rewards-wave-refunds-offered-forfeiting-Treasure-and-0-OS2-trading-fees-for-60-days | Whale Alert (secondary) | 2026-03 | 2026-10-13 |
| OC | On-chain: Tenderly/NodeReal public RPC via `scripts/common.py` (eth_call, eth_getLogs, eth_getStorageAt for ERC-1967 impl slot); Blockscout API v2 (verified source `smart-contracts/0x4e1f…`, address tx lists for `0x9f400619…` and `0x7a822bce…`, contract creation txs). Queries 2026-10-13 22:07–22:30 UTC. | — | — | — |

**Could not verify:**
- Public announcement date of Terraforms 2.0/Antenna (only on-chain deploy 2023-12-24).
- What TD(R)unes is and whether "tDR" = The Designers Republic.
- Any 2025–2026 Mathcastles statements.
- Notable collectors' identities (none confirmed beyond Le Random).
- Drivers of the Oct 2022, Dec 2022–Jan 2023 and Sept–Oct 2026 moves.
- Share of tokens opted into V2/Antenna (`tokenToURIAddressIndex` is not public; not computed).
