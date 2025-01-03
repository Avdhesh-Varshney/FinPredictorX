import streamlit as st
import pandas as pd

# Modules
from FinPredictorX.about import explainAboutApp
from FinPredictorX.price import price

features = ["Price Prediction", "Trend Prediction", "Volatility Prediction", "Volume Prediction", "Anomaly Detection"]

def finPredictorX(feature: str, df: pd.DataFrame):
    if feature == "Price Prediction":
        price(df)

if __name__ == '__main__':
    st.title("🌟 Welcome to FinPredictorX App")
    st.sidebar.title("FinPredictorX App")
    feature = st.sidebar.selectbox("Select the Prediction Type", features)

    file = st.sidebar.file_uploader("Upload your data", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)

        # Lowercasing the columns
        df.columns = df.columns.str.lower()
        if 'date' in df.columns:
            finPredictorX(feature=feature, df=df)
    else:
        explainAboutApp(feature)
        st.sidebar.warning("Upload a csv file to start the application!", icon="⚠️")
