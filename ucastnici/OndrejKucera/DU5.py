from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#TODO Lektor - zbytecny imporet keys ktere nejsou pouzite...

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
from selenium.webdriver.chrome.options import Options

#TODO Lektor - Bylo hodne komentovane na lekci tak jen par poznamek. Neni zmineno vse... .
#TODO Lektor - Super je ze skript +/- jede ale selhava... i bez toho... na posledni logoutu (chybejejici wait na menu), je fajn ze jeste drtiv to sleze na eeror usrrovi... krasa!

Option = Options()
Option.add_argument("start-maximized")
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,'user-name')
#TODO Lektor - ID melo byt oddeleno nekam jinam do promene treba nahoru...

username.send_keys('standard_user')
#TODO Lektor - mohl byt one liner s oddelenim do dictionary! driver.find_element(*username).send_keys(user['name'])

password = driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

#Add to Cart Functionality
item_ids = [f'item_{i}_title_link' for i in range(6)]
#TODO Lektor - nice, cely for a tka... ale muze jich tam teoreticky byt jiny pocet... (chtelo by to nacist dynamicky..)
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
    #TODO Lektor - no jako.. nice ale napsal bych tam spis ==
    print('Add to cart works fine')
    #TODO Lektor - super ze jsopu tu printy...
else:
    print('Add to cart does NOT work fine')
    #TODO Lektor -toto mel byt spis assert ze... nez if... .

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
#TODO Lektor - tady totiz musi byt wait nez se vysune menu... a proto skiprt selhava... treba: 
#TODO Lektor - driver.implicitly_wait(2)
logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
logout_button.click()
try:
    element = driver.find_element(By.ID, 'login-button')
    if element.is_displayed():
        print('Logout works fine')
except NoSuchElementException:
    print('Logout does NOT work fine')

#TODO Lektor - no sleep na kocni tvrdej neni fajn...
time.sleep(2)
driver.close()

#TODO Lektor - printy by mohli byt vice navodnejsi...