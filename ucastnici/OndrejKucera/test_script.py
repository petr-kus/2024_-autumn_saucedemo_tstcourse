from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

Option = Options()
Option.add_argument("start-maximized")
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,'user-name')
username.send_keys('standard_user') 
password = driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()



time.sleep(5)
driver.close()