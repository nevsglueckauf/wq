# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD
import base64
import datetime
import io

register_page(__name__, path="/")

layout = html.Div([
    # Header mit Gradient
    html.Div([
        html.H1("🧊🥃 Python Dashboard", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Mach dich frei von PowerBI", 
               style={
                   'color': 'rgba(255,255,255,0.9)', 
                   'fontStyle': 'italic',
                   'fontSize': '1.1rem',
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
        html.Div([
            html.H4("📊 Enthaltene Analysen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '25px',
                       'fontWeight': '600',
                       'borderBottom': '2px solid #f0f0f0',
                       'paddingBottom': '10px'
                   }),
            
            # Analysen als Kacheln
            html.Div([
                html.Div([
                    html.Div("📈", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Werbeerfolge", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("🔄", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Sitzungstypen", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("🌍", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Geodaten", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("🎯", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("KPIs", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("📦", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Produkte", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("💰", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Umsätze", style={'fontWeight': '500'})
                ], className='analysis-card'),
                
                html.Div([
                    html.Div("🔍", style={'fontSize': '2rem', 'marginBottom': '10px'}),
                    html.Div("Sitzungsanalysen", style={'fontWeight': '500'})
                ], className='analysis-card'),
            ], style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(auto-fit, minmax(150px, 1fr))',
                'gap': '15px',
                'marginBottom': '30px'
            }),
            
            # Zusätzliche Features
            html.Div([
                html.H5("🎛️ Weitere Features", 
                       style={
                           'color': '#2E86AB',
                           'marginBottom': '15px'
                       }),
                html.Div([
                    html.Span("🔧 Admin Panel", 
                             style={
                                 'backgroundColor': '#e8f4f8',
                                 'padding': '8px 15px',
                                 'borderRadius': '20px',
                                 'margin': '5px',
                                 'display': 'inline-block',
                                 'fontSize': '0.9rem'
                             }),
                ])
            ], style={
                'textAlign': 'center',
                'padding': '20px',
                'backgroundColor': '#f8f9fa',
                'borderRadius': '8px'
            }),
            
        ])
    ], style={
        'padding': '0 20px'
    }),
    
    html.Div(id='output-data-upload'),
], style={
    'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
    'textAlign': 'center',
    'margin': 'auto',
    'maxWidth': '900px',
    'padding': '0',
    'backgroundColor': 'white',
    'borderRadius': '10px',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
    'minHeight': '100vh'
})

# CSS für die Karten (kann auch in externer CSS-Datei sein)
analysis_card_style = {
    'backgroundColor': '#ffffff',
    'padding': '20px 15px',
    'borderRadius': '8px',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
    'border': '1px solid #e0e0e0',
    'transition': 'all 0.3s ease',
    'cursor': 'pointer'
}

# Hover-Effekt für die Karten (kann mit Callbacks implementiert werden)