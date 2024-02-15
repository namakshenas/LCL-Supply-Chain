import time
from dash import Input, Output, no_update


def serve_clb_display_drawer(app):
    @app.callback(
        Output("drawer-control", "opened"),
        Input("btn-drawer-control", "n_clicks"),
        prevent_initial_call=True,
    )
    def drawer_open(n_clicks):
        return True
