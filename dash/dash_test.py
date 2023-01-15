# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:58:27 2023

@author: manishv
"""

# Initialize the dash application.
import dash

# To add graphs,other visual components.
from dash import dcc

# include html tags.
from dash import html
import pandas as pd

data = pd.read_csv("C:/Users/manishv/Desktop/dashboard/indexData.csv")

data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

# Initialising dash application.
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children="Stock Exchange Analytics",
        ),
        html.P(
            children="Analyzing day wise high and low prices of indexes.",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["High"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise highest prices of indexes"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Low"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise lowest prices of indexes"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Close"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise closing prices of indexes"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Open"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise opening prices of indexes"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
