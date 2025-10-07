# Whisky Online Shop Data analysis & prediction stuff
# Projekt "Data on the rox"
# AUTHOR 
# SINCE 2025-09-26

# 3rd party libs
from dash import (
    Dash,
    html,
    page_registry,
    page_container,
    clientside_callback,
    Input,
    Output,
    callback,
    dcc,
    Patch
)
import plotly.express as px
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash

from dd import DD
from factory import TabFactory

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@master/dbc.css"

#   dbc_css = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css"

#ext_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']    

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.CYBORG],
    suppress_callback_exceptions=True,
)




df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="size"  )

app.title = '“Data on the rocks”: Datenanalyse und Vorhersagen'

app.layout = html.Div([
    html.H3(app.title),
    dcc.Tabs(id='tabs-example-1', value='tab-1', children=[
        dcc.Tab(label='Sitzungen', value='tab-1'),
        dcc.Tab(label='Umsätze', value='tab-2'),
        dcc.Tab(label='Werbung', value='tab-3'),
        dcc.Tab(label='Admin Panel', value='tab-4'),
    ]),
    html.Div(id='tabs-example-content-1')
])

@callback(
    Output(component_id="sales-sales-controls-and-graph", component_property="figure"),
    Input(component_id="sales-sales-controls-and-check-item", component_property="value"),
)
def update_graph_sales(col_chosen):
    fig = px.line(df, x="Tag", y=col_chosen, title="Umsätze", color='Vertriebskanal')
 
    return fig

@callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs-example-1', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Sessions'),
            dcc.Graph(
                figure=fig
            )
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Sales'),
            TabFactory.sales()
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Ads'),
        ])
    else: 
         return html.Div([
            html.H3('Admin'),
        ])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9999)
    
