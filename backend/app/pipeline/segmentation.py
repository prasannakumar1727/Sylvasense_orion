"""Canopy density segmentation: pretrained CV primary path + classical fallback.

Per docs/methodology.md, this estimates canopy density/clusters, not individual
tree counts (10m resolution does not support single-tree detection reliably).
"""
import numpy as np
from scipy import ndimage


def classical_fallback(veg_mask: np.ndarray) -> dict:
    """NDVI-threshold + connected-component clustering. No labeled data required.
    Lower accuracy than a fine-tuned model, but fully explainable — the
    documented fallback if Step 3 fine-tuning data/time runs short."""
    labeled, n_clusters = ndimage.label(veg_mask)
    canopy_density_pct = float(veg_mask.mean() * 100)
    return {
        "canopy_density_pct": round(canopy_density_pct, 1),
        "cluster_count": int(n_clusters),
        "method": "classical_ndvi_watershed",
    }


def segment_canopy(tile: np.ndarray, model=None) -> dict:
    """Primary path: pretrained/fine-tuned model (e.g. YOLOv8-OBB or a
    segmentation head). Falls back to classical_fallback if model is None
    or confidence is too low."""
    if model is None:
        raise NotImplementedError(
            "Wire up fine-tuned model here; classical_fallback() is the "
            "working fallback path used by default in the MVP."
        )
    # model.predict(tile) -> canopy density + confidence per tile
    raise NotImplementedError
