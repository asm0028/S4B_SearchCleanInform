#dependencies listed and imported here

import os
import shutil
import requests
import csv
import time
from tkinter import *
import tkinter.font as font
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


class BisonGUI:
    def __init__(self, master):
        self.master = master
        master.title("GeoBison")

        #initialize all variables that the user input can affect
        self.species_name = ""
        self.remove_no_entry_date = BooleanVar()
        self.remove_no_latitude = BooleanVar()
        self.remove_no_longitude = BooleanVar()
        self.remove_no_occurrence_ID = BooleanVar()
        self.remove_no_catalog_number = BooleanVar()
        self.remove_no_institution_ID = BooleanVar()
        self.map_color = StringVar()
        self.map_color.set("darkgray")
        self.marker_color = StringVar()
        self.marker_color.set("red")
        self.map_width = ""
        self.map_length = ""
        self.marker_size = ""

        title_font = font.Font(size = 20, weight="bold")
        subheader_font = font.Font(size = 18)


        #Initialize all GUI elements
        self.header_label = Label(master, text="Welcome to GeoBison!")
        self.header_label['font'] = title_font
        self.species_entry_label = Label(master, text = "Enter the scientific name of interest:")
        self.species_entry = Entry(master)
        self.species_entry.insert(0, "Example: Percina gymnocephala")
        self.cleaning_label = Label(master,
            text = "Data points will be excluded if\nthe checked parameters are missing.\n----->")
        self.entry_date_checkbox = Checkbutton(master, text = "Entry Date",
            variable = self.remove_no_entry_date, onvalue = "True", offvalue = "False")
        self.latitude_checkbox = Checkbutton(master, text = "Latitude",
            variable = self.remove_no_latitude, onvalue = "True", offvalue = "False")
        self.longitude_checkbox = Checkbutton(master, text = "Longitude",
            variable = self.remove_no_longitude, onvalue = "True", offvalue = "False")
        self.occurrence_ID_checkbox = Checkbutton(master, text = "Occurrence ID",
            variable = self.remove_no_occurrence_ID, onvalue = "True", offvalue = "False")
        self.catalog_number_checkbox = Checkbutton(master, text = "Catalog Number",
            variable = self.remove_no_catalog_number, onvalue = "True", offvalue = "False")
        self.institution_ID_checkbox = Checkbutton(master, text = "Institution ID",
            variable = self.remove_no_institution_ID, onvalue = "True", offvalue = "False")
        self.map_color_label = Label(master, text = "Map color:")
        self.map_color_dropdown = OptionMenu(master, self.map_color, "darkgray", "black", "blue",
            "white", "green", "red", "cyan", "magenta", "yellow", "navy")
        self.marker_color_label = Label(master, text = "Marker color:")
        self.marker_color_dropdown = OptionMenu(master, self.marker_color, "red", "black", "blue",
            "white", "green", "darkgray", "cyan", "magenta", "yellow", "navy")
        self.map_width_label = Label(master, text = "Map width:")
        self.map_width_entry = Entry(master, width=4)
        self.map_width_entry.insert(0, "10")
        self.map_length_label = Label(master, text = "Map length:")
        self.map_length_entry = Entry(master, width=4)
        self.map_length_entry.insert(0, "10")
        self.marker_size_label = Label(master, text = "Marker size:")
        self.marker_size_entry = Entry(master, width=4)
        self.marker_size_entry.insert(0, "10")
        self.go_button = Button(master, text = "Go!", command=self.go_button)
        self.close_button = Button(master, text="Close", command=master.quit)


        #Format each GUI unit using grid method:
        self.header_label.grid(row=0, columnspan=5)
        self.species_entry_label.grid(row=1, columnspan=3, sticky="E")
        self.species_entry.grid(row=1, column=3, columnspan=3, sticky = "W")
        self.cleaning_label.grid(rowspan=3, columnspan=2, sticky="E")
        self.entry_date_checkbox.grid(row=2, column=2, sticky="W")
        self.occurrence_ID_checkbox.grid(row=2, column=3, columnspan=2, sticky="W")
        self.latitude_checkbox.grid(row=3, column=2, sticky="W")
        self.catalog_number_checkbox.grid(row=3, column=3, columnspan=2, sticky="W")
        self.longitude_checkbox.grid(row=4, column=2, sticky="W")
        self.institution_ID_checkbox.grid(row=4, column=3, columnspan=2, sticky="W")
        self.map_color_label.grid(row=5, column=0, sticky="E", pady=(10,0))
        self.map_color_dropdown.grid(row=5, column=1, sticky="W", pady=(10,0))
        self.marker_color_label.grid(row=6, column=0, sticky="E")
        self.marker_color_dropdown.grid(row=6, column=1, sticky="W")
        self.map_width_label.grid(row=5, column=2, sticky="E", pady=(10,0))
        self.map_width_entry.grid(row=5, column=3, sticky="W", pady=(10,0))
        self.map_length_label.grid(row=5, column=4, sticky="E", pady=(10,0))
        self.map_length_entry.grid(row=5, column=5, sticky="W", pady=(10,0))
        self.marker_size_label.grid(row=6, column=3, sticky="E")
        self.marker_size_entry.grid(row=6, column=4, sticky="W")
        self.go_button.grid(row=7, column=2, pady=(5,0))
        self.close_button.grid(row=7, column=3, sticky="W", pady=(5,0))

    #Retrieve all user-input values and save them to pre-established variables
    def go_button(self):
        self.species_name = self.species_entry.get()
        self.remove_no_entry_date = self.remove_no_entry_date.get()
        self.remove_no_latitude = self.remove_no_latitude.get()
        self.remove_no_longitude = self.remove_no_longitude.get()
        self.remove_no_occurrence_ID = self.remove_no_occurrence_ID.get()
        self.remove_no_catalog_number = self.remove_no_catalog_number.get()
        self.remove_no_institution_ID = self.remove_no_institution_ID.get()
        self.map_color = self.map_color.get()
        self.marker_color = self.marker_color.get()
        self.map_width = self.map_width_entry.get()
        self.map_length = self.map_length_entry.get()
        self.marker_size = self.marker_size_entry.get()
        root.destroy()



#Initialize and run GUI window as root
root = Tk()
bison_gui = BisonGUI(root)
root.mainloop()

#User input values saved to appropriate variables for use in other functions
species_name = bison_gui.species_name
remove_no_entry_date = bison_gui.remove_no_entry_date
remove_no_latitude = bison_gui.remove_no_latitude
remove_no_longitude = bison_gui.remove_no_longitude
remove_no_occurrence_ID = bison_gui.remove_no_occurrence_ID
remove_no_catalog_number = bison_gui.remove_no_catalog_number
remove_no_institution_ID = bison_gui.remove_no_institution_ID
map_color = bison_gui.map_color
marker_color = bison_gui.marker_color
map_width = int(bison_gui.map_width)
map_length = int(bison_gui.map_length)
marker_size = int(bison_gui.marker_size)

#Print statements for testing - can remove in final version
print("User input for species name:", species_name)
print("Remove data with no entry date?", remove_no_entry_date)
print("Remove data with no latitude?", remove_no_latitude)
print("Remove data with no longitude?" , remove_no_longitude)
print("Remove data with no occurrence ID?" , remove_no_occurrence_ID)
print("Remove data with no catalog number?" , remove_no_catalog_number)
print("Remove data with no institution ID?" , remove_no_institution_ID)
print("What is the map color?" , map_color)
print("What is the marker color?" , marker_color)
print("What is the map width?" , map_width)
print("What is the map length?" , map_length)
print("What is the marker size?", marker_size)


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

#start bisonSearchandCSV

species_name_fixed = ('"' + species_name.capitalize() + '"')

with open('bisonCSV.csv', 'w', newline='') as file:
    wr = csv.writer(file)
    wr.writerow(['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID'])

def fetch_solr(page, rows):
    start = page * rows
    params = {'q' : 'scientificName:' + species_name_fixed, 'rows' : rows, 'start' : start, 'wt' : 'json'}
    match = requests.get('https://bison.usgs.gov/solr/occurrences/select?', params=params)
    match_result = match.json()
    return match_result

def result_csv_writer(record):
            arr = []
            for keyword in ['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID']:
                if keyword in (result['response']['docs'][record]):
                    arr.append(result['response']['docs'][record][keyword])
                else:
                    arr.append('')
            with open ('bisonCSV.csv', 'a', newline='') as file:
                wr = csv.writer(file)
                wr.writerow(arr)

result = fetch_solr(0, 1)
num_found = result['response']['numFound']

if num_found < 1000:
    result = fetch_solr(0, num_found)
    for record in range (0, num_found):
        result_csv_writer(record)

if num_found >= 1000:    
    total_pages = (num_found//1000)
    for page in range (0, total_pages + 1):
        result = fetch_solr(page, 1000)
        while page != total_pages:
            for record in range (0, 1000):
                result_csv_writer(record)
            break
            time.sleep(1)
        while page == total_pages:
            for record in range (0, num_found - (total_pages * 1000)):
                result_csv_writer(record)
            break

#start bisonCleanCSV

shutil.copy('bisonCSV.csv','bisonCSV.cleaned.csv')

def action(column):
        input = open('bisonCSV.cleaned.csv', 'r')
        output = open('bisonCSV.cleaned.int.csv', 'w', newline='')
        wr = csv.writer(output)
        for row in csv.reader(input):
            if row[column] != '':
                wr.writerow(row)
        input.close()
        output.close()
        os.remove('bisonCSV.cleaned.csv')
        os.rename('bisonCSV.cleaned.int.csv', 'bisonCSV.cleaned.csv')

n = 1
for x in [remove_no_entry_date, remove_no_longitude, remove_no_latitude, remove_no_occurrence_ID, remove_no_catalog_number, remove_no_institution_ID]:
    if x is True:
        action(n)
        n = n + 1
    else:
        n = n + 1
        pass

#starting geobison block

url = 'https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json'
r = requests.get(url, allow_redirects=True)

def geobison(cleaned_csv,  map_color, map_size, marker_color, marker_size, map_title, output=os.getcwd()):

    #getting USA data
    open('USA_data.json', 'wb').write(r.content)
    USA = gpd.read_file('USA_data.json')
    CONUS = USA[USA['NAME'].isin(['Alaska', 'Hawaii',
 'Puerto Rico']) == False]

    #adding input species data from BISON
    Species_data = pd.read_csv(cleaned_csv)
    Species_data['coords'] = Species_data[['decimalLongitude',
 'decimalLatitude']].values.tolist()
    Species_data['coords'] = Species_data['coords'].apply(Point)
<<<<<<< HEAD
    #Species_data['coords'] = int(Species_data['coords'])
=======
>>>>>>> eb8d9c49cc0d10e8d54c4acb04137ba102687023
    #print("Species data coords type:", type(Species_data['coords']))
    Species_data = gpd.GeoDataFrame(Species_data, geometry='coords')

    #mapping
    fig, ax = plt.subplots(1, figsize=map_size)
    base = CONUS.plot(ax=ax,color=map_color,alpha=1, edgecolor='black')
    Species_data.plot(ax=base, color=marker_color, marker="*",markersize=marker_size)
    ax.set_title(map_title, fontsize=20,pad=25)
    plt.savefig('my_new_map.png', dpi=350, bbox_inches='tight')

geobison(cleaned_csv = 'bisonCSV.cleaned.csv', map_color = map_color, map_size = (map_width, map_length),
    marker_color = marker_color, marker_size = marker_size, map_title = species_name)

#starting geobison_count block

def geobison_count(cleaned_csv, output=os.getcwd()):

    #getting USA data
    open('USA_data.json', 'wb').write(r.content)
    USA = gpd.read_file('USA_data.json')
    CONUS = USA[USA['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico']) == False]

    #adding input species data from BISON
    bd = pd.read_csv(cleaned_csv)
    points = bd.apply(lambda row: Point(row.decimalLongitude, row.decimalLatitude),axis=1)
    bd_species = gpd.GeoDataFrame(bd, geometry=points)
    bd_species.crs = {'init' :'epsg:4326'}

    #state counts
    bd_and_CONUS = gpd.sjoin(bd_species,CONUS, how='left', op='within')
    how_many_in_states = bd_and_CONUS['NAME'].value_counts()
    print(how_many_in_states, file=open('state_counts.txt', 'w'))

geobison_count('bisonCSV.cleaned.csv')
