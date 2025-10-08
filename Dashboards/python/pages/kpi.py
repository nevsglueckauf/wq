# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD
import base64
import datetime
import io

s = str(datetime.datetime.now())
#fn = 'uploads/' + s[:16].replace(' ', '_').replace(':', '').replace('-', '') + '.csv'

register_page(__name__)
sub_title = "Key Performance Indicators"


layout = html.Div(
    [
        html.H3(sub_title),
        
        html.Div(id='placeholder-id-3765987236'),
    ]
)

