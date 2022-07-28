# '''
# https://www.youtube.com/watch?v=9BQ353Yu1D0
# '''

from autoscraper import AutoScraper
from csv import writer
## Target URL
url  = 'https://quotes.toscrape.com/'

## Web Element Text
wanted_list = ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”','Albert Einstein']

## Scraping The Base Page
scraper = AutoScraper()
scraper.build(url, wanted_list)

# scraper.set_rule_aliases({'rule_bx31':'Quotes','rule_mx9a':'Authors'})
# scraper.keep_rules(['rule_bx31','rule_mx9a'])

# scraper.save('quote_scraper-rule')
# scraper.load('quote-scraper-rule')


pages = 10

for page in range(1,pages+1):
    data = scraper.get_result_similar(f'https://quotes.toscrape.com/page/{page}/',group_by_alias=True)
    print(data)