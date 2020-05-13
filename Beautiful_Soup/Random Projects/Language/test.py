import re
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from copy import deepcopy
import json

url = 'http://englishspeak.com/fr/english-phrases?category_key=1'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
request = urllib.request.Request(url,None,headers) #The assembled request
uClient = urlopen(request)
page_html = uClient.read()
uClient.close()
main = {}
page_soup = soup(page_html, "lxml")
# containers = page_soup.find("table", {"class": "table table-striped"}).findAll('p')
containers = page_soup.find("table", {"class": "table table-striped"}).findAll('td')

for i, container in enumerate(containers):
    temp = container.text.split("\n")
    temp = [i.strip() for i in temp]
    without_empty_strings = [string for string in temp if string != ""]
    without_empty_strings = " ".join(without_empty_strings)
    main[i] = without_empty_strings
    main = {k: v for k, v in main.items() if v != ''}

print(main)

    
