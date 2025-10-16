from dash import Dash, dcc, html, Input, Output, ctx, register_page, callback
import pandas as pd
import plotly.express as px
from wtf.provider import Provider


# filepath = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"
#
# df = pd.read_csv("exporte/sess_loc_DE.csv")
df_o = pd.read_csv("exporte/sess_loc_all.csv")
df = df_o[["datum", "sess_ctry", "sess_loc", "sessions", "lng", "lat", "kontrollland"]]

# df = pd.read_csv("exporte/sess_loc_non_DE.csv")
# df.to_csv("volcano.csv", index=False)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

str_proj = "natural earth"
register_page(__name__)

fig = px.scatter_geo(
    data_frame=df,
    lat="lat",
    lon="lng",
    size="sessions",
    hover_name="sess_loc",
    projection=str_proj,
)


layout = html.Div(
    [
        html.H3(
            "Geographische Verteilung der Sitzungen",
        ),
        html.Div(
            className="custom-dropdown-style",
            children=[
                dcc.Dropdown(
                    id="geo-dd",
                    options=Provider.proj,
                    value=str_proj,
                    multi=False,
                    className="dropdown-class",
                    style={"background-color": "#011213"},
                )
            ],
        ),
        dcc.Graph(id="geo-map", figure=fig),
    ],
    style={"margin": 10, "maxWidth": "500px"},
)


@callback(Output("geo-map", "figure"), Input("geo-dd", "value"))
def sync_input(loc):
    print(loc)
    return px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        size="sessions",
        hover_name="sess_loc",
        projection=loc,
        # scope="europe"
    )
