# Response to the independent critic (`reports/critic_review.md`)

The critic reviewed the draft (`reports/archive/DRAFT_conclusions_for_critic.md`), recomputed the scenario maths,
backtested the stated exit rules and checked key facts live and on-chain. **The headline changed** from "a staged,
exit-disciplined NFT position is defensible" to **"no NFT purchase now"**.

## How each challenge was resolved

| # | Severity | Challenge | Accepted? | What changed |
|---|---|---|---|---|
| 1 | Critical | The exit rules and the modelled capture were different strategies | **Yes** | Model v2 evaluates executable rules (HOLD, A = sell at 2×, B = 30% trailing stop once ≥1.5×), with TOP kept only as an optimistic bound. The "+211% to +470%" claim is withdrawn. Rule B is the recommended discipline: it beat HOLD and A on history for most names. |
| 2 | Critical | A staged position is impossible for single-item picks | **Yes** | Plans are now per collection and item-level: one V1 (~57% of budget), Milady 2–3 items, etc. All rules are single-sale executable. |
| 3 | Critical | Squiggle #1 contradicts the numbers | **Yes** | Squiggle is now #4, "collectible, not an investment". Its rule-B break-even is 55% vs ETH's 14%, and it beat BTC in 2–13% of historical windows. |
| 4 | Critical | "No purchase / ETH" should be the headline | **Yes** | It is now the headline. ETH is presented as the cleaner vehicle for the macro view: break-even 14%, S1 loss −20% vs −51% to −75% for the NFTs. |
| 5 | Major | Hand-set, inconsistent parameters; missing documentation | **Yes** | Every parameter is now derived by one rule (`scripts/scenario_model.py`), documented in `reports/scenario_model.md`, with a sensitivity table. Rankings no longer use break-even gaps under ~10 pp. |
| 6 | Major | S3 mixed an ETH/BTC ×2.2 rally with a ×1.33 scenario | **Partly** | No scaling. The ETH-terms elasticity of floors to ETH/BTC is only β−1 ≈ 0.1–0.4 (`rally_analysis.csv`). S3 still uses each name's own Aug-2025 ETH multiple, with a cycle-high cap. The issue is disclosed as a model weakness. |
| 7 | Major | 180-day retention, the S3:S4 mix and the S1:S2 weights lack a basis | **Yes** | Hold-through now uses 365-day post-peak retention. Break-evens are shown for 50:50 / 60:40 and 2:1 / 3:1 mixes. Weights are labelled as assumptions. |
| 8 | Major | Azuki valued on the ask, not the sell-now bid | **Yes** | Basis is now the net bid (e = 0.842). Azuki's rule-B break-even is 22%, like the other PFPs. The recommendation is now "exit patiently after the Blend deadline; don't hit the forced-selling bid", not "sell now". |
| 9 | Major | Squiggle holder metrics misread as demand | **Yes** | Dormant supply is described as partly illiquidity (13.1% in one minter entity; Safes 10.5%). First-time buyers are reported as levels (~281) as well as the share (45%). The fee-deterrence explanation for low churn is added. |
| 10 | Major | Inconsistent overhangs; V1 metrics cover only wrapped supply | **Yes** | The shortlist has one overhang table. The V1 dossier notes that metrics cover the 5,125 wrapped tokens only. |
| 11 | Major | "Durable" re-ratings mostly reversed | **Yes** | `historical_analysis.md` now states that all except Moonbirds have reversed in BTC terms, and that V1's NODE move was mostly beta (abnormal +13%). |
| 12 | Major | Event-study overcounting | **Yes** | 11 placeholder rows excluded, events de-duplicated (151 independent with 90-day data), IQRs reported. TGE-only: 6 tokens, median −64% vs BTC at 90 days (abnormal −47%), described as association, not cause. |
| 13 | Major | Rally drivers gone; survivorship | **Yes** | Stated in the memo and the model. S3 uses the 2025 (non-token) rally; S4 explicitly assumes the incentive mechanisms return. |
| 14 | Major | Post-Blur liquidity untested | **Yes** | Entry gate G1 requires a fresh OpenSea depth snapshot after 2026-11-12. The Blur/Blend share of Pudgy (58%) and Azuki (52%) liquidity is disclosed. |
| 15 | Major | Pudgy's rank conflicts with the mandate | **Yes** | Pudgy is now "not ranked — tactical alternative outside the mandate". The 0.94× "matched BTC" claim is reworded as a start-date effect. |
| 16 | Major | Entry and exit rules invented; trend filter misreported | **Yes** | Exit rules are backtested (`exit_rule_backtest.csv`, labelled in-sample). The trend-filter result is reported fully: it helped the sector 2–3× and hurt most single names after costs. It is used only as an entry gate. Entry limits are labelled patience heuristics. |
| 17–18 | minor | Squiggle royalty is a venue policy; haircut comes from one snapshot | **Yes** | Disclosed in `scenario_model.md` §7 and the Squiggle dossier. |
| 19 | minor | Wording of the sector number | **Yes** | Now reported as the geometric index, the buy-and-hold basket (0.25×) and the median collection (0.11×). Only 3 of 38 beat BTC, all founder-driven. |
| 20 | minor | Floors don't reconcile within an hour | **Yes** | Entry anchors use the order-book ask, with a ±5–12% uncertainty note. |
| 21 | minor | Milady wording ("CULT spent", "EF adoption") | **Yes** | Corrected in the dossier and memo. |
| 22 | minor | Missed costs: conversion, tax, wallet security | **Yes** | Added to the memo and to uncertainties. |
| 23 | minor | 1-year base date mislabelled | **Yes** | Corrected to 2025-10-13. |

## Where we kept a different view

- **CryptoDickbutts.** The critic excluded it on its 41% instant round trip. We keep it as conditional #3 (small,
  patient, bid-side only), for three reasons:
  - It is the only finalist that has already passed the "team vanished" test.
  - Its rule-based profile matches V1's (rule-B break-even 20%, hold 30%).
  - On-chain sales show single items clear near the floor (median 1.02× the NPF floor). That overturns the
    "floor not executable" flag, which came from NPF's volume/count data.

  The round-trip problem is size, not price, so the position must be 1–2 items accumulated by bids.
- **Milady stays #2 as a mandate exception.** The critic also ranks it third. Our order (Milady above CDB) reflects
  liquidity and divisibility, both of which matter for executing rule B.

## Net effect on the recommendation

| | Draft | Final |
|---|---|---|
| Headline | Staged, exit-disciplined NFT position defensible with conviction | **No NFT purchase now.** ETH is the cleaner vehicle for the macro view; otherwise stay in BTC |
| #1 | Chromie Squiggle | V1 CryptoPunks, conditional on entry gates |
| Squiggle | #1 survivability | #4, collectible only |
| Pudgy | #3 tactical | Not ranked (mandate exception) |
| Azuki | Replace | Exit patiently after the Blend deadline; V1 is the better "mania ticket" if one is kept |
| Exit rules | 2×/3×/30% trailing (inconsistent with the model) | Rule B: once ≥1.5× vs BTC, sell on a 30% drawdown from peak (single-sale, backtested) |
