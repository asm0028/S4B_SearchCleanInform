import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://explorer.natureserve.org'
response = requests.get(url, params={'q': 'sus+scrofa'},)
print(response) #response 200 means our request to access went through
##Could add in future: error handling for if the url is wrong?

#soup = BeautifulSoup(response, features="lxml")
#print(soup)
#soup.findAll
