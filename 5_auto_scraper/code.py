'''
Web Scraping is a technique of scraping data from the internet with the help of different tools and libraries. 
Web Scraping Is one of the important and first steps of any data science problem. There are many libraries in python that make
performing web scraping easy.



▶ Auto scrape is a library that automates the process of web scraping. 
It is a Smart, Automatic, Fast, and Lightweight Web Scraping library for Python. 
The Only Thing you need to provide is the URL or the HTML content of the website you want to scrape.




Features —
* Easy to Use.
* Faster than others.
* Scrape similar websites with one line of code.



▶ Installation:  `pip install autoscraper`





Important Links: 
Github: https://github.com/alirezamika/autoscraper

'''









#######################################################################################################
###################################   PROJECT - 1    ##################################################
#################   Let’s scrape stack overflow using this library.    ################################
#######################################################################################################
'''
Project 1 : Let’s scrape stack overflow using this library.
'''

# from autoscraper import AutoScraper

# url = 'https://stackoverflow.com/questions/67483624/how-to-install-tensorflow-object-detection-api-offline'
# wanted_list = ["How can I install pip on Windows?"]

# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# #print(result)

# print(scraper.get_result_similar('https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python'))

''' OUTPUT
['How can I get the source directory of a Bash script from within the script itself?', 'How to execute a program or call a system command?', 'How can I add a blank directory to a Git repository?', 'How can a file be copied?', 'How to get the current time in Python', 'How can I add new keys to a dictionary?', 'How do I concatenate two lists in Python?', 'How do I list all files of a directory?', 'How to find if directory exists in Python']
'''











#########################################################################################################
###################################   PROJECT - 2    ####################################################
#####################   Scraping https://quotes.toscrape.com/ quotes        #############################
#########################################################################################################

'''
Project 2: Let's Scrape https://quotes.toscrape.com/ quotes
'''
from autoscraper import AutoScraper
url = 'https://quotes.toscrape.com/'

wanted_list = ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”']

scraper = AutoScraper()
quotes = scraper.build(url,wanted_list)
print(quotes)
