"""Universe screening.

Sources (all keyless, fetched live; raw responses archived under data/raw/):
  - OpenSea API v2  GET /api/v2/collections/{slug}/stats   (live floor, owners, 1d/7d/30d volume+sales)
  - OpenSea API v2  GET /api/v2/collections/{slug}          (contracts, created_date, total_supply)
  - NFTPriceFloor   GET api-bff.nftpricefloor.com/projects/{slug}/charts/all  (3-day floor/volume/sales since ~May 2022)
  - Binance daily ETHBTC/BTCUSDT closes (data/processed/prices_daily.csv) for BTC-relative math.

Outputs: data/processed/npf_series/{slug}.csv, data/processed/screen_metrics.csv
"""
import os
import time
import pandas as pd
from common import get_json, save_raw, load_raw, PROC
from universe_config import UNIVERSE

OS = "https://api.opensea.io/api/v2"
NPF = "https://api-bff.nftpricefloor.com/projects/{}/charts/all"
SER = os.path.join(PROC, "npf_series")
os.makedirs(SER, exist_ok=True)

prices = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)


def fetch(refresh=False):
    for name, npf, oss, cat in UNIVERSE:
        for key, url in [(f"opensea/stats_{oss}.json", f"{OS}/collections/{oss}/stats"),
                         (f"opensea/collection_{oss}.json", f"{OS}/collections/{oss}"),
                         (f"nftpricefloor/charts_{npf}.json", NPF.format(npf))]:
            if not refresh and load_raw(key) is not None:
                continue
            try:
                save_raw(key, get_json(url))
            except Exception as e:  # noqa
                print("FAIL", name, url, e)
            time.sleep(0.6)


def series(npf):
    d = load_raw(f"nftpricefloor/charts_{npf}.json")
    if not d or "timestamps" not in d:
        return None
    s = pd.DataFrame({k: d[k] for k in ["floorNative", "floorUsd", "salesCount", "volumeNative", "volumeUsd"]},
                     index=pd.to_datetime(d["timestamps"], unit="ms").normalize())
    s = s[~s.index.duplicated(keep="last")]
    px = prices.reindex(s.index, method="ffill")
    s["eth_btc"] = px["eth_btc"].values
    s["floorBtc"] = s["floorNative"] * s["eth_btc"]
    s.to_csv(os.path.join(SER, f"{npf}.csv"))
    return s


def at(s, col, date):
    sub = s.loc[:date, col].dropna()
    return sub.iloc[-1] if len(sub) else float("nan")


def metrics():
    now = pd.Timestamp("2026-10-13")
    ethbtc_now = prices["eth_btc"].iloc[-1]
    ethusd_now = prices["eth_usd"].iloc[-1]
    rows = []
    for name, npf, oss, cat in UNIVERSE:
        st = load_raw(f"opensea/stats_{oss}.json") or {}
        co = load_raw(f"opensea/collection_{oss}.json") or {}
        tot = st.get("total", {})
        iv = {i["interval"]: i for i in st.get("intervals", [])}
        s = series(npf)
        r = dict(name=name, category=cat, opensea_slug=oss, npf_slug=npf,
                 contracts=";".join(c.get("address", "") for c in co.get("contracts", [])),
                 created=co.get("created_date", "")[:10], supply=co.get("total_supply"),
                 os_floor_eth=tot.get("floor_price"), os_owners=tot.get("num_owners"),
                 os_sales_total=tot.get("sales"), os_vol_total_eth=tot.get("volume"),
                 os_sales_1d=iv.get("one_day", {}).get("sales"), os_sales_7d=iv.get("seven_day", {}).get("sales"),
                 os_sales_30d=iv.get("thirty_day", {}).get("sales"),
                 os_vol_30d_eth=iv.get("thirty_day", {}).get("volume"))
        fl = r["os_floor_eth"] or float("nan")
        sup = r["supply"] or float("nan")
        r["floor_usd"] = fl * ethusd_now
        r["floor_btc"] = fl * ethbtc_now
        r["floor_cap_usd_m"] = fl * sup * ethusd_now / 1e6
        r["owners_per_supply"] = (r["os_owners"] or 0) / sup if sup else float("nan")
        r["avg_sale_30d_eth"] = (r["os_vol_30d_eth"] / r["os_sales_30d"]) if r["os_sales_30d"] else float("nan")
        r["sales_per_day_30d"] = (r["os_sales_30d"] or 0) / 30
        if s is not None and len(s):
            r["npf_first"] = s.index[0].date()
            r["npf_floor_now"] = s["floorNative"].iloc[-1]
            ath_i = s["floorNative"].idxmax()
            r["npf_ath_floor_eth"] = s["floorNative"].max()
            r["npf_ath_date"] = ath_i.date()
            r["npf_ath_floor_btc"] = s["floorBtc"].max()
            r["npf_ath_btc_date"] = s["floorBtc"].idxmax().date()
            for lbl, d in [("1y", now - pd.DateOffset(years=1)), ("2y", now - pd.DateOffset(years=2)),
                           ("3y", now - pd.DateOffset(years=3))]:
                f0 = at(s, "floorNative", d)
                b0 = at(s, "floorBtc", d)
                r[f"floor_eth_{lbl}_ago"] = f0
                r[f"chg_eth_{lbl}"] = fl / f0 - 1 if f0 == f0 and f0 else float("nan")
                r[f"chg_btc_{lbl}"] = (fl * ethbtc_now) / b0 - 1 if b0 == b0 and b0 else float("nan")
            r["drawdown_from_ath_eth"] = fl / r["npf_ath_floor_eth"] - 1
            r["drawdown_from_ath_btc"] = fl * ethbtc_now / r["npf_ath_floor_btc"] - 1
            last365 = s.loc[now - pd.DateOffset(days=365):]
            r["npf_sales_365d"] = last365["salesCount"].sum()
            r["npf_vol_365d_eth"] = last365["volumeNative"].sum()
            r["npf_floor_min_365d"] = last365["floorNative"].min()
            r["npf_floor_max_365d"] = last365["floorNative"].max()
        rows.append(r)
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(PROC, "screen_metrics.csv"), index=False)
    return df


if __name__ == "__main__":
    import sys
    fetch(refresh="--refresh" in sys.argv)
    df = metrics()
    pd.set_option("display.width", 300)
    pd.set_option("display.max_rows", 200)
    cols = ["name", "os_floor_eth", "floor_usd", "floor_cap_usd_m", "os_owners", "owners_per_supply", "os_sales_30d",
            "npf_ath_floor_eth", "npf_ath_date", "drawdown_from_ath_btc", "chg_btc_1y", "chg_btc_2y", "chg_btc_3y"]
    print(df[cols].sort_values("floor_cap_usd_m", ascending=False).round(3).to_string())
