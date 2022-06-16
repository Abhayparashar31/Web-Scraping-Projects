from bs4 import BeautifulSoup
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



def amazon(url):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    
    name = soup.select("#title")[0].getText().strip()
    








    details = [soup.select('#feature-bullets .a-list-item')[i].get_text().strip() for i in range(0,len(soup.select('#feature-bullets .a-list-item')))]
    
    try:
        price = soup.select("#priceblock_ourprice")[0].getText().strip()
    except:
        price = soup.select("#priceblock_dealprice")[0].getText().strip()
    #print(f"{name} with a price of {price}")
    
    
    
    
    
    
    
    
    
    
    print(f"\n{name}\n {price}")
    for detail in details:
        print(detail,end="\n")


amazon(input("Enter the url\n"))