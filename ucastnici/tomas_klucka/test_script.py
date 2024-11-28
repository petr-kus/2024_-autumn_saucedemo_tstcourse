

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

Option = Options()
Option.add_argument("--disable-features=PasswordManager")
Option.add_argument("start-maximized")

driver = webdriver.Chrome(options=Option)
driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID, 'user-name')
username.send_keys('problem_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
menu_button.click()

time.sleep(2)
about_page = driver.find_element(By.ID, 'about_sidebar_link')
about_page.click()

time.sleep(5)
driver.quit()
