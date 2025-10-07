# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from dd import DD
    
sub_title = "Werbeerfolgsmessung"
df = pd.read_csv('output/ads_all.csv')
df['Datum'] = pd.to_datetime(df['Datum'], format='%Y-%m-%d')

colz = ['Datum', 'Impressionen','Klicks','Kosten','CPC_Manuell','CRT_Manuell', 'Provider']
col_chosen = ['Impressionen']
#opt = [{"label": k, "value": k} for k in colz]
 
fig = px.line(df, x="Datum", y=col_chosen, color='Provider')


register_page(__name__)

 
@callback(
    Output(component_id="ads-controls-and-graph", component_property="figure"),
    Input(component_id="ads-controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="Datum", y=col_chosen, title=sub_title, color='Provider')
 
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        
        html.Div(className='custom-dropdown-style', children=[dcc.Dropdown(
            id="ads-controls-and-check-item",
            options=colz,
            value=col_chosen,
            multi=True,
            className='dropdown-class',
            style={'background-color':'#011213'}
        )]),
        dcc.Graph(figure=fig, id="ads-controls-and-graph"),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": x}
                for x in colz
            ],  
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
