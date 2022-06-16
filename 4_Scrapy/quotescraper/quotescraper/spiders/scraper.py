import scrapy
from ..items import QuotescraperItem

class Quotescraper(scrapy.Spider):
    name = 'quotes'
    counter = 1                                                                     ## Counter Variable To Check The Status of Scraped Pages
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        quotes = response.xpath('//span[@class="text"]/text()').extract()
        authors = response.css('small.author::text').extract()
        
        items = QuotescraperItem()
        items['author']=authors
        items['quote']=quotes

        yield items
         ## Simple Counter To Check The Status of Scraped Pages
        print("#####################################################################################")
        print(f'######################################  Page {self.counter} Scraped !!!! #########################')
        print("#####################################################################################")
        self.counter=self.counter+1        


        next_page_url = "https://quotes.toscrape.com"+response.xpath('//li[@class="next"]/a/@href')[0].extract()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)