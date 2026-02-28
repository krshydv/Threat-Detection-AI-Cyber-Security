import pandas as pd
import joblib

def predict_csv(df, model, encoder):
    try:
        # Load the expected feature names
        feature_names = joblib.load('model/feature_names.pkl')

        # Keep only the expected features (drop extras, ignore missing)
        df = df.reindex(columns=feature_names)

        # Fill any missing values with 0 or suitable default
        df.fillna(0, inplace=True)

        # Predict
        predictions = model.predict(df)
        return encoder.inverse_transform(predictions)
    except Exception as e:
        return f"Prediction failed: {str(e)}"
