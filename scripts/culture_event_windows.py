"""Event-window and quiet-window floor returns for the cultural-research catalysts.

Inputs
  data/processed/catalysts/{milady,remilio,cryptodickbutts}.csv   (date,collection,event,category,...)
  data/processed/culture/quiet_windows.csv                         (collection,start,end,label,...)
  data/processed/npf_series/{milady,remilio-babies,cryptodickbutts}.csv  (3-day NFTPriceFloor bars)

Outputs
  data/processed/culture/event_windows.csv
  data/processed/culture/quiet_window_returns.csv

Method: pre = last NPF bar dated strictly before the event date; post_3d / post_30d / post_90d = first bar dated
>= event date + 3 / 30 / 90 days. Returns are simple floor changes in ETH (floorNative) and BTC (floorBtc).
NPF 3-day floors are noisy (single-bar mispriced-listing artefacts exist, e.g. milady 2022-05-22, 2023-05-20,
2024-03-18; remilio 2024-02-17), so short windows are indicative only. Coincidence is not causation.
Bar alignment (inferred, unverified): the bar label appears to be the END of a trailing 3-day window and the
floor behaves like a window minimum. The volume spike for Musk's 2023-05-10 post lands in the 2023-05-11 bar,
and the one for Vitalik's 2025-01-18 purchase lands in the 2025-01-21 bar. Prefer the 30d/90d windows.
"""
import csv
import datetime as dt
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = os.path.join(ROOT, "data", "processed", "catalysts")
CUL = os.path.join(ROOT, "data", "processed", "culture")
NPF = os.path.join(ROOT, "data", "processed", "npf_series")
SLUG = {"milady": "milady", "remilio": "remilio-babies", "cryptodickbutts": "cryptodickbutts"}


def load_series(slug):
    out = []
    with open(os.path.join(NPF, f"{slug}.csv")) as f:
        for r in csv.DictReader(f):
            try:
                out.append((dt.date.fromisoformat(r[""]), float(r["floorNative"]), float(r["floorBtc"])))
            except (ValueError, KeyError):
                continue
    return sorted(out)


def before(ser, d):
    c = [x for x in ser if x[0] < d]
    return c[-1] if c else None


def on_or_after(ser, d):
    c = [x for x in ser if x[0] >= d]
    return c[0] if c else None


def chg(a, b, i):
    if a is None or b is None or a[i] == 0:
        return ""
    return round(b[i] / a[i] - 1, 4)


def main():
    os.makedirs(CUL, exist_ok=True)
    rows = []
    for coll, slug in SLUG.items():
        ser = load_series(slug)
        with open(os.path.join(CAT, f"{coll}.csv")) as f:
            for e in csv.DictReader(f):
                d = dt.date.fromisoformat(e["date"])
                pre = before(ser, d)
                rec = {"collection": coll, "date": e["date"], "category": e["category"],
                       "expected_direction": e["expected_direction"], "event": e["event"][:120],
                       "pre_bar": pre[0].isoformat() if pre else "", "pre_floor_eth": pre[1] if pre else ""}
                for k, days in (("3d", 3), ("30d", 30), ("90d", 90)):
                    post = on_or_after(ser, d + dt.timedelta(days=days))
                    rec[f"ret_eth_{k}"] = chg(pre, post, 1)
                    rec[f"ret_btc_{k}"] = chg(pre, post, 2)
                rows.append(rec)
    with open(os.path.join(CUL, "event_windows.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    qrows = []
    with open(os.path.join(CUL, "quiet_windows.csv")) as f:
        for q in csv.DictReader(f):
            ser = load_series(SLUG[q["collection"]])
            a = on_or_after(ser, dt.date.fromisoformat(q["start"]))
            b = before(ser, dt.date.fromisoformat(q["end"]) + dt.timedelta(days=1))
            days = (b[0] - a[0]).days if a and b else ""
            qrows.append({"collection": q["collection"], "start": q["start"], "end": q["end"], "label": q["label"],
                          "start_floor_eth": a[1] if a else "", "end_floor_eth": b[1] if b else "", "days": days,
                          "ret_eth": chg(a, b, 1), "ret_btc": chg(a, b, 2)})
    with open(os.path.join(CUL, "quiet_window_returns.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(qrows[0].keys()))
        w.writeheader()
        w.writerows(qrows)
    print(f"wrote {len(rows)} event windows, {len(qrows)} quiet windows")


if __name__ == "__main__":
    main()
