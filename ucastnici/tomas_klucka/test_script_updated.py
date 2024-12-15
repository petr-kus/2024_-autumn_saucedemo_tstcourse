from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

test_page = "https://www.saucedemo.com/"

def setup(test_page):
 Option = Options()
 Option.add_argument("--disable-features=PasswordManager")
 Option.add_argument("start-maximized")
 driver = webdriver.Chrome(options=Option)
 driver.get(test_page)
 return driver

def login_test(username_text, password_text):
 username = driver.find_element(By.ID, 'user-name')
 username.send_keys(username_text)
 password = driver.find_element(By.ID, 'password')
 password.send_keys(password_text)
 login_button = driver.find_element(By.ID, 'login-button')
 login_button.click()

def menu_test(menu_button, menu_item):
 menu_button = driver.find_element(By.ID, menu_button)
 menu_button.click()
 driver.implicitly_wait(2)
 menu_item = driver.find_element(By.ID, menu_item)
 menu_item.click()

def close_page():
 time.sleep(5)
 driver.quit()

driver = setup(test_page)
login_test('problem_user', 'secret_sauce')
menu_test('react-burger-menu-btn', 'about_sidebar_link')
close_page()