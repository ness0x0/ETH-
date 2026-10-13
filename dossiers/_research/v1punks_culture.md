# V1 CryptoPunks: cultural durability and catalyst history

_Cultural Researcher / Market Historian workstream. Written 2026-10-13 (UTC). All web sources accessed 2026-10-13._
_Labels: **[F]** = fact with a citation; **[OC]** = verified on-chain by this workstream (method in §1); **[I]** = interpretation or inference; **UNVERIFIED** = could not confirm. Dated events are in `data/processed/catalysts/v1punks.csv`._

**Snapshot (2026-10-13):**
- **Price.** Wrapped-V1 floor is 1.585 ETH (OpenSea and NPF), about $3,970 or 0.0477 BTC.
  - **V1/V2 floor ratio: 5.1%** (V2 floor 31.29 ETH).
  - In ETH: −28% over 1y, −9% over 2y, −49% over 3y. In BTC: −40% over 1y, −30% over 2y, −74% over 3y, −91% from the BTC-terms series high (`screen_metrics.csv`).
- **Holders and activity.** OpenSea: 1,169 owners of the wrapper collection; 30 sales / 52 ETH in the last 30 days.
- **Fees.** No creator royalty.
- **[I] Answer to the key question.** V1s are an **on-chain-authentic historical artifact that every rights-holder and every institution has declined to recognize**. Larva Labs called them "not official" (2022); Yuga said "no current plans" and excluded them from the license; NODE's official timeline omits them; every museum acquisition found is V2.
  - The market prices V1 as a **~5–10% beta-call on V2 Punks** with occasional narrative spikes (Jan 2022 revival, Aug 2025, May 2026 native-market fix).
  - It is a **speculative derivative with a genuine provenance story**, not a durable provenance asset in the institutional sense.

---

## 1. Identity & provenance

- **[OC] Contracts** (Blockscout API, creation txs, queried 2026-10-13):
  - **V1:** `0x6Ba6f2207e343923BA692e5Cae646Fb0F566DB8D` ("CRYPTOPUNKS"), created **2017-06-09 00:22 UTC** by `0xC352B534…`.
  - **V2:** `0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB` ("CryptoPunksMarket"), created **2017-06-22 19:40 UTC** by the **same deployer**. Same 10,000 images and IDs.
- **[F] The bug.** The V1 built-in marketplace credited the paid ETH to the wrong party, so a buyer could receive the Punk and withdraw their ETH. Larva Labs abandoned V1 and airdropped V2 to claimers (V2 airdrop 2017-06-23 per [S1]) [S2][S3].
- **[OC] Wrappers** (competing; all community-made):

  | Wrapper | Address | Deployed | Status (2026-10-13) |
  |---|---|---|---|
  | **WPV1** "V1 Cryptopunks (Wrapped)" | `0x282bdd42…8c5d` | **2022-01-17** by franknft.eth | `totalSupply` 5,125. V1 contract shows it holding **5,130** (5 V1s sit in the wrapper without a wrapped token). OpenSea slug `official-v1-punks` (safelist "verified") |
  | **WPUNKS1** "Wrapped CryptoPunks V1" (0xfoobar, "Classic") | `0xf4a4644e…5114` | **2021-03-25** | Holds 9 V1s; effectively abandoned |

  - Also catalogued: a "V1 Phunks" wrapper (WPHV1) and an "unofficial" WV1PUNKS [S4]. Treat these as distinct, lesser derivatives.
  - **Native venue:** PunksMarket (`punksmarket.app`, jalil.eth, announced **2026-05-18**) trades unwrapped V1s through the original contract using an intermediary contract that calls `withdraw()` and pays the seller [S5][S6].
- **[OC] WPV1 admin powers.** Verified source (`PunksV1Wrapper`):
  - Wrap and unwrap are permissionless.
  - The owner (franknft.eth `0xF40Fd88a…ACC0d`) can only change `setBaseTokenURI`, i.e. the metadata/image pointer (initially `ipfs://Qma3sC19…`).
  - The owner cannot seize or mint Punks.
  - **[I]** Dependence on the wrapper author is limited to metadata display.
- **[OC] Ownership of the 10,000 V1 Punks.** Multicall3 batch of `punkIndexToAddress(i)` at block 26,186,525, 2026-10-13 22:21 UTC.
  - 222 distinct addresses.
  - **WPV1 wrapper 5,130.**
  - **Gnosis Safe `0xa858ddc0…2ef1`: 1,084 unwrapped (+1 WPV1).**
  - Next holders: `0x883dc31e…` 1,005; `0x00bd9fd5…` 506; `0xe45df57d…` 195; `0x26f74471…` 141.
  - **The four largest non-wrapper holders control 2,790 V1s (27.9%).**
- **[OC][I] The 1,084-V1 Safe is very likely Yuga Labs.**
  - It received exactly 1,084 V1s via PunkTransfer from `0x5b098b00…` on **2022-03-17** (block 14,406,058 onward), matching the community record that Larva Labs' 1,084 unwrapped V1s went to Yuga in March 2022 [S7].
  - It holds **414 V2 Punks**, matching the reported 414 Punks Yuga retained after the 2025 IP sale [S8].
  - It has **never sent a V1** (0 outbound PunkTransfer since block 14.3M).
  - **[I]** The 2025 NODE deal did not move them. ~10.8% of V1 supply is a dormant, Yuga-controlled overhang (or a future "burn/donate" catalyst).

## 2. Narrative timeline (condensed; full list in CSV)

| Date | Event | V1 floor / V1:V2 ratio |
|---|---|---|
| 2017-06-09 / 06-22 | V1 deployed; V2 deployed after bug; V2 airdrop 06-23 [OC][S1] | — |
| 2021-03-25 | First V1 wrapper (WPUNKS1, 0xfoobar) [OC] | — |
| 2021-12 | V1 revival: WPUNKS1 wrapping wave from 2021-12-15 [OC] | — |
| 2022-01-17 | WPV1 wrapper (franknft.eth) and OpenSea collection created; 1,322 wraps in Jan 2022 [OC] | — |
| 2022-01-23–26 | Larva Labs side wallet wraps 40, sells 39 V1s (~210–270 ETH) [S7][S9] | — |
| 2022-01-25 | Larva Labs PSA: "'V1 Punks' are not official Cryptopunks… we've got 1,000 of them" [S10] | — |
| 2022-02-01 | #5905 sale reported at 1,000 ETH (Meta4 Capital reported buying two V1s for 1,000 and 200 ETH) [S7][S9] | — |
| 2022-02-02/04 | Larva Labs apologizes ("a bad decision"), matches 210 ETH to Rainforest Foundation, threatens action [S9] | — |
| 2022-02-07 | Larva Labs DMCA; OpenSea delists V1 [S7][S11] | — |
| 2022-03-11 | Yuga buys Punks IP incl. Larva's ~1,085 V1s [S7] | — |
| 2022-03-17 | 1,084 V1s land in the Safe described above [OC] | — |
| 2022-03-18 | V1 relisted on OpenSea (DMCA claim lapsed) [S7][S11] | — |
| 2022-05-18 | Community marketplace with Rarible (v1punks.io) reported [S11] | ~5.0 ETH / ~10% |
| 2022-08-15/18 | Yuga's Punks license covers V2 only; "There are no current plans for V1 Punks" [S12] | 5.0 → 4.15 / 7% → 6% |
| 2022-12 → 2023-01 | 869 wraps by 21 addresses (one wallet 402) [OC] | ~4.7–5.8 / ~7–9% |
| 2023-03 → 04 | Blur-incentive era: Punks $211M in 30 days [S13]; V1 3-day sales spike to 403 (03-24 bar). V1-specific cause UNVERIFIED | ~3.9–4.6 / ~6–8% |
| 2023-10 → 11 | 818 wraps by 9 addresses (one wallet 558) [OC] | ~3.0–3.9 |
| 2025-05-13 | NODE acquires Punks IP; V1 not mentioned [S14] | ~2.0 / ~4.5% |
| 2025-07/08 | Punks rally (whale buying; NFT cap +66% in 30d) [S15]; V1 outperforms V2 | 2.0 → 4.13 (08-28) / 5% → 9% |
| 2025-12-21 | MoMA acquires 8 Punks, all V2 [S16] | ~1.5 / ~6% |
| 2026-01 | NODE's "10,000" exhibition opens in Palo Alto (V2) [S8][S17] | ~1.7 |
| 2026-05-18/19 | **jalil.eth launches PunksMarket: native, wrapper-free V1 trading** [S5][S6] | 1.7 → 2.39 (05-22, 105 sales) → 3.0 (05-28) / ~9.5% |
| 2026-05-25 | V1 #1119 sells natively for 42.69 ETH [OC] | — |
| 2026-07-10 | V1 Alien #2890 sells for 180 ETH via PunksMarket (seller: original minter StrayBits per [S1]); wrapped by buyer 07-15 [OC] | ~2.2 |
| 2026-10-12 | Blur frontend shutdown announced (2026-11-12) [S18] | 1.585 / 5.1% |

## 3. Founder/team dependence and team status (as of Oct 2026)

- **[F] There is no "team".** V1 has no issuer, no roadmap and no treasury. The creators (Larva Labs) disowned it; the IP holders (Yuga 2022–25, NODE since 2025-05-13) have not recognized it [S10][S12][S14].
  - NODE's official CryptoPunks timeline (2017–2026) does not mention V1 [S17].
- **[F] Community infrastructure is run by individuals:**
  - FrankNFT (WPV1 wrapper owner) is active on-chain in Sept 2026 [OC].
  - jalil.eth built PunksMarket (May 2026) and is building networked.art, an auction house with ygg and Jack Butcher, which may support V1+V2 pair auctions [S5][S6].
  - A community X account and wiki exist [S7].
- **[I] Dependence is unusual:**
  - **Artwork/ledger survival:** none. V1 is immutable 2017 Larva Labs code.
  - **Legitimacy:** high, and adverse. Legitimacy depends on V2 rights-holders, who have every incentive not to bless a second 10,000-unit Punks supply.
  - **Liquidity:** depends on wrappers and PunksMarket, both maintained by individuals.

## 4. Tokens, airdrops, companion collections, incentives — and their effects

- **[F] No token, airdrop or staking.** V1 holders have **no commercial IP license** (Yuga 2022 license is V2-only [S12]). NODE's terms for V1: UNVERIFIED (none found).
- **[F] Incentive-driven liquidity:**
  - Blur listing/bidding incentives in 2023 drove wrapped-Punks volume [S13]. V1 trade counts spiked in Mar–Apr 2023 (NPF). **[I]** Likely the same incentive-farming dynamic (0% royalty, cheap flips). The V1-specific link is UNVERIFIED.
  - Blur's frontend closure (2026-11-12) removes one venue [S18].
- **[OC] Native-market reboot (2026).**
  - PunksMarket produced **29 paid native V1 sales May–Sept 2026** (May 10, Jun 4, Jul 3, Aug 10, Sep 2), out of 165 PunkBought events (most are 0-value wraps). Range: V1 contract logs over the last ~1.1M blocks, 2026-10-13 22:33 UTC.
  - **97 unwraps from WPV1 in May 2026** (vs ~0–20/month before).
  - **[I]** Some holders are moving from wrapped to "original-contract" form. This could split liquidity further.

## 5. Controversies & reputation

- **[F] Origin controversy (2022):**
  - Larva Labs publicly disowned V1 while its own side wallet had sold 39 wrapped V1s.
  - It apologized and donated, then issued a DMCA takedown that delisted V1 from OpenSea until the claim lapsed after the Yuga sale [S7][S9][S10][S11].
  - **[I]** This left V1 with a permanent "the artists don't want this" stigma, and a counter-narrative that V1 is "more punk" [S19].
- **[F] Ongoing provenance debate (2026):**
  - After the PunksMarket fix, collectors split.
    - Sean Bonner called it "a technical achievement solving a technical puzzle, not a sales strategy." Elsewhere he argues V1s are real and Larva Labs' stance is inconsistent [S19][S20].
    - Others argue Punks culture grew around V2 [S19].
  - Beeple made V1 Punks the subject of an Everydays work (per [S19]; UNVERIFIED independently).
- **[F] Thin-market price prints.**
  - The early 1,000 ETH #5905 sale is reported but not independently explained [S7][S9].
  - Gazette's "floor roughly doubled to ~4 ETH" after the fix [S19] is not matched by NPF 3-day floors (max 3.0 ETH, 2026-05-28 bar).
  - **[I]** Use on-chain/NPF data, not fan-press numbers.

## 6. Community continuity through downturns (evidence)

- **[OC] Wrapped supply has grown in waves:** Jan 2022 1,322; Dec 2022–Jan 2023 869; Oct–Nov 2023 818. Each wave was dominated by a handful of 2017-claimant wallets.
  - **[I]** Large holders periodically convert dormant V1s into tradable supply. That is a recurring source of sell pressure, not a sign of new demand.
- **[F] Holders.** 1,169 wrapped-collection owners (OpenSea) plus 222 addresses holding unwrapped V1s (incl. the wrappers) [OC].
- **[F] Builders keep returning.** WPUNKS1 (2021), WPV1 (2022), Rarible-based v1punks.io (2022), PunksMarket (2026) [S5][S11].
  - **[I]** Real, if small, cultural persistence across four years without any issuer support.
- **[I] Price persistence is weak.** The floor fell from ~5.4 ETH (May 2022) to ~1.5 ETH (2024) and back to 1.585 ETH now. The V1:V2 ratio compressed from ~6–10% (2022–23) to ~4.5–6% (2025–26), apart from short spikes (9% Aug 2025, 9.5% May 2026).

## 7. Competitive threats / displacement

- **[I] V2 Punks are the substitute and the gravity well.** Every institutional and IP-holder action (NODE museum program; MoMA, Toledo, Pompidou, LACMA, ICA Miami, ZKM [S16][S17]) reinforces V2. Rising V2 prestige helps V1 only via the "cheap Punk-adjacent" trade.
- **[I] Supply/derivative competition.** Phunks, V1 Phunks, Punk derivatives and the Yuga-held 1,084 V1s all compete for "cheap Punk exposure" demand.
- **[I] Venue risk.** Blur closure; OpenSea's continued listing is at OpenSea's discretion. It was removed once via DMCA in 2022, and NODE now holds the IP.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

- **[I] There is no team to vanish.** V1's 2028 demand depends on two things outside its control:
  - **(a) V2 Punks' price**, since V1 trades as a fraction of it.
  - **(b) Whether NODE/IP holders or major institutions ever acknowledge V1** as part of the CryptoPunks story.
- If NODE were to burn, donate or exhibit Yuga's 1,084 V1s, or museums began pairing V1+V2, V1 could re-rate.
- If NODE enforced IP (e.g., DMCA), V1 could be delisted again. **[I]** That is the key tail risk, and it has a 2022 precedent.

## 9. Possible future manufactured catalysts (separate from the collectible thesis)

- **[I] Speculative:**
  - **networked.art V1+V2 pair auctions** (jalil.eth/ygg/Jack Butcher) [S6].
  - **More native-contract sales** of rare V1s (aliens, apes, zombies) setting headline comps. 180 ETH Alien in Jul 2026 [OC].
  - **Yuga/NODE action on the 1,084 V1s**: sale (bearish overhang realized), burn or donation (bullish), or legal action (bearish).
  - **V2 Punks macro moves** (e.g., Jul–Aug 2025) and **ETH/BTC**.
  - **Marketplace incentive regimes** (Blur 2023 precedent; OpenSea SEA TGE postponed indefinitely [S21]).

## 10. Strongest bull thesis & strongest bear thesis

- **Bull [I]:**
  - V1s are the literal first CryptoPunks contract, deployed by Larva Labs 13 days before V2, with identical art. They are the oldest Punks on Ethereum, with a dramatic, well-documented story.
  - The 2026 PunksMarket fix makes the original contract tradable "as intended".
  - The liquid float is ~5.1k wrapped, with 28% of supply in four dormant wallets.
  - At **5% of the V2 floor**, a re-rating to the May 2022 ratio (~10%) would double the price even with flat V2. Any NODE/museum nod would be a step-change.
  - $7k buys one floor V1 plus change.
- **Bear [I]:**
  - The artists disowned it; the IP owner of record (NODE, a museum-facing nonprofit) has ignored it; every museum has chosen V2; holders have no IP license.
  - A Yuga-controlled 1,084-unit block (10.8%) plus several 500–1,000-unit whale wallets can flood the market. Past wrap waves preceded weak prices.
  - The ratio to V2 has compressed from ~7–10% (2022–23) to ~5% over four years. For a BTC-benchmarked holder, it is a leveraged bet on V2 Punks *and* on a legitimacy shift that has repeatedly failed to arrive.
  - DMCA/delisting precedent exists.

## 11. Sources

| # | URL | Publisher | Date | Accessed |
|---|---|---|---|---|
| S1 | https://www.theboredapegazette.com/post/v2-punks-are-not-alone-a-v1-alien-cryptopunk-sells-for-180-eth-or-312k-months-after-jalil-patched | Bored Ape Gazette (fan outlet) | 2026-07-10 (inferred; page shows "July 10") | 2026-10-13 |
| S2 | https://seanbonner.com/2022/02/13/explaining-cryptopunks-versions/ | Sean Bonner blog | 2022-02-13 | 2026-10-13 |
| S3 | https://www.bankless.com/read/v1-cryptopunks-trade-original-again | Bankless (W. Peaster) | 2026-05-19 | 2026-10-13 |
| S4 | https://github.com/cryptopunksnotdead/awesome-cryptopunks-bubble/blob/master/PUNKS_V1_NOTES.md | GitHub community notes | n/a | 2026-10-13 |
| S5 | https://www.bankless.com/read/v1-cryptopunks-renaissance | Bankless | 2026-05-19 | 2026-10-13 |
| S6 | https://cryptopunks.networked.art/ | Punks SDK docs (jalil.eth) | 2026 | 2026-10-13 |
| S7 | https://v1punks.gitbook.io/cryptopunks-v1-wiki/notable-events-in-2022 ; https://v1punks.gitbook.io/cryptopunks-v1-wiki/wrapping | V1 Punks community wiki | n/a | 2026-10-13 |
| S8 | https://thedigitalarttimes.substack.com/p/cryptopunks-after-the-20-million | Digital Art Times (cites NFT Now for "Yuga kept 414 Punks") | 2026-08-14 | 2026-10-13 |
| S9 | https://decrypt.co/92155/cryptopunks-controversy-creators-apologize-v1-ethereum-nft | Decrypt | 2022-02-04 | 2026-10-13 |
| S10 | https://x.com/cryptopunks/status/1486092138534387712 | Larva Labs / CryptoPunks X (via search snippet; post time 2022-01-25 21:42 UTC from snowflake ID) | 2022-01-25 | 2026-10-13 |
| S11 | https://decrypt.co/100692/v1-cryptopunks-rarible-marketplace-larva-labs-dispute | Decrypt | 2022-05-18 | 2026-10-13 |
| S12 | https://decrypt.co/107740/no-current-plans-for-v1-cryptopunks-nfts-yuga-labs | Decrypt (Andrew Hayward) | 2022-08-18 | 2026-10-13 |
| S13 | https://www.theblock.co/post/225954/cryptopunks-210-million-hot-streak-fueled-by-added-liquidity-and-blur-incentives | The Block | 2023-04-12 | 2026-10-13 |
| S14 | https://www.theblock.co/post/354114/yuga-labs-sells-cryptopunks-ip-to-nonprofit-infinite-node-foundation | The Block | 2025-05-13 | 2026-10-13 |
| S15 | https://www.coindesk.com/markets/2025/07/25/crypto-whale-spends-usd4-3m-on-cryptopunks-as-nft-market-cap-climbs-66-in-30-days | CoinDesk | 2025-07-25 | 2026-10-13 |
| S16 | https://www.theblock.co/post/383446/moma-adds-cryptopunks-and-chromie-squiggles-nfts-to-permanent-collection-following-coordinated-donation | The Block | 2025-12-21 | 2026-10-13 |
| S17 | https://nodefoundation.com/cryptopunks | Infinite Node Foundation | accessed 2026-10-13 | 2026-10-13 |
| S18 | https://www.theblock.co/news/ecosystems/2026-10-12-blur-nft-marketplace-shutting-down-frontend-blend-418363 | The Block | 2026-10-12 | 2026-10-13 |
| S19 | https://www.theboredapegazette.com/post/are-punks-the-next-punks-jalil-eth-found-a-fix-for-the-original-cryptopunks-v1-contract-sparking | Bored Ape Gazette (fan outlet) | ~2026-05-20 | 2026-10-13 |
| S20 | https://decrypt.co/121238/lacma-art-museum-nft-donation-cryptopunk-art-blocks | Decrypt (Pompidou/LACMA context) | 2023-02-14 | 2026-10-13 |
| S21 | https://whale-alert.io/stories/ea98012535090c/OpenSea-delays-SEA-token-launch-indefinitely-last-Treasure-rewards-wave-refunds-offered-forfeiting-Treasure-and-0-OS2-trading-fees-for-60-days | Whale Alert (secondary) | 2026-03 | 2026-10-13 |
| OC | On-chain: Tenderly/NodeReal public RPC via `scripts/common.py`; Multicall3 `0xcA11bde0…CA11` aggregate of `punkIndexToAddress` (block 26,186,525); V1 contract PunkTransfer/PunkBought logs (blocks 14.3M–26.19M; last ~1.1M blocks for PunkBought); WPV1/WPUNKS1 Transfer mint/burn logs (blocks 13.6M–26.19M); Blockscout API v2 for creation txs and verified source. Queries 2026-10-13 21:53–22:37 UTC. Dates for monthly log aggregates use block→time interpolation (±hours). | — | — | — |

**Could not verify:**
- NODE's explicit position on V1 (only omission observed).
- Any auction-house V1 lot.
- Whether `0xa858…` is formally labeled Yuga (strong on-chain inference only).
- The identity of the 1,005- and 506-V1 wallets.
- The V1-specific driver of the Aug 2025 outperformance.
- The OpenSea supply figure (5,154) vs on-chain `totalSupply` (5,125).
