# to show Dashboard input, plot, dropdown menue 
# thanks chatgpt

import dash
from dash import html
from dash import dcc
from dash import Input
from dash import Output
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

app.layout = html.Div([
    html.H1("My Dashboard"),
    dcc.Dropdown(options=[{'label': 'NYC', 'value': 'NYC'},
                          {'label': 'MTL', 'value': 'MTL'},
                          {'label': 'SF', 'value': 'SF'}],
                 id='demo-dropdown',
                 placeholder="Select a city"),
    html.Div(id='dd-output-container'),
    dcc.DatePickerRange(
        start_date_placeholder_text="Start Period",
        end_date_placeholder_text="End Period",
        calendar_orientation='vertical',
    ),
    html.Br(),
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),
    dcc.Graph(figure=fig),
    
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
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


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

if __name__ == '__main__':
    app.run_server(host='localhost', port=8050, debug=True)
