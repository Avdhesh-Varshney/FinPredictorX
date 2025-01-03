import matplotlib.pyplot as plt
from autots import AutoTS
import streamlit as st
import pandas as pd
import time

def modelAutoTS(df: pd.DataFrame, forecast_days: int, target_col: str, credentials: list):
    with st.spinner("Building the model... Please wait!"):
        start_time = time.time()

        model = AutoTS(
            forecast_length=forecast_days,
            frequency='infer',
            ensemble='simple',
            model_list="fast",
            max_generations=credentials[0],
            num_validations=credentials[1],
            verbose=0
        )

        model = model.fit(df, date_col="date", value_col=target_col, id_col=None)

        end_time = time.time()
        training_time = end_time - start_time

        st.markdown("---")
        st.success(f"Model training completed in {training_time:.2f} seconds.", icon="✅")

    # Prediction
    st.toast("Working on Prediction!", icon="🎉")
    prediction = model.predict()

    # Forecasting for the required no. of days
    st.markdown(f"---\n#### Forecast for {target_col}:")
    st.write(prediction.forecast)

    with st.expander("Show Upper and Lower Forecast", expanded=False):
        st.markdown("##### Upper Forecast:")
        st.write(prediction.upper_forecast)
        st.markdown("---\n##### Lower Forecast:")
        st.write(prediction.lower_forecast)

    # Graphical visualization of the prediction
    with st.expander("Show Prediction Graph", expanded=False):
        fig, ax = plt.subplots()
        prediction.plot(model.df_wide_numeric, series=model.df_wide_numeric.columns[0], start_date=df['date'].iloc[0], ax=ax)
        st.pyplot(fig)

    return model
