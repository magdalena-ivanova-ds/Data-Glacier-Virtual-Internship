# Week 5 – Cloud and API Deployment (Report)

**Name:** {Your Name}  
**Batch code:** {Your Batch}  
**Submission date:** 2025-10-01  
**Submitted to:** {Course / Instructor}

## 1. Toy Data (CSV)
- Path: `data/example_house_prices.csv`
- Description: Synthetic housing dataset with features: rooms, area_sqm, age_years, distance_km; target: price.
- Screenshot: dataset head and summary stats.

## 2. Model Training
- Method: NumPy linear regression (normal equation).
- Command(s): `python train_model.py`
- Output: coefficients + intercept (paste or screenshot).

## 3. API & Web App
- Framework: Flask
- Endpoints:
  - `GET /` – HTML form
  - `POST /predict` – JSON: `{ "features": {...} }` → `{ "ok": true, "prediction": <number> }`
- OpenAPI file: `openapi.yaml` (include excerpt).

## 4. Cloud Deployment
- Provider: {GCP Cloud Run / Render / Azure / AWS}
- Steps: brief bullet list + screenshots (build logs, dashboard).
- Live URL: `https://...`

## 5. Testing Evidence
- `curl` or Postman request + response (screenshot).
- Unit tests: `pytest` output (screenshot).

## 6. Repository
- Link to GitHub repo + tree screenshot.

## 7. Lessons & Next Steps
- What worked, what you'd improve next (e.g., input validation, CI/CD, monitoring).
