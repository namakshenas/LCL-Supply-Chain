from controls.cl_control_accordion import create_control_accordion
from controls.cl_button_run import create_btn_run
import dash_mantine_components as dmc
from dash import html


def create_control_layout():
    return html.Div(
        dmc.Stack(
            id="div-control-layout",
            children=[
                create_control_accordion(),
                create_btn_run(),
            ],

        ),
        className='control-layout'
    )
