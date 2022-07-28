from bs4 import BeautifulSoup #pip install bs4
import requests #pip install requests

res = requests.get('https://www.spotrac.com/epl/rankings/')  
soup = BeautifulSoup(res.text,'html.parser')

player_names = soup.select('a.team-name')

data = []

for i in range(len(player_names)):
    player_name = soup.select('a.team-name')[i].getText()
    player_team = soup.select('td.center')[i].getText()
    player_salary = soup.select('span.info')[i].getText()

    row = list(zip(player_name,player_salary,player_team))
    data.append(row)

print(row)