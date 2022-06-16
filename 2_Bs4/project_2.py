from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



# def amazon(book):
#     book = book.replace(" ",'+')
#     url = f'https://www.amazon.in/s?k={book}&ref=nb_sb_noss_2'
#     print(url)

# amazon(input("Enter the book name\n"))


















# def amazon(book):
#     book = book.replace(" ",'+')
#     url = f'https://www.amazon.in/s?k=python&ref=nb_sb_noss_2'

#     res = requests.get(url,headers=headers)
#     soup = BeautifulSoup(res.text,'html.parser')
#     with open('books.csv','a',newline='') as f:
#         writer = csv.writer(f)

#         names = soup.select(".a-size-medium")
#         for i in range(len(names)):
#             lst = []
#             try:
#                 price = soup.select(".a-spacing-top-small .a-price-whole")[i].get_text().strip()
#                 if price != "":
#                     names = soup.select(".a-color-base.a-text-normal")[i].get_text().strip()
#                     link = soup.select(".a-link-normal")[i].attrs.get("href")
#             except:
#                 price = ""
#                 names = ""
#             lst = [names,price,link]
#             writer.writerow(lst)
# amazon(input("Enter the book name\n"))






















def amazon(book,num):
    book = book.replace(" ",'+')
    for i in range(num):
        url = f'https://www.amazon.in/s?k={book}&page={num}&qid=1599544528&ref=sr_pg_{num}'
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')
        with open('books.csv','a',newline='') as f:
            writer = csv.writer(f)
            names = soup.select(".a-size-medium")
            for i in range(len(names)):
                lst = []
                try:
                    price = soup.select(".a-spacing-top-small .a-price-whole")[i].get_text().strip()
                    if price != "":
                        names = soup.select(".a-color-base.a-text-normal")[i].get_text().strip()
                        link = soup.select(".a-link-normal")[i].attrs.get("href")
                except:
                    price = ""
                    names = ""
                lst = [names,price,link]
                writer.writerow(lst)
amazon(input("Enter the book name\n"),int(input("Number of pages")))