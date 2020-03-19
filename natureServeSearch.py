import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import webbrowser

searchbar_url = 'https://explorer.natureserve.org/Search?q='
query = 'sus%20scrofa'

session = HTMLSession()

page = session.get(searchbar_url+query)
#webbrowser.open(searchbar_url+query)
rendered = page.html.render()
#results = page.html.find('#resultsSection')
#print(results)
#results.attrs
#query_search = page.html.search('Sus Scrofa')
#print(query_search)
#print(page.content)

species_result = rendered.html.find('a', containing='Taxon')
print(species_result)
#results = page.html.search('top-line')
#print(results)
#page = requests.get(url)
#print(page.content)
#response = requests.get(url, params={'q': 'sus+scrofa'},)
#print(response) #response 200 means our request to access went through
##Could add in future: error handling for if the url is wrong?

#soup = BeautifulSoup(page.content, 'html.parser')
#results = soup.find(id='resultsSection')
#print(soup.prettify())
#print(results.prettify())
#print(soup)
#soup.findAll
