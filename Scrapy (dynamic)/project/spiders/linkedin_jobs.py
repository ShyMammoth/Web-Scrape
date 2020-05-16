import scrapy
from scrapy import Request
import datetime
from scrapy_splash import SplashRequest

class LinkedinItem(scrapy.Item):
    Date = scrapy.Field()
    Title = scrapy.Field()
    start_urls = ["https://www.linkedin.com/jobs/search/?keywords=data%20scientist"]


class LinkedinSpider(scrapy.Spider):
    name = 'linkedin_jobs'    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})
    
    def parse(self, response):
        for symbols in response.xpath('//ul[@class="jobs-search-results__list artdeco-list"]'): # Common attribute in page
            item = LinkedinItem()
            item["Date"] = datetime.datetime.today()  
            item["Title"] = symbols.xpath('//div[@class="full-width artdeco-entity-lockup__title ember-view"]/a/text()').extract_first()
            yield item