'''
Price Prediction (Regression Problem)

Predict Column: Close, Adj Close, or High/Low.

Use Case:
- Predict future prices of the cryptocurrency (e.g., tomorrow's price or the next hour's price).
- Useful for trading strategies, forecasting, or portfolio management.

Used Models: LSTM (time series), ARIMA, XGBoost, AutoTS.
'''

import streamlit as st
import pandas as pd

# Modules
from FinPredictorX.PricePrediction.AutoTS import modelAutoTS

models = {
    "AutoTS": modelAutoTS
}

models_name = [None, 'AutoTS']

def price(df: pd.DataFrame):
    # Remove non-numeric features and the date column 
    numeric_columns = df.select_dtypes(exclude=['object']).columns

    target_options = [col for col in ['close', 'adj close', 'high', 'low'] if col in numeric_columns]

    if not target_options:
        st.error("Close, Adj Close, High, or Low columns not found in the dataset.", icon="🚨")
        return

    # Getting the target column from the user for prediction
    target_cols = st.multiselect("Select the target feature", target_options)

    # Choosing the model and it's configuration 
    chosen_model = st.selectbox("Select a model", models_name)

    forecast_days = st.slider("Select the number of days for forecasting", 1, 30, 3)

    credentials = []
    if chosen_model is not None:
        st.markdown('---\n### Model Configuration')

        if chosen_model == 'AutoTS':
            max_generations = st.slider("Select the maximum generations", 1, 20, 3)
            max_validations = st.slider("Select the maximum validations", 1, 10, 2)
            credentials = [max_generations, max_validations]

    if target_cols != [] and chosen_model is not None and st.button("Show Predictions"):
        st.markdown("---\n## Results")
        st.markdown("#### Last 5 Rows of the Dataset")
        st.dataframe(df[['date'] + target_cols].tail())
        for target_col in target_cols:
            model = models[chosen_model]
            model(df, forecast_days, target_col, credentials)
