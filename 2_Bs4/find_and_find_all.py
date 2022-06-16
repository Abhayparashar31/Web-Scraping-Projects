from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

res = requests.get(url)
#print(res)
##<Response [200]>
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)


#print(soup.find('h1').text)



















#print(soup.find('a',{'class':'tag'}).text)






#print(soup.find('div', {'class': 'tags'}))













##FIND_ALL
#print(soup.find_all('div', {'class': 'tags'}))

#rint(soup.find_all(class_="tags"))

# lst = []
# lst.append(soup.find_all(class_="tags")[0].text.replace("\n"," ").strip())
# print(lst[0])

##Tags:    change deep-thoughts thinking world



tags = soup.find_all(class_="tags")
lst = []
for tag in tags:
    lst.append(tag.text.replace("\n"," ").strip())
lst2 = [tag.replace("  ","") for tag in lst]
print(lst2)