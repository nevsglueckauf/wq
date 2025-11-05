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
from dd import DD
import base64
import datetime
import io
import dash_daq as daq

register_page(__name__)

s = str(datetime.datetime.now())
fn = "uploads/" + s[:16].replace(" ", "_").replace(":", "").replace("-", "") + ".csv"

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Admin Panel", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Dateiverwaltung und Systemsteuerung", 
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
        # System Info
        html.Div([
            html.H4("Systeminformation", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600'
                   }),
            html.P(f"Aktueller Zeitpunkt: {s}", 
                   style={
                       'color': '#666',
                       'marginBottom': '10px'
                   }),
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '25px'
        }),
        
        # File Upload Section
        html.Div([
            html.H4("Datei-Upload", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600'
                   }),
            dcc.Upload(
                id="upload-data",
                children=html.Div([
                    "📁 Per Drag & Drop oder ",
                    html.A("Dateiauswahl", style={'color': '#2E86AB', 'fontWeight': 'bold'})
                ]),
                style={
                    "width": "100%",
                    "height": "120px",  # Größer gemacht
                    "lineHeight": "120px",
                    "borderWidth": "2px",
                    "borderStyle": "dashed",
                    "borderRadius": "8px",
                    "textAlign": "center",
                    "margin": "10px 0",
                    "backgroundColor": "#f8f9fa",
                    "borderColor": "#2E86AB",
                    "color": "#2E86AB",
                    "fontSize": "1.1rem"
                },
                multiple=True,
            ),
        ], style={
            'marginBottom': '25px'
        }),
        
        # Power Button Control
        html.Div([
            html.H4("Systemsteuerung", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600'
                   }),
            html.Div([
                daq.PowerButton(
                    id="our-power-button-1", 
                    on=False,
                    color="#2E86AB",
                    size=100
                ),
                html.Div(id="power-button-result-1",
                        style={
                            'marginTop': '15px',
                            'fontWeight': '500',
                            'color': '#2E86AB'
                        }),
            ], style={
                'textAlign': 'center',
                'padding': '20px'
            })
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '25px'
        }),
        
        # Upload Results
        html.Div(id="output-data-upload"),
        
    ], style={
        'padding': '0 30px 30px 30px'
    }),
    
], style={
    'fontFamily': '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
    'textAlign': 'left',
    'margin': 'auto',
    'maxWidth': '1000px',
    'padding': '0',
    'backgroundColor': 'white',
    'borderRadius': '10px',
    'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)',
    'minHeight': '100vh'
})

@callback(
    Output("power-button-result-1", "children"), 
    Input("our-power-button-1", "on")
)
def update_output(on):
    status = "EINGESCHALTET" if on else "AUSGESCHALTET"
    color = "#28a745" if on else "#dc3545"
    return html.Span(f"Systemstatus: {status}", 
                    style={'color': color, 'fontWeight': 'bold'})

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(",")
    decoded = base64.b64decode(content_string)
    
    try:
        if "csv" in filename:
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
            df.to_csv(fn, index=False)
        elif "xls" in filename:
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            html.H5("❌ Fehler beim Verarbeiten der Datei", 
                   style={'color': '#dc3545'})
        ])

    return html.Div([
        html.H5(f"✅ {filename}", 
               style={'color': '#28a745', 'marginBottom': '10px'}),
        html.H6(f"Hochgeladen: {datetime.datetime.fromtimestamp(date)}",
               style={'color': '#666', 'marginBottom': '20px'}),
        
        html.Div([
            html.H6("Vorschau der Daten:",
                   style={'color': '#2E86AB', 'marginBottom': '15px'}),
            dag.AgGrid(
                id="main_grid_basic",
                rowData=df.head(10).to_dict("records"),  # Nur erste 10 Zeilen anzeigen
                columnDefs=[{"field": x, "headerName": x, "filter": True, "sortable": True} 
                           for x in df.columns],
                columnSize="responsiveSizeToFit",
                dashGridOptions={
                    "pagination": True,
                    "paginationPageSize": 10
                },
                style={
                    'height': '400px',
                    'width': '100%',
                    'border': '1px solid #e0e0e0',
                    'borderRadius': '8px'
                }
            ),
        ], style={
            'marginBottom': '20px'
        }),
        
        html.Hr(style={'margin': '20px 0'}),
    ], style={
        'backgroundColor': '#f8f9fa',
        'padding': '20px',
        'borderRadius': '8px',
        'marginBottom': '20px'
    })

@callback(
    Output("output-data-upload", "children"),
    Input("upload-data", "contents"),
    State("upload-data", "filename"),
    State("upload-data", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children