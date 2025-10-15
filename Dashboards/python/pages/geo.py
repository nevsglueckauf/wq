from dash import Dash, dcc, html, Input, Output, ctx, register_page, callback
import pandas as pd
import plotly.express as px

#filepath = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"
# 
#df = pd.read_csv("exporte/sess_loc_DE.csv")
df_o = pd.read_csv("exporte/sess_loc_all.csv")
df = df_o[['datum', 'sess_ctry', 'sess_loc', 'sessions', 'lng', 'lat', 'kontrollland'] ]

#df = pd.read_csv("exporte/sess_loc_non_DE.csv")
#df.to_csv("volcano.csv", index=False)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#len_df = len(df)

register_page(__name__)
# country,state,county,name,lat,lng
#print(f"Länge DF:{len_df}")
fig = px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        size="sessions",
        hover_name="sess_loc",
        projection="eckert4",
        #projection="natural earth",
        #projection="transverse mercator",
        #projection="robinson",#kavrayskiy7
        #projection="orthographic",#
        #projection="equirectangular",
        #scope="europe"        
    )





layout = html.Div(
    [
        html.H3(
            "Geographische Verteilung der Sitzungen",
        ),
        html.Div(className='custom-dropdown-style', children=[dcc.Dropdown(
            id="geo-controls",
            options=["Deutschland", "International"],
            value=["Deutschland"],
            multi=False,
            className='dropdown-class',
            style={'background-color':'#011213'}
        )]),
        dcc.Graph(id="map", figure=fig),
    ],
    style={"margin": 10, "maxWidth": 800},
)



@callback(
    Output("map", "figure"),
    Input("custom-dropdown-style", "value"),
    
)
def sync_input(loc):
    if loc == "Deutschland":
        fig = px.scatter_geo(
            data_frame=df_de,
            lat="lat",
            lon="lng",
            #size=range(0, len(df))  ,
            hover_name="name",
            #projection="natural earth",
            #projection="transverse mercator",
            #projection="robinson",#kavrayskiy7
            #projection="orthographic",#
            #projection="equirectangular",
            scope="europe"        
        )
    else:fig = px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        #size=range(0, len(df))  ,
        hover_name="name",
        projection="natural earth",
        #projection="transverse mercator",
        #projection="robinson",#kavrayskiy7
        #projection="orthographic",#
        #projection="equirectangular",
        #scope="europe"        
    )

    return fig

