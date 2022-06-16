from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://hoopshype.com/salaries/players/')

players = driver.find_elements_by_xpath('//td[@class="name"]')
print(type(players))
print(players.text)

# players_list = []
# for p in range(len(players)):
#     players_list.append(players[p].text)

# print(players_list)