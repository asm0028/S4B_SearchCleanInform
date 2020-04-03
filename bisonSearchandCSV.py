import requests
import json
import csv

species_name = '"Bison bison"'

#search_url ="https://bison.usgs.gov/api/search.json?species=" + species_name + "&type=scientific_name&start=0&count=1"
search_url ="https://bison.usgs.gov/solr/occurrences/select?q=scientificName:" + species_name + "&wt=json&indent=true"

#search_url = "https://bison.usgs.gov/solr/occurrences/select?q=scientificName:%22Bison%20bison%22&wt=json&indent=true&rows=2147483647"

match = requests.get(search_url)
##print(match.content) #uncomment to test whether match is retrieved

match_result = match.json()

for a in range(0, 8):
    arr = []
    for i in ['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID']:
        if i in match_result['response']['docs'][a]:
            arr.append(match_result['response']['docs'][a][i])
        else:
            arr.append('-')
    with open ('bisonCSV.csv', 'a') as file:
        wr = csv.writer(file, dialect='excel')
        wr.writerow(arr)






