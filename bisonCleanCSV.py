
import argparse
import csv
import shutil
import os

parser = argparse.ArgumentParser()

parser.add_argument('-e', '--evt', help='Removes all data without event date', action='store_true')
parser.add_argument('-a', '--lat', help='Removes all data without latitudes', action='store_true')
parser.add_argument('-g', '--lng', help='Removes all data without longitudes', action='store_true')
parser.add_argument('-o', '--occ', help='Removes all data without occurrence ID', action='store_true')
parser.add_argument('-c', '--cat', help='Removes all data without catalog number', action='store_true')
parser.add_argument('-i', '--ins', help='Removes all data without institution ID', action='store_true')

args = parser.parse_args()

shutil.copy('bisonCSV.csv','bisonCSV.cleaned.csv')

def action(column):
        input = open('bisonCSV.cleaned.csv', 'r')
        output = open('bisonCSV.cleaned.int.csv', 'w')
        wr = csv.writer(output)
        for row in csv.reader(input):
            if row[column] != '-':
                wr.writerow(row)
        input.close()
        output.close()
        os.rename('bisonCSV.cleaned.int.csv', 'bisonCSV.cleaned.csv')

n = 1
for x in [args.evt, args.lng, args.lat, args.occ, args.cat, args.ins]:
    if x is True:
        action(n)
        n = n + 1
    else:
        n = n + 1
        pass
