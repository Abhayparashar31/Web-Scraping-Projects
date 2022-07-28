from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def scrape(url):    
    res = requests.get(url,headers=headers)
    print("\nSearching in Goodreads......")
    soup = BeautifulSoup(res.text,'html.parser')

    quote = soup.select('.quoteText')
    length = len(quote)
    for i in range(0,length):
        quote = soup.select('.quoteText')[i].getText().strip()
        quote = quote.replace("―","Author:")
        quote = quote.replace("\n","")
        print("\n"+quote)

for i in range(0,10):
    url = f'https://www.goodreads.com/quotes?page={i}'
    scrape(url)