# Sitzungsverfolgung
from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    Output,
    Input,
    State,
    register_page,
)
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from wtf.dd import DD
import base64
import datetime
import io
import dash_daq as daq

s = str(datetime.datetime.now())

sessions = {"Absprünge": 1592, "Warenkorb": 114, "CO err.": 91, "CO= abgeschl.": 39}
header = "Im Zeitraum 2024-10-01 bis 2025-08-01"

df = pd.read_csv("Dta/exporte/kpi.csv")
pie = px.pie(names=sessions.keys(), values=sessions.values(), hole=0.3)

register_page(__name__)
sub_title = "Key Performance Indicators"

card = dbc.Col(
    [
        #dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.Card(
            [
                html.H4("Conversion Rate", className="card-title"),
                daq.LEDDisplay(label="CR", value="0.098", color="#385682"),
                html.H4("Click-throuh-Rate", className="card-title"),
                daq.LEDDisplay(label="CTR", value="0.019018", color="#385682"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

pie_col = dbc.Col(
    [
        html.Div([
            dcc.Graph(figure=pie, id="pie-kpi"),
        ])
    ]
)



layout = html.Div(
    [   
     
        html.H3(sub_title),
        html.H3(header),
        card,
        pie_col,
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": x, "headerName": x} for x in df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
    ]
)
from dash import (
    Dash,
    html,
    dash_table,
    dcc,
    callback,
    Output,
    Input,
    State,
    register_page,
)
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from wtf.dd import DD
import base64
import datetime
import io
import dash_daq as daq

register_page(__name__)

# Daten laden
sessions = {"Absprünge": 1592, "Warenkorb": 114, "CO err.": 91, "CO abgeschl.": 39}
header = "Im Zeitraum 2024-10-01 bis 2025-08-01"
df = pd.read_csv("Dta/exporte/kpi.csv")
pie = px.pie(names=sessions.keys(), values=sessions.values(), hole=0.3)

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Key Performance Indicators", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Übersicht der wichtigsten Leistungskennzahlen", 
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
        # Zeitraum Info
        html.Div([
            html.H4(header, 
                   style={
                       'color': '#2E86AB',
                       'textAlign': 'center',
                       'marginBottom': '30px',
                       'fontWeight': '500'
                   }),
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '15px',
            'borderRadius': '8px',
            'marginBottom': '30px'
        }),
        
        # KPIs und Pie Chart Row
        dbc.Row([
            # KPIs Cards
            dbc.Col([
                html.Div([
                    html.H4("Conversion Rate", 
                           style={
                               'color': '#2E86AB',
                               'marginBottom': '15px',
                               'fontWeight': '600'
                           }),
                    daq.LEDDisplay(
                        label="CR", 
                        value="0.098", 
                        color="#2E86AB",
                        size=40,
                        style={'marginBottom': '20px'}
                    ),
                    html.H4("Click-through-Rate", 
                           style={
                               'color': '#2E86AB',
                               'marginBottom': '15px',
                               'fontWeight': '600'
                           }),
                    daq.LEDDisplay(
                        label="CTR", 
                        value="0.019018", 
                        color="#2E86AB",
                        size=40
                    ),
                ], style={
                    'backgroundColor': 'white',
                    'padding': '30px',
                    'borderRadius': '8px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                    'textAlign': 'center',
                    'height': '100%'
                })
            ], width=12, lg=4, className="mb-4"),
            
            # Pie Chart
            dbc.Col([
                html.Div([
                    html.H4("Sitzungsverteilung", 
                           style={
                               'color': '#2E86AB',
                               'marginBottom': '20px',
                               'fontWeight': '600',
                               'textAlign': 'center'
                           }),
                    dcc.Graph(figure=pie, id="pie-kpi",
                             style={
                                 'height': '400px'  # Größerer Pie Chart
                             })
                ], style={
                    'backgroundColor': 'white',
                    'padding': '30px',
                    'borderRadius': '8px',
                    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                    'height': '100%'
                })
            ], width=12, lg=8, className="mb-4"),
        ], className="mb-4"),
        
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
                    for x in df.columns
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