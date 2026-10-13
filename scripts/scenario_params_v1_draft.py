"""Scenario parameters (judgmental, evidence-anchored). Every number is explained in reports/scenario_model.md.

M[s]   = floor multiple in ETH terms at exit vs today's entry ask (18-month horizon; S3/S4 = disciplined exit near the
         rally high, capturing ~75% of the assumed peak gain: M = 1 + 0.75*(peak-1)).
hold[s]= hold-through multiple for S3/S4 (still held at horizon end after the rally fades): peak x RET (S3) and
         peak x RET x 0.85 (S4, manias bust harder), where RET = the collection's own average 180-day post-peak
         retention (ETH terms) in the 2024 and 2025 rallies (rally_analysis.csv); CDB capped at 0.50 (its 2024 value
         >1 reflects a second rally wave).
e      = entry slippage for a ~$7.5k multi-item position: half the instant-book average-cost premium over the floor
         (assumes patient accumulation with bids/limit orders). 1.0 for single-item positions.
h[s]   = exit haircut: instant position-exit gap to funded OpenSea bids + seller fees (liquidity_position.csv) in S1;
         ~half of that + fees in S2/S3; 3-5% in S4 (deep bids in manias).
Anchors per collection (ETH terms): S1 = sector decay (~-33%/yr -> x0.55 over 18m) adjusted for idiosyncratic
pressure; S2 = flat-to-down (moderate recoveries have not lifted NFT floors in ETH terms since 2023);
S3 peak = Aug-2025 rally trough->peak ETH multiple, sized vs the current level; S4 peak = a fraction (25-60%) of the
2024-25 cycle ETH-terms peak, lower where the prior peak was token-airdrop-driven and the token is already spent.
"""


def disc(peak):
    return round(1 + 0.75 * (peak - 1), 3)


def mk(s1, s2, p3, p4, h1, h2, h3, h4, ret, e=1.0):
    return {"e": e,"M": {"S1_weak": s1, "S2_moderate": s2, "S3_strong": disc(p3), "S4_mania": disc(p4)},
            "hold": {"S3_strong": round(p3 * ret, 3), "S4_mania": round(p4 * ret * 0.85, 3)}, "ret": ret,
            "h": {"S1_weak": h1, "S2_moderate": h2, "S3_strong": h3, "S4_mania": h4},
            "peak": {"S3_strong": p3, "S4_mania": p4}}


PARAMS = {
    # entry 0.745 ETH ask. S3 peak 1.6 (Aug-25 ETH mult 1.56). S4 peak 4.0 (3.0 ETH = 47% of Dec-24 6.34 peak;
    # CULT spent). S1 0.45: quiet windows since 2025 -28%..-59% ETH; founder-shock & CULT-overhang risk.
    "milady": mk(0.45, 0.85, 1.6, 4.0, 0.10, 0.06, 0.05, 0.03, 0.36, e=1.045),
    # entry 0.118 (20-item position averages ~1.24x floor on the instant book). beta ~1.3x Milady. S4 peak 5x (0.59 = 31% of Apr-24 1.88).
    "remilio": mk(0.35, 0.75, 1.7, 5.0, 0.14, 0.08, 0.06, 0.04, 0.26, e=1.12),
    # entry 0.473 (but 90d avg sale ~0.64x floor; instant exit -40%). S3 peak 2.5 (Aug-25 peak 1.65 = 3.5x now).
    # S4 peak 4.0 (1.9 ETH ~ half of 2022 ATH 3.69).
    "cryptodickbutts": mk(0.50, 0.85, 2.5, 4.0, 0.25, 0.14, 0.10, 0.05, 0.5, e=1.14),
    # entry 2.43. S1 0.45: Blur/Blend shock, PENGU insider unlocks to 2028, Igloo losses. S3 peak 1.8 (Aug-25 1.82).
    # S4 peak 4.0 (9.7 ETH ~ 2025 range; 39% of PENGU-driven 25.2 peak).
    "pudgy": mk(0.45, 0.85, 1.8, 4.0, 0.09, 0.05, 0.04, 0.03, 0.33),
    # incumbent: valued from today's bid 0.466 (sell-now alternative); multiples applied to 0.548 ask-equivalent.
    # S3 peak 1.4 (Aug-25 1.11; 2024 3.4 was ANIME-driven). S4 peak 3.0 (1.6 ETH = 13% of 12.2 pre-ANIME peak).
    "azuki": mk(0.45, 0.80, 1.4, 3.0, 0.18, 0.10, 0.08, 0.04, 0.24),
    # entry 2.642 (8.5% seller fees incl. 7.5% enforced royalty). Art held up better (1y BTC -35%, no Blur shock).
    # S3 peak 1.5 (Aug-25 1.44). S4 peak 2.5 (6.6 ETH = 78% of Jan-24 8.49; 40% of Jan-23 16.4).
    "chromie_squiggle": mk(0.65, 1.00, 1.5, 2.5, 0.31, 0.19, 0.17, 0.12, 0.66),
    # entry 0.30; one entity = 13.5% of t12m buying (bid dependence); latent 1,193-token owner allotment. S3 peak 1.5; S4 peak 3.5
    # (1.05 ETH = 52% of Jan-24 2.0).
    "terraforms": mk(0.55, 0.95, 1.5, 3.5, 0.23, 0.13, 0.10, 0.05, 0.46, e=1.05),
    # entry 1.70. Tied to V2 Punks (most resilient asset) x V1/V2 ratio (compressed to ~5%). S3 peak 2.0 (Aug-25 2.11);
    # S4 peak 2.6 (4.4 ETH ~ Aug-25 4.13 high).
    "v1punks": mk(0.60, 0.95, 2.0, 2.6, 0.14, 0.08, 0.06, 0.04, 0.54),
}
