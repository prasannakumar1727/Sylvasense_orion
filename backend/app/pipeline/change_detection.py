"""Multi-date change detection — the flagship, most defensible feature.

Compares canopy density/NDVI between two dates. Does not require single-tree
resolution, so it avoids the Sentinel-2 resolution limitation entirely.
"""
import numpy as np


def detect_change(ndvi_before: np.ndarray, ndvi_after: np.ndarray,
                   loss_threshold: float = -0.15) -> dict:
    """Return a change map and a simple flag.

    Note: seasonal NDVI variation can mimic loss — a real deployment should
    compare same-season dates or apply seasonal detrending before flagging.
    """
    diff = ndvi_after.astype(float) - ndvi_before.astype(float)
    loss_mask = diff < loss_threshold
    loss_pct = float(loss_mask.mean() * 100)
    flag = "loss_detected" if loss_pct > 5 else "stable"
    return {"loss_pct": round(loss_pct, 2), "change_flag": flag, "diff_map": diff}
