# Contributing (team workflow)

- Branch per feature (`ingestion`, `segmentation`, `frontend-map`, etc.)
- Run `pytest tests/ -v` before pushing — CI runs the same suite on every PR
- Keep pipeline functions pure (input array → output dict) so they stay testable
  without GEE credentials
- Update `docs/model_card_template.md` whenever the model version changes
