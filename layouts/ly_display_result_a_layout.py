from components.c_graph_group import create_graph_group
from components.c_kpi_group import create_kpi_group
import dash_mantine_components as dmc
from dash import html


def create_display_result_a_layout():
    return dmc.Stack(
        children=[
                     create_kpi_group()
                 ]
                 +
                 create_graph_group(),
        className="result-layout-a"
    )
