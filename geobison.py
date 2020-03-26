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

"""there are two functions housed in this code that perform the following:
	1.) geobison: provide the geobison with the cleaned bison dataset of
	    your species of interest, and provide it with a series of figure
	    specifications (color, size, etc.). In turn, the function will
	    provide the user with a quick figure for illustrative purposes
	    of where in CONUS the species is located.
	2.) geobison_count: provide the geobison_count with the cleaned
	    bison dataset as before, and the function will return a counted
	    list of all records within the lower 48 states that the species
	    occurs in, and how many records there are in each state.

"""

#starting geobison block

def geobison(bison_data, output=os.getcwd(),  map_color='darkgray', map_size=(10,10), marker_color='red', marker_size=10, map_title="[Will insert name of user's species here]"):
    
    #getting USA data
    url = 'https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json'
    r = requests.get(url, allow_redirects=True)
    open('USA_data.json', 'wb').write(r.content)
    USA = gpd.read_file('USA_data.json')
    CONUS = USA[USA['NAME'].isin(['Alaska', 'Hawaii',
 'Puerto Rico']) == False]
    
    #adding input species data from BISON
    Species_data = pd.read_csv(bison_data)
    Species_data['coords'] = Species_data[['decimalLongitude',
 'decimalLatitude']].values.tolist()
    Species_data['coords'] = Species_data['coords'].apply(Point)
    Species_data = gpd.GeoDataFrame(Species_data, geometry='coords')
    
    #mapping
    fig, ax = plt.subplots(1, figsize=map_size)
    base = CONUS.plot(ax=ax,color=map_color,alpha=1, edgecolor='black')
    Species_data.plot(ax=base, color=marker_color, marker="*",markersize=marker_size)
    ax.set_title(map_title, fontsize=20,pad=25)
    plt.savefig('my_new_map.png', dpi=350, bbox_inches='tight')

#starting geobison_join block

def geobison_count(join_data, output=os.getcwd())

    #getting USA data
    url = 'https://eric/clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json'
    r = requests.get(url, allow_redirects=True)
    open('USA_data.json', 'wb').write(r.content)
    USA = gpd.read_file('USA_data.json')
    CONUS = USA[USA['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico']) == False]

    #adding input species data from BISON
    bd = pd.read_csv(join_data)
    points = bd.apply(lambda row: Point(row.decimalLongitude, row.decimalLatitude),axis=1)
    bd_species = gpd.GeoDataFrame(bd, geometry=points)
    bd_species.crs = {'init' :'epsg:4326'}

    #state counts
    bd_and_CONUS = gpd.sjoin(bd_species,CONUS, how='left', op='within')
    how_many_in_states = bd_and_CONUS['NAME'].value_counts()
    print(how_many_in_states, file=open('state_counts.txt', 'w'))
