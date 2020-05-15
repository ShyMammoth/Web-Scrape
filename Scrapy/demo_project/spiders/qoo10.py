import scrapy

class Qoo10Item(scrapy.Item):
    Item = scrapy.Field()
    Price = scrapy.Field()
    Rating = scrapy.Field()

    
class Qoo10Spider(scrapy.Spider):
  name = 'qoo10'
  start_urls = ["https://www.qoo10.sg/s/FACE-MASKS?keyword=face+masks&keyword_auto_change="]
  for i in range(2,306): # Change range appropriately to reflect end of page
    start_urls.append("https://www.qoo10.sg/gmkt.inc/Search/DefaultAjaxAppend.aspx?search_keyword=face%20masks&search_type=SearchItems&f=&st=SG&s=r&v=lt&p={}&pm=&so=&cc=N&cb=N&___cache_expire___=1589544554716".format(i)) 

  def parse(self, response):
    for field in response.xpath('//body/table/tbody'): # Common attribute in page
        item = Qoo10Item()
        item["Item"] = field.xpath('.//div[@class="sbj"]/a/@title').extract_first()
        item["Price"] = field.xpath('.//strong[@title="Discounted Price"]/text()').extract_first()
        item["Rating"] = field.xpath('.//span[@class="rate_v"]/span/text()').extract_first()

        yield item  