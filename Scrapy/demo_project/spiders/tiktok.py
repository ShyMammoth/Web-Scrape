import scrapy
import datetime
import json

class TiktokItem(scrapy.Item):
    date = scrapy.Field()
    name = scrapy.Field()
    DisplayUnit = scrapy.Field()
    mrp = scrapy.Field()

class TiktokSpider(scrapy.Spider):
    name = 'fairprice'
    start_urls = ["https://website-api.omni.fairprice.com.sg/api/product?includeTagDetails=true&page=1&pageType=search&q=rice&query=rice&storeId=165&url=rice&sourceHash=7b7bcff0-9724-11ea-a4ea-d1ca4a53facd"]
    for i in range(2,48):
        start_urls.append("https://website-api.omni.fairprice.com.sg/api/product?includeTagDetails=true&page={}&pageType=search&q=rice&query=rice&storeId=165&url=rice&sourceHash=8065bf30-9724-11ea-a4ea-d1ca4a53facd".format(i))
   
    def parse(self, response):
        jsonresponse = json.loads(response.text)
        item = TiktokItem()
        # with open("fairprice_ref.json", "w") as outfile:
            # json.dump(jsonresponse, outfile, indent=4, separators=(',',':'))
        for rice in jsonresponse["data"]["product"]: # Common attribute in page
            item["date"] = datetime.datetime.today()
            item["name"] = rice["name"]
            item["DisplayUnit"] = rice["metaData"]["DisplayUnit"]
            item["mrp"] = rice["storeSpecificData"][0]["mrp"]
            yield item  
