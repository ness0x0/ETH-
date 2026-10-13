"""Assemble universe.csv: screening metrics + rally/beta stats + decision and reason.

Decision tiers: FINALIST (deep research), WATCHLIST (light check; could be promoted), REJECT, REFERENCE (unaffordable
but used as comparable). Affordability threshold: one floor item <= ~3.2 ETH (~$8k at ETH $2,509).
"""
import os
import pandas as pd
from common import ROOT, PROC

D = {
    "Milady Maker": ("FINALIST", "Strongest crypto-native meme/identity brand; survived 2022 founder scandal; floor $1.9k affordable; liquid (~370 sales/30d). Must separate Musk/CULT catalysts from organic demand."),
    "Pudgy Penguins": ("FINALIST", "Largest consumer-facing ETH NFT brand (toys, PENGU token); most liquid finalist (~1,100 sales/30d); 2.31 ETH fits budget. Highly team/token dependent; -73% vs BTC in 1y."),
    "Lil Pudgys": ("WATCHLIST", "High-beta, cheaper Pudgy proxy (0.23 ETH, 21.9k supply); same team dependence with weaker scarcity. Covered inside Pudgy dossier."),
    "Azuki": ("FINALIST", "Investor's incumbent position — must be evaluated as hold/replace benchmark. -99% vs BTC from ATH; founder trust issues; ANIME token."),
    "Redacted Remilio Babies": ("FINALIST", "Higher-beta Milady-ecosystem exposure at 0.118 ETH; tests whether Milady culture extends to derivatives."),
    "Chromie Squiggle": ("FINALIST", "Genesis Art Blocks project (2020); museum/auction-grade generative-art provenance; floor 2.64 ETH ($6.6k) is the only affordable 'blue-chip art' entry; low founder dependence; thin trading (~42 sales/30d)."),
    "Terraforms": ("FINALIST", "Fully on-chain dynamic art (Mathcastles); best 1y BTC-relative of finalists (-11%); cult collector base; floor 0.30 ETH; thin and concentrated."),
    "CryptoDickbutts": ("FINALIST", "CC0 crypto-meme with a decades-old internet meme behind it; +47% vs BTC over 2y; 5.2k supply; low liquidity (~55 sales/30d)."),
    "V1 CryptoPunks (wrapped)": ("FINALIST", "Cheapest access to 2017 Larva Labs provenance (1.59 ETH); derivative/legitimacy debate is the core question."),
    "CryptoPunks": ("REFERENCE", "Unaffordable (31.3 ETH ≈ $78k). Used as the blue-chip comparable and sector bellwether."),
    "Bored Ape Yacht Club": ("REFERENCE", "Unaffordable (5.45 ETH ≈ $13.7k > budget); Yuga/ApeCoin dependent; -98% vs BTC from ATH. Comparable only."),
    "Autoglyphs": ("REFERENCE", "Unaffordable (~60 ETH). Historical comparable for on-chain generative art."),
    "Fidenza": ("REFERENCE", "Unaffordable (24 ETH). Generative-art comparable."),
    "Ringers": ("REFERENCE", "Unaffordable (8.4 ETH). Generative-art comparable."),
    "Grifters by XCOPY": ("REFERENCE", "Unaffordable (12 ETH); artist-dependent. Comparable for crypto-native art."),
    "Gazers by Matt Kane": ("REFERENCE", "Unaffordable (5 ETH); 2 sales/30d."),
    "Etheria v0.9": ("REJECT", "3.6 ETH (> budget at ~$9k); 0 sales/30d — untradeable at size; 398 items."),
    "Mutant Ape Yacht Club": ("REJECT", "Yuga-dependent derivative; 19.5k supply; -98% vs BTC from ATH; no evidence of independent collector demand."),
    "Moonbirds": ("WATCHLIST", "Owner-of-the-month brand (Proof→Yuga→Orange Cap); R2025 rally 18.7x then gave back ~73% within 180d — token/incentive-driven. Founder/owner dependent."),
    "Doodles": ("REJECT", "Brand/company dependent (DOOD token); -99% vs BTC from ATH; no distinct collectible thesis."),
    "Meebits": ("WATCHLIST", "Larva Labs 2021 provenance at 0.30 ETH, but 20k supply and Yuga ownership; weaker cultural mindshare than Punks."),
    "Clone X": ("REJECT", "RTFKT (Nike) wound down — permanent impairment of the brand thesis."),
    "Curio Cards": ("WATCHLIST", "2017 historical art; card-by-card market (30 cards, 29.7k items); affordable cards are commons. Covered in historical light dossier."),
    "MoonCats (Acclimated)": ("WATCHLIST", "2017 provenance at 0.124 ETH; 25k supply; low mindshare. Covered in historical light dossier."),
    "CryptoKitties": ("REJECT", "2M+ supply; floor ~$2; historical but no scarcity."),
    "Max Pain and Frens by XCOPY": ("REJECT", "Editions across 3 contracts; artist-dependent; weaker scarcity than Grifters."),
    "Meridian by Matt DesLauriers": ("REJECT", "Affordable generative art (2.2 ETH) but lower recognition than Squiggle; 18 sales/30d. Squiggle preferred for the same thesis."),
    "Nouns": ("REJECT", "Perpetual daily auctions dilute supply; treasury-driven valuation largely unwound after forks; -99.5% vs BTC from ATH."),
    "Hashmasks": ("WATCHLIST", "Early-2021 art PFP at 0.064 ETH; 16k supply; NCT token dead; niche."),
    "mfers": ("WATCHLIST", "CC0 meme already passed the 'founder left' test (sartoshi exit 2022) but cultural momentum faded; 0.128 ETH."),
    "CrypToadz": ("WATCHLIST", "CC0 meme-art (Gremplin) at 0.247 ETH; artist-dependent; modest liquidity."),
    "Rektguy": ("REJECT", "-75% vs BTC 1y; founder/brand dependent; no distinguishing evidence."),
    "Chimpers": ("REJECT", "Contract redeployed 2026-01 (migration); provenance/continuity complicated; thin."),
    "NORMIES": ("WATCHLIST", "Feb-2026 on-chain AI/pixel project; supply in flux (20k target vs ~7k live); too new to judge durability."),
    "Good Vibes Club": ("REJECT", "Launched 2025; -69% vs BTC in 1y; insufficient history."),
    "Wassies by Wassies": ("REJECT", "Thin (34 sales/30d); niche meme."),
    "Checks - VV Originals": ("REJECT", "Jack Butcher editions with burn/composite mechanics; -70% vs BTC 1y; artist-dependent."),
    "Opepen Edition": ("REJECT", "16k open-edition supply; artist-dependent; -97% vs BTC from ATH."),
    "Cool Cats": ("REJECT", "Brand-dependent; -99% vs BTC from ATH; no distinct thesis."),
    "World of Women": ("REJECT", "Brand-dependent; -99% vs BTC from ATH."),
    "Loot": ("REJECT", "Historically important but 35 sales/30d; derivative ecosystem dormant."),
    "DeGods (ETH)": ("REJECT", "Chain-hopping history (SOL→ETH), founder-dependent; -99% vs BTC from ATH."),
    "Sappy Seals": ("REJECT", "Incentive-driven spikes (R2025 16.8x then -80%); -98% vs BTC from ATH."),
    "VeeFriends": ("REJECT", "Gary Vaynerchuk dependence is total; +53% vs BTC 2y but 33M cap with ~97 sales/30d."),
    "Quirkies Originals": ("REJECT", "+105% vs BTC 1y, but Blockscout top-50 holders own ~45% of supply and Gondi lending escrow holds ~10% — rise looks concentrated and leveraged, not broad demand (checked 2026-10-13)."),
    "Sproto Gremlins": ("REJECT", "Memecoin-adjacent; -92% vs BTC 2y."),
    "The Captainz": ("REJECT", "Memeland/MEME-token driven; -99.9% vs BTC from ATH — incentive collapse case study."),
}

df = pd.read_csv(os.path.join(PROC, "screen_metrics.csv"))
ra = pd.read_csv(os.path.join(PROC, "rally_analysis.csv"))
keep = ["name", "R2024_mult_btc", "R2024_retain180_btc", "R2025_mult_btc", "R2025_retain180_btc",
        "beta_floorbtc_to_ethbtc", "ann_vol_floorbtc"]
df = df.merge(ra[keep], on="name", how="left")
df["decision"] = df["name"].map(lambda n: D.get(n, ("?", ""))[0])
df["reason"] = df["name"].map(lambda n: D.get(n, ("?", ""))[1])
df["affordable_1_item"] = df["floor_usd"] <= 8000
order = {"FINALIST": 0, "WATCHLIST": 1, "REFERENCE": 2, "REJECT": 3}
df = df.sort_values(["decision", "floor_cap_usd_m"], key=lambda c: c.map(order) if c.name == "decision" else -c)
cols = ["name", "decision", "reason", "category", "contracts", "opensea_slug", "supply", "os_floor_eth", "floor_usd",
        "floor_btc", "floor_cap_usd_m", "affordable_1_item", "os_owners", "owners_per_supply", "os_sales_1d",
        "os_sales_7d", "os_sales_30d", "os_vol_30d_eth", "avg_sale_30d_eth", "npf_sales_365d", "npf_vol_365d_eth",
        "npf_ath_floor_eth", "npf_ath_date", "drawdown_from_ath_eth", "drawdown_from_ath_btc", "chg_eth_1y",
        "chg_btc_1y", "chg_eth_2y", "chg_btc_2y", "chg_btc_3y", "npf_floor_min_365d", "npf_floor_max_365d",
        "R2024_mult_btc", "R2024_retain180_btc", "R2025_mult_btc", "R2025_retain180_btc", "beta_floorbtc_to_ethbtc",
        "ann_vol_floorbtc", "created"]
out = df[cols].round(4)
out.to_csv(os.path.join(ROOT, "universe.csv"), index=False)
print(out[["name", "decision", "os_floor_eth", "floor_cap_usd_m"]].to_string())
