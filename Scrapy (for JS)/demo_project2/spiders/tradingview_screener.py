import scrapy
from scrapy import Request
import datetime
from scrapy_selenium import SeleniumRequest

class TradingviewScreenerItem(scrapy.Item):
    Date = scrapy.Field()
    Symbol = scrapy.Field()
    Last = scrapy.Field()
    # Change = scrapy.Field()
    # Change_Percent = scrapy.Field()

class TradingviewSpider(scrapy.Spider):
    name = 'tradingview_screener'
    start_urls = ["https://www.tradingview.com/crypto-screener/"]
    
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait":3})
    
    
    def parse_result(self, response):
    # def parse(self, response):
        # container = response.xpath('//tbody[@class="tv-data-table__tbody"]')
        for symbols in response.xpath('//tbody[@class="tv-data-table__tbody'): # Common attribute in page
            # if container == None:
                # continue
            item = TradingviewScreenerItem()
            item["Date"] = datetime.datetime.today()  
            item["Symbol"] = symbols.xpath('.//div[@class="tv-screener-table__symbol-right-part"]/a/text()').extract_first()
            item["Last"] = symbols.xpath('.//td[@class="tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--with-marker"]/span/text()').extract_first()
            # item["Change"] = symbols.xpath('.//span[@class="cell-2dpljH_9 change-2u7N-Juv"]/span/text()').extract_first()
            # item["Change_Percent"] = symbols.xpath('.//span[@class="lastItem-2kcQWdD4 cell-2dpljH_9 changeInPercents-23LFemIM"]/span/text()').extract_first()
            yield item  s
