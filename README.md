# Frontend (Next.js map dashboard)

Planned structure:
- `pages/index.tsx` — AOI selector + map (Leaflet/Mapbox GL)
- `components/ResultsPanel.tsx` — canopy density, AGB range, confidence flag
- `components/ReportExport.tsx` — PDF audit report (SHOULD BUILD)

Fetches from `backend/app/main.py` → `GET /api/aoi/{aoi_id}/result`
(see root README for the JSON contract shape).
