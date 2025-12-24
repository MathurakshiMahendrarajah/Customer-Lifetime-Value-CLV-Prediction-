# Customer Lifetime Value (CLV) Prediction App

A Streamlit web application to predict Customer Lifetime Value (CLV) using RFM (Recency, Frequency, Monetary) features.
This app demonstrates how machine learning models can help businesses estimate the future value of customers and make data-driven marketing decisions.

## Features
- Predict CLV based on:
- Recency: Days since the last purchase
- Frequency: Number of purchases
- Monetary: Total spending
- User-friendly interface built with Streamlit
- Deployed on Streamlit for easy public access
- Model trained with XGBoost, leveraging robust regression for accurate predictions
- Handles log-transformed CLV to manage outliers effectively

## How It Works
- User inputs the RFM values for a customer.
- The app sends the input to the pre-trained XGBoost regression model.
- The model predicts the CLV, which is then displayed in dollars.

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/MathurakshiMahendrarajah/Customer-Lifetime-Value-CLV-Prediction-.git
    cd Customer-Lifetime-Value-CLV-Prediction

2. Install dependencies
    ```bash
    pip install -r requirements.txt

3. Run the app
    ```bash
    streamlit run app.py

## Deployment
1. The app is deployed on Streamlit, making it accessible without local setup:
    ```bash
    https://customerlifetimevaluepredictionapp.streamlit.app

#  Technology Stack
- Python 3.12
- Streamlit – Frontend UI
- Pandas & Numpy – Data processing
- XGBoost – Regression model
- Streamlit – Deployment

# Screenshots
<img width="1702" height="695" alt="Screenshot 2025-12-24 at 10 10 05 PM" src="https://github.com/user-attachments/assets/b466309a-9315-4a01-a2ae-73ff872f6273" />


