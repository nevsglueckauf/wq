from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
import plotly.graph_objects as go
from wtf.dd import DD

register_page(__name__)

sub_title = "📈 Werbeerfolgsmessung"
df = pd.read_csv('Dta/output/sorted_all_ads.csv')
df['Datum'] = pd.to_datetime(df['Datum'], format='%Y-%m-%d')

colz = ['Datum', 'Impressionen', 'Klicks', 'Kosten', 'CPC', 'CTR', 'Provider']
flt_colz = ['Impressionen', 'Klicks', 'Kosten', 'CPC', 'CTR']
col_chosen = ['Impressionen']

sales = pd.read_csv("Dta/exporte/total_sales_month.csv")
df['Datum'] = pd.to_datetime(sales['Datum'], format='%Y-%m-%d')

# Initialer Graph
bar = px.bar(df, x="Datum", y=col_chosen, color='Provider')

@callback(
    Output(component_id="var-ads-controls-and-graph", component_property="figure"),
    Input(component_id="ads-controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    bar = px.bar(df, x="Datum", y=col_chosen, color='Provider')
    
    # Modernes Styling für den Graph
    bar.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2E86AB'),
        title_font=dict(size=20, color='#2E86AB'),
        hoverlabel=dict(bgcolor='#2E86AB', font_color='white')
    )
    bar.update_xaxes(gridcolor='#f0f0f0')
    bar.update_yaxes(gridcolor='#f0f0f0')
    return bar

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Werbeerfolgsmessung", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Analyse und Tracking von Werbekampagnen", 
               style={
                   'color': 'rgba(255,255,255,0.9)', 
                   'fontSize': '1.2rem',
                   'marginBottom': '0'
               }),
    ], style={
        'background': 'linear-gradient(135deg, #2E86AB 0%, #1A535C 100%)',
        'padding': '40px 20px',
        'borderRadius': '10px 10px 0 0',
        'marginBottom': '30px'
    }),
    
    # Hauptinhalt
    html.Div([
        # Dropdown Controls
        html.Div([
            html.H4("Metriken auswählen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600',
                       'fontSize': '1.3rem'
                   }),
            dcc.Dropdown(
                id="ads-controls-and-check-item",
                options=[{"label": k, "value": k} for k in flt_colz],
                value=col_chosen,
                multi=True,
                style={
                    'backgroundColor': 'white',
                    'border': '1px solid #e0e0e0',
                    'borderRadius': '8px',
                    'padding': '5px'
                }
            ),
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '25px'
        }),
        
        # Graph Section
        html.Div([
            html.H4("Visualisierung", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(figure=bar, id="var-ads-controls-and-graph",
                     style={
                         'border': '1px solid #e0e0e0',
                         'borderRadius': '8px',
                         'padding': '15px',
                         'backgroundColor': 'white',
                         'height': '600px'
                     })
        ], style={
            'marginBottom': '30px'
        }),
        
        # Data Grid Section
        html.Div([
            html.H4("Rohdaten", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dag.AgGrid(
                id="main_grid_basic",
                rowData=df.to_dict("records"),
                columnDefs=[
                    {"field": x, "headerName": x, "filter": True, "sortable": True}
                    for x in colz
                ],  
                columnSize="responsiveSizeToFit",
                dashGridOptions={
                    "pagination": True,
                    "paginationPageSize": 10,
                    "animateRows": True
                },
                style={
                    'height': '500px',
                    'width': '100%',
                    'border': '1px solid #e0e0e0',
                    'borderRadius': '8px'
                }
            ),
        ]),
        
    ], style={
        'padding': '0 30px 30px 30px'
    }),
    
], style={
    'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
    'textAlign': 'left',
    'margin': 'auto',
    'maxWidth': '1400px',
    'padding': '0',
    'backgroundColor': 'white',
    'borderRadius': '10px',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
    'minHeight': '100vh'
})