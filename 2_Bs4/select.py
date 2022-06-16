from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
#print(res)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)


#print(soup.select('p'))

#print(soup.select('.title').get_text())










## Scrape all three product details
name = soup.select(".title")
for i in range(0,len(name)):
    price = soup.select(".price")[i].text
    name = soup.select(".title")[i].get_text()
    description = soup.select(".description")[i].get_text()
    print(name)
    print(description)
    print(price,end="\n\n")