import scrapy
from scrapy import Request
import datetime
from scrapy_splash import SplashRequest

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    start_urls = ["http://quotes.toscrape.com/js/"]


class QuoteSpider(scrapy.Spider):
    name = 'quotes'    
    def start_requests(self):
        # for url in self.start_urls:
        yield SplashRequest("http://quotes.toscrape.com/js/", self.parse, args={'wait': 0.5})
    
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text' : quote.css("span.text::text").extract_first(),
                'author' : quote.css("small.author::text").extract_first(),
                'tags' : quote.css("div.tags > a.tag::text").extract_first()
            }