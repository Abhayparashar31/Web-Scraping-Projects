from os import link
from matplotlib.pyplot import title
import scrapy
from ..items import AmazonItem  

## https://pypi.org/project/scrapy-user-agents/

class Amazonbookscraper(scrapy.Spider):
    name = "amazonbooks"

    start_urls = [
        "https://www.amazon.com/s?k=python+programming&page=1&crid=YZEI0VGEO20K&qid=1644079860&sprefix=python+programming&ref=sr_pg_2"
    ]
    
    def parse(self, response):
        items = AmazonItem()
        titles = response.css('.a-size-base-plus::text').extract()
        prices = response.css('.a-price-whole::text').extract()
        authors = response.css('.a-color-secondary .a-size-base+ .a-size-base::text').extract()
        ratings = response.css('.s-link-style .s-underline-text::text').extract()

        for i in list(zip(titles,prices,authors,ratings)):
            title,price,author,rating = i
            items['title']=title
            items['price']=price
            items['author']=author
            items['rating']=rating
        
            yield items

        next_page_url = "https://www.amazon.com"+response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-pagination-next", " " ))]/@href')[0].extract()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)


    