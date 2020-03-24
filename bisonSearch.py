import requests
from bs4 import BeautifulSoup
import webbrowser
import json
import pandas

url = "https://bison.usgs.gov/api/search.json?species=Bison%20bison&type=scientific_name&start=0&count=1"

#webbrowser.open(url) #uncomment to test whether url is valid
matched_species = []
match = requests.get(url)
#print(match.content) #uncomment to test whether match is retrieved

match_result = match.json()
match_result["inputName"] = "Bison bison"
#print(match_result)
#print(match_result.type)

matched_species.append(match_result)
result = pandas.DataFrame(matched_species)
print(result)