"""Unit tests for the core pipeline functions (no GEE auth needed to run)."""
import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.app.pipeline.preprocessing import compute_ndvi, vegetation_mask
from backend.app.pipeline.segmentation import classical_fallback
from backend.app.pipeline.change_detection import detect_change
from backend.app.pipeline.biomass import estimate_agb


def test_ndvi_range():
    nir = np.array([[0.5, 0.4]]); red = np.array([[0.1, 0.2]])
    ndvi = compute_ndvi(nir, red)
    assert (ndvi <= 1).all() and (ndvi >= -1).all()

def test_ndvi_no_div_by_zero():
    nir = np.zeros((2, 2)); red = np.zeros((2, 2))
    ndvi = compute_ndvi(nir, red)
    assert np.isfinite(ndvi).all()

def test_vegetation_mask_threshold():
    ndvi = np.array([[0.1, 0.5], [0.6, 0.2]])
    mask = vegetation_mask(ndvi, threshold=0.3)
    assert mask.tolist() == [[False, True], [True, False]]

def test_classical_fallback_returns_expected_keys():
    mask = np.array([[True, False], [True, True]])
    result = classical_fallback(mask)
    assert {"canopy_density_pct", "cluster_count", "method"} <= result.keys()
    assert 0 <= result["canopy_density_pct"] <= 100

def test_change_detection_flags_loss():
    before = np.full((4, 4), 0.6)
    after = before.copy(); after[:2, :2] = 0.2
    result = detect_change(before, after)
    assert result["change_flag"] == "loss_detected"

def test_change_detection_stable_when_no_change():
    same = np.full((4, 4), 0.5)
    result = detect_change(same, same)
    assert result["change_flag"] == "stable"

def test_agb_always_returns_range():
    result = estimate_agb(50.0)
    agb = result["agb_tons_per_ha"]
    assert agb["low"] <= agb["mid"] <= agb["high"]
    assert result["confidence"] in {"low", "medium", "high"}
    assert result["citation"] == "Chave et al. 2014"
