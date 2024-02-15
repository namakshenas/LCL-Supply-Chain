import dash_mantine_components as dmc
from dash import html


# category_list : .json
def create_kpi(item):
    return html.Div(
        [
            dmc.Badge(
                item["label"],
                color=item["color"],
                size="lg"
            ),
            dmc.Text(
                str(item["value"]) + " " + item["unit"],
                size="xl",
                id="text_" + "kpi_" + item['id'],
            )
        ],
        className="tr-row-kpi",
    )
