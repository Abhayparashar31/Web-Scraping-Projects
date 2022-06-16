from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

PATH = 'chromedriver.exe' ##Same Directory as Python Program
driver = webdriver.Chrome(executable_path=PATH)
driver.get("https://www.facebook.com/")

def login(id,password):
 email = driver.find_element_by_id("email")
 email.send_keys(id)
 Password = driver.find_element_by_id("pass")
 Password.send_keys(password)
 button = driver.find_element_by_name("login").click()
 pass
login("YOUR_LOGIN_ID","YOUR_PASSWORD")