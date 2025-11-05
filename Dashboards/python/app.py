# Main app für die Multipage-Ansicht
#
#
# 3rd party libs
from dash import (
    Dash,
    html,
    page_registry,
    page_container,
    clientside_callback,
    Input,
    Output,
    dcc,
)

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash

load_figure_template(["sandstone", "simplex"])

# project libs
from dd import DD

# from cfg import Cfg

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.FLATLY, dbc_css],
    suppress_callback_exceptions=True,
)
app.title = "Data on the rocks"

navbar = dbc.NavbarSimple(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(DD.pages[page["name"]], href=page["path"])
                for page in page_registry.values()
                if page["module"] != "pages.not_found_404"
            ],
            nav=True,
            label="Auswahl",
        ),
    ],
    brand=[
        html.Span("🧊🥃", style={'fontSize': '1.5rem', 'marginRight': '10px'}),
        html.Span("Data on the rocks", style={'fontWeight': '600'})
    ],
    color="primary",
    dark=True,
    className="mb-2 custom-navbar",
)

app.layout = dbc.Container([navbar, page_container], fluid=True, className="dbc")

# Custom CSS im Index String --> Farbverlauf in oberer
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            .custom-navbar {
                background: linear-gradient(135deg, #2E86AB 0%, #1A535C 100%) !important;
                border-bottom: 3px solid #F9C74F;
            }
            
            .navbar-brand {
                font-size: 1.3rem !important;
                font-weight: 600 !important;
                color: white !important;
            }
            
            .custom-dropdown .dropdown-toggle {
                color: rgba(255,255,255,0.9) !important;
                font-weight: 500;
                border-radius: 6px;
                transition: all 0.3s ease;
            }
            
            .custom-dropdown .dropdown-toggle:hover {
                background-color: rgba(255,255,255,0.15) !important;
                color: white !important;
            }
            
            /* Verbesserte Card Styles */
            .custom-card {
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
                border: none;
                transition: all 0.3s ease;
                overflow: hidden;
            }
            
            .custom-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 15px rgba(0, 0, 0, 0.12);
            }
            
            .analysis-card {
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                border: 1px solid #e9ecef;
                border-radius: 10px;
                padding: 25px 15px;
                text-align: center;
                transition: all 0.3s ease;
                cursor: pointer;
                height: 100%;
            }
            
            .analysis-card:hover {
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(46, 134, 171, 0.2);
                border-color: #2E86AB;
            }
            
            /* Hero Section */
            .hero-section {
                background: linear-gradient(135deg, #2E86AB 0%, #1A535C 100%);
                border-radius: 15px;
                padding: 60px 40px;
                color: white;
                margin-bottom: 40px;
                text-align: center;
            }
            
            body {
                background-color: #f8f9fa;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    
