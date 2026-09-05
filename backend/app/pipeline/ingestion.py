"""Fetch Sentinel-1/2 imagery for an AOI via Google Earth Engine.

Requires `earthengine-api` and an authenticated GEE account
(`earthengine authenticate`) — see README for the free academic tier.
"""
from typing import Any


def fetch_sentinel2(aoi_geojson: dict, start_date: str, end_date: str) -> Any:
    """Return a cloud-filtered Sentinel-2 SR image collection for the AOI.

    TODO: implement with ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(ee.Geometry(aoi_geojson)).filterDate(start_date, end_date)
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))
    """
    raise NotImplementedError("Wire up GEE auth + query here")


def fetch_sentinel1(aoi_geojson: dict, start_date: str, end_date: str) -> Any:
    """Return Sentinel-1 GRD backscatter for the AOI (SAR fusion — scoped use only:
    cloud-gap fill and biomass-saturation flagging, per docs/methodology.md)."""
    raise NotImplementedError("Wire up GEE auth + query here")
