from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD
import base64
import datetime
import io

register_page(__name__, path="/")

# Mapping der Karten zu Seiten
page_mapping = {
    "Werbeerfolge": "/ads",
    "Sitzungstypen": "/funnel",
    "Geodaten": "/geo",
    "KPIs": "/kpi",
    "Produkte": "/products",
    "Umsätze": "/sales",
    "Sitzungsanalysen": "/sessions",
    "Admin Panel": "/upload"
}

# Größere CSS für die Karten
analysis_card_style = {
    'backgroundColor': '#ffffff',
    'padding': '30px 20px',  
    'borderRadius': '12px',   
    'boxShadow': '0 4px 8px rgba(0,0,0,0.15)',  
    'border': '1px solid #e0e0e0',
    'transition': 'all 0.3s ease',
    'cursor': 'pointer',
    'minHeight': '140px',     
    'display': 'flex',
    'flexDirection': 'column',
    'justifyContent': 'center',
    'alignItems': 'center'
}

layout = html.Div([
    # Header mit Gradient
    html.Div([
        html.H1("🧊🥃 Data on the Rocks", 
                style={
                    'color': 'white', 
                    'marginBottom': '15px',
                    'fontSize': '3rem',      
                    'fontWeight': '300'
                }),
        html.P("Mach dich frei von PowerBI", 
               style={
                   'color': 'rgba(255,255,255,0.9)', 
                   'fontStyle': 'italic',
                   'fontSize': '1.3rem',    
                   'marginBottom': '0'
               }),
    ], style={
        'background': 'linear-gradient(135deg, #2E86AB 0%, #1A535C 100%)',
        'padding': '60px 20px',             
        'borderRadius': '15px 15px 0 0',     
        'marginBottom': '40px'
    }),
    
    # Hauptinhalt
    html.Div([
        html.Div([
            html.H4("📊 Enthaltene Analysen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '35px', 
                       'fontWeight': '600',
                       'fontSize': '1.8rem',     
                       'borderBottom': '3px solid #f0f0f0',
                       'paddingBottom': '15px'
                   }),
            
            # Analysen als Kacheln
            html.Div([
                # Werbeerfolge
                dcc.Link(
                    html.Div([
                        html.Div("📈", style={'fontSize': '3rem', 'marginBottom': '15px'}),  
                        html.Div("Werbeerfolge", style={'fontWeight': '600', 'fontSize': '1.1rem'})  
                    ], style=analysis_card_style),
                    href=page_mapping["Werbeerfolge"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
                
                # Sitzungstypen
                dcc.Link(
                    html.Div([
                        html.Div("🔄", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("Sitzungstypen", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["Sitzungstypen"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
             
                # Geodaten
                dcc.Link(
                    html.Div([
                        html.Div("🌍", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("Geodaten", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["Geodaten"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
                
                # KPIs
                dcc.Link(
                    html.Div([
                        html.Div("🎯", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("KPIs", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["KPIs"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
                
                # Produkte
                dcc.Link(
                    html.Div([
                        html.Div("📦", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("Produkte", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["Produkte"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
                
                # Umsätze
                dcc.Link(
                    html.Div([
                        html.Div("💰", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("Umsätze", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["Umsätze"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
                
                # Sitzungsanalysen
                dcc.Link(
                    html.Div([
                        html.Div("🔍", style={'fontSize': '3rem', 'marginBottom': '15px'}),
                        html.Div("Sitzungsanalysen", style={'fontWeight': '600', 'fontSize': '1.1rem'})
                    ], style=analysis_card_style),
                    href=page_mapping["Sitzungsanalysen"],
                    style={'textDecoration': 'none', 'color': 'inherit'}
                ),
            ], style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(auto-fit, minmax(200px, 1fr))',
                'gap': '25px', 
                'marginBottom': '40px'
            }),
            
            # Zusätzliche Features
            html.Div([
                html.H5("🎛️ Weitere Features", 
                       style={
                           'color': '#2E86AB',
                           'marginBottom': '20px',
                           'fontSize': '1.4rem' 
                       }),
                html.Div([
                    dcc.Link(
                        html.Span("🔧 Admin Panel", 
                                 style={
                                     'backgroundColor': '#e8f4f8',
                                     'padding': '12px 20px',  
                                     'borderRadius': '25px', 
                                     'margin': '8px',
                                     'display': 'inline-block',
                                     'fontSize': '1.1rem',
                                     'transition': 'all 0.3s ease',
                                     'cursor': 'pointer',
                                     'fontWeight': '500'
                                 }),
                        href=page_mapping["Admin Panel"],
                        style={'textDecoration': 'none', 'color': 'inherit'}
                    ),
                ])
            ], style={
                'textAlign': 'center',
                'padding': '30px', 
                'backgroundColor': '#f8f9fa',
                'borderRadius': '12px',
                'border': '2px solid #e8f4f8'
            }),
            
        ])
    ], style={
        'padding': '0 30px 40px 30px' 
    }),
    
    html.Div(id='output-data-upload'),
], style={
    'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
    'textAlign': 'center',
    'margin': 'auto',
    'maxWidth': '1200px', 
    'padding': '0',
    'backgroundColor': 'white',
    'borderRadius': '15px',
    'boxShadow': '0 8px 25px rgba(0, 0, 0, 0.15)',  
    'minHeight': '100vh'
})