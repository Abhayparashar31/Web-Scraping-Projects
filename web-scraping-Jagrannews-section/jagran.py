import scrapy
from ..items import Jagran

class jagran(scrapy.Spider):
    name = "jagran" #unchangable 
    page_number = 2
    start_urls = [
        'https://english.jagran.com/latest-news'
    ]

    def parse(self,response):
        data = Jagran()
        news_stories = response.css('#ls-row-3-area-1 .h3::text').extract()
        for i in range(len(news_stories)):
            data['news'] = news_stories[i]
            data['link'] = response.css(".topicList a").xpath("@href")[i].extract()
            yield data 

        next_page = 'https://english.jagran.com/technology-page'+str(jagran.page_number)

        if jagran.page_number <= 36:
            jagran.page_number += 1

            yield response.follow(next_page, callback = self.parse)

