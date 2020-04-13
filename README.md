# *GeoBison*: a Python-implemented toolkit for acquiring, cleaning and visualizing geographic occurrence data of species in the contiguous United States

Nicholas Gladstone, Anne Maguire, and Madison Watkins

## Summary

The functions in this toolkit allow for the acquisition, cleaning/filtering, and visualization of species occurrence data sourced from the U.S. Node the Global Biodiversity Information Facility - BISON (Biodiversity Information Serving Our Nation).

## Quick tutorial for losers who don't want to read to full documentation

### Getting started

Open up your terminal or preferred terminal environment. Then, install and import the following packages:

```
import os
import requests
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import descartes

[Anne and Madison please put other dependencies here]

```
*Note: we reccommend utilizing the Anaconda software distribution (v.3.7), as most of these packages are already included along with beginner-friendly coding environments (e.g., Spyder). This can be downloaded at: https://www.anaconda.com/distribution/#download-section*


After installing the necessary packages, download and run the **RunAllParts.py** script found in this repo.

You are now ready to go!

### Using *GeoBison*

[Anne and Madison include information about your scripts and the GUI here]




For producing a visualization of your occurrence data pre- or post- cleaning, you will use the *geobison* function:

```
geobison('INPUT_DATA.csv', output=[OUTPUT DIRECTORY HERE], map_color='COLOR OPTION HERE',
             map_size=(DIMENSIONS OF IMAGE HERE), marker_color='COLOR OPTION HERE', marker_size=[SIZE VALUE HERE])
```

The defaults for *geobison* are:

output=os.getcwd()  # i.e., your current working directory
map_color='darkgray'
map_size=(11,9)
marker_color='red'
marker_size=10

*Note: if you need a list of available color options on python, please visit https://python-graph-gallery.com/196-select-one-color-with-matplotlib/*


For producing a quick summary file of how many records there are total, including a list of how many records are in each individual state within the contiguous U.S., you will use the *geobison_count* function:

```
geobison_count('INPUT_DATA.csv', output=[OUTPUT DIRECTORY HERE])
```

As with *geobison*, the default output is the cwd.



