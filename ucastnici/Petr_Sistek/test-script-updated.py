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
username = driver.find_element(By.ID,'user-name')
username.send_keys('standard_user') 
password = driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
time.sleep(3)

# Kliknutí na ikonu košíku (vpravo nahoře)
cart_button = driver.find_element(By.ID, "shopping_cart_container")
cart_button.click()
time.sleep(3)

# Kliknutí na burger menu
burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
burger_menu.click()
time.sleep(3)

# Kliknutí na Logout v burger menu
logout = driver.find_element(By.ID, "logout_sidebar_link")
logout.click()
time.sleep(3)

# Přihlášení jako problem_user
username = driver.find_element(By.ID, "user-name")
username.send_keys("problem_user")
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(3)

driver.close()
