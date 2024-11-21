from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

import logging
logging.basicConfig(filename='my_log.log', level=logging.DEBUG)
logging.info('This is an info message.')

login_btn = (By.ID,'login-button')
test_page = "https://www.saucedemo.com/"
login_page = {'username':(By.ID,'user-name')}
field_password = 'password'

def human_watch(seconds=5):
        time.sleep(seconds)

def setup(test_page):
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    logging.debug(f"Starting browser chrome...")
    driver.get(test_page)
    return driver

def login_test(username,password):
    user = driver.find_element(*login_page['username'])
    user.send_keys(username)
    human_watch()
    user_password = driver.find_element(By.ID, field_password)
    user_password.send_keys(password)
    human_watch()
    login_button = driver.find_element(*login_btn)
    login_button.click()

def teradown():
    driver.close()
    driver.quit()

driver = setup(test_page)
login_test('standard_user','secret_sauce')
teradown()