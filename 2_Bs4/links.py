from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

# for a_tag in soup.findAll("a"):
#         href = a_tag.attrs.get("href")
#         if href != "":
#             print(href)
#             continue


# Anchor tag
# div = soup.find('div',{'class':'col-sm-4 col-lg-4 col-md-4'})
# a = div.find('a')
# link = a.attrs.get("href")
# print(link)



## Images
# for a_tag in soup.findAll("img"):
#         href = a_tag.attrs.get("src")
#         if href != "":
#             print(href)
#             continue

# Img tag
div = soup.find('div',{'class':'col-sm-4 col-lg-4 col-md-4'})
a = div.find('img')
link = a.attrs.get("src")
print(link)