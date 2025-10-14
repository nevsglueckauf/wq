# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from dd import DD
    
sub_title = DD.pages['Products']
df = pd.read_csv('Whiskyquartier_Rohdaten/products.csv')
df["short"] = df["prod_name"].str[0:14]

colz2 = ["invent_start","invent_end","sold_units","sell_rate"]
colz = ["prod_name","invent_start","invent_end","sold_units","sell_rate"]
strt_colz = ["short"]
lbl = {x: DD.prd_trans for x in colz} 
#opt = [{"label": k, "value": k} for k in colz]
fig = px.line(df, x="short", y=colz2, labels=lbl)


register_page(__name__)

layout = html.Div(
    [
        html.H3(sub_title),
        dcc.Graph(figure=fig, id="prd-controls-and-graph"),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": DD.prd_trans[x]}
                for x in colz
            ],  
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
