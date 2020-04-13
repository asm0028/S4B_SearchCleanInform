import argparse
import requests
import json
import csv

parser = argparse.ArgumentParser()

parser.add_argument('name', nargs=2, help='Scientific name you would like to input.'
                    ' Must be formatted for genus in the first name position, and'
                    ' species in the second name position.')

args = parser.parse_args()

spaced_input = ' '.join(args.name)

species_name = ('"' + spaced_input.capitalize() + '"')

#search_url ="https://bison.usgs.gov/solr/occurrences/select?q=scientificName:" + species_name + "&wt=json&indent=true"
#Use this search URL if you only want 10 records.

search_url = "https://bison.usgs.gov/solr/occurrences/select?q=scientificName:" + specices_name + "&wt=json&indent=true&rows=2147483647"

match = requests.get(search_url)

match_result = match.json()

num_found = match_result['response']['numFound']

with open('bisonCSV.csv', 'w', newline='') as file:
    wr = csv.writer(file)
    wr.writerow(['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID'])

for a in range(0, num_found):
    arr = []
    for i in ['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID']:
        if i in match_result['response']['docs'][a]:
            arr.append(match_result['response']['docs'][a][i])
        else:
            arr.append('-')
    with open ('bisonCSV.csv', 'a') as file:
        wr = csv.writer(file)
        wr.writerow(arr)




