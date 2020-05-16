import scrapy
from scrapy.loader import ItemLoader
import datetime
import os

class TiktokItem(scrapy.Item):
    date = scrapy.Field()
    user = scrapy.Field()
    like_count = scrapy.Field()
    comment_count = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    
class TiktokSpider(scrapy.Spider):
    name = "tiktok"
    directory = os.path.join(os.getcwd(), "tiktok\spiders\Find links\careforsg.txt")
    f = open(directory)
    start_urls = f.read().splitlines() 
    f.close()

    def parse(self, response):
        item = TiktokItem()
        for link in response.xpath('//div[@class="jsx-4197545929 video-card-big detail-mode"]'):
            item["date"] = datetime.datetime.today()
            item["user"] = link.xpath('//div[@class="jsx-1195476613 user-info"]/a/h2[1]/text()').extract_first()
            item["like_count"] = link.xpath('//span[@class="jsx-319872377 action-wrapper like-part disable"]/strong/text()').extract_first()
            item["comment_count"] = link.xpath('//span[@class="jsx-319872377 action-wrapper disable"]/strong/text()').extract_first()
            loader = ItemLoader(item=TiktokItem(), selector = link)
            relative_url = response.xpath('//video[@class="jsx-3382097194 horizontal video-player"]/@src').extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            yield loader.load_item()
            # item
            # , 
# //div[@class="jsx-1195476613 user-info"]/a[@class="user-avatar"]/@href