from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import random
from selenium.webdriver.chrome.options import Options

Option = Options()
Option.add_argument("start-maximized")
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#--->login page
#fill user name
driver.find_element(By.ID, "user-name").send_keys("standard_user")
#fill password
driver.find_element(By.ID, "password").send_keys("secret_sauce")
#login
driver.find_element(By.ID, "login-button").click()

#--->inventory page
#add rnd item to cart

#TODO - Lektor: 
# Pochvala za miru nahodnosti v testu! 
# Upozorneni ze btn_primary class name nemaji vsechna tlacitka produktu! 
# danemu testu by melo existovat logovani aby jsme zpetne z logu videli proc treba selhal kdyz si neco nahodne vybral! (to je ale za rozsahem lekce)

AtCs=driver.find_elements(By.CLASS_NAME, "btn_primary")
AtCs[random.randrange(1,len(AtCs))].click()
#enter the cart
driver.find_element(By.ID, "shopping_cart_container").click()

#--->cart page
#check for items in the cart
cartItems = driver.find_elements(By.CLASS_NAME, "cart_item")

#TODO - Lektor: 
# okej ale tady vis ze tam ma byt jeden prave ne? A hodila by se naka message, kdyz to sleze... .
assert len(cartItems) > 0 , "Lektor: Jejda asi neco chybi v kosiku!"

#continue with checkout
driver.find_element(By.ID, "checkout").click()

#--->1st checkout step
#fill first name
driver.find_element(By.ID, "first-name").send_keys("John")
#fill last name
driver.find_element(By.ID, "last-name").send_keys("Doe")
#fill postalCode
driver.find_element(By.ID, "postal-code").send_keys("111")
#continue with checkout
driver.find_element(By.ID, "continue").click()

#--->2nd checkout step
#check for items in order
#TODO - Lektor: 
# Hej! to uz tam jednou mas a nenaplnil jsi to znova! Mezitim se pocet v te promene nezmenil. 
# To neni zivy interface dle me! Takze opakovanim tehoz se vysledek nezmeni... . 
# Tento krok noveruje pocet znovu na jine strance! 
assert len(cartItems) > 0
#finish the checkout
driver.find_element(By.ID, "finish").click()

#--->confirmation page
#validate expected URL
#TODO - Lektor: 
# Validuje sice url... ale ne obsah stranky. Nevis na co se uzivatel diva... .
# Autotesty jsou lepsi checklisty - pri psani autotestu je potreba na to brat ohled. 
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

time.sleep(5)
driver.close()