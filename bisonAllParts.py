#dependencies listed and imported here

import os
import requests
import json
from tkinter import *
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import descartes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm


class BisonGUI:
    def __init__(self, master):
        self.master = master
        master.title("Search-Clean-Inform")

        #initialize all variables that the user input can affect
        self.species_name = ""
        self.remove_no_entry_date = BooleanVar()
        self.remove_no_latitude = BooleanVar()
        self.remove_no_longitude = BooleanVar()
        self.remove_no_occurrence_ID = BooleanVar()
        self.remove_no_catalog_number = BooleanVar()
        self.remove_no_institution_ID = BooleanVar()

        #Initialize all GUI units
        self.header_label = Label(master, text="Welcome to Search-Clean-Inform")
        self.species_entry_label = Label(master, text = "Enter the scientific name of interest:")
        self.species_entry = Entry(master)
        self.species_entry.insert(0, "Example: Bison bison")
        self.entry_date_checkbox = Checkbutton(master, text = "Entry Date",
            variable = self.remove_no_entry_date)
        self.latitude_checkbox = Checkbutton(master, text = "Latitude",
            variable = self.remove_no_latitude, onvalue = "True", offvalue = "False")
        self.longitude_checkbox = Checkbutton(master, text = "Longitude",
            variable = self.remove_no_longitude, onvalue = "True", offvalue = "False")
        self.occurrence_ID_checkbox = Checkbutton(master, text = "Occurrence ID",
            variable = self.remove_no_occurrence_ID, onvalue = "True", offvalue = "False")
        self.go_button = Button(master, text = "Go!", command=self.go_button)
        self.close_button = Button(master, text="Close", command=master.quit)


        #Format each GUI unit using grid method:
        self.header_label.grid(row=0, columnspan=3)
        self.species_entry_label.grid(row=1, columnspan=2)
        self.species_entry.grid(row=1, column=2)
        self.entry_date_checkbox.grid(row=2, column=0)
        self.occurrence_ID_checkbox.grid(row=2, column=1)
        self.latitude_checkbox.grid(row=3, column=0)
        self.longitude_checkbox.grid(row=4, column=0)
        self.go_button.grid(row=5, column=0)
        self.close_button.grid(row=5, column=1)

    def go_button(self):
        self.species_name = self.species_entry.get()
        self.remove_no_entry_date = self.remove_no_entry_date.get()
        self.remove_no_latitude = self.remove_no_latitude.get()
        self.remove_no_longitude = self.remove_no_longitude.get()
        self.remove_no_occurrence_ID = self.remove_no_occurrence_ID.get()
        root.destroy()




root = Tk()
bison_gui = BisonGUI(root)
root.mainloop()


species_name = bison_gui.species_name
remove_no_entry_date = bison_gui.remove_no_entry_date
remove_no_latitude = bison_gui.remove_no_latitude
remove_no_longitude = bison_gui.remove_no_longitude
remove_no_occurrence_ID = bison_gui.remove_no_occurrence_ID

#Print statements for testing - can remove in final version
print("User input for species name:", species_name)
print("Remove data with no entry date?", remove_no_entry_date)
print("Remove data with no latitude?", remove_no_latitude)
print("Remove data with no longitude?", remove_no_longitude)
print("Remove data with no occurrence ID?", remove_no_occurrence_ID)


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
