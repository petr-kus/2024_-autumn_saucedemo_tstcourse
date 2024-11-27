from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

#Add to Cart Functionality
item_ids = [f'item_{i}_title_link' for i in range(6)]
for item_id in item_ids:
    select_product = driver.find_element(By.ID, f'{item_id}')
    select_product.click()
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart')
    add_to_cart_button.click()
    time.sleep(1)
    back_to_main_page = driver.find_element(By.ID, 'back-to-products')
    back_to_main_page.click()
shopping_cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
badge_count = int(shopping_cart_badge.text)
if badge_count >= 6:
    print('Add to cart works fine')
else:
    print('Add to cart does NOT work fine')

#Remove from Cart Functionality
item_ids = [f'item_{i}_title_link' for i in range(6)]
for item_id in item_ids:
    select_product = driver.find_element(By.ID, f'{item_id}')
    select_product.click()
    remove_from_cart_button = driver.find_element(By.ID, 'remove')
    remove_from_cart_button.click()
    time.sleep(1)
    back_to_main_page = driver.find_element(By.ID, 'back-to-products')
    back_to_main_page.click()
try:
    element = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    if element.is_displayed():
        print('Remove from cart does NOT work fine')
except NoSuchElementException:
    print('Remove from cart works fine')

#Logout Functionality
main_menu_icon = driver.find_element(By.ID, 'react-burger-menu-btn')
main_menu_icon.click()
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()
try:
    element = driver.find_element(By.ID, 'login-button')
    if element.is_displayed():
        print('Logout works fine')
except NoSuchElementException:
    print('Logout does NOT work fine')


time.sleep(2)
driver.close()