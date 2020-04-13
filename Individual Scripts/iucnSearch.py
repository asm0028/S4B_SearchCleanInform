import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import webbrowser

search_url = "https://www.iucnredlist.org/search?query="
query = "sus%20scrofa"
species_term = "&searchType=species"

#webbrowser.open(search_url+query+species_term) #uncomment to test that url is correct

session = HTMLSession()

page = session.get("https://www.iucnredlist.org/search?query=sus%20scrofa&searchType=species")
#print(page.content)
page.html.render()
#print(page.content)
soup = BeautifulSoup(page.content, features='lxml')
print(soup)
print(soup, prettify()) #not sure why prettify doesn't work

redlist_results = soup.find(id='redlist-js')
content_test = soup.find(id='content')
#print("redlist test: " + str(redlist_results))
#print("content test: " + str(content_test))
