# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, State, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD
import base64
import datetime
import io
from wtf.namer import Namer

s = Namer.now()
fn = Namer.fn_now()


register_page(__name__, path="/")
sub_title = "Willkommen!"


layout = html.Div(
    [
        html.H3(sub_title),
        html.P(s),
        html.Pre(fn),
        html.P("Lorem Ispum"),
    ]
)

