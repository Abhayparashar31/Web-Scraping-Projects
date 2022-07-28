from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def search(url):   
    res = requests.get(url,headers=headers)
    print("\nSearching for history....\n")
    print("Things happens today...\n")
    soup = BeautifulSoup(res.text,'html.parser')
    length = len(soup.select('.event'))
    for i in range (0,length):
        history = soup.select('.event')[i].getText().strip()
        print(history)

url = 'https://www.onthisday.com/'
search(url)
while True:
    user = input("\nWnat to search for a specific date\n").upper()
    if user =='YES':
        date = int(input("Enter the date"))
        month = str(input("Enter the month name"))
        url = f'https://www.onthisday.com/day/{month}/{date}'
        search(url)

    else:
        print("\nok! Have a Nice Day")
        break
