import requests
import urllib.request
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import webbrowser

url = "https://bison.usgs.gov/api/search.json?species=Bison%20bison%type=scientific_name&start=0&count=1"

#webbrowser.open(url)

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

soup = BeautifulSoup(html, 'html.parser')
print(soup.content)
