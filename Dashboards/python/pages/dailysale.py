

# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from dd import DD
    
sub_title = 'Umsätze je Tag (Kaggle)'


# "kaggle_san/brand_sale_per_day.csv"
# "kaggle_san/cat_sale_per_day.csv"


#df = pd.read_csv('output/ec_agg.csv')
df = pd.read_csv("kaggle_san/brand_sale_per_day.csv")
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
fig = px.line(df, x='date', y='price', color='brand')

#register_page(__name__)

 
# @callback(
#     Output(component_id="funnel-controls-and-graph", component_property="figure"),
#     Input(component_id="funnel-controls-and-check-item", component_property="value"),
# )
# def update_graph(col_chosen):
#     fig = px.line(df, x="Tag", y=col_chosen, title=sub_title, color='Vertriebskanal')
 
#     return fig


layout = html.Div(
    [
        html.H3(sub_title),
        
         
        dcc.Graph(figure=fig, id="funnel-controls-and-graph"),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            # columnDefs=[
            #     {"field": x, "headerName": x}
            #     for x in colz
            # ],  
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
