# Sitzungsverfolgung
from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    Output,
    Input,
    State,
    register_page,
)
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from wtf.dd import DD
import base64
import datetime
import io
import dash_daq as daq
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
import plotly.graph_objects as go
import numpy as np

register_page(__name__)


models = {'Lin. Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

layout = html.Div([
    html.H4("Vorhersage Klickrate"),
    html.P("Modellwahl:"),
    dcc.Dropdown(
        id='dropdown',
        options=["Lin. Regression", "Decision Tree", "k-NN"],
        value='k-NN',
        clearable=False
    ),
    dcc.Graph(id="graph"),
])

@callback(
    Output("graph", "figure"),
    Input('dropdown', "value"))
def train_and_display(name):
    #df = px.data.tips() # replace with your own data source
    #df = pd.read_csv('Dta/output/sales_per_channel.csv')
    mn = 'Impressionen' # Bruttoumsatz
    prt = 'Klicks' # Bruttoumsatz
    df = pd.read_csv('Dta/output/sorted_all_ads.csv')
    X = df[mn].values[:, None]
    X_train, X_test, y_train, y_test = train_test_split(
        X, df[prt], random_state=42)

    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train,
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test,
                   name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range,
                   name='prediction')
    ])
    return fig
