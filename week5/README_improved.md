# Cloud & API Deployment – Improved Guide

This repository contains:
- A simple Flask API (`app.py`) that predicts house prices.
- A NumPy linear regression model trained from `data/example_house_prices.csv`.
- Deployment configs for Docker → Google Cloud Run and (optionally) Render.
- A minimal web UI template in `templates/index.html`.

## 1) Project layout

```
.
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── data/
│   └── example_house_prices.csv
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── tests/
│   └── test_api.py
├── Dockerfile
├── openapi.yaml
├── cloudrun_deploy.sh
└── render.yaml
```

## 2) Create/refresh the model

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
```

This writes `model.pkl` used by the API.

## 3) Run locally

```bash
export FLASK_APP=app.py
export PORT=5000
python app.py
# open http://127.0.0.1:5000
```

Try the API:

```bash
curl -s -X POST http://127.0.0.1:5000/predict   -H "Content-Type: application/json"   -d '{"features": {"rooms": 6, "area_sqm": 250, "age_years": 1, "distance_km": 3}}'
```

## 4) Tests

```bash
pip install pytest
pytest -q
```

## 5) Containerize

```bash
docker build -t house-price-api .
docker run -p 8080:8080 house-price-api
# open http://127.0.0.1:8080
```

## 6) Deploy to **Google Cloud Run**

Prereqs: gcloud CLI logged in, a GCP project with free trial credits.

```bash
export PROJECT_ID=your-gcp-project-id
export REGION=europe-west1
export SERVICE=house-price-api

bash cloudrun_deploy.sh
```

The script prints a public URL at the end.

## 7) (Optional) Deploy to **Render**

- Commit/push to GitHub.
- In Render → "New" → "Web Service" → "Build from repository".
- Render will read `render.yaml` and build the Docker image. The service URL will be shown after deploy.

## 8) What to screenshot for your PDF

1. Dataset preview (head of CSV) and a note on features/target.
2. Training command output showing coefficients.
3. Local app running in the browser (`/` form) and a successful prediction.
4. API test via curl or Postman.
5. Cloud dashboard showing the service is live.
6. The live URL and a sample JSON response.
7. GitHub repo page.

---

**Tip**: Include `openapi.yaml` in your repo to document the API schema.
