"""Trade-frequency liquidity metrics for finalists from NFTPriceFloor 3-day bars (sales count, volume) and OpenSea
live stats. Exit-liquidity proxies that do not require order-book access.
Output: data/processed/liquidity_activity.csv
"""
import os
import numpy as np
import pandas as pd
from common import PROC, load_raw
F = [("milady", "milady", "milady"), ("remilio", "remilio-babies", "remilio-babies"),
     ("cryptodickbutts", "cryptodickbutts", "cryptodickbutts-s3"), ("pudgy", "pudgy-penguins", "pudgypenguins"),
     ("lil_pudgys", "lil-pudgys", "lilpudgys"), ("azuki", "azuki", "azuki"),
     ("chromie_squiggle", "chromie-squiggle-art-blocks-curated", "chromie-squiggle-by-snowfro"),
     ("terraforms", "terraforms-by-mathcastles", "terraforms"), ("v1punks", "v1-cryptopunks-wrapped", "official-v1-punks"),
     ("moonbirds", "proof-moonbirds", "moonbirds"), ("cryptopunks", "cryptopunks", "cryptopunks")]
px = pd.read_csv(os.path.join(PROC, "prices_daily.csv"), index_col=0, parse_dates=True)
rows = []
end = pd.Timestamp("2026-10-13")
for k, slug, oss in F:
    s = pd.read_csv(os.path.join(PROC, "npf_series", f"{slug}.csv"), index_col=0, parse_dates=True)
    st = load_raw(f"opensea/stats_{oss}.json")
    floor = st["total"]["floor_price"]
    r = {"key": k, "floor_eth": floor}
    for d in (30, 90, 365):
        w = s.loc[end - pd.Timedelta(days=d):]
        r[f"sales_{d}d"] = int(w.salesCount.sum())
        r[f"sales_per_day_{d}d"] = w.salesCount.sum() / d
        r[f"avg_price_over_floor_{d}d"] = (w.volumeNative.sum() / max(w.salesCount.sum(), 1)) / w.floorNative.mean()
        r[f"zero_sale_bars_pct_{d}d"] = (w.salesCount == 0).mean()
    # worst 90-day window in last 2y (sales/day) — liquidity in a drought
    w2 = s.loc[end - pd.Timedelta(days=730):].salesCount.rolling(30).sum() / 90
    r["worst_90d_sales_per_day_2y"] = w2.min()
    w2y = s.loc[end - pd.Timedelta(days=730):]
    r["usd_volume_365d_m"] = s.loc[end - pd.Timedelta(days=365):].volumeUsd.sum() / 1e6
    r["est_median_gap_hours_90d"] = 24 / r["sales_per_day_90d"] if r["sales_per_day_90d"] else np.nan
    rows.append(r)
df = pd.DataFrame(rows)
df.to_csv(os.path.join(PROC, "liquidity_activity.csv"), index=False)
pd.set_option("display.width", 250)
print(df[["key", "floor_eth", "sales_30d", "sales_90d", "sales_365d", "sales_per_day_90d", "avg_price_over_floor_90d",
          "zero_sale_bars_pct_90d", "worst_90d_sales_per_day_2y", "usd_volume_365d_m", "est_median_gap_hours_90d"]].round(2).to_string())
