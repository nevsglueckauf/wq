from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from wtf.dd import DD

register_page(__name__)

sub_title = "🔄 Sitzungstypen Analyse"

# Daten laden
df = pd.read_csv("Dta/exporte/_funnel.csv")
df["Datum"] = pd.to_datetime(df["Datum"], format="%Y-%m-%d")

# Original Graph
fig = px.funnel(df, x="Datum", y="Anzahl", color="Typ")

colz = ['Datum', 'Land', 'Ort', 'Empfehlungsplattform', 'Anzahl', 'Typ']

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Sitzungstypen Analyse", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Funnel-Darstellung der Sitzungsverläufe", 
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
        # Graph Section
        html.Div([
            html.H4("Funnel Visualisierung", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(figure=fig, id="funnel-controls-and-graph",
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
        # Daterange Slider
        dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=df['Datum'].min(),
        max_date_allowed=df['Datum'].max(),
        ),
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
                    "paginationPageSize": 15,
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