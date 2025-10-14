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
from dd import DD
import base64
import datetime
import io
import dash_daq as daq
from wtf.container import Container

s = str(datetime.datetime.now())
now =  s[:16]
sub_title = "DEV Lab"
register_page(__name__)
sessions = {"Absprünge": 1592, "Warenkorb": 114, "CO err.": 91, "CO= abgeschl.": 39}
df = pd.read_csv("exporte/kpi.csv")
pie = px.pie(names=sessions.keys(), values=sessions.values(), hole=0.3)

colz = []
for x in range(9):
    
    ele = pie_col = dbc.Col(
        [
            html.H3(str(x)+'_Foo')
        ]
    )
    colz.append(ele)

tab = Container()

tab.apd_row([colz[7], colz[5]])
tab.apd_row([colz[6], colz[8], colz[4]])
tab.apd_row([colz[0], colz[1]])
tab.apd_row([colz[2], colz[3]])
#dbc.Row()

container = Container()
container.apd(html.H3(sub_title))
container.apd(dcc.Graph(figure=pie, id="pie-kpi"))
container.apd(tab.rndr())


#print(tab.rndr())

layout = html.Div(
    container.rndr()    
)
