import dash_ag_grid as dag
import pandas as pd


def create_table():
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")
    return dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        className="ag-theme-alpine compact",
        columnSize="sizeToFit",
    )
