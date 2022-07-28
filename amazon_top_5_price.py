from bs4 import BeautifulSoup
import requests
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
amazon=''

def amazon(name):
    global amazon
    name1 = name.replace(" ","-")
    name2 = name.replace(" ","+")
    amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
    print(amazon)
    res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
    print("\nSearching in amazon:")
    soup = BeautifulSoup(res.text,'html.parser')
    num = int(input("How many products you want to search"))
    for i in range(0,num):
        amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
        amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
        amazon_desc = soup.select('.aok-align-bottom')[i].getText().strip().upper()
        amazon_delivery = soup.select('.s-align-children-center')[i].getText().strip().upper()
        print("Amazon:")
        print(amazon_name)
        print(amazon_price)
        print(amazon_desc)
        print(amazon_delivery)


amazon(input("Product name\n"))