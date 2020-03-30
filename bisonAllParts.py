#dependencies listed and imported here

import os
import requests
import json
import tkinter as tk
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import descartes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm



def build_GUI():

    #event handler functions
    def handle_go_button(event):
        species_name = species_entry.get()
        print(species_name)
        return species_name

    def close_window():
        window.destroy()

    #initiate main (master) window
    window = tk.Tk()
    window.title("Search-Clean-Inform")

    #place greeting frame in master window and greeting label within that
    greeting_frame = tk.Frame(master=window, height=25)
    greeting_frame.grid(row=0, column=0)
    greeting_label = tk.Label(master=greeting_frame, text="Welcome to Search-Clean-Inform!")
    greeting_label.grid(row=0, column=0)

    #place species entry frame in master window -- will split into label (query prompt) and entry box
    species_entry_frame = tk.Frame(master=window)
    species_entry_frame.grid(row=1, column=0)
    #place species label (query prompt) within species entry frame
    species_label = tk.Label(master=species_entry_frame, text = "Please enter the scientific name of your species of interest:")
    species_label.grid(row=0, column=0)
    #place species entry box within species entry frame, initialize example text
    species_entry = tk.Entry(master=species_entry_frame)
    species_entry.insert(0, "Ex: Bison bison")
    species_entry.grid(row=0, column=1)

    #place button frame within master window
    go_button_frame = tk.Frame(master=window, relief=tk.RAISED)
    go_button_frame.grid(row=2, column=0)
    #initalize go button and place in button frame
    go_button = tk.Button(master=go_button_frame, text = "Go!", command = handle_go_button)
    go_button.grid(row=0, column=0)
    #initialize exit button and place in button frame
    exit_button = tk.Button(master=go_button_frame, text = "Exit", command = close_window)
    exit_button.grid(row=0, column=1)

    #calls for information from GUI and their assignment to return variables
    species_name = go_button.bind("<Button-1>", command = handle_go_button)

    #keeps window up and running until closed
    window.mainloop()

    return species_name

species_name = build_GUI()
#print statements for testing
print(species_name)


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

def geobison_count(join_data, output=os.getcwd()):

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
