import scrapy
from ..items import BookscraperItem                                                ## Importing The Class Inside Items.py for storing data

class Bookscraper(scrapy.Spider):
    name='books'                                                                    ## Name of Spider
    counter = 1                                                                     ## Counter Variable To Check The Status of Scraped Pages

    def start_requests(self):
       

        urls = [
            'https://books.toscrape.com/catalogue/page-1.html'                      ## Index Page URL 
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)                      ## Requesting For Source Code For Both The Pages
    def parse(self, response):
        titles = response.css("h3 a::text").extract()                               ## Scraping Titles
        prices = response.css("div p.price_color::text").extract()                  ## Scraping Prices
        ratings = response.xpath("//article/p/@class").extract()                    ## Scraping Ratings Class
        ratings = [rating.replace("star-rating ","") for rating in ratings]         ## Configuring Ratings By Extracting The Rating From The Class Name and replacing everything else with an empty space
        links = response.xpath('//h3/a/@href').extract()                            ## Scraping Links
        links = [f"http://books.toscrape.com/{link}" for link in links]             ## Configuring Links 
        items = BookscraperItem()
        
        for row in list(zip(titles,prices,links,ratings)):                          ## Loop To Extract Each Element From The List of Elements
            title,price,link,ratings = row       
            items['title'] = title                                                  ## Storing title in temporary item container
            items['price'] = str(price)
            items['link'] = link
            items['rating'] = ratings

            yield items                                                             ## Output
       
        ## Simple Counter To Check The Status of Scraped Pages
        print(f'\n######################################  Page {self.counter} Scraped !!!! #########################\n')
        self.counter=self.counter+1                                                 ## Increasing Counter Value Every Time Script Scraped a Web Page

        next_page_url = "http://books.toscrape.com/catalogue/"+(response.xpath('//li[@class="next"]/a/@href')[0].extract())
                         ## Common URL In ALL web Pages                       ## Xpath For Next Button (Return The page number(page-3.html, page-4.html,etc))
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)
                     ## Follwing Links          ## callback to parse function to scrape that data again.          
        