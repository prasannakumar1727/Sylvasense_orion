"""AGB (aboveground biomass) estimation — always a range, never a bare number.

Cites: Chave, J. et al. (2014), "Improved allometric models to estimate the
aboveground biomass of tropical trees", Global Change Biology.
Real deployments must set biome-specific coefficients; the placeholders below
are illustrative only and must not be treated as calibrated values.
"""


def estimate_agb(canopy_density_pct: float, biome: str = "tropical_generic") -> dict:
    """Return AGB as {low, mid, high} tons/ha with a confidence label.

    TODO: replace placeholder coefficients with biome-calibrated values from
    the cited model before treating output as anything but illustrative.
    """
    base = canopy_density_pct * 2.5  # placeholder scaling — NOT calibrated
    low, mid, high = base * 0.75, base, base * 1.25

    confidence = "medium"
    if canopy_density_pct > 80:
        confidence = "low"  # dense canopy saturates optical signal
    elif canopy_density_pct < 20:
        confidence = "high"

    return {
        "agb_tons_per_ha": {"low": round(low, 0), "mid": round(mid, 0), "high": round(high, 0)},
        "confidence": confidence,
        "citation": "Chave et al. 2014",
        "biome": biome,
    }
