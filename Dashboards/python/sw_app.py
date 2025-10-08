import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Dash, Input, Output, clientside_callback, html, dcc
import dash_mantine_components as dmc
import plotly.express as px
import plotly.express as px
import dash_bootstrap_components as dbc


df = px.data.gapminder()
dff = df[df.year == 2007]

theme_toggle = dmc.Switch(
    offLabel=DashIconify(
        icon="radix-icons:sun", width=15, color=dmc.DEFAULT_THEME["colors"]["yellow"][8]
    ),
    onLabel=DashIconify(
        icon="radix-icons:moon",
        width=15,
        color=dmc.DEFAULT_THEME["colors"]["yellow"][6],
    ),
    id="color-scheme-switch",
    persistence=True,
    color="grey",
)

app = Dash()
app.title ="App with Dash and them switch"
app.layout = dmc.MantineProvider(
    [
        html.H1("Page mit Darkmode Switch"),
        theme_toggle,
        dmc.Text("Your page content"),
        dmc.SimpleGrid(
            [
                # dcc.Graph(
                #     figure=px.bar(
                #         dff,
                #         x="continent",
                #         y="pop",
                #         template="plotly_white",
                #         title="plotly_white theme",
                #     )
                # ),
                dcc.Graph(
                    figure=px.bar(
                        dff,
                        x="continent",
                        y="pop",
                        template="plotly_dark",
                        title="plotly_dark theme",
                    )
                ),
            ],
            cols=2,
        ),
    ],
)

clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-switch", "id"),
    Input("color-scheme-switch", "checked"),
)


if __name__ == "__main__":
    app.run(debug=True, port=9999)
