import scrapy
import datetime

class RiceItem(scrapy.Item):
    Date = scrapy.Field()
    Brand = scrapy.Field()
    Details = scrapy.Field()
    Quantity = scrapy.Field()
    Price = scrapy.Field()

class RiceSpider(scrapy.Spider):
  name = 'rice'
  start_urls = [
    # "https://www.fairprice.com.sg/search?query=rice",
    "https://giant.sg/food-pantry/rice",
    "https://giant.sg/food-pantry/rice/?Product_page=2",
    "https://giant.sg/food-pantry/rice/?Product_page=3"
    ]

  def parse(self, response):
    for rice in response.xpath('//div[@class="col-lg-2 col-md-4 col-6 col_product open-product-detail algolia-click"]'): # Common attribute in page
      item = RiceItem()
      item["Date"] = datetime.datetime.today()
      item["Brand"] = rice.xpath('.//div[@class="category-name"]/a/text()').extract_first()
      item["Details"] = rice.xpath('.//div[@class="product_name "]/a/text()').extract_first()
      item["Quantity"] = rice.xpath('.//div[@class="product_desc"]/span/text()').extract_first()
      item["Price"] = rice.xpath('.//div[@class="price_now f-green price_normal product-price"]/text()').extract_first()
      yield item  
