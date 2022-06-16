'''
Websites:-
▶ https://quotes.toscrape.com/ 
▶ https://webscraper.io/test-sites/e-commerce/allinone
'''
########################################################
######################## BASICS ########################
########################################################
'''### Scraping Data From HTML Pages
from requests_html import HTML
with open("simple.html") as html_file:
    source  = html_file.read()
    html = HTML(html=source)

match = html.find('title') ## List of elements ## Find method looks for a CSS Selector
#match = html.find('title', first=True) ## Only the first element

#print(match[0].text) ## To View the text
#print(match[0].html) ## To View The HTML

### Scraping data thew classes and IDs
heading  = html.find('.heading')
#print(heading[0].text)


### Tag with an selector (class,ID)
summary = html.find('div.summary .heading2', first=True)
print(summary.text)

'''



############################################################
######################### PROJECT 1 ########################
############################################################

from requests_html import HTML,HTMLSession

session = HTMLSession()
r = session.get("https://quotes.toscrape.com/")

#print(r.html)

quotes = r.html.find('.text')
quotes_list = [quote.text for quote in quotes]

authors = r.html.find('.author')
authors_list = [author.text for author in authors]

data = {"Authors":authors_list,"Quotes":quotes_list}

for i in range(len(quotes_list)):
    print(data['Authors'][i], data['Quotes'][i], end='\n')


