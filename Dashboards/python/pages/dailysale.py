

# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from wtf.dd import DD
    
sub_title = 'Umsätze je Tag (Kaggle)'

df = pd.read_csv("Dta/kaggle_san/brand_sale_per_day.csv")
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
fig = px.line(df, x='date', y='price', color='brand')

#register_page(__name__)

layout = html.Div(
    [
        html.H3(sub_title),
        
         
        dcc.Graph(figure=fig, id="funnel-controls-and-graph"),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
