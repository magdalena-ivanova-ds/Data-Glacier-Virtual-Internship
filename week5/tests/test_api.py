import json
from app import app

def test_predict_smoke():
    client = app.test_client()
    payload = {"features": {"rooms": 3, "area_sqm": 120, "age_years": 10, "distance_km": 5}}
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    data = res.get_json()
    assert data.get("ok") is True
    assert isinstance(data.get("prediction"), (int, float))
