from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW')

## Smooth Scrolling Till The End
page_height = driver.execute_script("return document.body.scrollHeight")
for value in range(0,page_height):
	driver.execute_script(f"window.scrollTo(0, {value});")
	

## Scraping Movie Names
movies_names = driver.find_elements_by_xpath('//td[@class="a-text-left mojo-field-type-title"]/a[@class="a-link-normal"]')  ## targets all the elements on the web that has same Xpath
movie_name_list = []                                                                                                        ## an empty list for storing movie names
for movie in range(len(movies_names)):                                                                                      ## a loop that runs until the length of movies_name list
    movie_name_list.append(movies_names[movie].text)                                                                        ## extracting text from the movie name and appending it on the movies name list
#print(movie_name_list)

## Scraping Movies Lifetime Grossings
lifetime_gross = driver.find_elements_by_xpath('//td[@class="a-text-right mojo-field-type-money"]') 
lifetime_gross_list = []
for i in range(len(lifetime_gross)):
    lifetime_gross_list.append(lifetime_gross[i].text)
#print(lifetime_gross_list)


## Scraping Movies Release Date
release_year = driver.find_elements_by_xpath('//td[@class="a-text-left mojo-field-type-year"]/a[@class="a-link-normal"]')
release_year_list = []
for year in range(len(release_year)):
    release_year_list.append(release_year[year].text)
#print(release_year_list)

data =list( zip(movie_name_list, release_year_list, lifetime_gross_list))


df = pd.DataFrame(data,columns=['Movie Name', 'Release Date','Lifetime Earnings'])
                 ## dataset name ## columns names
print(df)
df.to_csv('top_200_movies_with_lifetime_gross.csv',index=False)