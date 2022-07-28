from bs4 import BeautifulSoup
import requests
import time
import random
import time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
google=''

def google(name):
    global google
    name2 = name.replace(" ","+")
    google=f'https://www.google.com/search?q={name2}&oq={name2}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'
    res = requests.get(f'https://www.google.com/search?q={name2}&oq={name2}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google......\n")
    soup = BeautifulSoup(res.text,'html.parser')
    try:
        try:
            ans=soup.select('.e24Kjd')[0].getText().strip().upper()
            print("Google says:")
            print(ans)
        except:
            try:
                ans = soup.select('.RqBzHd')[0].getText().strip().upper()
                print("Google says:")
                print(ans)
            except:
                ans=soup.select('.kno-rdesc span')[0].getText().strip().upper()
                print("Google says:")
                print(ans) 
    except:
        print("Not a query")
        link = soup.select('.r')[0].getText().strip().upper()
        print("Visit: ",link)


google(input("What is your query?\n"))

def jokes():
    res = requests.get(f'https://fungenerators.com/random/joke',headers=headers)
    print("Looking for a joke\n")
    soup = BeautifulSoup(res.text,'html.parser')
    title=soup.select('h3.text-muted')[0].getText().strip()
    joke=soup.select('p')[0].getText().strip()
    print(title)
    print(joke,end="")


#jokes()
def riddle():
    res = requests.get(f'https://www.riddles.nu/random',headers=headers)
    print("Looking for a riddle\n")
    soup = BeautifulSoup(res.text,'html.parser')
    riddles=soup.select('blockquote p')
    riddle=soup.select('blockquote p')[0].getText().strip()
    answer=soup.select('.well-small ')[0].getText().strip()
    print(riddle)
    time.sleep(8)
    print(answer)

#riddle()
##quote of the day
def quote():
    res = requests.get("https://www.brainyquote.com/quote_of_the_day",headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    quote = soup.select(".oncl_q")[0].getText().strip()
    print(quote)
#quote()
