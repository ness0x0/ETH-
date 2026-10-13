"""Empirical test of executable exit rules on history (in-sample, overlapping windows — a sanity check, not proof).

For every start date (3-day bars, 2022-06-03 → 2025-04-15) buy at the BTC-terms floor x entry slippage e and hold up
to 18 months, applying:
  HOLD : sell at the end of the window
  A    : sell when BTC-terms floor >= 2.0x entry, else at the end
  B    : once BTC-terms floor >= 1.5x entry, sell when it falls 30% below its post-entry peak; else at the end
Exit proceeds x (1 - h_S2) (patient exit haircut, scenario_params_v2.csv). Compared with BTC (=1) and ETH (ETH/BTC
ratio over the same window). Overlapping windows: ~3 independent 18-month periods in the sample; bear-dominated.
Output: data/processed/exit_rule_backtest.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC
from npf_utils import load_series
from scenario_model import F

P = pd.read_csv(os.path.join(PROC, "scenario_params_v2.csv"), index_col=0)
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)["eth_btc"]
H = pd.Timedelta(days=548)
rows = []
for k, slug in F.items():
    s = load_series(slug)["floorBtc"].dropna()
    e = 1.0 if k == "azuki" else P.loc[k, "e"]  # history: treat Azuki as a fresh purchase
    h = P.loc[k, "h_S2"]
    starts = s.loc["2022-06-03":"2025-04-15"].index
    res = {"HOLD": [], "A": [], "B": [], "ETH": []}
    for t0 in starts:
        w = s.loc[t0: t0 + H]
        rel = w / (w.iloc[0] * e)
        res["HOLD"].append(rel.iloc[-1] * (1 - h))
        hitA = rel[rel >= 2.0]
        res["A"].append((2.0 if len(hitA) else rel.iloc[-1]) * (1 - h))
        outB, armed, peak = rel.iloc[-1], False, 0.0
        for v in rel.values:
            peak = max(peak, v)
            armed = armed or peak >= 1.5
            if armed and v <= 0.7 * peak:
                outB = v
                break
        res["B"].append(outB * (1 - h))
        eb = px.reindex(w.index, method="ffill")
        res["ETH"].append(eb.iloc[-1] / eb.iloc[0])
    eth = np.array(res["ETH"])
    for rule in ("HOLD", "A", "B"):
        a = np.array(res[rule])
        rows.append(dict(collection=k, rule=rule, windows=len(a), mean_multiple_vs_btc=a.mean(),
                         median_multiple_vs_btc=np.median(a), p_beat_btc=(a > 1).mean(), p_beat_eth=(a > eth).mean(),
                         mean_eth_multiple=eth.mean(), p10=np.quantile(a, .1), p90=np.quantile(a, .9)))
df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "exit_rule_backtest.csv"), index=False)
pd.set_option("display.width", 220)
print(df.round(2).to_string())
