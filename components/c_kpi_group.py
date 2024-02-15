import dash_mantine_components as dmc
from dash import html
from components.c_kpi import create_kpi
from controls.cl_json_parser import parse_json
import os


# category_list : .json
def create_kpi_group():
    item_list = parse_json(
        os.path.join(
            os.path.dirname('./params/'),
            'kpi.json')
    )
    return dmc.SimpleGrid(
        cols=3,
        spacing="lg",
        children=[
            html.Div(
                create_kpi(item),
            )
            for item in item_list
        ],
    )
