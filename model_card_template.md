# Model Card — sylvasense-v0.3

*(Mitchell et al. 2019 practice — fill in per model release)*

**Scope:** Canopy density segmentation + change flagging from Sentinel-2 tiles.

**Training data:** [describe labeled/unlabeled sources, region, dates]

**Intended use:** Wide-area canopy monitoring, deforestation flagging, biomass
range estimation for forestry/carbon-audit workflows.

**Not intended for:** Individual tree counting, legal-grade carbon certification
without human review, biomes outside calibration region.

**Metrics:** [IoU / F1 for segmentation; correlation vs. GFW layer for validation]

**Known failure modes:** Dense closed-canopy overlap undercounts clusters; sparse/dry
vegetation may be misclassified by NDVI threshold; SAR speckle noise near coastlines.

**Confidence flagging logic:** [describe how low-confidence tiles are detected/shown]
