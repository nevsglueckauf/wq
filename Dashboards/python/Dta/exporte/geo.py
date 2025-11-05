from dash import Dash, dcc, html, Input, Output, ctx
import pandas as pd
import plotly.express as px

#filepath = "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv"
df = pd.read_csv("Dta/geo_not_de.csv")
#df.to_csv("volcano.csv", index=False)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
len_df = len(df)
# country,state,county,name,lat,lng
print(f"Länge DF:{len_df}")
fig = px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        #size=range(0, len(df))  ,
        hover_name="name",
        #projection="natural earth",
        #projection="transverse mercator",
        #projection="robinson",#kavrayskiy7
        projection="orthographic",#
        
    )




app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    [
        html.Header(
            "Geographische Verteilung der Sitzungen",
            style={"font-size": "30px", "textAlign": "center"},
        ),
        
        dcc.Graph(id="map", figure=fig),
    ],
    style={"margin": 10, "maxWidth": 800},
)



# @app.callback(
#     Output("meter", "value"),
#     Output("feet", "value"),
#     Output("map", "figure"),
#     Input("meter", "value"),
#     Input("feet", "value"),
# )
# def sync_input(meter, feet):
#     if ctx.triggered_id == "meter":
#         feet = None if meter is None else round((float(meter) * 3.28084), 0)
#     else:
#         meter = None if feet is None else round((float(feet) / 3.28084), 1)

#     fig = px.scatter_geo(
#         data_frame=df.loc[df["Elev"] >= meter],
#         lat="Latitude",
#         lon="Longitude",
#         size="Elev",
#         hover_name="Volcano Name",
#         projection="natural earth",
#     )

#     return meter, feet, fig


if __name__ == "__main__":
    app.run(debug=True, port=8989)