"""SylvaSense API entrypoint.

Run: uvicorn backend.app.main:app --reload
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="SylvaSense API", version="0.3.0")

# --- cached demo results (offline-safe) ---------------------------------
DEMO_RESULTS = {
    "AOI-014": {
        "aoi_id": "AOI-014",
        "date_range": ["2024-01", "2024-07"],
        "canopy_density_pct": 62.4,
        "change_flag": "loss_detected",
        "agb_tons_per_ha": {"low": 118, "mid": 146, "high": 171},
        "confidence": "medium",
        "model_version": "sylvasense-v0.3",
        "citation": "Chave et al. 2014",
    }
}


class AOIResult(BaseModel):
    aoi_id: str
    date_range: list[str]
    canopy_density_pct: float
    change_flag: str
    agb_tons_per_ha: dict
    confidence: str
    model_version: str
    citation: str


@app.get("/api/aoi/{aoi_id}/result", response_model=AOIResult)
def get_result(aoi_id: str):
    """Return cached/precomputed result for a demo AOI.

    In production this triggers ingestion -> preprocessing -> segmentation ->
    change_detection -> biomass (see backend/app/pipeline/). For hackathon
    demo reliability, cached results are served directly so judging never
    depends on a live Earth Engine call.
    """
    result = DEMO_RESULTS.get(aoi_id)
    if not result:
        raise HTTPException(status_code=404, detail="AOI not cached for demo")
    return result


@app.get("/health")
def health():
    return {"status": "ok"}
