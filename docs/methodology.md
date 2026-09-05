# Methodology & Honest Framing

## What we do NOT claim
Sentinel-2 is 10m/pixel. Most tree crowns are smaller than one pixel, so
**individual-tree counting is not physically reliable** at this resolution.
We do not claim it.

## What we DO claim
- **Canopy density / cover %** per tile (defensible at 10m).
- **Change detection** (loss/gain) via multi-date NDVI/segmentation diff — flagship
  feature, does not require single-tree resolution.
- **AGB (biomass) as a range**, from a named published allometric model
  (Chave et al. 2014), never a bare point estimate.
- **Confidence flag** per output tile (dense canopy = lower count confidence,
  shown on the map, not hidden).

## Validation
One external ground-truth sanity check per demo AOI against Global Forest Watch's
open canopy-cover layer — directional correlation, not full validation.

## Known limitations
- Allometric error margins are typically 30–50%+ and biome-calibrated.
- SAR fusion is scoped to exactly one job (cloud-gap fill / biomass-saturation
  flagging) — not a vague "improves everything" claim.
- Generalization across biomes is future work, not a current claim.
