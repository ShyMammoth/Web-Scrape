import re
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
from time import sleep

# Variables
main = {}
User = []
Liked_Review = []
Disliked_Review = []


# Manually create range of pages
start_urls = ["https://www.booking.com/reviewlist.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaMkBiAEBmAEJuAEXyAEM2AED6AEBiAIBqAIDuALT4-n1BcACAQ&sid=08f6a3bf129cd820092f93b893c1a1c6&cc1=sg&dist=1&pagename=ascott-singapore-raffles-place&srpvid=0f3e456eafb1007c&type=total&rows=10&offset=0"]
for i in range(10, 600, 10):
    url = "https://www.booking.com/reviewlist.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaMkBiAEBmAEJuAEXyAEM2AED6AEBiAIBqAIDuALT4-n1BcACAQ&sid=08f6a3bf129cd820092f93b893c1a1c6&cc1=sg&dist=1&pagename=ascott-singapore-raffles-place&srpvid=0f3e456eafb1007c&type=total&rows=10&offset=20;rows={}".format(i)
    start_urls.append(url)

try:
    for index, url_created in enumerate(start_urls):
        print("Sleeping z.z.z.")
        sleep(5)
        print("Awake!")
        print("Starting {}/{}".format(index+1, len(start_urls)))
        url = url_created

        # 1 page
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request = urllib.request.Request(url,None,headers) 
        uClient = urlopen(request)
        page_html = uClient.read()
        uClient.close()
        main = {}
        page_soup = soup(page_html, "lxml")

        # Container
        containers = page_soup.findAll("li", class_ =  "review_list_new_item_block")
        for container in containers:
            try:
                tags = container.find("span", class_ =  "bui-avatar-block__title")
                user = tags.text
            except AttributeError:
                print("Unable to find user")
                user = None
               
            try:
                tags = container.find("div", class_ =  "c-review__row")
                tags1 = tags.p
                tags2 = tags1.find("span", class_ = "c-review__body")
                Liked_Review = tags2.text
            except AttributeError:
                print("Unable to find a Liked_Review")
                Liked_Review = None

            try:
                tags = container.find("div", class_ =  "c-review__row lalala")
                tags1 = tags.p
                tags2 = tags1.find("span", class_ = "c-review__body")
                Disliked_Review = tags2.text
            except AttributeError as e:
                print("Unable to find a Disliked_Review")
                Disliked_Review = None
                
            main[user] = {"Liked_Review" : Liked_Review, "Disliked_Review" : Disliked_Review}
            
        
except TimeoutError as e:
    print("RIP", e)
    with open('booking.json', 'w', encoding = 'utf8') as fp:
        json.dump(main, fp, indent = 4, ensure_ascii=False)
        
print("Completed")
with open('booking.json', 'w', encoding = 'utf8') as fp:
    json.dump(main, fp, indent = 4, ensure_ascii=False)


# Liked_Review
# tags = page_soup.find("div", class_ =  "c-review__row")
# tags1 = tags.p
# tags2 = tags1.find("span", class_ = "c-review__body")
# print(tags)

# Disliked_Review
# tags = page_soup.find("div", class_ =  "c-review__row lalala")
# tags1 = tags.p
# tags2 = tags1.find("span", class_ = "c-review__body")
# tags3 = tags2.text
# print(tags3)



# for tag in tags:
    # print(tag.p.span)
    # for index, sentence in enumerate(table):
        # temp = sentence.text.split("\n")
        # temp = [i.strip() for i in temp]
        # without_empty_strings = []
        # without_empty_strings = [string for string in temp if string != ""]
        # without_empty_strings = " ".join(without_empty_strings)
        # details[index] = without_empty_strings
        # details = {k: v for k, v in details.items() if v != ''}
        # print(details)
    # main[section] = details
# with open('Chinese.json', 'w', encoding = 'utf8') as fp:
    # json.dump(main, fp, indent = 4, ensure_ascii=False)