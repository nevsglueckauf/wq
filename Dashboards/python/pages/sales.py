from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD

register_page(__name__)

# Daten laden
sub_title = DD.pages['Sales']
df = pd.read_csv('output/sales_per_channel.csv')
df['Tag'] = pd.to_datetime(df['Tag'], format='%Y-%m-%d')

colz = ["Bestellungen","Bruttoumsatz","Rabatte","Rückgaben","Nettoumsatz","Versandgebühren","Steuern","Gesamtumsatz"]
strt_colz = ["Nettoumsatz"]
opt = [{"label": k, "value": k} for k in colz]

# Initialer Graph
fig = px.line(df, x="Tag", y=strt_colz, color='Vertriebskanal')

@callback(
    Output(component_id="sales-sales-controls-and-graph", component_property="figure"),
    Input(component_id="sales-sales-controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="Tag", y=col_chosen, color='Vertriebskanal')
    
    # Modernes Styling für den Graph
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2E86AB'),
        title_font=dict(size=20, color='#2E86AB'),
        hoverlabel=dict(bgcolor='#2E86AB', font_color='white')
    )
    fig.update_xaxes(gridcolor='#f0f0f0')
    fig.update_yaxes(gridcolor='#f0f0f0')
    return fig

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Umsatzanalyse", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Umsätze nach Vertriebskanal", 
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
            html.H4("Umsatzmetriken auswählen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600',
                       'fontSize': '1.3rem'
                   }),
            dcc.Dropdown(
                id="sales-sales-controls-and-check-item",
                options=opt,
                value=strt_colz,
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
        
        # Graph Section - Vergrößert
        html.Div([
            html.H4("Umsatzentwicklung", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(figure=fig, id="sales-sales-controls-and-graph",
                     style={
                         'border': '1px solid #e0e0e0',
                         'borderRadius': '8px',
                         'padding': '15px',
                         'backgroundColor': 'white',
                         'height': '600px'  # Vergrößert
                     })
        ], style={
            'marginBottom': '30px'
        }),
        
        # Data Grid Section
        html.Div([
            html.H4("Umsatzdaten", 
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
                    "paginationPageSize": 15,
                    "animateRows": True
                },
                style={
                    'height': '500px',  # Vergrößert
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