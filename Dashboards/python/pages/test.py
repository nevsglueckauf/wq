# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag

from dd import DD

sub_title = "Laborseite"


register_page(__name__)


# @callback(
#     Output(component_id="sales-sales-controls-and-graph", component_property="figure"),
#     Input(component_id="sales-sales-controls-and-check-item", component_property="value"),
# )
# def update_graph(col_chosen):
#     fig = px.line(df, x="Tag", y=col_chosen, title=sub_title, color='Vertriebskanal')

#     return fig

layout = html.Div([
     html.H1(sub_title),
        dcc.Checklist(
            ["New York City", "Montréal", "San Francisco"],
            ["New York City", "Montréal"],
            inline=True,
        ),
    dcc.Tabs(id='tabs-example-1', value='tab-1', children=[
        dcc.Tab(label='Sitzungen', value='tab-1'),
        dcc.Tab(label='Umsätze', value='tab-2'),
        dcc.Tab(label='Admin Panel', value='tab-3'),
    ]),
    html.Div(id='tabs-example-content-1')
])

@callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs-example-1', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                figure=dict(
                    data=[dict(
                        x=[1, 2, 3],
                        y=[3, 1, 2],
                        type='bar'
                    )]
                )
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                figure=dict(
                    data=[dict(
                        x=[1, 2, 3],
                        y=[5, 10, 6],
                        type='bar'
                    )],
                    template="plotly_dark",
                )
            )
        ])
    else: 
         return html.Div([
            html.H3('Admin'),
            dcc.Graph(
                figure=dict(
                    data=[dict(
                        x=[1, 2, 3, 99, 102, 300],
                        y=[5, 10, 6, 99, 235, 666],
                        type='bar'
                    )]
                )
            )
        ])

