import joblib
import numpy as np
import pandas as pd

model = joblib.load('model.pk1')


def predict_fraud(feature):
    features = np.array(feature).reshape(1, -1)
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    return {
        "is_fraud": bool(prediction[0]),
        "confidence": round(float(np.max(probability) * 100), 2)
    }