import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import webbrowser

url = "https://bison.usgs.gov/api/search.json?species=Bison bison%type=scientific_name&start=0&count=1"

#webbrowser.open(url)

page = session.get(url)
print(page.content)
