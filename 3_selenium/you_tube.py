from itertools import dropwhile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)

# driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.youtube.com')

input_field = driver.find_element_by_xpath('//div[@id="search-input"]/input[@id="search"]')
input_field.send_keys("Python Programming")
input_field.send_keys(Keys.ENTER)

time.sleep(5)

titles = driver.find_element_by_xpath('//a[@id="video-title"]')
print(type(titles))

# # iterate through all videos
# for video in titles:
#     # collect each video title
#     #please note that the find_element_by_xpath under the video variable
#     title = video.find_element_by_xpath('.//*[@id="video-title"]')
#     #print the title collected
#     print (title.text)


driver.quit() 