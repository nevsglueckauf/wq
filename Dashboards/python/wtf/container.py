# Factory Klasse für Tab-Content
#
# AUTHOR Sven Schrodt
# SINCE 2025-10-07

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
    Patch,
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from typing import Self

class Container:

    rt = None
    dta = None
    
    def __init__(self, child=None, rt:str='Div'):
        if child == None:
            self.dta = []
        else :
            self.dta = child
        self.rt = rt
            
        
    def apd(self, dta):
        """ Appending element

        Args:
            dta (Any): HTML elements and descendants
        """
        self.dta.append(dta)
        
    def apd_row(self, dta) -> Self:
        """ Appending element(s)

        Args:
            dta (Any): HTML elements and descendants
        """
        self.dta.append(dbc.Row(dta))
        return self
    
    def rndr(self) -> list:
        """ Rendering contents

        Returns:
            list: _description_
        """
        return html.Div(self.dta)
        