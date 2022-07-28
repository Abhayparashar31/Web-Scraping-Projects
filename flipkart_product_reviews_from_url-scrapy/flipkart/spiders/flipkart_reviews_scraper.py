import scrapy
from ..items import FlipkartItem
import pandas as pd

class Flipkartreviewscraper(scrapy.Spider):
    name = "flipkartreviews"
    counter = 1   
    
    allowed_domains = ['flipkart.com']
    url = input("Paste Your Product URL \n")
    start_urls = [url]

    def parse(self, response):
        # This will get the link for the all reviews tag on amazon page.
        all_reviews = response.xpath('//div[@class="col JOpGWq"]/a/@href').extract_first()
        # This will tell scrapy to move to all reviews page for further scraping.
        yield response.follow("https://www.flipkart.com"+all_reviews, callback=self.parse_flipkart_review)

    def parse_flipkart_review(self,response):
        items = FlipkartItem()

        try:
            reviews = response.xpath('//*[@class="t-ZTKy"]/div/div')
            ratings = response.xpath('//*[@class="_3LWZlK _1BLPMq"]')
            
            for i in range(len(ratings)):
                review = ''.join(reviews[i].xpath('./text()').extract()).replace('\n',"").strip()
                rating = ''.join(ratings[i].xpath('./text()').extract())
                
                items['review'] = review
                items['rating'] = rating
            
                yield items

            print(f'########################## Page {self.counter} Scraped !!! ###########')
            self.counter=self.counter+1
        
        except:
            print(f"Nothing Found On The Page {self.counter}")
            self.counter=self.counter+1

  
        page = response.xpath('//nav/a[@class="_1LKTO3"]//text()')[0].extract()
        if page=='Next':
            next_page_url = "https://www.flipkart.com"+response.xpath('//nav/a[@class="_1LKTO3"][1]/@href')[0].extract()
        else:
            next_page_url = "https://www.flipkart.com"+response.xpath('//nav/a[@class="_1LKTO3"][2]/@href')[0].extract()
        
        print(next_page_url,"\n")

        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse_flipkart_review)






