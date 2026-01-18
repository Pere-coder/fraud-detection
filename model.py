import joblib
import numpy as np
import pandas as pd

model = joblib.load('model.pk1')


def predict_fraud(feature):

    column_names = [
        'profile pic',             # Space instead of underscore
        'nums/length username', 
        'fullname words', 
        'nums/length fullname', 
        'name==username', 
        'description length',      # Space
        'external URL',            # Space and Uppercase URL
        'private', 
        '#posts',                  # Hashtag used
        '#followers',              # Hashtag used
        '#follows'                 # Hashtag used
    ]

    features_df = pd.DataFrame([feature], columns=column_names)
    # features = np.array(feature).reshape(1, -1)
    prediction = model.predict(features_df)
    probability = model.predict_proba(features_df)

    return {
        "is_fraud": bool(prediction[0]),
        "confidence": round(float(np.max(probability) * 100), 2)
    }