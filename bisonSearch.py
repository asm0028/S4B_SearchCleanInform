import requests
from bs4 import BeautifulSoup
import webbrowser
import json
import pandas
import csv

species_name = '"Bison bison"'
#search_url ="https://bison.usgs.gov/api/search.json?species=" + species_name + "&type=scientific_name&start=0&count=1"
search_url ="https://bison.usgs.gov/solr/occurrences/select?q=scientificName:" + species_name + "&wt=json&indent=true"
print(search_url)
#search_url = "https://bison.usgs.gov/solr/occurrences/select?q=scientificName:%22Bison%20bison%22&wt=json&indent=true&rows=2147483647"

#webbrowser.open(url) #uncomment to test whether url is valid
matched_species = []
match = requests.get(search_url)
#print(match.content) #uncomment to test whether match is retrieved

match_result = match.json()
#match_result["inputName"] = "Bison bison"
#print(match_result)
#print(match_result.type)

matched_species.append(match_result)
#result = pandas.DataFrame(matched_species)
#print(result)

with open('match_result.json', 'w', encoding='utf-8') as f:
    json.dump(match_result, f, ensure_ascii=False, indent=4)

#result.to_csv('Bison_test.csv')

df = pandas.read_json('match_result.json')
df.to_csv('match_result.csv')
