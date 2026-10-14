"""Cycle A (2019/20 lows → 2021–22 euphoria) low→high multiples, and leadership rotation into Cycle B.

Inputs : data/processed/cycleA_weekly.csv (OpenSea sampled sales, weekly 48h windows, 10th-percentile price),
         data/processed/punks_weekly.csv (on-chain PunkBought, weekly 10th percentile),
         data/processed/cycle_episodes.csv (Cycle B results), prices_daily.csv
Method : USD floor proxy = ETH proxy x ETH/USD on the sample date. Peak = max USD proxy 2021-08-01..2022-05-31.
         Low = min USD proxy from (first sample + 28 days, to skip the mint window) to the peak date.
         Collections minted in 2021 have a "launch-phase" low, not a cycle low; flagged.
         Rough timing as in Cycle B: entry = mean ±45d around low, exit = mean ±15d around peak, −10% costs.
         Proxies are 3-point rolling medians to suppress single-window noise.
Output : data/processed/cycleA_summary.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC

px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
NAMES = {"chromie-squiggle-by-snowfro": ("Chromie Squiggle", "OG (pre-2021)"), "milady": ("Milady Maker", "2021 mint"),
         "pudgypenguins": ("Pudgy Penguins", "2021 mint"), "cryptodickbutts-s3": ("CryptoDickbutts", "2021 mint"),
         "boredapeyachtclub": ("Bored Ape Yacht Club", "2021 mint"), "meebits": ("Meebits", "2021 mint"),
         "hashmasks": ("Hashmasks", "OG (Jan-2021)"), "cool-cats-nft": ("Cool Cats", "2021 mint"),
         "doodles-official": ("Doodles", "2021 mint"), "azuki": ("Azuki", "2022 mint"),
         "terraforms": ("Terraforms", "2021 mint"), "mutant-ape-yacht-club": ("Mutant Ape Yacht Club", "2021 mint"),
         "cryptopunks": ("CryptoPunks", "OG (2017)")}


def series():
    out = {}
    a = pd.read_csv(os.path.join(PROC, "cycleA_weekly.csv"), parse_dates=["date"])
    for slug, g in a.groupby("slug"):
        s = g.set_index("date").floor_proxy_p10.dropna()
        out[slug] = s.rolling(3, center=True, min_periods=2).median()
    p = pd.read_csv(os.path.join(PROC, "punks_weekly.csv"), index_col=0, parse_dates=True)
    s = p.loc["2019-01-01":"2022-06-30", "floor_proxy_p10"].dropna()
    out["cryptopunks"] = s.rolling(3, center=True, min_periods=2).median()
    return out


def main():
    rows = []
    for slug, s in series().items():
        if len(s) < 8:
            continue
        eth = s
        usd = eth * px["eth_usd"].reindex(eth.index, method="ffill").values
        btc = eth * px["eth_btc"].reindex(eth.index, method="ffill").values
        pk_win = usd.loc["2021-08-01":"2022-05-31"]
        if pk_win.empty:
            continue
        pk = pk_win.idxmax()
        start = eth.index[0] + pd.Timedelta(days=28)
        lo_win = usd.loc[start:pk]
        if lo_win.empty:
            continue
        lo = lo_win.idxmin()
        ent = lambda x: x.loc[lo - pd.Timedelta(days=45): lo + pd.Timedelta(days=45)].loc[:pk].mean()
        ext = lambda x: x.loc[pk - pd.Timedelta(days=15): pk + pd.Timedelta(days=15)].mean()
        name, kind = NAMES.get(slug, (slug, ""))
        b0, b1 = px.btc_usd.asof(lo), px.btc_usd.asof(pk)
        rows.append(dict(slug=slug, name=name, kind=kind, low_date=lo.date(), peak_date=pk.date(),
                         low_eth=eth[lo], peak_eth=eth[pk], usd_perfect=usd[pk] / usd[lo],
                         btc_usd_mult=b1 / b0, vs_btc_perfect=btc[pk] / btc[lo],
                         usd_rough=ext(usd) / ent(usd) * 0.9, vs_btc_rough=ext(btc) / ent(btc) * 0.9,
                         eth_rough=ext(eth) / ent(eth) * 0.9,
                         jun2022_vs_peak_usd=usd.loc["2022-05-15":"2022-06-30"].mean() / usd[pk]))
    df = pd.DataFrame(rows).sort_values("vs_btc_rough", ascending=False)
    # leadership rotation: Cycle B (rough) for the same collections
    cb = pd.read_csv(os.path.join(PROC, "cycle_episodes.csv"))
    cb = cb[cb.episode == "BIG_2022_2025"].set_index("name")["vs_btc_rough"]
    df["cycleB_vs_btc_rough"] = df.name.map(cb)
    df.to_csv(os.path.join(PROC, "cycleA_summary.csv"), index=False)
    return df


if __name__ == "__main__":
    pd.set_option("display.width", 250)
    print(main().round(2).to_string())
