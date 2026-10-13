# Terraforms (Mathcastles) — dossier

Contract `0x4e1f41613c9084fdb9e34e11fae9412427480e56`. The full research with sources is in
[`_research/terraforms_culture.md`](_research/terraforms_culture.md). Catalysts are in
`data/processed/catalysts/terraforms.csv`. Chart: `reports/charts/terraforms_history.png`.

<!-- VERDICT -->

<!-- TABLES -->

## 1. Cultural durability thesis

- **A fully on-chain, dynamic "world artwork".** Each token is a parcel of a 20-level Hypercastle rendered at runtime
  from Ethereum, and holders can "dream" and "terraform" their parcel. It is respected among on-chain-art collectors
  and has engaged holders: 1,913 dreamers, 5 tokens per holder.
- **The founder-vanishes test: partial.**
  - The original (V0) art is immutable and works forever.
  - The investment narrative ("living artwork that keeps receiving broadcasts") depends on Mathcastles, an anonymous
    two-person team.
  - The newer v1/v2 renderers and the Antenna system are team-controlled upgradeable proxies.
- **No institutional anchoring** found: no museum holdings and no major auction comps.

## 2. Historical valuation & catalysts

- **Its best re-rating was structural:** writing three.js and p5.js into EVM storage (Sept 2022) gave +243% vs BTC at
  90 days. It then co-peaked with Squiggle in the Jan-2023 generative-art rotation (3.45 ETH), and fell ~97% vs BTC
  after.
- **Team releases did not re-rate it durably:** Terraforms 2.0/Antenna (Dec 2023): −3% at 90 days. Angelus: −8%.
- **A new signal.** On 2026-07-14 Mathcastles deployed an empty "TD(R)unes — tDR x Mathcastles" contract. The
  inference that tDR is The Designers Republic is unverified, and nothing has been announced.

## 3. Collector behaviour

- **Excellent retention:** 74% of supply untouched for 24 months; 78% of holders retained; median token age 1,347
  days.
- **Concentration:** top-50 hold 42%, and Safes hold 12.7% (two Safes with 333 and 268).
- **Bid dependence:** one entity made **13.5% of all trailing-year purchases** (net +129, mostly by filling floor
  bids). If it stops, the bid side thins visibly.
- **Lending:** Gondi only, 58 (0.6%). No Blend. It did not sell off in the Blur shock.

## 4. Liquidity

- Best bid is 90% of floor, but only 4 funded bids sit at ≥80%.
- A budget-sized position is ~9 tokens. Building it costs ~10% above floor on the instant book, and the instant
  round trip loses ~28%.
- Organic turnover is ~2.5/day.

## 5. Failure mechanisms

- **Dilution.** The owner EOA (not a multisig) can still mint **1,193 more tokens (+12%)** via `ownerClaim`. There is
  no lock. Only 7 of the 1,200 allotment have been used in ~4.8 years.
- **Team risk.** A compromised key or a team departure freezes the living features. The upgradeable renderers can be
  changed.
- **The bid-side buyer** (13.5% of purchases) stops or reverses.
- **Niche status.** No museum or auction anchor; the category is shrinking.

## 6. Bull thesis / bear thesis

- **Bull.**
  - A genuinely novel on-chain artwork with an active, engaged collector base. Best 1-year BTC-relative performance of
    the finalists (−11%).
  - Tiny floor cap (~$7.5M).
  - An unrevealed outside-studio collaboration is being prepared.
  - The 2022 precedent shows technical or structural events re-rate it sharply.
  - About $750 a parcel makes it a granular, option-like position.
- **Bear.**
  - Founder-dependent by design, with a latent 12% mint.
  - Down 96.6% vs BTC from peak.
  - No institutional anchor.
  - Price support relies on one large bidder.
  - Exits are slow and expensive.

## 7. Entry conditions & what would change the view

- **Entry.** Only as a small satellite. Bid ≤ ~0.27 ETH (current best bid); the 2026 median was ~0.25.
- **Upgrade if:**
  - The owner renounces or locks the 1,193-token allotment.
  - TD(R)unes is announced with a credible partner.
  - A museum acquisition.
- **Downgrade if:**
  - Any `ownerClaim` use.
  - The large bidder distributes.
