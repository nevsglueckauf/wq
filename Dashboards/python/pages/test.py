# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag


from wtf.factory import TabFactory
from wtf.generic_elements import ElementBuilder
from dd import DD

sub_title = "Laborseite:: Umsätze je Tag pro Marke"
start_brands = ["apple", "electrolux", "beko", "a-mega"]
brand = TabFactory.df(f"../../Data/Norm/brandz.csv")
bl = list(brand["brand_name"])
dd = ElementBuilder.dd(
    df=bl,
    strt_colz=start_brands,
    id="brnd-dd"
)
file = "brnd_per_day_sales_all.csv"
df = pd.read_csv(f"../../Data/Agg/{file}")
df_g = df[df["brand"].isin(start_brands)]
fig = px.line(data_frame=df_g, x="date", y="price", color="brand")


# print(bl)
register_page(__name__)


# @callback(
#     Output(component_id="sales-sales-controls-and-graph", component_property="figure"),
#     Input(component_id="sales-sales-controls-and-check-item", component_property="value"),
# )
# def update_graph(col_chosen):
#     fig = px.line(df, x="Tag", y=col_chosen, title=sub_title, color='Vertriebskanal')

#     return fig

layout = html.Div(
    [
        html.H1(sub_title),
        dd,
        dcc.Graph(figure=fig, id="brnd-controls-and-graph"),
    ]
)

 
@callback(
    Output(component_id="brnd-controls-and-graph", component_property="figure"),
    Input(component_id="brnd-dd", component_property="value"),
)
def update_data(brands):
    df_g = df[df["brand"].isin(brands)]
    return  px.line(data_frame=df_g, x="date", y="price", color="brand")