import dash_leaflet as dl
from controls.cl_map_marker import create_map_marker
from dash import html


def create_map_layout():
    return html.Div(

        dl.Map(
            [
                dl.TileLayer(),
            ]
            +
            create_map_marker()
            +
            [
                html.Div(id='position-data'),
                # dl.GeoJSON(url="/assets/europe_GR.json",
                #            hoverStyle=arrow_function(dict(weight=1, color='#666', dashArray='')),
                #            ),
                #     dl.WMSTileLayer(url="https://demotiles.maplibre.org/style.json",
                #                     layers="nexrad-n0r-900913", format="image/png", transparent=True)
            ],
            center=[49.4, 5], zoom=7, style={'height': '100vh', }),
    )
