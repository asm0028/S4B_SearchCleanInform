import requests
from bs4 import BeautifulSoup
import webbrowser
import json

url = "https://bison.usgs.gov/api/search.json?species=Bison%20bison&type=scientific_name&start=0&count=1"

#webbrowser.open(url) #uncomment to test whether url is valid

match = requests.get(url)
print(match.content)
