import dash_leaflet as dl
from dash_extensions.javascript import arrow_function
import os
from dash import html
import pandas as pd

df = pd.read_csv(os.path.join(
            os.path.dirname('./data/'),
            'nodes.csv'), delimiter=';', decimal=",")

def create_map_layout():
    return html.Div(

        dl.Map(
            [
                dl.TileLayer(),
            ]
            +
            [
                dl.Marker(position=[df['latitude'].iloc[i], df['longitude'].iloc[i]],
                          icon=dict(
                              iconUrl='/assets/' + str(df['type'].iloc[i]) + '.svg',
                              iconSize=[30, 80],
                          ),
                          children=[dl.Tooltip(
                              content=str(df['node'].iloc[i]) + '<br>' + str(
                                  df['param_name'].iloc[i]) + ": " + str(
                                  df['param_value'].iloc[i]))])
                for i in range(df.shape[0])
            ]
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
        style={'z-index': 1}
    )
