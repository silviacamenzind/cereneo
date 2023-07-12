# example from Documentation with Haruns Data

import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Interactive scatter plot with data'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filter by PacketCounter:"),
    dcc.RangeSlider(
        id='range-slider',
        min=0, max=15, step=0.1,
        marks={0: '0', 15: '15'},
        value=[5, 10]
    ),
])


@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = pd.read_csv('Data/mydata.csv',nrows=15) # replace with your own data source

    low, high = slider_range
    mask = (df['PacketCounter'] > low) & (df['PacketCounter'] < high)
    fig = px.scatter(
        df[mask], x="PacketCounter", y="Euler_X", 
        color="Euler_X", size='PacketCounter', 
        hover_data=['PacketCounter'],
        )
    return fig


app.run_server(debug=True)