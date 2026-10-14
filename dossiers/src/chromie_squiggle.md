# Chromie Squiggle (Art Blocks project 0, Snowfro) — dossier

Contract `0x059edd72cd353df5106d2b9cc5ab83a52287ac3a`, tokenIds 0–9999. The full culture and catalyst research with
sources is in [`_research/chromie_squiggle_culture.md`](_research/chromie_squiggle_culture.md). Catalysts are in
`data/processed/catalysts/chromie_squiggle.csv`. Chart: `reports/charts/chromie_squiggle_history.png`.

<!-- VERDICT -->

<!-- TABLES -->

## 1. Cultural durability thesis

- **It is the "first page" of on-chain long-form generative art.** Squiggle is project #0 of the platform that defined
  the 2020–22 generative-art movement. The script is **locked on-chain**, so the artist or admin can no longer change
  it. Supply is **fixed at 10,000** (the last token was minted 2024-08-21 for LACMA). Art Blocks reports that all
  AB500 works render from Ethereum alone (2026-09-09).
- **Institutional anchoring is the strongest of any affordable ETH NFT:**
  - **MoMA** received 8 Squiggles (a complete type set) by coordinated donation (The Block, 2025-12-21; verified
    independently).
  - **LACMA** holds #9999.
  - **Toledo Museum** exhibited 9 Squiggles in 2025. On-chain evidence suggests only 2 sit in Toledo's wallet; the
    rest were likely loans.
- **The founder-vanishes test: passes.** The art, the provenance and the museum holdings don't need Art Blocks or
  Snowfro. Art Blocks is in retrenchment: the curated program ended with the "Art Blocks 500", and there are reports of
  a release pause. If the company disappeared, the loss would be a demand-generator (events, marketplace), not the
  asset.
- **Caveat: what the floor actually is.** The floor is a common "Normal" Squiggle (~60% of supply). Museum and
  auction demand concentrates in rare types (Perfect Spectrum, HyperRainbow) and complete sets. Validation of the
  category does not transmit fully to floor tokens.

## 2. Historical valuation & catalysts

- **Price path.** Series peak 16.4 ETH (2023-01-11 bar, during the generative-art rotation; cause unverified). The
  2021 record sale was 945 ETH for a rare token. The floor fell to ~3.2 ETH by Aug 2024, rose to ~5.75 ETH in the
  Aug-2025 ETH rally, and is 2.64 ETH now.
- **What moved it.** Art Blocks' own events and institutional news produced **no durable effect**:
  - MoMA donation (coordinated by holders and SquiggleDAO; not a purchase): +18% vs BTC at 30 days, −5% at 90 days.
  - LACMA announcement: −36% at 90 days.
  - Toledo opening: +114% at 30 days, but overlapping the Jul-2025 macro rally.
  - The only meaningful driver has been ETH/NFT beta (β ≈ 1.07 to ETH/BTC).
  - The Jan-2023 peak coincided with Blur-era airdrop farming and a sector-wide generative-art bid.
- **No token or airdrop distortion** in its history. The Friendship Bracelets claim (2022) and *send/receive* (2025)
  were negligible.

## 3. Collector behaviour

- **The most dormant supply of the nine finalists:** median token age 1,848 days; 84% of supply untouched for 24
  months; 79% of EOA holders from two years ago still hold.
  - This is partly *illiquidity*, not demand. One minter entity holds 13.1% (990 tokens untouched in the minting
    wallet since 2020–21), and Safes hold 10.5%.
- **High-quality but small turnover:**
  - Only 20% dealer churn. All of the 675 trailing-year sales went through Seaport and none through Blur. The 8.5%
    seller fee makes dealer flipping uneconomic.
  - **45% of purchases went to first-time wallets**, the highest *share* of the nine. In *level* terms that is
    ~283 new buyers (402 unique), against ~1,460 for Pudgy and ~1,390 for Milady. New wallets absorbed a net +540
    tokens.
- **Concentration risk.** One original minter (`0xd110…e588`) still holds 990 (9.9%); with three linked wallets the
  entity holds 1,314 (13.1%). Identity is unverified. A sale programme by this holder would overwhelm ~1.5 organic
  sales/day.
- **No Blend exposure.** Lending escrow is 1.0% (Gondi and NFTfi) and fell from 250 a year ago. **The floor did not
  react to the Blur shutdown**, unlike the PFPs.

## 4. Liquidity

Liquidity is the weakest point:
- Best funded bid is **78% of floor**, with zero bids at ≥80%.
- Sellers pay **8.5%** (1% marketplace plus a 7.5% enforced creator royalty).
- A whole-budget position is one token, and the instant round trip loses ~29%.
- Exit realistically means listing near the floor and waiting days. The median organic gap is ~9–11 hours, and
  buyers at size are scarce.

## 5. Failure mechanisms

- **Generative art becomes a closed historical niche** (Christie's closed its digital department in 2025). The floor
  drifts with ETH/BTC and the sector, even while institutions hold rare pieces.
- **A large holder distributes** (the 13% entity; pre-2024 holders net sold 220 in the last year).
- **Marketplace attrition** (Blur, Reservoir, Christie's digital): fewer bids, wider spreads.
- **The royalty regime persists**, a structural ~7.5% drag on every exit.
- **Not material:** contract or provenance risk (the script is locked; supply is fixed).

## 6. Bull thesis / bear thesis

- **Bull.** The single most defensible "survives to 2029" *object* under ~$8k on Ethereum. The artwork is immutable
  and founder-independent, the institutional holdings (mainly donations coordinated by the founder and holders)
  canonize the category, and it still attracts first-time buyers. At 0.08 BTC it sits 94%
  below its BTC-terms peak. In an NFT revival, "blue-chip generative art at the first-page price" is an obvious
  rotation target, as in Jan 2023.
- **Bear.** None of that has protected the price:
  - −35% vs BTC in the last year, −86% over 3 years.
  - Museum validation has had zero durable price effect.
  - Its rally convexity is the lowest of the finalists.
  - Fees and the bid gap make it expensive to trade.
  - It is effectively a single, illiquid, high-beta ETH position with a royalty tax. A collector is paying for
    cultural certainty that the market has not been willing to price.

## 7. Entry conditions & what would change the view

- **Entry.** Use bids, not asks. Buyers who lifted asks paid ~22% more than the best bid. A bid of ~2.2–2.3 ETH
  (≤~0.07 BTC) is a reasonable patience level given the 2026 range of 2.0–2.9 ETH (NPF).
- **Upgrade if:**
  - Floor sales sustain >3/day with a shrinking ask stack.
  - Rare-type auction comps rise.
  - Another institutional acquisition is followed by floor strength rather than a fade.
- **Downgrade if:** the 13% entity starts distributing, or royalty enforcement widens.
