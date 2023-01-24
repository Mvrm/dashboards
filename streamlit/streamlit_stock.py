# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 10:59:18 2023

@author: manishv
"""
import streamlit as st
import plotly.express as px

import pandas as pd
import numpy as np

st.write("# Stock Prices dashboard")
st.write("### Apple Stock  Prices dashboard")

st.markdown(
    """
            This is a dashboard showing the *Stock prices* of Apple:  
            Data source: [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data)
            """
)
    
aapl = pd.read_csv("C:/Users/manishv/Desktop/dashboards/streamlit/AAPL.csv")
aapl["Date"] = pd.to_datetime(aapl["Date"], format="%d-%m-%Y")

aapl["year"] = aapl["Date"].dt.year
aapl["month"] = aapl["Date"].dt.month
aapl["week"] = aapl["Date"].dt.week

st.header("Avg. Summary statistics")
# st.header('Line chart by geographies')

aapl_stats = aapl.groupby("year").agg(
    High=("High", np.mean),
    Low=("Low", np.mean),
    Close=("Close", np.mean),
    Volume=("Volume", np.mean),
)

st.dataframe(aapl_stats)

st.header("Stock Price Chart")

selected_year = st.selectbox(
    label="Select a year to generate the chart:", options=aapl["year"].unique()
)
submitted = st.button("Submit")
if submitted:
    filtered_year = aapl[aapl["year"] == selected_year]
    line_fig = px.line(
        filtered_year[["Date", "High"]],
        x="Date",
        y="High",
        # color='type',
        title=f"Apple high price trend in {selected_year}",
    )
    st.plotly_chart(line_fig)

with st.sidebar:
    st.subheader("About")
    st.markdown("This dashboard is made by Manish, using **Streamlit**")

st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=30)
