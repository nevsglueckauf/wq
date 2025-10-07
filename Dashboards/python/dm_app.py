import dash_mantine_components as dmc
import plotly.express as px
from dash import Dash, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="size", template="plotly_dark")

app=Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.layout = dbc.Container([
    html.H1("Dash App in Dark Mode", className="text-center"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True, port=9999)
