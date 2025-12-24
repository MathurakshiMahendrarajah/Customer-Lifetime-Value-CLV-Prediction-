import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load model
with open("xgb_clv_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Customer Lifetime Value Prediction")

st.write("Enter customer RFM features to predict CLV:")

recency = st.number_input("Recency (days since last purchase)", min_value=0)
frequency = st.number_input("Frequency (number of purchases)", min_value=0)
monetary = st.number_input("Monetary (total spending)", min_value=0.0, step=0.01)

if st.button("Predict CLV"):
    X_new = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency","Frequency","Monetary"])
    prediction_log = model.predict(X_new)[0]        # model outputs log-transformed CLV
    prediction = np.expm1(prediction_log)          # convert back to actual CLV
    st.success(f"Predicted CLV: ${prediction:.2f}")