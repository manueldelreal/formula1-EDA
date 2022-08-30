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

import random

########### Define your variables ######

tabtitle = 'F1 Data analysis'
sourceurl = 'https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020'
githublink = 'https://github.com/manueldelreal/formula1-EDA'



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('Visualising circuits around the world on a world map using clusters'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


# make a function that can intake any varname and produce a map.

def random_colors(number_of_colors):
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(number_of_colors)]
    return color
    
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
circuits_map


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)