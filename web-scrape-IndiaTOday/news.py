import scrapy
from ..items import NewsData

class IndiaToday(scrapy.Spider):
    name = "news" #unchangable 
    start_urls = [
        'https://www.indiatoday.in/'
    ]

    def parse(self,response):
        data = NewsData()
        news_stories = response.xpath('//*[(@id = "block-itg-widget-top-stories-ordering")]//a/text()').extract()
        for i in range(len(news_stories)):
            data['news'] = news_stories[i]
            yield data 

