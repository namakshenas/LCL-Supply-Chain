import dash_mantine_components as dmc


def create_btn_run():
    return dmc.Button(
        "Start",
        id="btn_run",
        variant="filled",
        fullWidth=True,
        className="btn_run",
    )
