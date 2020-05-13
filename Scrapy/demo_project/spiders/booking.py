import scrapy

class BookingItem(scrapy.Item):
    User = scrapy.Field()
    Liked_Review = scrapy.Field()
    Disliked_Review = scrapy.Field()
    
class BookingSpider(scrapy.Spider):
  name = 'booking'
  start_urls = ["https://www.booking.com/reviewlist.en-gb.html?label=gen173nr-1DCAEoggI46AdIM1gEaMkBiAEBmAEJuAEXyAEM2AED6AEBiAIBqAIDuALT4-n1BcACAQ&sid=08f6a3bf129cd820092f93b893c1a1c6&cc1=sg&dist=1&pagename=ascott-singapore-raffles-place&srpvid=0f3e456eafb1007c&type=total&rows=10&offset=0"]
  
  def parse(self, response):
    for field in response.xpath('//div[@class="c-review"]'): # Common attribute in page
        item = BookingItem()
        item["User"] = field.xpath('.//a[@class = "ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"]/text()').extract_first()
        item["Liked_Review"] = field.xpath('.//div[@class="c-review__row"]/p/span[@class="c-review__body"]/text()').extract_first()
        item["Disliked_Review"] = field.xpath('.//div[@class="c-review__row lalala"]/p/span[@class="c-review__body"]/text()').extract_first()
        yield item  
      
        next_page = response.xpath('//div[@class="bui-pagination__item bui-pagination__next-arrow"]/a/@href').extract_first()
        if next_page is not None:
          next_page_link = response.urljoin(next_page)
          yield scrapy.Request(url = next_page_link, callback = self.parse)