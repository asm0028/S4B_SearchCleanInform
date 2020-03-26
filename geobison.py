#dependencies listed and imported here

import os
import requests
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import descartes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm


#starting geobison block

def geobison(bison_data, output=cwd, map_color='darkgray', map_size=(10,10), marker_color='red', marker_size=10, map_title="[Will insert name of user's species here]"):
    
    #getting USA data
    url = 'https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json'
    r = requests.get(url, allow_redirects=True)
    open('USA_data.json', 'wb').write(r.content)
    USA = gpd.read_file('USA_data.json')
    CONUS = USA[USA['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico']) == False]
    
    #adding input species data from BISON
    Species_data = pd.read_csv(bison_data)
    Species_data['coords'] = Species_data[['decimalLongitude', 'decimalLatitude']].values.tolist()
    Species_data['coords'] = Species_data['coords'].apply(Point)
    Species_data = gpd.GeoDataFrame(Species_map, geometry='coords')
    
    #mapping
    fig, ax = plt.subplots(1, figsize=map_size)
    base = CONUS.plot(ax=ax,color=map_color)
    Species_map.plot(ax=base, color=maker_color, marker="*",markersize=marker_size)
    ax.set_title(map_title, fontsize=25)
    plt.savefig('/Users/NickG/Documents/S4B_Project/GIS_Project_Master_Repo/test.png',bbox_inches='tight')
