import argparse
import requests
import json
import csv
import time

parser = argparse.ArgumentParser()

parser.add_argument('name', nargs=2, help='Scientific name you would like to input.'
                    ' Must be formatted for genus in the first name position, and'
                    ' species in the second name position.')

args = parser.parse_args()

spaced_input = ' '.join(args.name)

species_name = ('"' + spaced_input.capitalize() + '"')

with open('bisonCSV.csv', 'w', newline='') as file:
    wr = csv.writer(file)
    wr.writerow(['scientificName','eventDate','decimalLongitude','decimalLatitude','occurrenceID','catalogNumber','institutionID'])
        
def fetch_solr(page, rows):
    start = page * rows
    params = {'q' : 'scientificName:' + species_name, 'rows' : rows, 'start' : start, 'wt' : 'json'}
    match = requests.get('https://bison.usgs.gov/solr/occurrences/select?', params=params)
    match_result = match.json()
    match.close()
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




