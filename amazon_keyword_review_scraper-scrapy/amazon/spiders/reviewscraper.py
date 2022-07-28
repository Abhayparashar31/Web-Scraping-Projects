import scrapy
from twisted.internet import reactor, defer
from ..items import AmazonItem 

class Amazonlinkscraper(scrapy.Spider):
    name = "amazonkeywordreviews"
    asin_numbers = [] 
    query = input("Enter The Keyword You Want Reviews For \n")
    first_part = query.replace(" ","-")
    second_part = query.replace(" ","+")
    url = f'https://www.amazon.in/{first_part}/s?k={second_part}'
    import sys    
    if "twisted.internet.reactor" in sys.modules:
        del sys.modules["twisted.internet.reactor"]
    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse_product_lists)


    def parse_product_lists(self,response):
        products = response.xpath('//*[@data-asin]')

        for product in products:
            asin = product.xpath('@data-asin').extract_first()
            if asin!="":
                product_url = f'https://www.amazon.in/product-reviews/{asin}/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&pageNumber=1'
                yield scrapy.Request(url=product_url, callback=self.parse_product_page, meta={'asin': asin})

        try:
            next_page_url = "https://www.amazon.com"+response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "s-pagination-next", " " ))]/@href')[0].extract()
            if next_page_url is not None:
                yield response.follow(next_page_url, callback=self.parse_product_lists) 
        except:
            print("All Products Scraped !!!!")

    def parse_product_page(self, response):
        items = AmazonItem()

        div = response.css('#cm_cr-review_list')
        ratings = div.css('.review-rating')
        reviews = div.css('.review-text')
        
        for i in range(len(ratings)):
            rating= ''.join(ratings[i].xpath('.//text()').extract())
            review=(''.join(reviews[i].xpath('.//text()').extract())).replace('\n',"").strip()

            items['review'] = review
            items['rating'] = rating

            yield items

        next_page_url = "https://www.amazon.in"+response.xpath('//li[@class="a-last"]/a/@href')[0].extract()
                        # Common URL In ALL web Pages                       ## Xpath For Next Button (Return The page number(page-3.html, page-4.html,etc))
        try:
            if next_page_url is not None:
                yield response.follow(next_page_url, callback=self.parse_product_page)
                        #Follwing Links          ## callback to parse function to scrape that data again.
        except:
            print("all page scraped !!!")      