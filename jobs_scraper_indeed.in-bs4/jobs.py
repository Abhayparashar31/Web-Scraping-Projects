from bs4 import BeautifulSoup #pip install bs4
import requests #pip install requests

name = input("Job name:\n").replace(" ","-")
city = input("City name:\n")
state = input("State name:\n")
res = requests.get(f'https://www.indeed.com/{name}-jobs-in-{city},-{state}')  
soup = BeautifulSoup(res.text,'html.parser')
print(soup)
job_name = soup.select('.jobtitle')
for i in range(len(job_name)):
    job_name = soup.select('.jobtitle')[i].getText()
    job_n = soup.select('.company')[i].getText()
    job_b = soup.select('.location')[i].getText()
    try :
        job_money = soup.select(".salaryText")[i].getText()
    except :
        job_money = ""
    print(job_name)
    print(job_n)
    print(job_b)
    print(job_money)