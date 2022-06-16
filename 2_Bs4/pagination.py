from bs4 import BeautifulSoup
import requests

# url = "http://quotes.toscrape.com/"
# res = requests.get(url)
# soup = BeautifulSoup(res.text,'html.parser')
# quotess = []
# quotes = soup.find_all('span', {'class': 'text'})
# for quote in quotes:
#     quotess.append(quote.text)
# for quote in quotess:
#     print(quote)














def quote_scrape(url):
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    quotess = []
    quotes = soup.find_all('span', {'class': 'text'})
    for quote in quotes:
        quotess.append(quote.text)
    for quote in quotess:
        print(quote)

if __name__ == "__main__":

    upper = 5
    for num in range(1,upper+1):
        url = f"http://quotes.toscrape.com/page/{num}/"
        quote_scrape(url)