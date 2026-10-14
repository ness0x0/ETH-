"""Ordinals panel: do Bitcoin-native collections behave differently from the Ethereum set? (investor question,
2026-10-14; outside the Ethereum mandate, a check rather than a full study)

Ordinals are priced in BTC, so floor_native IS the BTC-relative price: NFT/BTC = floor ratio.
Data:
  NFTPriceFloor 3-day bars per slug (Ordinals feeds are live from launch to ~Apr/May-2025, then frozen with zero
  sales; bars after the last sale are dropped).
  CoinGecko /nfts/{id}: current floor in BTC and its 1-year change (-> floor ~1 year ago, i.e. ~Oct-2025, near BTC's
  top). CoinGecko's USD floor uses a stale BTC price; we use BTC-native values only.
Tests (same definitions as the Ethereum work; 10% costs):
  cycle trade   2024 low (own min, 2024-06-15..2024-10-31; rough entry = mean +-45d) -> Nov-2024..Jan-2025 euphoria
                (rough exit = mean +-15d around own peak); also a pre-set 2x-vs-BTC sell from 2024-11-01 to feed end
  hold          2024 low -> ~Oct-2025 (CoinGecko 1y-ago) and -> today
  peaks         ATH (BTC) -> Dec-2024 peak -> ~Oct-2025 -> today
Outputs: data/processed/ordinals_panel.csv, printed summary
"""
import os
import time
import numpy as np
import pandas as pd
from common import RAW, PROC, get_json, save_raw, load_raw

# (name, NPF slug, CoinGecko id, type)
PANEL = [
    ("Bitcoin Puppets", "bitcoin-puppets", "bitcoin-puppets", "pfp"),
    ("NodeMonkes", "nodemonkes", "nodemonkes", "pfp"),
    ("Quantum Cats", "quantum-cats", "quantum-cats", "pfp"),
    ("Bitcoin Frogs", "bitcoin-frogs", "bitcoin-frogs", "pfp"),
    ("Ordinal Maxi Biz", "omb", "ordinal-maxi-biz-omb", "pfp"),
    ("OCM Genesis", "ocm-genesis", "ocm-genesis-by-onchainmonkey", "art"),
    ("Aeons", "aeons-btc", "aeons", "pfp"),
    ("BTC DeGods", "degods-ordinals", "btc-degods", "pfp"),
    ("Bitcoin Punks", "bitcoin-punks", "bitcoin-punks", "pfp"),
    ("Bitcoin Wizards", "bitcoin-wizards", "bitcoin-wizards", "pfp"),
    ("Natcats", "dmtnatcats", "natcats", "pfp"),
    ("Pizza Ninjas", "pizza-ninjas", "pizza-ninjas", "pfp"),
    ("Recursive Doodinals", "recursive-doodinals", "recursive-doodinals", "pfp"),
    ("BTC Machines", "btc-machines", "btc-machines", "art"),
    ("Honey Badgers", "honey-badgers", "honey-badgers", "pfp"),
    ("The Wizards of Ord", "wizards-of-ord", "the-wizards-of-ord", "pfp"),
    ("Little Pups", "little-pups", "little-pups", "pfp"),
    ("Game of Blocks", "gob-btc", "game-of-blocks", "pfp"),
    ("Goosinals", "goosinals", "goosinals", "pfp"),
    ("Tiny Vikings", "tiny-vikings", "tiny-vikings", "pfp"),
    ("Blob", "book-of-blob", "blob", "pfp"),
    ("Bitdogs", "bitdogs-btc", "bitdogs", "pfp"),
    ("Frucks", "frucks", "frucks", "pfp"),
    ("Bitcoin Shrooms", "bitcoin-shrooms", "bitcoin-shrooms", "pfp"),
    ("Based Angels", "based-angels", "based-angels", "pfp"),
    ("Billy Cats", "billy-cats", "billy-cats", "pfp"),
    ("Puppet Maxi Biz", "puppet-maxi-biz", "puppet-maxi-biz-pmb", "pfp"),
    ("Hashlings", "hashlings", "hashlings", "pfp"),
    ("Taproot Wizards", "taproot-wizards", "taproot-wizards", "pfp"),
    ("Idiots", "idiots-ordinals", "idiots", "pfp"),
    ("Airhead", "airhead", "airhead", "pfp"),
    ("O.P.I.U.M", "opium-nft", "o-p-i-u-m", "pfp"),
    ("Prometheans", "prometheans-nft", "prometheans", "pfp"),
    ("Bitmap", "bitmap", "bitmap", "other"),
    ("INK", "ink", "ink", "art"),
    ("CC0 Ordinals", "cc0-ordinals", "cc0", "art"),
    ("Twelvefold", "twelvefold", "twelvefold", "art"),
    ("The Golden Ratio (Harto)", "the-golden-ratio-by-harto-x-vivid", "the-golden-ratio-by-harto-x-vivid", "art"),
    ("FloraForms (Harto)", "floraforms-by-harto", "floraforms-by-harto-x-belvedere", "art"),
    ("Fukuhedrons", "fukuhedrons", "fukuhedrons", "art"),
    ("Pizza Pets", "pizza-pets", "pizza-pets-game", "other"),
    ("UniWorlds", "uniworlds-key-of-destiny", "uniworlds-key-of-destiny", "other"),
    ("Runestone", "runestone", "runestone", "runes-airdrop"),
    ("Rune Pups", "runes-pups", "rune-pups", "runes-airdrop"),
    ("Rune Doors", "rune-doors", "rune-doors", "runes-airdrop"),
    ("RSIC Metaprotocol", "rsic-metaprotocol", "rsic-metaprotocol", "runes-airdrop"),
    ("The Rune Guardians", "the-rune-guardians", "the-rune-guardians", "runes-airdrop"),
]
LOW = ("2024-06-15", "2024-10-31")
EUPH = ("2024-11-01", "2025-01-31")
COST = 0.10


def fetch(refresh=False):
    for name, npf, cg, _ in PANEL:
        p1, p2 = f"npf/{npf}.json", f"coingecko/nft_{cg}.json"
        if refresh or not os.path.exists(os.path.join(RAW, p1)):
            try:
                save_raw(p1, get_json(f"https://api-bff.nftpricefloor.com/projects/{npf}/charts/all"))
            except Exception as e:
                print("NPF fail", npf, e)
        if refresh or not os.path.exists(os.path.join(RAW, p2)):
            try:
                save_raw(p2, get_json(f"https://api.coingecko.com/api/v3/nfts/{cg}"))
            except Exception as e:
                print("CG fail", cg, e)
            time.sleep(3)


def series(npf):
    d = load_raw(f"npf/{npf}.json")
    if not isinstance(d, dict) or "timestamps" not in d:
        return None
    s = pd.DataFrame({k: d[k] for k in ("floorNative", "floorUsd", "salesCount")},
                     index=pd.to_datetime(d["timestamps"], unit="ms")).dropna()
    s = s[s.floorNative > 0]
    live = s[s.salesCount > 0]
    return s.loc[:live.index[-1]] if not live.empty else None


def cg_now(cg):
    d = load_raw(f"coingecko/nft_{cg}.json")
    if not isinstance(d, dict) or "floor_price" not in d or not d["floor_price"].get("native_currency"):
        return None, None
    now = d["floor_price"]["native_currency"]
    ch = (d.get("floor_price_1y_percentage_change") or {}).get("native_currency")
    return now, (now / (1 + ch / 100) if ch is not None and ch > -100 else None)


def run():
    rows = []
    for name, npf, cg, typ in PANEL:
        s = series(npf)
        now, yago = cg_now(cg)
        r = dict(name=name, type=typ, now_btc=now, oct2025_btc=yago)
        if s is None or len(s) < 10:
            rows.append(r)
            continue
        f = s.floorNative
        r.update(first_bar=f.index[0].date(), feed_end=f.index[-1].date(), ath_btc=f.max(), ath_date=f.idxmax().date(),
                 end_btc=f.iloc[-1])
        low = f.loc[LOW[0]:LOW[1]]
        eu = f.loc[EUPH[0]:EUPH[1]]
        if len(low) >= 10 and len(eu) >= 5:
            ld = low.idxmin()
            e = low.loc[ld - pd.Timedelta(days=45): ld + pd.Timedelta(days=45)].mean()
            pk = eu.idxmax()
            x = f.loc[pk - pd.Timedelta(days=15): pk + pd.Timedelta(days=15)].mean()
            path = f.loc[EUPH[0]:]
            r.update(low_btc=low.min(), low_date=ld.date(), dec_peak_btc=eu.max(), dec_peak_date=pk.date(),
                     trade_rough=x / e * (1 - COST), trade_perfect=eu.max() / low.min(),
                     hit_2x=bool((path >= 2 / (1 - COST) * e).any()), entry_btc=e,
                     hold_to_oct2025=(yago / e * (1 - COST)) if yago else np.nan,
                     hold_to_now=(now / e * (1 - COST)) if now else np.nan)
        rows.append(r)
    return pd.DataFrame(rows)


if __name__ == "__main__":
    import sys
    fetch(refresh="--refresh" in sys.argv)
    df = run()
    df.to_csv(os.path.join(PROC, "ordinals_panel.csv"), index=False)
    pd.set_option("display.width", 260)
    pd.set_option("display.max_columns", 30)
    cols = ["name", "type", "first_bar", "ath_btc", "ath_date", "low_btc", "dec_peak_btc", "oct2025_btc", "now_btc",
            "trade_rough", "hit_2x", "hold_to_oct2025", "hold_to_now"]
    print(df[cols].round(4).to_string())
    t = df.dropna(subset=["trade_rough"])
    print(f"\ncycle panel n={len(t)} (with CG now: {t.hold_to_now.notna().sum()})")
    for lab, g in (("all", t), ("pfp", t[t.type == "pfp"]), ("non-pfp", t[t.type != "pfp"])):
        h = g.dropna(subset=["hold_to_now"])
        print(f"{lab:8s} n={len(g)} trade beat BTC {(g.trade_rough > 1).mean():.0%}  >=2x {(g.trade_rough >= 2).mean():.0%}"
              f"  hit 2x target {g.hit_2x.mean():.0%} | hold->Oct25 beat {(h.hold_to_oct2025 > 1).mean():.0%}"
              f" median {h.hold_to_oct2025.median():.2f} | hold->now beat {(h.hold_to_now > 1).mean():.0%}"
              f" median {h.hold_to_now.median():.2f}")
    a = df.dropna(subset=["ath_btc", "now_btc"])
    print(f"now vs ATH (BTC): median {(a.now_btc / a.ath_btc).median():.3f}; share above 25% of ATH "
          f"{(a.now_btc / a.ath_btc > 0.25).mean():.0%}; n={len(a)}")
    b = df.dropna(subset=["dec_peak_btc", "oct2025_btc", "now_btc"])
    print(f"lower-highs: Dec-24 peak < ATH {(b.dec_peak_btc < b.ath_btc).mean():.0%}; Oct-25 < Dec-24 peak "
          f"{(b.oct2025_btc < b.dec_peak_btc).mean():.0%}; now < Oct-25 {(b.now_btc < b.oct2025_btc).mean():.0%}; n={len(b)}")
