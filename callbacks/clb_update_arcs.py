from app import app
import dash_leaflet as dl
from dash import Input, Output
import time
import os
import numpy as np
import pandas as pd
from scgraph_data.world_highways import world_highways_geograph
from scgraph.utils import get_line_path
import random
import distinctipy


def rgb_to_hex(rgb):

    rgb = tuple(max(0, min(1, val)) for val in rgb)
    rgb_int = tuple(int(val * 255) for val in rgb)
    hex_value = '#{:02x}{:02x}{:02x}'.format(*rgb_int)

    return hex_value


def serve_clb_update_arcs(app):
    @app.callback(Output('position-data', 'children'),
                  Input("btn_run", "n_clicks"),
                  prevent_initial_call=True)
    def update_arcs(n_clicks):
        time.sleep(5)
        df = pd.read_csv(os.path.join(
            os.path.dirname('./data/'),
            'nodes.csv'), delimiter=';', decimal=",")
        df2 = pd.DataFrame(columns=['origin', 'destination', 'transport_value'])
        arcs = {}
        for p in range(20):
            i = np.random.randint(0, 8)
            j = np.random.randint(8, 16)
            k = np.random.randint(16, 28)
            df2.at[p, 'origin'] = df['node'].iloc[i] + " - " + df['country'].iloc[i]
            df2.at[p, 'destination'] = df['node'].iloc[j] + " - " + df['country'].iloc[j]
            df2.at[p, 'transport_value'] = np.random.randint(500, 999)
            arcs.update({f"'{p}'": [[df['latitude'].iloc[i], df['longitude'].iloc[i]],
                                    [df['latitude'].iloc[j], df['longitude'].iloc[j]]]})
            arcs.update({f"'{p + 50}'": [[df['latitude'].iloc[j], df['longitude'].iloc[j]],
                                         [df['latitude'].iloc[k], df['longitude'].iloc[k]]]})
        arcs_polyline = []
        df2.to_csv("./data/solution.csv", index=False)
        colors = distinctipy.get_colors(len(arcs))
        for p in arcs.values():
            output = world_highways_geograph.get_shortest_path(
                origin_node={"latitude": p[0][0], "longitude": p[0][1]},
                destination_node={"latitude": p[1][0], "longitude": p[1][1]}
            )
            # Write the output to a geojson file
            line_path = get_line_path(output)
            line_path_modified = [[s[1], s[0]] for s in line_path['coordinates']]
            rand_color = random.choice(colors)
            arcs_polyline += [
                dl.Polyline(positions=line_path_modified, color=rgb_to_hex(rand_color), weight=random.randint(1, 5))
                # dl.Polyline(positions=line_path['coordinates'],
                #             children=[dl.Tooltip(content=str(np.random.randint(500, 999)))], color='red')

            ]
            colors.remove(rand_color)
        return arcs_polyline
