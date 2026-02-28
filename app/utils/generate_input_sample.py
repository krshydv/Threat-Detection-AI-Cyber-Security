import pandas as pd
import joblib

# Load expected features
features = joblib.load('model/feature_names.pkl')

# Create dummy data (5 rows of zeros)
sample_data = pd.DataFrame(0, index=range(5), columns=features)

# Save to CSV
sample_data.to_csv('valid_input.csv', index=False)

print("✅ valid_input.csv has been generated.")
