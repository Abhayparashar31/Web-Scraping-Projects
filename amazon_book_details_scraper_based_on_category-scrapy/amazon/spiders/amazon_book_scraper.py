from os import link
import scrapy
from ..items import AmazonItem  
import pandas as pd


## https://pypi.org/project/scrapy-user-agents/

class Amazonbookscraper(scrapy.Spider):
    name = "amazonbooks"
    query = input("Please Enter The Name of Your Book Category \n")
    first_part = query.replace(" ","-")
    second_part = query.replace(" ","+")
    url = f'https://www.amazon.com/{first_part}/s?k={second_part}'

    start_urls = [
        url
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
            items['price']=str(price)+'$'
            items['author']=author
            items['rating']=rating
        
            yield items
        

        try:    

            next_page_url = "https://www.amazon.com"+response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-pagination-next", " " ))]/@href')[0].extract()
            if next_page_url is not None:
                yield response.follow(next_page_url, callback=self.parse)
        except:
            print("All Pages Scraped !!!!")

    