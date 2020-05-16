import scrapy
from scrapy import Request
import json
import base64
import scrapy
from scrapy_splash import SplashRequest


class LinkedinItem(scrapy.Item):
    Date = scrapy.Field()
    Title = scrapy.Field()
    start_urls = ["https://www.linkedin.com/jobs/search/?keywords=data%20scientist"]
    
class LinkedinSpider(scrapy.Spider):
    name = 'html_contents'    
    def start_requests(self):
        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.json',
                                args=splash_args)    
                                
    def parse_result(self, response):
        # magic responses are turned ON by default,
        # so the result under 'html' key is available as response.body
        html = response.body

        # you can also query the html result as usual
        title = response.css('title').extract_first()

        # full decoded JSON data is available as response.data:
        png_bytes = base64.b64decode(response.data['png'])
        
        yield html

    # def parse(self, response):
        # for symbols in response.xpath('//ul[@class="jobs-search-results__list artdeco-list"]'): # Common attribute in page
            # item = LinkedinItem()
            # item["Date"] = datetime.datetime.today()  
            # item["Title"] = symbols.xpath('//div[@class="full-width artdeco-entity-lockup__title ember-view"]/a/text()').extract_first()
            # yield item