from flask import Flask, render_template, request
import pandas as pd
import pickle
import os
from app.utils.model_loader import load_model_and_encoder
from app.utils.predictor import predict_csv
from collections import Counter
import json

# Load model and encoder
model, encoder = load_model_and_encoder(
    'model/rf_model.pkl',
    'model/label_encoder.pkl'
)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in request'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    df = pd.read_csv(file)
    predictions = predict_csv(df, model, encoder)
    df['Predicted Label'] = predictions

    # Prepare results for table and chart
    result_html = df[['Predicted Label']].value_counts().to_frame('Count').reset_index().to_html(index=False, classes="table")
    chart_data = json.dumps(dict(Counter(predictions)))

    return render_template('index.html', result=result_html, chart_data=chart_data)

if __name__ == '__main__':
    app.run(debug=True)