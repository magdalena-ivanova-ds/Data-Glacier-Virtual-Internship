"""
Train a simple linear regression (NumPy) on data/toy_house_prices.csv
and save model.pkl with coef, intercept, and feature names.
"""
import os, pickle
import numpy as np
import pandas as pd

HERE = os.path.dirname(__file__)
CSV = os.path.join(HERE, "data", "example_house_prices.csv")
MODEL_OUT = os.path.join(HERE, "model.pkl")

def main():
    df = pd.read_csv(CSV)
    features = ["rooms", "area_sqm", "age_years", "distance_km"]
    X = df[features].to_numpy()
    y = df["price"].to_numpy()

    X_i = np.hstack([X, np.ones((X.shape[0], 1))])
    beta = np.linalg.pinv(X_i.T @ X_i) @ (X_i.T @ y)
    coef = beta[:-1]
    intercept = float(beta[-1])
    model = {"features": features, "coef": coef.tolist(), "intercept": intercept}

    with open(MODEL_OUT, "wb") as f:
        pickle.dump(model, f)

    print("Saved model to", MODEL_OUT)
    print("Features:", features)
    print("Coef:", coef)
    print("Intercept:", intercept)

if __name__ == "__main__":
    main()
