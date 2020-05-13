import scrapy

class TripAdvisorItem(scrapy.Item):
    User = scrapy.Field()
    Date = scrapy.Field()
    Rating = scrapy.Field()
    Review_Title = scrapy.Field()
    Review = scrapy.Field()
    
class TripAdvisorSpider(scrapy.Spider):
  name = 'tripadvisor'
  start_urls = ["https://www.tripadvisor.com.sg/Hotel_Review-g294265-d1083872-Reviews-Ascott_Raffles_Place_Singapore-Singapore.html"]
  for i in range(5, 480, 5): # Change range appropriately to reflect end of page
    start_urls.append("https://www.tripadvisor.com.sg/Hotel_Review-g294265-d1083872-Reviews-or{}-Ascott_Raffles_Place_Singapore-Singapore.html#REVIEWS".format(i)) 

  def parse(self, response):
    for field in response.xpath('//div[@class = "hotels-community-tab-common-Card__card--ihfZB hotels-community-tab-common-Card__section--4r93H"]'): # Common attribute in page
        item = TripAdvisorItem()
        item["User"] = field.xpath('.//a[@class = "ui_header_link social-member-event-MemberEventOnObjectBlock__member--35-jC"]/text()').extract_first()
        item["Date"] = field.xpath('.//div[@class = "social-member-event-MemberEventOnObjectBlock__event_type--3njyv"]/span/text()').extract_first()
        item["Rating"] = field.xpath('.//div[@class = "location-review-review-list-parts-RatingLine__bubbles--GcJvM"]/span/@class').extract_first()
        item["Review_Title"] = field.xpath('.//div[@class = "location-review-review-list-parts-ReviewTitle__reviewTitle--2GO9Z"]/a/span/span/text()').extract_first()
        item["Review"] = field.xpath('.//q[@class = "location-review-review-list-parts-ExpandableReview__reviewText--gOmRC"]/span').extract_first()
        yield item  