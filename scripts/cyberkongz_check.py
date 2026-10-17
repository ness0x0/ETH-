"""CyberKongz quick check (investor question, 2026-10-17). Not in the 47-collection universe; same tests as the rest.
NFTPriceFloor 3-day floors (coverage from May-2022) for Genesis, Babies and VX; BTC terms via prices_daily.csv.
Tests: 2024 low -> best euphoria to BTC's top (rough / perfect / pre-set 2x sell); 2024 low held to BTC's top and to
today; Oct-2022 halving-phase entry laddered into the three 2024-25 euphorias; floor around dated events.
"""
import os
import numpy as np
import pandas as pd
from common import PROC, get_json, save_raw, load_raw

px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
EVENTS = {"SEC Wells notice": "2024-12-16", "SEC probe closed": "2025-04-15", "KONG TGE (BANANA 1:25)": "2025-09-10",
          "DUMPSTR mint (Solana)": "2026-07-01"}


def series(slug, refresh=False):
    if refresh or load_raw(f"npf/{slug}.json") is None:
        save_raw(f"npf/{slug}.json", get_json(f"https://api-bff.nftpricefloor.com/projects/{slug}/charts/all"))
    d = load_raw(f"npf/{slug}.json")
    s = pd.DataFrame({k: d[k] for k in ("floorNative", "floorUsd", "salesCount")},
                     index=pd.to_datetime(d["timestamps"], unit="ms"))
    s = s[s.floorNative > 0]
    s["floorBtc"] = s.floorNative * px.eth_btc.reindex(s.index, method="ffill").values
    return s


def tests(s):
    f = s.floorBtc
    low = s.loc["2024-06-15":"2024-10-31"]
    ld = low.floorUsd.idxmin()
    eb = low.floorBtc.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)].mean()
    pk = s.loc["2024-11-01":"2025-10-06"]
    pdt = pk.floorBtc.idxmax()
    xw = f.loc[pdt - pd.Timedelta(days=15): pdt + pd.Timedelta(days=15)].mean()
    e0 = f.loc["2022-10-01":"2022-10-31"].mean()
    lad = np.mean([f.loc[a:b].mean() for a, b in (("2024-02-01", "2024-03-31"), ("2024-11-01", "2025-01-31"),
                                                  ("2025-07-01", "2025-09-30"))]) / e0 * 0.9
    return dict(now_eth=s.floorNative.iloc[-1], now_usd=s.floorUsd.iloc[-1], now_vs_peak_btc=f.iloc[-1] / f.max(),
                trade_rough=xw / eb * 0.9, trade_perfect=pk.floorBtc.max() / low.floorBtc.min(),
                hit_2x=bool((pk.floorBtc >= 2 / 0.9 * eb).any()),
                hold_to_btc_top=f.asof(pd.Timestamp("2025-10-06")) / eb * 0.9, hold_to_now=f.iloc[-1] / eb * 0.9,
                halving_ladder=lad)


if __name__ == "__main__":
    import sys
    rows = {}
    for slug in ("cyberkongz-genesis", "cyberkongz-babies", "cyberkongz-vx"):
        s = series(slug, refresh="--refresh" in sys.argv)
        rows[slug] = tests(s)
        if slug == "cyberkongz-genesis":
            for lab, dt in EVENTS.items():
                t = pd.Timestamp(dt)
                b = s.floorBtc.asof(t - pd.Timedelta(days=3))
                r = {h: round(s.floorBtc.asof(t + pd.Timedelta(days=h)) / b, 2) for h in (30, 90)
                     if t + pd.Timedelta(days=h) <= s.index[-1]}
                print(f"Genesis around {lab} ({dt}): floor in BTC vs 3 days before {r}")
    out = pd.DataFrame(rows).T
    out.to_csv(os.path.join(PROC, "cyberkongz_check.csv"))
    print(out.round(3).to_string())
