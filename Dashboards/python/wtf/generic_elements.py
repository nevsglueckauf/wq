# Factory-Klasse für HTML Elemente
#
# AUTHOR Sven Schrodt
# SINCE 2025-10-14
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

from wtf.container import Container


class ElementBuilder:

    title_el = "h3"

    def __init__(self):
        pass

    @staticmethod
    def card(dta, title: str = "", img_src="", wdth="23rem") -> dbc.Card:
        tmp = Container()

        if img_src != "":
            tmp.apd(dbc.CardImg(src=img_src, top=True))

        if title != "":
            tmp.apd(html.H4(title, className="card-title"))

        tmp.apd(dbc.CardBody(dta))
        return dbc.Card(
            tmp.rndr(),
            style={"width": wdth},
            outline=True,
        )

    @staticmethod
    def dd(df, strt_colz=[], id=""):
        return dcc.Dropdown(
            id=id,
            options=df,
            value=strt_colz,
            multi=True,
            className="dropdown-class",
            style={"background-color": "#011213"},
        )

    @staticmethod
    def col(ctnt) -> dbc.Col:
        return dbc.Col(ctnt)

    @staticmethod
    def row(ctnt) -> dbc.Row:
        return dbc.Row(ctnt)

    @staticmethod
    def row(rows: list) -> list:
        tmp = []
        for row in rows:
            tmp.append(dbc.Row(row))
        return tmp
