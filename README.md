# Customer Lifetime Value (CLV) Prediction App

A machine learning project that estimates Customer Lifetime Value (CLV) using transactional data and RFM (Recency, Frequency, Monetary) feature engineering. This project focuses on realistic modeling decisions, handling skewed business data, and clearly explaining model limitations rather than overclaiming accuracy.

The application includes a Streamlit-based demo to showcase how CLV predictions change with different customer profiles.

## Project Objective

To predict the future monetary value of customers based on their historical purchasing behavior and demonstrate how CLV models can support data-driven marketing and retention strategies.

## Key Concepts Used

- RFM (Recency, Frequency, Monetary) feature engineering
- Time-based train–test split to avoid data leakage
- Zero-inflated and highly skewed target handling
- Log transformation of CLV for stable regression
- Model comparison and selection based on robustness

## Data Preparation

- Removed invalid records (null customer IDs, negative quantities and prices)
- Converted invoice dates to datetime format
- Created total transaction value per invoice
- Defined CLV as future customer spend over a fixed time horizon using a temporal cutoff
- Aggregated transaction-level data into customer-level RFM features

## Feature Engineering (RFM)

- Recency – Days since last purchase 
- Frequency – Number of transactions
- Monetary – Total historical spend
Customers with no future purchases were assigned a CLV of zero to reflect real-world churn behavior.

## Modeling Approach

- Initial experiments included Linear Regression and tree-based models
- Due to the highly skewed and zero-inflated nature of CLV, the target variable was log-transformed using log1p
- XGBoost Regressor was selected as the final model due to:
    - Stable predictions
    - Better handling of non-linearity
    - Robustness to outliers

Model evaluation focused on MAE and RMSE rather than inflated R² scores.

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

These metrics were prioritized to ensure realistic error interpretation on noisy customer behavior data.

## Streamlit Demo Application

The Streamlit app allows users to input RFM values and observe predicted CLV behavior.

⚠️ Important Note:
Due to the skewed and noisy nature of CLV data, predictions for individual customers may vary widely. This app is intended to demonstrate relative customer value and model behavior, not to provide exact financial forecasts for production use.

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

The application is deployed using Streamlit for easy access and demonstration purposes.
1. Deployment link:
    ```bash
    https://customerlifetimevaluepredictionapp.streamlit.app

## Technology Stack
- Python 3.12
- Streamlit – Frontend UI
- Pandas & Numpy – Data processing
- XGBoost – Regression model
- Streamlit – Deployment

## Disclaimer

This project is designed for educational and demonstration purposes. CLV prediction is inherently uncertain, and real-world deployments typically require continuous retraining, segmentation strategies, and business-specific constraints.

## Screenshots
<img width="1702" height="695" alt="Screenshot 2025-12-24 at 10 10 05 PM" src="https://github.com/user-attachments/assets/b466309a-9315-4a01-a2ae-73ff872f6273" />


