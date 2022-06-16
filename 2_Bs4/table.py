from bs4 import BeautifulSoup
import requests
import csv
url = 'https://webscraper.io/test-sites/tables'

res = requests.get(url)
#print(res)
soup  = BeautifulSoup(res.text,'html.parser')






# Table 1(thead and tbody)

# table = soup.select('.table')[0]
# table_header = table.find('thead').find_all('th')
# with open('table.csv','a',newline='') as f:
#     writer = csv.writer(f)
#     header = []

#     for th in table_header:
#         header.append(th.text)
#     #print(header)
#     writer.writerow(header)

#     for row in table.find_all('tr'):
#         body = []
#         for data in row.find_all('td'):
#                 body.append(data.text)
#                 print(body)
#         writer.writerow(body)












# Table 2(without thead)

# table = soup.select('.table')[2]
# with open('table.csv','a+',newline='') as f:
#     writer = csv.writer(f)  
#     for row in table.find_all('tr'):
#         csvRow = []
#         for data in row.find_all('th'):
#             csvRow.append(data.text)
#         for data in row.find_all('td'):
#             csvRow.append(data.text)
        
#         writer.writerow(csvRow)











# Table 3 (multiple header rows and an empty data row)

table = soup.select('.table')[3]
with open('table.csv','a+',newline='') as f:
    writer = csv.writer(f)  
    for row in table.find_all('tr'):
        csvRow = []
        for data in row.find_all('th'):
            csvRow.append(data.text)
        for data in row.find_all('td'):
            csvRow.append(data.text)
        print(csvRow)
        writer.writerow(csvRow)