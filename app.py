import os
import numpy as np
import pandas as pd

# Data visualisation libraries
import plotly.offline as py # Plotly
from plotly import tools
import plotly.graph_objs as go
import plotly.figure_factory as ff

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import folium                               # for visualizing geospatial data                                      
import seaborn as sns
import matplotlib.pyplot as plt             # for plotting graphs
from folium.plugins import MarkerCluster    # for visualising clusters

########### Define your variables ######

tabtitle = 'F1 Data analysis'
sourceurl = 'https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020'
githublink = 'https://github.com/manueldelreal/formula1-EDA'

def create_map():
    circuitsdf = pd.read_csv('race-data/circuits.csv')
    circuits_folium = circuitsdf[['name', 'location', 'country', 'lat', 'lng']]
    circuits_map = folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(circuits_map)
    for i in range(len(circuits_folium)):
        lat = circuits_folium.iloc[i]['lat']
        lng = circuits_folium.iloc[i]['lng']
        radius = 5
        popup_text = circuits_folium.iloc[i]['name']
        folium.CircleMarker(location = [lat, lng], radius = radius,
        popup = popup_text, fill = True).add_to(marker_cluster)
        circuits_map.save('assets/circuits_map.html')
    return circuits_map

map_of_circuits = create_map()



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div([
    html.H1('Location of F1 circuits around the world'),
    html.Iframe(id = 'map', srcDoc = open('assets/circuits_map.html', 'r').read(), width='100%', height='600')
]
)


# make a function that can intake any varname and produce a map.


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)