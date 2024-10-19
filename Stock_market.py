# Stock market analyser

import streamlit as st
import yfinance as yf
import datetime as dt

title = st.text_input('Provide data source','MSFT')
st.write("SOurce", title)
ticker_symbol=title
ticker = yf.Ticker(ticker_symbol)
col1, col2 = st.columns(2)

with col1:
    d = st.date_input("please enter start date", dt.date(2019, 7, 6))

with col2:
    d1 = st.date_input("please enter end date", dt.date(2019, 7, 6))




hist_df = ticker.history(period="1mo",start=d,end=d1)
st.title('Stock Market Prices')
st.write('Here is month wise data for stock')
st.dataframe(hist_df)


import numpy as np


st.subheader('Price movement over time')
st.line_chart(hist_df['Close'])

st.subheader('Volume movement over time')
st.line_chart(hist_df['Volume'])

