"""Forward conditional view for the investor's framing.

If NFTs are bought now (assumed near a cycle low, ETH/BTC 0.0301) and sold into the next euphoria, with BTC
going to $180–210k (2.16–2.52× from $83,350): the NFT beats holding BTC iff  (NFT/ETH swing) × (ETHBTC_exit/0.0301) > 1
(selling the NFT and rotating into BTC at the NFT exit; identical to the USD comparison if the NFT exit coincides
with BTC's top). NFT/ETH swing distributions come from Cycle B (2022–25) with the investor's "rough" timing
(entry = mean floor ±45d around the low; exit = mean floor ±15d around the euphoria peak; −10% costs):
  - CYCLE: cycle low (2022-06→2023-10) → best euphoria of the cycle (2023-11→2025-10), 37 collections
  - SWINGS: each low → next euphoria (E1–E4), 171 collection-episodes
Output: data/processed/cycle_forward.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC

d = pd.read_csv(os.path.join(PROC, "cycle_episodes.csv"))
EB0, BTC0 = 0.0301, 83350.0
levels = [0.020, 0.025, 0.030, 0.035, 0.040, 0.050]
GRP = {"historical-pfp": "art", "generative-art": "art", "generative-art-historical": "art", "onchain-art": "art",
       "historical-art": "art", "historical": "art", "art-editions": "art", "artist-pfp": "art", "artist-editions": "art",
       "onchain-text": "art", "historical-game": "art"}
d["group"] = d.category.map(GRP).fillna("pfp")
rows = []
for label, g in [("CYCLE: low→best euphoria (all 37)", d[d.episode == "BIG_2022_2025"]),
                 ("CYCLE: finalists (7)", d[(d.episode == "BIG_2022_2025") & d.finalist]),
                 ("SWINGS: low→next euphoria (171)", d[d.episode != "BIG_2022_2025"]),
                 ("SWINGS: finalists (32)", d[(d.episode != "BIG_2022_2025") & d.finalist]),
                 ("CYCLE: historical/art (17)", d[(d.episode == "BIG_2022_2025") & (d.group == "art")]),
                 ("CYCLE: PFPs (20)", d[(d.episode == "BIG_2022_2025") & (d.group == "pfp")]),
                 ("CYCLE, BLIND timing: all", d[d.episode == "BIG_2022_2025"])]:
    x = (g.eth_blind if "BLIND" in label else g.eth_rough).dropna().values
    r = {"sample": label, "n": len(x), "nft_eth_median": np.median(x), "nft_eth_p25": np.quantile(x, .25),
         "nft_eth_p75": np.quantile(x, .75)}
    for lv in levels:
        r[f"P_beat_BTC@ETHBTC={lv}"] = float(np.mean(x * lv / EB0 > 1))
        r[f"P_2x_BTC@ETHBTC={lv}"] = float(np.mean(x * lv / EB0 > 2))
    rows.append(r)
out = pd.DataFrame(rows)
out.to_csv(os.path.join(PROC, "cycle_forward.csv"), index=False)
pd.set_option("display.width", 250)
print(out.round(2).T.to_string())
# USD view at BTC 200k for illustration
for lv in levels:
    eth = lv * 200000
    print(f"ETH/BTC {lv}: ETH ${eth:,.0f} at BTC $200k = {eth / 2508.69:.2f}x ETH; NFT needs NFT/ETH > {EB0 / lv:.2f}")
