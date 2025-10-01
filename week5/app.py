from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

with open(os.path.join(os.path.dirname(__file__), 'model.pkl'), 'rb') as f:
    MODEL = pickle.load(f)

FEATURES = MODEL["features"]
COEF = np.array(MODEL["coef"], dtype=float)
INTERCEPT = float(MODEL["intercept"])

def predict_price(feat_dict):
    x = np.array([float(feat_dict[name]) for name in FEATURES], dtype=float)
    return float(np.dot(COEF, x) + INTERCEPT)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", features=FEATURES)

@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        payload = request.get_json(silent=True) or {}
        feats = payload.get("features", {})
        try:
            pred = predict_price(feats)
            return jsonify({"ok": True, "prediction": pred})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 400
    else:
        feats = {name: request.form.get(name, type=float) for name in FEATURES}
        try:
            pred = predict_price(feats)
            return render_template("index.html", features=FEATURES, last_input=feats, prediction=pred)
        except Exception as e:
            return render_template("index.html", features=FEATURES, last_input=feats, error=str(e)), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
