from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest
logging.basicConfig(filename='my_log.log', level=logging.DEBUG)
logging.info('This is an info message.')


test_page = "https://www.saucedemo.com/"

# =========================================
# Níže příklady strukturovani identifiaktorů prvků
# proč? - Vy pracujete s webem sucedemo.com - tam jsou ID, attributy atd. krasně pojmenované... 
# ale jinde to může být totalně nesrozumitelné a dlouhé!
# a take to můžete hodně přepoužívat... proto je vhodné použít na to něco...
# ----------------------------------------- 
login_btn = (By.ID,'login-button')
LoginPage = {'username':(By.ID,'user-name')}
field_password = 'password'

class login_page():
      login_button = (By.ID,'login-button')
      password = (By.ID,'password')
      username = (By.ID,'user-name')

# základ myšlenky pro použití POM - page object modelu:
# (všimněte si nápovědy přes tečku při použití!)
class burger_menu():
      
      all_items = (By.XPATH, "//a[text()='All Items']")
      about = (By.XPATH,"//a[text()='About']")
      logout = (By.XPATH,"//a[text()='Logout']")
      reset_app = (By.XPATH,"//a[text()='Reset App State']")
      cross_close = (By.ID,'react-burger-cross-btn')
      open_button = (By.ID,'react-burger-menu-btn')

      def open():
           logging.info('Opening burger menu')
           driver.find_element(*burger_menu.open_button).click()
           #počkání až se otevře menu...
           WebDriverWait(driver, 5).until(EC.visibility_of_element_located(burger_menu.cross_close))

# =========================================

def slowdown(seconds=2):
        time.sleep(seconds)

def test_setup():
    test_page = "https://www.saucedemo.com/"
    Option = Options()
    Option.add_argument("start-maximized")
    global driver
    driver = webdriver.Chrome()
    #driver.implicitly_wait(2)
    logging.info(f"Starting browser chrome...")
    driver.get(test_page)
    return driver

def test_login():
    username = "standard_user"
    password = "secret_sauce"
    user = driver.find_element(*LoginPage['username'])
    user.send_keys(username)
    slowdown()
    user_password = driver.find_element(By.ID, field_password)
    user_password.send_keys(password)
    slowdown()
    login_button = driver.find_element(*login_btn)
    login_button.click()

def test_logout():
    slowdown()
    burger_menu.open()
    slowdown()
    driver.find_element(*burger_menu.logout).click()
    slowdown()

def test_teardown():
    driver.close()
    driver.quit()