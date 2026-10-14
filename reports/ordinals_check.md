# Ordinals vs the Ethereum set: does Bitcoin-native provenance change the odds? (check, 2026-10-14)

_Outside the Ethereum mandate; a check, not a full study. Script: `scripts/ordinals_check.py` → `data/processed/ordinals_panel.csv`._

**Panel.** 47 notable Ordinals collections: PFPs, art, and the Runes-era airdrop collections.

**Data.**
- *NFTPriceFloor* 3-day floors. Its Ordinals feeds run from launch (or Aug-2023, when its coverage starts) to ~Apr-2025,
  then freeze.
- *CoinGecko* current floors, plus the 1-year change, which gives the ~Oct-2025 level near BTC's top. The tiniest
  collections' CoinGecko floors are noisy.

**Units.** Ordinals are priced in BTC, so the floor ratio *is* the result vs BTC. All figures deduct 10% costs, except
the peak and launch figures.

## Same tests as the Ethereum work

| Test (rough timing) | Ordinals (n=41) | Ethereum set (n=44) |
|---|---|---|
| 2024 low → Dec-2024 euphoria: beat BTC | **22%** (PFPs 30%) | 73% |
| …reached 2× vs BTC (pre-set sell) | **1 of 41** (Based Angels) | 32% |
| 2024 low, held to ~Oct-2025 (BTC's top): beat BTC | **1 of 41**, median 0.36× | 41%, median 0.82× |
| 2024 low, held to today: beat BTC | **0 of 41**, median 0.13× | 5%, median 0.36× |

**Lower highs every time.**
- The Dec-2024 peak was below the ATH for 95% of collections.
- The ~Oct-2025 level was below the Dec-2024 peak for all of them, and today is below Oct-2025 for all of them.
- The median collection is at 2.7% of its ATH in BTC terms. Only 2 of 47 are above 25% of it.

**The multiples came from the launch phase.**
- 34 of 47 ATHs fell between Dec-2023 and May-2024, during the Ordinals and Runes launch boom around the halving.
- From the first tracked month to the ATH, the median was 2.2× vs BTC, and 34% did ≥4×: Puppets 17.9×, Bitcoin Frogs
  17.0×, Based Angels 10.9×, OMB 5.7×, NodeMonkes 4.5×.
- Today the median collection is at 0.09× its first-month floor in BTC. Only 9% are above it.

## Bitcoin Puppets in this panel

Puppets was one of the better ones.
- **Cycle trade:** the 2024 low → Dec-2024 trade returned 1.33× vs BTC, the 4th best of 41. A pre-set 2× sell just
  missed (peak 0.172 BTC against a ~0.18 target).
- **Hold:** from the 2024 low, it was 0.38× vs BTC at BTC's top and is 0.10× today.
- **Since launch:** it trades at 0.46× its first-month floor in BTC, which is flat in USD since Jan-2024 (~$860 then,
  ~$850 now) while BTC roughly doubled.
- **The investor's $7–10k at BTC $180–210k** means 0.033–0.056 BTC: 3.3–5.4× vs BTC from 0.0102. That is above where
  Puppets traded at the last BTC top (~0.040).

## Catalyst: a new art drop or holder mint (Ethereum event study, `event_study.csv`)

- **Overall:** in 9 independent companion-collection events, the median 90-day return vs the sector was −9%, and 4 of
  9 were positive.
- **Range:** from Azuki Elementals (−64%; seen as diluting the originals) to Remilia's Bonkler (+144%, overlapping
  Musk's Milady post).
- **Caveat:** a holder mint can carry value outside the floor, in the new pieces themselves. This test does not
  capture that.

## Provenance

On Ethereum, the most provenance-valued names did worst against BTC.
- **Halving-cycle test (`cycle_analysis.md` F):** none of the 11 art and historical collections beat BTC. CryptoPunks
  finished at 0.38×, Autoglyphs 0.30×, Squiggle 0.25×.
- **Ordinals:** the art names here (Twelvefold, Harto, OCM, BTC Machines, INK, CC0) beat BTC in 1 of 7 cycle trades,
  and in none of the holds.

## Read

- **Ordinals have been a stronger version of the Ethereum pattern, not an exception to it.** The multiples happened
  in the launch boom. After that, it was decay vs BTC with each peak lower than the last.
- **A new Ordinals meta (new collections, a new protocol) is where the past multiples came from.** An existing
  collection getting back to old USD levels would need 3–5× vs BTC, which no collection in this panel did after its
  launch phase.
- **Data limits:** the NPF feeds freeze in spring 2025, Oct-2025 values are derived from CoinGecko's 1-year change,
  and there is one cycle of data.
