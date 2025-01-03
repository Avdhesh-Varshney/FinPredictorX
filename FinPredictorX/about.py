import streamlit as st

def explainAboutApp(feature):
    st.subheader("Your One-Stop Solution for Financial Market Predictions")

    st.markdown(
        """
        **FinPredictorX** is a powerful application designed to help traders, investors, and researchers make informed decisions in the financial markets. It leverages advanced machine learning techniques to provide insights into key financial metrics. Here's what it can do:
        """
    )

    if feature == 'Price Prediction':
        st.header("📈 Price Prediction")
        st.markdown(
            """
            Predict future prices of financial assets like cryptocurrencies using historical data.

            **Key Features:**
            - **Predict Columns:** `Close`, `Adj Close`, or `High/Low`.
            - **Use Case:** Forecast tomorrow's price or the next hour's price for trading strategies, portfolio management, or market analysis.
            - **Models Used:** LSTM (time series), ARIMA, XGBoost, AutoTS.

            **Benefits:**
            - Helps develop trading strategies based on price movements.
            - Aids in portfolio management and long-term forecasting.
            """
        )

    elif feature == 'Trend Prediction':
        st.header("📊 Trend Prediction")
        st.markdown(
            """
            Predict whether the price will go up or down based on historical trends.

            **Key Features:**
            - **Predict Column:** `Direction` or `Binary Trend`.
            - **Derived Column:** Create labels such as 1 for "Price Up" and 0 for "Price Down."
            - **Use Case:** Make momentum-based trading or buy/sell decisions.
            - **Models Used:** Logistic Regression, Random Forest, SVM.

            **Benefits:**
            - Assists traders in identifying upward or downward trends.
            - Enables smarter and quicker decision-making.
            """
        )

    elif feature == 'Volatility Prediction':
        st.header("📉 Volatility Prediction")
        st.markdown(
            """
            Predict periods of high or low price fluctuations to manage risk effectively.

            **Key Features:**
            - **Predict Column:** `High - Low` (Range) or `Standard Deviation of Returns`.
            - **Derived Column:** Measure volatility using price ranges.
            - **Use Case:** Forecast periods of high volatility to avoid or exploit them.
            - **Models Used:** Regression models or time series models.

            **Benefits:**
            - Enhances risk management by identifying volatile periods.
            - Assists in capitalizing on volatile market opportunities.
            """
        )

    elif feature == 'Volume Prediction':
        st.header("📊 Volume Prediction")
        st.markdown(
            """
            Predict the trading activity and liquidity of financial markets.

            **Key Features:**
            - **Predict Column:** `Volume`.
            - **Use Case:** Anticipate large market movements or inactivity periods.
            - **Models Used:** Regression models.

            **Benefits:**
            - Helps traders and investors gauge market activity levels.
            - Useful for planning large trades or portfolio rebalancing.
            """
        )

    else:
        st.header("🚨 Anomaly Detection")
        st.markdown(
            """
            Detect unusual events in the market, such as price spikes, crashes, or abnormal trading volumes.

            **Key Features:**
            - **Predict Column:** `Outlier` (derived from `Volume`, `High`, `Low`, etc.).
            - **Derived Column:** Label anomalies based on significant deviations from expected patterns.
            - **Use Case:** Identify potential fraud, manipulation, or significant market events.
            - **Models Used:** Classification models.

            **Benefits:**
            - Alerts users to unusual activity or events.
            - Enables faster responses to critical market changes.
            """
        )

    st.markdown(
        """
        ---
        🌟 **Start exploring FinPredictorX today and take your financial market analysis to the next level!**
        """
    )
