from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from wtf.dd import DD
from datetime import date
import plotly.graph_objects as go

register_page(__name__)

# Daten laden
sub_title = "Analyse der Sitzungen"
df = pd.read_csv("Dta/exporte/sessions.csv")
df["datum"] = pd.to_datetime(df["datum"], format="%Y-%m-%d")
df["Sitzung_min"] = round(df["session_duration"] / 60, 2)

# Scatter Plot mit Error Bars
fig_scatt = go.Figure(data=go.Scatter(
    x=df["datum"],
    y=df["sessions"],
    error_y=dict(
        type='data',
        array=df["sess_co_done"],
        visible=True
    )
))

# Modernes Styling für Scatter Plot
fig_scatt.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='#2E86AB'),
    title_font=dict(size=20, color='#2E86AB'),
    hoverlabel=dict(bgcolor='#2E86AB', font_color='white')
)
fig_scatt.update_xaxes(gridcolor='#f0f0f0')
fig_scatt.update_yaxes(gridcolor='#f0f0f0')

# Bar Chart
opt = [{"label": k, "value": k} for k in DD.session_y]
start_val = 'sessions'
fig = px.bar(df, x="datum", y=start_val, color='sug_platform')

# Modernes Styling für Bar Chart
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='#2E86AB'),
    title_font=dict(size=20, color='#2E86AB'),
    hoverlabel=dict(bgcolor='#2E86AB', font_color='white')
)
fig.update_xaxes(gridcolor='#f0f0f0')
fig.update_yaxes(gridcolor='#f0f0f0')

@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.bar(df, x="datum", y=col_chosen)
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2E86AB'),
        hoverlabel=dict(bgcolor='#2E86AB', font_color='white')
    )
    fig.update_xaxes(gridcolor='#f0f0f0')
    fig.update_yaxes(gridcolor='#f0f0f0')
    return fig

layout = html.Div([
    # Hero Section
    html.Div([
        html.H1("Sitzungsanalyse", 
                style={
                    'color': 'white', 
                    'marginBottom': '10px',
                    'fontSize': '2.5rem',
                    'fontWeight': '300'
                }),
        html.P("Detaillierte Analyse der Sitzungsdaten", 
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
        # Scatter Plot Section
        html.Div([
            html.H4("Sitzungen mit Error Bars", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(figure=fig_scatt, id="sess_scatter",
                     style={
                         'border': '1px solid #e0e0e0',
                         'borderRadius': '8px',
                         'padding': '15px',
                         'backgroundColor': 'white',
                         'height': '500px'  # Vergrößert
                     })
        ], style={
            'marginBottom': '30px'
        }),
        
        # Controls Section
        html.Div([
            html.H4("Sitzungsmetriken auswählen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600',
                       'fontSize': '1.3rem'
                   }),
            dcc.Dropdown(
                id="controls-and-check-item",
                options=opt,
                value=start_val,
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
        
        # Date Picker Section
        html.Div([
            html.H4("Zeitraum auswählen", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '15px',
                       'fontWeight': '600',
                       'fontSize': '1.3rem'
                   }),
            dcc.DatePickerRange(
                id="date_picker_range",
                start_date_placeholder_text="Startdatum",
                end_date_placeholder_text="Enddatum",
                calendar_orientation="vertical",
                style={
                    'padding': '10px'
                }
            ),
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '25px'
        }),
        
        # Bar Chart Section
        html.Div([
            html.H4("Sitzungsverteilung nach Plattform", 
                   style={
                       'color': '#2E86AB',
                       'marginBottom': '20px',
                       'fontWeight': '600',
                       'fontSize': '1.5rem'
                   }),
            dcc.Graph(figure=fig, id="controls-and-graph",
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
            html.H4("Sitzungsdaten", 
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
                    {"field": x, "headerName": DD.col_transl[x], "filter": True, "sortable": True}
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