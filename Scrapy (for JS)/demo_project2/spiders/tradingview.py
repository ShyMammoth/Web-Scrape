import scrapy
from scrapy import Request
import datetime
from scrapy_selenium import SeleniumRequest

class TradingviewItem(scrapy.Item):
    Date = scrapy.Field()
    Symbol = scrapy.Field()
    Last = scrapy.Field()
    Change = scrapy.Field()
    Change_Percent = scrapy.Field()

class TradingviewSpider(scrapy.Spider):
    name = 'tradingview'
    allowed_domains = ['https://www.tradingview.com/']
    start_urls = [
    "https://www.tradingview.com/chart/aSudk8cN/"
    ]

    @classmethod
    def setUpClass(cls):
        """Create a scrapy process and a spider class to use in the tests"""
        cls.settings = {
            'SELENIUM_DRIVER_NAME': 'firefox',
            'SELENIUM_DRIVER_EXECUTABLE_PATH': which('geckodriver'),
            'SELENIUM_DRIVER_ARGUMENTS': ['-headless']
        }
        cls.spider_klass = cls.SimpleSpider
        
    def parse_result(self, response):
    # def parse(self, response):
        for symbols in response.xpath('//div[@class="listContainer-1OhjZIMS"]'): # Common attribute in page
          item = TradingviewItem()
          item["Date"] = datetime.datetime.today()  
          item["Symbol"] = symbols.xpath('.//div[@class="firstItem-1fMdZzn9 symbolName-aMd2VpDf"]/span/span/text()').extract_first()
          item["Last"] = symbols.xpath('.//span[@class="cell-2dpljH_9 last-31ae42tU"]/span/text()').extract_first()
          item["Change"] = symbols.xpath('.//span[@class="cell-2dpljH_9 change-2u7N-Juv"]/span/text()').extract_first()
          item["Change_Percent"] = symbols.xpath('.//span[@class="lastItem-2kcQWdD4 cell-2dpljH_9 changeInPercents-23LFemIM"]/span/text()').extract_first()
          yield item  
