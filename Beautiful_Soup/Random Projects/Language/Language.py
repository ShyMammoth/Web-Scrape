import re
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from copy import deepcopy
import json

# All section
url = 'http://englishspeak.com/zh-cn/english-phrases?category_key=1'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 
request = urllib.request.Request(url,None,headers) 
uClient = urlopen(request)
page_html = uClient.read()
uClient.close()
main = {}
page_soup = soup(page_html, "lxml")
tags = page_soup.find("div", {"class": "col-sm-12"}).findAll('a')

# Per section
for tag in tags:
    details = {}
    print(tag.text)
    section = tag.text.strip()
    href =  'http://englishspeak.com' + tag.get('href').strip()
    details["Link"] = href
    # Enter individual section
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request = urllib.request.Request(href,None,headers)
    uClient = urlopen(request)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "lxml")
    table = page_soup.find("table", {"class": "table table-striped"}).findAll('td')
    
    for index, sentence in enumerate(table):
        temp = sentence.text.split("\n")
        temp = [i.strip() for i in temp]
        without_empty_strings = []
        without_empty_strings = [string for string in temp if string != ""]
        without_empty_strings = " ".join(without_empty_strings)
        details[index] = without_empty_strings
        details = {k: v for k, v in details.items() if v != ''}
        print(details)
    main[section] = details
with open('Chinese.json', 'w', encoding = 'utf8') as fp:
    json.dump(main, fp, indent = 4, ensure_ascii=False)