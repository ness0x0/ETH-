"""Scenario chart: return vs BTC by scenario (small multiples), rule B (disciplined) vs HOLD, finalists vs ETH.
Input: data/processed/scenarios.csv. Output: reports/charts/scenarios_vs_btc.png
Form: one panel per scenario; horizontal bars from a zero baseline; ETH benchmark bar in a distinct slot; two marks per
row (hold, rule B) identified by a legend + direct value labels on rule-B bars. No dual axes.
"""
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import PROC, ROOT

SURF, INK, INK2, GRID, NEUTRAL = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#8a8985"
C_B, C_HOLD, C_ETH = "#2a78d6", "#a9c8ef", "#eb6834"
ORDER = ["ETH", "v1punks", "milady", "cryptodickbutts", "chromie_squiggle", "pudgy", "terraforms", "remilio", "azuki"]
LAB = {"ETH": "ETH (benchmark)", "v1punks": "V1 Punks", "milady": "Milady", "cryptodickbutts": "CryptoDickbutts",
       "chromie_squiggle": "Chromie Squiggle", "pudgy": "Pudgy", "terraforms": "Terraforms", "remilio": "Remilio",
       "azuki": "Azuki (held)"}
d = pd.read_csv(os.path.join(PROC, "scenarios.csv"))
fig, axes = plt.subplots(1, 4, figsize=(15, 6), sharey=True, facecolor=SURF)
for ax, (s, title) in zip(axes, [("S1_weak", "S1 weak (ETH/BTC 0.024)"), ("S2_moderate", "S2 moderate (0.032)"),
                                 ("S3_strong", "S3 strong (0.040)"), ("S4_mania", "S4 mania (0.050)")]):
    ax.set_facecolor(SURF)
    g = d[d.scenario == s]
    for i, c in enumerate(ORDER):
        hold = g[(g.collection == c) & (g.rule == "HOLD")].R_btc.iloc[0] * 100
        b = g[(g.collection == c) & (g.rule == "B")].R_btc.iloc[0] * 100
        y = len(ORDER) - 1 - i
        if c == "ETH":
            ax.barh(y, b, height=0.6, color=C_ETH)
        else:
            ax.barh(y + 0.17, hold, height=0.32, color=C_HOLD)
            ax.barh(y - 0.17, b, height=0.32, color=C_B)
        ax.text(b + (6 if b >= 0 else -6), y - (0 if c == "ETH" else 0.17), f"{b:+.0f}%", va="center",
                ha="left" if b >= 0 else "right", fontsize=7.5, color=INK)
    ax.axvline(0, color=INK2, lw=0.9)
    ax.grid(axis="x", color=GRID, lw=0.6)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.tick_params(colors=INK2, labelsize=8)
    ax.set_title(title, fontsize=10, color=INK, loc="left")
    lo, hi = min(-100, g.R_btc.min() * 100 - 30), max(100, g[g.rule.isin(["B", "HOLD"])].R_btc.max() * 100 + 60)
    ax.set_xlim(lo, hi)
    ax.set_xlabel("Return vs holding BTC, %", color=INK2, fontsize=8)
axes[0].set_yticks(range(len(ORDER)))
axes[0].set_yticklabels([LAB[c] for c in ORDER][::-1], fontsize=9, color=INK)
from matplotlib.patches import Patch
fig.legend(handles=[Patch(color=C_B, label="NFT, rule B (sell on 30% drawdown once ≥1.5× vs BTC)"),
                    Patch(color=C_HOLD, label="NFT, hold to horizon"), Patch(color=C_ETH, label="ETH benchmark")],
           loc="upper right", ncol=3, fontsize=8.5, frameon=False)
fig.suptitle("~18-month return vs BTC by scenario (rule-based model v2; no probabilities assigned)", x=0.01, ha="left",
             color=INK, fontsize=12)
fig.text(0.01, 0.01, "Source: scripts/scenario_model.py → data/processed/scenarios.csv. Values on bars = rule B (ETH: "
         "plain). Parameters derived by one rule per input; see reports/scenario_model.md.", fontsize=7.5, color=INK2)
fig.tight_layout(rect=(0, 0.03, 1, 0.93))
fig.savefig(os.path.join(ROOT, "reports", "charts", "scenarios_vs_btc.png"), dpi=125, facecolor=SURF)
print("ok")
