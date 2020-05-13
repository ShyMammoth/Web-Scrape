import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from copy import deepcopy
import json

# All companies
url = 'http://cmtda.com/pagefiles/distributors.php'
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()
companies = {}
page_soup = soup(page_html, "lxml")
containers = page_soup.find("section", {"class": "container page-content"}).findAll('a', {'href': re.compile(r'(distributor\.php\?dID=)')})

# Individual company
for container in containers:
    details = {}
    contacts = ""
    company = container.text.strip()
    href =  'http://cmtda.com/pagefiles/' + container.get('href').strip()
    details["Link"] = href
    company_url = href
    # Enter individual company
    uClient = urlopen(company_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "lxml")
    particulars = page_soup.find("div", {"class": "eight columns"}).findAll('li')
    for index, particular in enumerate(particulars): # Dictionary for individual company 
        if particular.attrs["class"] == ["arrow2"] and  index == 0:
            details["Address"] = particular.text.strip('<br/>').replace("\r\n", " ")
        elif particular.attrs["class"] == ["arrow2"] and  index == 1:
            details["Telephone"] = particular.text
        elif particular.attrs["class"] == ["arrow2"] and  index == 2:
            details["Fax"] = particular.text
        elif particular.attrs["class"] == ["arrow2"] and  index == 3:
            details["Email"] = particular.text
        elif particular.attrs["class"] == ["arrow2"] and  index == 4:
            details["Website"] = particular.text
        else:
            contacts += particular.text + ", "
            details["Contacts"] = contacts.rstrip(", ")
        companies[company] = {"Details": details}  # Collate dictionary into master dictionary
    print(details)
    
# Write 
with open('Canadian Machine Tool Distributors Association.json', 'w') as fp:
    json.dump(companies, fp, indent = 4, ensure_ascii=True)