from dash import Dash, dcc, html, Input, Output, ctx, register_page, callback
import pandas as pd
import plotly.express as px
from wtf.provider import Provider

register_page(__name__)

# Daten laden
df_o = pd.read_csv("Dta/exporte/sess_loc_all.csv")
df = df_o[["datum", "sess_ctry", "sess_loc", "sessions", "lng", "lat", "kontrollland"]]

str_proj = "natural earth"

# Initialer Graph
fig = px.scatter_geo(
    data_frame=df,
    lat="lat",
    lon="lng",
    size="sessions",
    hover_name="sess_loc",
    projection=str_proj,
)

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Geodaten Analyse", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Geographische Verteilung der Sitzungen", 
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
            html.H4("Kartenprojektion auswählen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600',
                       'fontSize': '1.3rem'
                   }),
            dcc.Dropdown(
                id="geo-dd",
                options=Provider.proj,
                value=str_proj,
                multi=False,
                style={
                    'backgroundColor': 'white',
                    'border': '1px solid #e0e0e0',
                    'borderRadius': '8px',
                    'padding': '5px',
                    'maxWidth': '300px'
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
            html.H4("Geographische Visualisierung", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(id="geo-map", figure=fig,
                     style={
                         'border': '1px solid #e0e0e0',
                         'borderRadius': '8px',
                         'padding': '15px',
                         'backgroundColor': 'white',
                         'height': '700px'  # Viel größer!
                     })
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

@callback(Output("geo-map", "figure"), Input("geo-dd", "value"))
def sync_input(loc):
    return px.scatter_geo(
        data_frame=df,
        lat="lat",
        lon="lng",
        size="sessions",
        hover_name="sess_loc",
        projection=loc,
    )