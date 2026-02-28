import pandas as pd
import numpy as np

def preprocess_input(data_dict):
    df = pd.DataFrame([data_dict])
    
    # Ensure columns are in the same order used for training
    expected_columns = [...]  # List all feature names used during training
    df = df.reindex(columns=expected_columns, fill_value=0)

    # Convert to numeric if needed
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    
    return df
