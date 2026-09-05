"""Cloud masking, normalization, tiling, and NDVI computation."""
import numpy as np


def compute_ndvi(nir: np.ndarray, red: np.ndarray) -> np.ndarray:
    """Standard NDVI = (NIR - Red) / (NIR + Red), safe against divide-by-zero."""
    denom = nir.astype(float) + red.astype(float)
    denom[denom == 0] = 1e-6
    return (nir.astype(float) - red.astype(float)) / denom


def vegetation_mask(ndvi: np.ndarray, threshold: float = 0.3) -> np.ndarray:
    """Boolean mask of likely-vegetated pixels. Threshold is adjustable —
    expose as a UI slider per docs/architecture.md fallback design."""
    return ndvi > threshold


def cloud_mask_placeholder(scl_band: np.ndarray) -> np.ndarray:
    """Sentinel-2 Scene Classification Layer (SCL) cloud/shadow mask.
    Classes 3 (shadow), 8/9 (cloud medium/high), 10 (cirrus) are excluded."""
    excluded = {3, 8, 9, 10}
    return ~np.isin(scl_band, list(excluded))
