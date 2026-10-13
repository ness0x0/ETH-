# Milady Maker: cultural durability and catalyst history

*Cultural Researcher / Market Historian workstream. Written 2026-10-13. All web sources were accessed 2026-10-13.*
Contract `0x5af0d9827e0c53e4799bb226655a1de152a425a5` · supply 10,000 (9,976 per OpenSea) · issuer Remilia Corporation.
Floor 0.744 ETH (OpenSea, 2026-10-13), about $1,866 or 0.0224 BTC. NPF ATH 6.34 ETH (2024-12-07 bar); BTC-terms ATH 0.2835 BTC (2024-06-28).

Companion files:
- Catalyst list: `data/processed/catalysts/milady.csv` (40 rows).
- Event-window returns: `data/processed/culture/event_windows.csv`.
- Quiet-window returns: `data/processed/culture/quiet_windows.csv` and `quiet_window_returns.csv`.
- On-chain CULT price samples: `data/processed/culture/cult_price_samples.csv`.
- Raw data: `data/raw/culture/`.
- Script: `scripts/culture_event_windows.py`.

**Labels:** [F] = fact with a source; [OC] = verified on-chain by this workstream; [I] = interpretation or speculation; UNVERIFIED = tried and could not confirm.

---

## 1. Identity and provenance

- [F] Milady Maker is a 10,000-piece generative "neochibi" PFP collection by **Remilia Corporation**. Remilia describes itself as an avant-garde net-art collective that treats posting as an art form, and it is run by **Charlotte Fang** (legal name Krishna Okhandiar, per court filings reported by Bitcoin.com, 2023-09-14).
  - Remilia says it was founded in Jan 2021. Ex-colleagues dispute this: they say the venture was a joint art collective formed in Sept 2021 (CryptoPotato, 2023-09-26).
- [F] Its intellectual lineage is "network spirituality", from Remilia's show *I Long For Network Spirituality* (Hunters & Collectors, NZ, and online, June 2021), plus the *New Net Art Manifesto* (March 2022). Its social scene is the 2021–22 NYC "Vibe Shift" / downtown and post-left-internet world (Remilia wiki; The Block, 2022-07-19).
- [OC] **Mint.** The first mints were at block 13,090,452 (2021-08-24 21:13 UTC). Paid public mints at **0.08 ETH** began 2021-08-25 03:57 UTC.
  - The Remilia wiki says the mint completed on 2022-04-19, about eight months later; IQ.wiki says March 2022. The slow sellout means the community was not built on a hype mint.
- [F] **Licence.** Remilia releases its assets under the "Viral Public License" (Remilia wiki). Holders actively encourage people to copy the Milady avatar *without owning one* (Unchained, 2025-01-21).
  - [I] This helps the meme spread, but it weakens the link between cultural reach and NFT demand.
- [F] **Remilia ecosystem (official).**
  - Remilio Babies (Aug 2022).
  - Bonkler (Apr 2023; daily treasury-backed auctions, halted Sept 2023).
  - Kagami Academy with FRUiTS (Jan 2024).
  - Remilia Quarterly (May 2024).
  - **$CULT** (presale June 2024, token generation event (TGE) Dec 2024).
  - RemiliaNET (Sept 2025).
  - Remilia Atelier and HIKKI PUNKS fashion lines (Feb and Mar 2026).
  - Recurring "Milady Raves" (NYC, London, LA, Denver, Tokyo, Warsaw, St Petersburg, 2021 to 2026).
  - MiladyCraft Minecraft server.
  - (Sources: Remilia wiki, Remilia blog, Business Wire.)

## 2. Narrative timeline (key dated events; the full list is in the CSV)

| Date | Event | Floor context (NPF 3-day bars; see the caveat below) |
|---|---|---|
| 2021-08-24/25 | Mint opens at 0.08 ETH [OC] | n/a |
| mid-Apr 2022 | Pre-scandal peak, a little over $6k (The Block) | n/a |
| ~2022-05-05 | CoinDesk story on the founder's past. Exact date UNVERIFIED (secondary sources only) | |
| **2022-05-21** | Fang admits being "Miya" (abusive and extremist 4chan-adjacent account) and "steps down". The step-down was later called performative | The Block: floor fell 1.44 to 0.25 ETH (−82%, CryptoSlam); >1,000 holders sold that week |
| 2022-05-23 | 0xngmi thread compiling Miya's posts; floor briefly below $500 | NPF low about 0.15–0.26 ETH |
| Jun–Jul 2022 | Recovery with **no verified catalyst** | 0.26 to 0.85 ETH by late July |
| **2022-08-11** | Remilio Babies mint (0.125 ETH) [OC] | Milady 0.65 to 0.36 over the next 3 weeks |
| Jan 2023 | Rally with no Remilia-specific catalyst verified (broad NFT rally; Remilio sellout 2023-01-19) | 0.70 to 1.5 |
| 2023-04-11 to 21 | Milady Rave Tokyo and Bonkler launch (first auction about 60 ETH) | 1.0 to 1.7 by mid-April (PEPE memecoin season overlaps) |
| 2023-05-07 | **LADYS** memecoin launched (unaffiliated) and airdropped to Milady/PEPE holders | |
| **2023-05-10** | **Elon Musk** posts a Milady image reading "There is no meme. I love you." | Decrypt: 3.75 to 5.25 (+57%). Cointelegraph: 3.8 to 7.3 intraday. The Block: 7,433 ETH OpenSea volume. **30 days later the NPF floor was −5% vs the pre-tweet bar** |
| 2023-07-14 | Binance Awards "NFT Project of the Year" | |
| **2023-09-11** | **"Bonkler 9/11"**: developer allegedly diverts about $1M of fees; three social accounts seized; Fang sues three contractors (D. Nev.); Bonkler mint halted for good | **3.31 to 2.15 (−35%) in one bar; −47% in BTC over 30d** |
| 2023-09-22 | Ex-colleagues' countersuit (Delaware Chancery) alleging Fang took more than $600k, then $1.7M, from the treasury and removed them from the multisig | Outcome UNVERIFIED |
| Oct 2023 – Mar 2024 | No Remilia catalysts (quiet window). Broad crypto/ETF rally | 1.8 to 4.1 (+130% ETH) |
| **2024-03-16** | Remilia treasury wallets drained (ETH plus NFTX-staked Miladys liquidated); Fang claims a hack | One-bar dip to 2.04, recovered within days |
| 2024-05-22 | +35% intraday move with "no clear catalyst" (The Defiant) | 4.0 to 5.8 intraday |
| **2024-06-13** | **CULT presale announced**: holder tiers for Milady and Remilio; BAYC/MAYC wallets pay a 10% premium; about $20.5M raised in about a week | 4.3 to 5.2 by early July |
| 2024-11-05 to 12-07 | US election rally, then the run-up to the CULT TGE | 4.1 to **6.34 (NPF ATH, 2024-12-07 bar)** |
| **2024-12-09 00:04 UTC** [OC] | **CULT TGE** and seed airdrop (about 25B CULT; weighting about 80% NFT holdings, 20% merch/achievements) | **6.34 to 5.00 within one bar; −41% ETH and −49% BTC over 30 days; −70% BTC over 90 days** |
| 2024-12-11 | Whitepaper v2: supply ×10 to 100B; roadmap pushed back two quarters | |
| **2025-01-18 23:25 UTC** [OC] | `vitalik.eth` (0xd8dA…6045) buys **#9286 for 5.82 ETH** and adopts a Milady PFP ("wartime mode"); Stani Kulechov follows | 3.41 to 5.07 (+49%) within about a week; BTC-terms 30d ≈ 0%; 90d −55% |
| 2025-02 to 2025-09 | **Longest quiet window**, no verified Remilia catalysts. CULT Manipulation Round 1 (Q2 2025) not evidenced | 4.72 to 1.94 (−59% ETH, −46% BTC) |
| 2025-09-19 | RemiliaNET alpha ("social credit score", feeds future CULT "manipulation rounds") | −25% ETH over 30d |
| 2025-10-10 | Market-wide ~$19B liquidation cascade | 1.69 to 0.99 by 2025-11-05 |
| **2026-01-01** | Vitalik: "Welcome to 2026! Milady is back." Milady PFP again | Reported 0.84 to 1.07 intraday (Crypto Times). NPF 0.69 to 1.18 by mid-Jan, then back to 0.90 by 2026-02-03 |
| 2026-02-11 | Remilia Atelier × Elena Velez (NYFW) | 1.03 to 1.37 by 2026-03-02 (thin volume) |
| 2026-03-13 | Ethereum Foundation "EF Mandate" (CROPS) uses Milady-inspired design. Backlash over "milady purity tests" (The Block, 2026-03-27) | Flat |
| 2026-07-15 | Remilia announces a book, *The Exegesis of Miya Black Hearted Cyber Angel Baby* | |
| 2026-10-12 | Blur announces frontend closure (2026-11-12); Blend stops new loans | 0.93 (Oct 7) to 0.744 (Oct 13); the decline started before the announcement |

**Data caveat:** NPF bars appear to be trailing 3-day windows, labelled by the end date, with window-minimum floors. Single-bar artefacts exist (2022-05-22, 2023-05-20, 2024-03-18). Use 30d/90d windows for event studies.

**Explicit low-catalyst ("quiet") windows**, for evaluating price behaviour without promotion. Returns are from `quiet_window_returns.csv`.

| Window | Inside | ETH | BTC |
|---|---|---|---|
| 2022-06-01 → 2022-08-09 | Milady Rave 5 only | +86% | +132% |
| 2022-08-15 → 2023-01-10 | Minor raves and a Substack rebuttal | +80% | +73% |
| 2023-06-01 → 2023-09-09 | Binance award (minor) | −6% | −14% |
| 2023-10-01 → 2024-03-14 | Kagami Academy (minor); ETF-era rally | +130% | +112% |
| 2024-03-25 → 2024-06-12 | none verified | +24% | +30% |
| **2025-02-01 → 2025-09-09** | none verified | **−59%** | **−46%** |
| 2025-09-24 → 2025-12-30 | Oct-10 macro shock | −48% | −53% |
| **2026-03-28 → 2026-10-10** | Remilia product posts only | **−28%** | **−28%** |

[I] The 2022–24 quiet windows were positive, as the collection rebuilt from the scandal low during a rising NFT/crypto tape. Every quiet window since the CULT TGE has been strongly negative in both ETH and BTC terms. Post-2024 price support has depended on discrete celebrity or token events, and each one faded within 1–3 months.

## 3. Founder/team dependence and company status (as of Oct 2026)

- [F] **Founder-centric.** Fang is creative director, public voice and controller of treasury and social accounts. The 2023 suits on both sides centre on whether Remilia is Fang's company or a partnership.
  - No ruling or settlement was found for either the Nevada or the Delaware suit (UNVERIFIED; searched 2026-10-13).
- [F] **The company is operating in 2026.**
  - HQ moved to Irvine, CA in Jan 2025; it also has a Korea office and a fashion team (Remilia wiki).
  - Chief of Staff Michael Dragovic is quoted by Decrypt (2025-09-19).
  - The Remilia blog has regular posts through **2026-08-26**: RemiliaNET v0.7–v0.8.1 (developer API, 2026-08-10), Milady Rave Tokyo (2026-05-08), St Petersburg rave (2026-08-26), Miya book pre-release (2026-07-15), HIKKI PUNKS streetwear (2026-03-13/20), Remilia Atelier (2026-02-11).
  - No posts were found for Sept to mid-Oct 2026.
  - Headcount and revenue: unavailable.
- [OC] **CULT treasury overhang.**
  - The CULT contract holds **53.1B CULT (53% of supply)**. That is down from 57.9B at TGE and **unchanged since Dec 2025**.
  - The claim contract that received 40B at TGE still holds 5.88B, presumably unclaimed.
  - [I] Combined with no news of a 2025 or 2026 "Manipulation Round", this suggests the scheduled holder distributions (15% Q2 2025, 20% Q2 2026, 15% Q2 2027) have not been delivered as written, or are being done off this address (UNVERIFIED).
- [I] **Dependence assessment: HIGH for catalysts, MEDIUM for culture.** Almost every positive price event since 2023 was either Remilia-manufactured (Bonkler, CULT) or a third-party celebrity gesture (Musk, Vitalik) that Remilia's culture attracted. Every major negative event apart from macro was a Fang or Remilia governance event: Miya 2022, Bonkler coup 2023, treasury drain 2024, CULT sell-the-news 2024.

## 4. Tokens, airdrops, companion collections: measured and perceived price effects

| Item | Date | Measured effect (NPF floor) | Comment |
|---|---|---|---|
| Remilio mint (companion) | 2022-08-11 | 30d: −48% ETH, −43% BTC | [I] diluted attention and capital in a bear market; not provable |
| Bonkler (companion) | 2023-04 | Milady rising already; 30d after 04-11: +64% | Overlaps the PEPE season and the Musk post |
| LADYS (unaffiliated memecoin airdrop) | 2023-05-07 | Mixed into the Musk event | DWF Labs put $5M into LADYS (2024-06-03), not into Remilia. LADYS market cap now about $6–8M (Datawallet; aggregator) |
| CULT presale announcement | 2024-06-13 | 30d +10% ETH/+12% BTC; 90d −42% BTC | Promised TGE within 45 days; it took about 6 months |
| **CULT TGE/airdrop** | **2024-12-09** | Run-up: 4.1 to 6.34 (Nov to Dec 7). Post: **30d −41% ETH / −49% BTC; 90d −70% BTC** | Classic airdrop sell-the-news |
| CULT token price (on-chain pool `0xc4ce8e63…`) [OC] | | $0.0057 (launch, FDV about $570M) → $0.0019 (2025-01-01) → $0.00071 (2025-04-01) → $0.00026 (2025-12-01) → **$0.000117 (2026-10-13, FDV about $11.7M)** | **−98% USD and −97% ETH-terms since launch.** CoinGecko ATH $0.00772 (2024-12-08) |
| Value of the airdrop per Milady (illustrative) | | Arkham: GCR received 174.9M CULT (about $1M at the time) holding 150 Miladys, about 1.17M CULT each, worth about $6.6k at launch | **Worth about $135 today** [I]. Per-NFT allocation was never published, and GCR's figure may include other achievements |
| Vitalik purchase/PFP (celebrity) | 2025-01-18 | +49% in about a week; 30d BTC ≈ 0; 90d −55% BTC | CULT pool +75% in the same week |
| Vitalik "Milady is back" (celebrity) | 2026-01-01 | NPF +71% from the bar low (0.69 to 1.18), back to 0.90 within 5 weeks | CULT pool +112% that day, −50% within a month |

**Takeaway [I].** Every token or celebrity catalyst produced a one-to-three-week spike that fully retraced within one to three months. The CULT airdrop was net value-destructive for NFT holders who did not sell their CULT quickly: the token lost about 98%, and the NFT floor fell from about 5.8 to 0.74 ETH. The airdrop moved demand forward and then left an overhang.

**Derivative ecosystem.**
- Remilio is official and is examined in its own dossier.
- Community and adjacent derivatives: Pixelady Maker (about 0.01 ETH floor, undated OpenSea snapshot), "Milady, That B.I.T.C.H.", Radbro Webring and SchizoPosters (a "brother community" of Remilia, per Delphi), plus endless free-mint derivatives.
- Memecoins trading on Milady's name: **LADYS** (unaffiliated) and a "Charlotte Fang (REMILIA)" token on Bybit/MEXC (about $9–11 in Feb–Mar 2026; unaffiliated, UNVERIFIED).
- [I] **Net effect: dilutive for the NFT.** The memetic brand is free to copy (Viral Public License, plus the PFP-without-owning norm). Fungible proxies such as LADYS, CULT and REMILIA give traders cheaper, more liquid exposure to the "Milady" narrative. The derivatives raise awareness but compete for the same speculative capital.

## 5. Controversies and reputation

- [F] **May 2022 Miya affair.** Fang ran an abusive, extremist-adjacent persona ("Miya", linked by critics to Kaliacc / "Kali Yuga accelerationism" and a 4chan "suicide cult" milieu). Fang confessed, called it performance art, and nominally stepped down. The floor fell 82%.
  - **Fang is still in charge** and the persona is being re-monetised: the 2026 Miya "Exegesis" book, and the annual "Cancelversary" (Remilia wiki).
- [F] **Sept 2023 "Bonkler 9/11" coup and cross-lawsuits.** Duelling theft allegations.
- [F] **Mar 2024 treasury drain.** Fang said it was a hack. On-chain watchers flagged an earlier transfer from the treasury to the draining wallet (The Block, citing PeckShield).
- [F] **CULT.**
  - Presale buyers waited about 6 months; there were 290+ messages alleging fraud (Decrypt, 2024-12-10).
  - Supply was changed tenfold after launch.
  - RemiliaNET is openly described as an "audience manipulation engine" with a "social credit score" (Remilia design notes, 2025-09-19).
  - The "Manipulation Rounds" are not evidenced.
- [F] **March 2026 EF Mandate.** Milady aesthetics appeared in Ethereum Foundation material. Critics called Milady "larp" and "inward-facing" and objected to "milady purity tests" (The Block, 2026-03-27).
- [I] **Reputation is polarised, and that is part of the brand.** Edgelord, anti-woke positioning attracts a loyal tribe and occasional elite endorsement (Musk, Vitalik, the EF). It also caps mainstream or institutional adoption: brand partners, museums, and an exchange or ETF wrapper are unlikely. A new scandal is a standing tail risk, because the founder's persona *is* the product.

## 6. Community continuity through downturns (evidence)

- [F] **2022.** After the Miya crash, more than 1,000 holders sold. Within about 2 months the holder count was over 3,300, up 33% from the low (The Block, 2022-07-19). The floor recovered from about 0.25 to about 0.8 ETH by July 2022, with no catalyst.
- [F] **IRL continuity.** Raves have run every year since Nov 2021: 5 in NYC in 2021–22; London, LA, Denver, Tokyo and Warsaw in 2022–23; the London 33reisen series in 2023–24; NYC in Feb 2026; Tokyo in May 2026; St Petersburg in Aug 2026 (Remilia wiki and blog; self-reported).
- [F] **Liquidity decay** (NPF sales per 3-day bar):

| Year | Sales per bar | Volume |
|---|---|---|
| 2022 | 98 | 5.9k ETH |
| 2023 | 306 | 105k ETH |
| 2024 | 152 | 74k ETH |
| 2025 | 103 | 38k ETH |
| 2026 YTD | **34** | **3.6k ETH** |

  The last 30 days had 370 sales (OpenSea, via `screen_metrics.csv`).
- [F] **Holders.** 5,129 owners for 9,976 items (51%), per OpenSea on 2026-10-13. Historical holder-count series: see the on-chain collector workstream (not duplicated here).
- [F] **Elite attachment persists.** vitalik.eth still holds #9286 and #595 [OC, ownerOf 2026-10-13]. GCR held 150 at the end of 2024 (Arkham).
- [I] **The cultural community clearly persists:** events, the EF and Vitalik adoption, a Minecraft server, publishing. **The trading community has thinned sharply.** In 2026 volume is about 3% of 2023's. Continuity of culture has not translated into price support: −88% from the ETH peak and −92% from the BTC peak.

## 7. Competitive threats and displacement

- [I] **Fungible meme vehicles.** Memecoins (Solana/Base/ETH) capture "culture-coin" flows more efficiently than a 0.74-ETH NFT. Milady's own CULT failed to channel value back to the NFT.
- [I] **Free copying.** PFP adoption without ownership is encouraged. Vitalik wearing a Milady is worth less to the floor once anyone can wear one.
- [I] **Peer PFP brands with mainstream retail distribution** (e.g. Pudgy Penguins) compete for "the culture PFP" slot with a non-controversial brand. Note STATE.md mentions Igloo's Abstract chain shutting down; not examined here.
- [I] **Internal cannibalisation.** Remilia's attention is now on RemiliaNET/Chat, fashion (Atelier, HIKKI PUNKS) and media rather than the NFT. New "Remilia-native" products may displace Milady as the flagship.
- [I] **Structural NFT-market decline.** Blur is closing and Blend is ending (Oct–Nov 2026). Market liquidity is shrinking regardless of brand.

## 8. "If the team vanished tomorrow, would collectors still want this in 2028?"

[I] **Probably yes as a cultural artefact, at a much lower and thinner price.** The meme, the network-spirituality canon and Vitalik's and the Ethereum Foundation's adoption give Milady a claim as *the* Ethereum counter-culture PFP of 2021–26. That claim does not need Remilia.

However, the evidence that price depends on team or celebrity activity is strong:
- Every Remilia-free window since late 2024 lost 28–59% in ETH terms.
- Remilia governance shocks (2022, 2023, 2024) each cost 35–80%.

A disappearance would probably hit the floor initially, given treasury, CULT and social-account uncertainty. A second scenario is also plausible: the absence of Fang removes scandal risk and the CULT overhang becomes irrelevant.

On the investor's criterion (low dependence on founder execution), Milady **fails**. The cultural moat is real, but the price has been a function of Remilia-driven and celebrity-driven events.

## 9. Possible future manufactured catalysts (kept separate from the collectible thesis) [I]

All of these are speculative and listed only so they can be monitored. None of them is part of the collectible thesis.
- CULT "Manipulation Round 2/3" airdrops via RemiliaNET scores (scheduled Q2 2026 / Q2 2027; delivery unverified).
- Full RemiliaChat launch.
- Remilia Atelier "Universal Work Suit" retail release (winter 2026).
- Miya "Exegesis" book release (controversy risk).
- The Beautiful Tragedy feature film / China-tour documentary (festival circuit, per Fang's "2025 Wrapped").
- A Bonkler v2 relaunch ("designed and ready once trust is rebuilt"; no launch).
- Further celebrity PFP moments (Vitalik has done this twice, in Jan 2025 and Jan 2026, so a Jan 2027 repeat is plausible but cannot be counted on).
- Exchange listings of CULT.

Historical base rate: **every such catalyst retraced within 1–3 months.**

## 10. Strongest bull and bear theses

**Bull [I]**
- Milady is the single most culturally "load-bearing" Ethereum PFP after CryptoPunks:
  - It was endorsed in deed by Ethereum's founder twice (an on-chain purchase that he still holds).
  - It is woven into EF identity (the 2026 Mandate).
  - It survived a founder-scandal crash (−82%) and a coup.
  - It has a 5-year unbroken IRL scene.
- At 0.744 ETH it is −88% from its ETH peak, near the 2022 post-scandal / pre-Musk range (0.3–0.8 ETH), and 9.3× its 0.08 ETH mint.
- The CULT overhang has largely been absorbed: CULT FDV is about $12M.
- If Ethereum culture or an ETH/BTC recovery returns, Milady is the high-beta "culture" expression.
- The 2026 YTD BTC-relative change is −4%, the most resilient of the three names this year.

**Bear [I]**
- Price has been driven by manufactured or celebrity catalysts that retrace, and quiet periods since 2024 bleed 28–59%.
- The founder is the brand and a recurring source of governance, legal and reputational shocks.
- The lawsuits are unresolved, and the 2026 Miya book re-engages the scandal.
- Remilia's token experiment destroyed about 98% of value and left a 53B-CULT contract-held overhang with opaque distribution.
- Liquidity in 2026 is about 3% of 2023's.
- The meme is free to copy, so cultural reach does not require buying the NFT.
- Versus BTC: −84% since 2025-01-01 and −59% over the last 12 months.

## 11. Sources (all accessed 2026-10-13)

**Primary and on-chain**
- [OC] Ethereum mainnet via Tenderly public gateway `https://gateway.tenderly.co/public/mainnet`, queries 2026-10-13 21:52–22:17 UTC (block head 26,186,499). The script is `scripts/culture_onchain_checks.py` and the raw output is `data/raw/culture/onchain_checks.json`. It covers:
  - Milady Transfer logs to/from 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045, blocks 21,300,000–head, plus `ownerOf`.
  - Milady first mints, blocks 12.9M–13.2M.
  - Remilio first mints, blocks 15.2M–15.4M.
  - CULT `0x0000000000c5dc95539589fbD24BE07c6C14eCa4`: `totalSupply` = 100B. The genesis mint (block 21,318,642, 2024-12-03 01:17 UTC) and the first distribution (block 21,361,238, 2024-12-09 00:04 UTC) were located with `eth_getLogs` in 200–10k-block ranges (ad hoc query, 2026-10-13 21:52–21:53 UTC). `balanceOf` at historical blocks is also included.
  - CULT/WETH Uni v3 pool `0xc4ce8e63921b8b6cbdb8fcb6bd64cc701fb926f2`: `slot0()` at 28 historical blocks (`data/processed/culture/cult_price_samples.csv`).
- Etherscan transactions: Vitalik #9286 purchase https://etherscan.io/tx/0x8b52f966d7ec360050ccea1c2c13c4f6b42f826da16c118e43a4ad4950261e91 ; #595 transfer https://etherscan.io/tx/0x93b8b1c009d291f81f4bcbbb478d56e739193ee211e73d9726b64177db561882
- CoinGecko public API, `milady-cult-coin` coin and 365d chart (`data/raw/culture/coingecko_cult_*.json`). **Caveat:** CoinGecko's Jan 10 – Mar 27, 2026 prices (~$0.0006) conflict with on-chain pool prices (~$0.00017) and are treated as a data error. GeckoTerminal OHLCV, last 364 days (`data/raw/culture/geckoterminal_cult_*.json`).
- Remilia wiki (Remilia-run, so treat as self-interested): https://wiki.remilia.org/Milady_Maker (last edited 2026-09-09), /Remilia_Corporation (2026-06-25), /$CULT (2026-03-19), /Bonkler, /Milady_Raves, /Remilio_Babies.
- Remilia blog: https://blog.remilia.org/ (post list to 2026-08-26); RemiliaNET design notes, 2025-09-19 https://blog.remilia.org/remilianet-alpha-design-notes/ ; Spectator US repost (2025-02-17) https://blog.remilia.org/press-feature-the-spectator-us-the-topsy-turvy-world-of-remilia-2025/
- PR Newswire (Remilia), 2023-04-11: https://www.prnewswire.com/news-releases/remilia-corporation-debuts-milady-rave-tokyo-and-announces-momentous-new-nft-bonkler-301793389.html
- Business Wire (Remilia/Velez), 2026-02-11: https://www.businesswire.com/news/home/20260211894271/en/Elena-Velez-Partners-with-Remilia-Corporation-to-Launch-Remilia-Atelier-Debuting-the-Universal-Work-Suit ; HIKKI PUNKS, 2026-03-13: https://www.businesswire.com/news/home/20260313786403/en/Remilia-Corporation-Debuts-Luxury-Streetwear-Collection-HIKKI-PUNKS-EXIT-SOCIETY
- KuCoin listing announcement (2024-12-30): https://kucoin.com/announcement/en-milady-cult-coin-miladycult-gets-listed-on-kucoin
- DWF Labs (2024-06-03): https://www.dwf-labs.com/news/427-dwf-labs-invests-5m-in-milady-memecoin

**Reputable outlets**
- The Block, MK Manoylov, 2022-07-19, "The metaverse that crashed into reality": https://www.theblock.co/news/web3/2022-07-19-the-metaverse-that-crashed-into-reality-the-story-of-miya-and-milady-maker-157907
- The Block, Stephanie Murray, 2023-05-10, Musk meme: https://www.theblock.co/post/230279/elon-musk-milady-price-twitter-meme ; volume follow-up: https://www.theblock.co/post/230466/counterculture-nft-collection-milady-maker-surged-in-volume-after-elon-musk-tweet
- Decrypt, Andrew Hayward, 2023-05-10: https://decrypt.co/139593/elon-musk-tweets-miladys-nft-meme-price-predictably-pumps
- Cointelegraph, Zhiyuan Sun, 2023-05-10: https://cointelegraph.com/news/milady-nft-floor-price-surges-after-elon-musk-tweet
- Bitcoin.com News, Terence Zimwara, 2023-09-14, Remilia sues contractors: https://news.bitcoin.com/nft-based-firm-remilia-corporation-sues-independent-contractors-accused-of-siphoning-1-million/
- CryptoPotato, 2023-09-26, countersuit: https://cryptopotato.com/co-founders-of-remilia-file-lawsuit-in-new-milady-vs-milady-case-against-charlotte-fang/
- The Block, Zack Abrams, 2024-03-16, treasury drain: https://www.theblock.co/post/282972/remilia-founder-charlotte-fang-claims-he-was-hacked-as-treasury-is-drained-of-millions
- The Defiant, May 2024, unexplained rally: https://thedefiant.io/news/nfts-and-web3/milady-nfts-soar-amid-nft-market-volatility
- The Block, Danny Park, 2024-12-09, CULT launch: https://www.theblock.co/post/329935/cult-memecoin-from-milady-nft-creators-goes-live-at-over-600-million-fdv
- Decrypt, Ryan S. Gladwin, 2024-12-10, CULT delay: https://decrypt.co/295800/milady-cult-coin-finally-launched-why-did-it-take-so-long-and-whats-next
- Arkham Research, 2024-12-13, GCR claims CULT: https://info.arkm.com/research/gcr-wakes-up-to-claim-cult-airdrop-53iul
- Cryptopolitan, 2024-12-11, whitepaper v2: https://www.cryptopolitan.com/milady-cult-token-500m-market-cap-whitepaper/
- Unchained, Sage D. Young, 2025-01-21, Vitalik "wartime": https://unchainedcrypto.com/ethereum-founder-vitalik-buterins-nft-choice-spurs-talk-of-wartime-mode/
- Decrypt, Ryan S. Gladwin, 2025-03-16, "What is Milady?": https://decrypt.co/309506/what-is-milady-edgy-ethereum-nft-community
- Decrypt, Ryan S. Gladwin, 2025-09-19, RemiliaNET: https://decrypt.co/340424/remilia-launching-milady-social-media-network-serve-4chan-diaspora
- The Crypto Times, Dishita Malvania, 2026-01-02, Vitalik 2026 PFP: https://www.cryptotimes.io/2026/01/02/milady-nft-floor-price-rises-50-after-vitaliks-profile-update/
- The Crypto Times, 2023-07-18, Binance award: https://www.cryptotimes.io/2023/07/18/milady-maker-wins-nft-project-of-the-year-at-binance-awards/
- The Block, Daniel Kuhn, 2026-03-27, EF mandate and Milady: https://www.theblock.co/amp/post/395541/miladys-loyalty-pledge-unnecessary-culture-schism-ethereum-community
- CoinGecko Learn, Oct 2025 crash explainer: https://www.coingecko.com/learn/october-10-crypto-crash-explained
- Blur closure: STATE.md (coordinator-verified CoinDesk/The Block); Cryptonews (2026-10-13), https://cryptonews.com/news/blur-nft-volume-collapse-shut-down/ (search snippet only)

**Secondary / low-reliability (last resort, flagged)**
- 0xcow Substack, 2022-05-21 (contemporaneous timeline): https://0xcow.substack.com/p/saved-milady-and-how-we-planned-to
- IQ.wiki events (contains errors, e.g. dates "Bonkler embezzlement" to Aug 2025): https://iq.wiki/wiki/milady-maker/events
- Datawallet (updated 2026-03-30; contains errors, e.g. mint 0.05 ETH, DWF→ecosystem): https://www.datawallet.com/crypto/what-is-milady-nft
- Koinly / Changelly (LADYS launch): https://koinly.io/blog/milady-meme-coin/ ; https://changelly.com/blog/milady-crypto/
- Cryptoticker (Oct 2026 snapshot citing CoinGecko ATH 7.35 ETH "Dec 2024", which conflicts with the NPF ATH of 6.34): https://cryptoticker.io/en/nft-prices-october-2026-bored-ape-cryptopunks-floor

**UNVERIFIED / not found**
- **No 2022 lawsuit over Remilio funds was found.** The Remilia disputes with former collaborators are the Sept 2023 "Bonkler 9/11" suits: Nevada, filed 2023-09-10/11, and the Delaware countersuit, 2023-09-22.
- **No Binance-related factor around the May 2023 rally was found.** The only Binance link is the Binance Awards in July 2023. Bonkler launched in April 2023, before the Musk post.
- **The CULT TGE was not delayed into 2025.** It happened 2024-12-09 00:04 UTC [OC], about 6 months after the June 2024 presale.
- The "there's a Milady meme for everything" Musk quote (the actual text was "There is no meme. I love you."). No later Musk Milady posts were found.
- The original CoinDesk May 2022 article.
- Lawsuit outcomes.
- Delivery of the 2025/2026 Manipulation Rounds.
- Per-NFT CULT allocation.
- Remilia headcount and finances.
- Derivative collections' current floors.
- Any 2026 Musk/X references.
