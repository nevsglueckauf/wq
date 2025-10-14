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
from dd import DD
import base64
import datetime
import io
import dash_daq as daq

s = str(datetime.datetime.now())
# fn = 'uploads/' + s[:16].replace(' ', '_').replace(':', '').replace('-', '') + '.csv'

# df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d")
# df["cr"] = round(df["sess_co_done"] / df["sessions"], 3)
# part = df[["jump_offs", "sess_cart_add", "sess_co", "sess_co_done", "sessions"]].sum()

sessions = {"Absprünge": 1592, "Warenkorb": 114, "CO err.": 91, "CO= abgeschl.": 39}
header = "Im Zeitraum 2024-10-01 bis 2025-08-01"

# fig = px.line(df, x="datum", y="cr")

#df["nm"] = DD.col_transl(df["Kennzahl"])
df = pd.read_csv("exporte/kpi.csv")
pie = px.pie(names=sessions.keys(), values=sessions.values(), hole=0.3)

register_page(__name__)
sub_title = "Key Performance Indicators"

# cr = dbc.Col(
#     [
#         #dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
#         html.Div(
#             [
#                 html.H4("Conversion Rate", className="card-title"),
#                 daq.LEDDisplay(label="CR", value="0.001578", color="#010101"),
             
#             ]
#         ),
#     ],
#     style={"width": "18rem"},
# )

card = dbc.Col(
    [
        #dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.Card(
            [
                html.H4("Conversion Rate", className="card-title"),
                daq.LEDDisplay(label="CR", value="0.098", color="#385682"),
                html.H4("Click-throuh-Rate", className="card-title"),
                daq.LEDDisplay(label="CTR", value="0.019018", color="#385682"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

pie_col = dbc.Col(
    [
        html.Div([
            dcc.Graph(figure=pie, id="pie-kpi"),
        ])
    ]
)



layout = html.Div(
    [   
     
        html.H3(sub_title),
        html.H3(header),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": x, "headerName": x} for x in df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
    ]
)
