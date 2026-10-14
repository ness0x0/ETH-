"""Bitcoin Puppets (Ordinals) sanity check for the investor's intuition (2026-10-14): "at BTC $180k, Puppets must be
$5k+". Out of the Ethereum mandate; a quick check, not a dossier.

Puppets are priced in BTC, so floor_USD = floor_BTC x BTC_USD. The question is whether the floor holds in BTC terms.
Inputs : data/raw/npf/bitcoin-puppets.json (NFTPriceFloor 3-day bars; live Jan-2024 -> Apr-2025, then frozen with zero
         sales, so bars after the last sale are dropped), data/raw/coingecko/nft_bitcoin-puppets.json (current floor in
         BTC and its 1-year change; CoinGecko's USD figure uses a stale BTC price, so USD is recomputed here),
         prices_daily.csv
Output : data/processed/puppets_monthly.csv; printed summary
"""
import json
import os
import pandas as pd
from common import PROC, RAW

BTC_NOW, BTC_TARGETS = 83350.0, (180000.0, 210000.0)


def main():
    d = json.load(open(os.path.join(RAW, "npf", "bitcoin-puppets.json")))["data"]
    s = pd.DataFrame({k: d[k] for k in ("floorNative", "floorUsd", "salesCount", "volumeUsd")},
                     index=pd.to_datetime(d["timestamps"], unit="ms"))
    s = s.loc[:s[s.salesCount > 0].index[-1]]
    m = s.resample("ME").agg({"floorNative": "mean", "floorUsd": "mean", "salesCount": "sum", "volumeUsd": "sum"})
    m.to_csv(os.path.join(PROC, "puppets_monthly.csv"))
    cg = json.load(open(os.path.join(RAW, "coingecko", "nft_bitcoin-puppets.json")))
    fetched, cg = cg["fetched_at_utc"], cg["data"]
    now_btc = cg["floor_price"]["native_currency"]
    yago_btc = now_btc / (1 + cg["floor_price_1y_percentage_change"]["native_currency"] / 100)
    px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
    yago_date = pd.Timestamp(fetched[:10]) - pd.Timedelta(days=365)
    print(m.round(4).to_string())
    print(f"NPF peak floor {s.floorNative.max():.3f} BTC on {s.floorNative.idxmax().date()} "
          f"(${s.floorUsd.max():,.0f}); last live bar {s.index[-1].date()} {s.floorNative.iloc[-1]:.4f} BTC")
    print(f"CoinGecko now ({fetched}): {now_btc:.5f} BTC = ${now_btc * BTC_NOW:,.0f} at BTC ${BTC_NOW:,.0f}; "
          f"supply {cg['total_supply']:.0f} -> cap ${now_btc * BTC_NOW * cg['total_supply'] / 1e6:.1f}M; "
          f"1y ago ~{yago_btc:.4f} BTC (~{yago_date.date()}, BTC ${px.btc_usd.asof(yago_date):,.0f} "
          f"-> ${yago_btc * px.btc_usd.asof(yago_date):,.0f})")
    for floor in (now_btc, 1000 / BTC_NOW):
        for b in BTC_TARGETS:
            print(f"from {floor:.4f} BTC: at BTC ${b:,.0f} flat-in-BTC = ${floor * b:,.0f}; "
                  f"$5k needs {5000 / b / floor:.2f}x vs BTC")


if __name__ == "__main__":
    main()
