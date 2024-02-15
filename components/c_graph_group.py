import dash_ag_grid as dag
from dash import html
from utils.utils import create_graph
import dash_mantine_components as dmc


def create_graph_group():
    return [
        html.Div(create_graph(),
                 className="drawer-fig-layout"),
        html.Div(create_graph(),
                 className="drawer-fig-layout"),
        html.Div(create_graph(),
                 className="drawer-fig-layout")
    ]
