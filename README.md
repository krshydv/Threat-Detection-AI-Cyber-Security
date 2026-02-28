# AI-Powered Cyber Threat Detection System

This project is a machine learning-based system designed to detect and classify malicious network traffic using supervised learning techniques. It leverages well-known intrusion detection datasets such as CICIDS2017 and NSL-KDD to identify different categories of cyber attacks including DoS, Port Scan, Infiltration, and other anomalous behaviors.

## Problem Statement

Modern networks face increasingly sophisticated cyber threats. Traditional rule-based intrusion detection systems struggle to adapt to evolving attack patterns. This project aims to build an intelligent detection system capable of identifying malicious traffic patterns and classifying attack types using machine learning models.

## System Overview

The system consists of the following components:

- Data preprocessing pipeline for structured network traffic data
- Feature engineering and alignment module
- Random Forest classification model
- Model serialization using pickle
- Flask-based web application interface for predictions

The backend processes input features such as flow duration, protocol type, and packet size, and predicts whether the traffic is benign or malicious, along with the potential attack category.

## Features

- Multi-class attack classification
- Support for batch-based prediction via CSV uploads
- Preprocessing and feature validation
- Modular and extensible project structure
- Web interface built using Flask

## Machine Learning Approach

Algorithm used:
- Random Forest Classifier

Datasets:
- CICIDS2017
- NSL-KDD

Evaluation metrics:
- Accuracy
- Precision
- Recall
- F1-Score

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

## Project Structure

Threat-Detection-AI-Cyber-Security/

app/ – Flask application code  
model/ – Serialized model files  
run.py – Application entry point  
.gitignore  
README.md  

## Installation and Setup

1. Clone the repository:

git clone https://github.com/krshydv/Threat-Detection-AI-Cyber-Security.git  
cd Threat-Detection-AI-Cyber-Security  

2. Create a virtual environment:

python -m venv venv  
source venv/bin/activate  

3. Install dependencies:

pip install -r requirements.txt  

4. Run the application:

python run.py  

Open the application in your browser at:

http://127.0.0.1:5000

## Future Improvements

- Integration of deep learning models such as LSTM or Autoencoders
- Real-time packet capture support
- Docker-based containerization
- Cloud deployment
- Automated model retraining pipeline

## Author

Krish Yadav  
B.Tech Computer Science Engineering