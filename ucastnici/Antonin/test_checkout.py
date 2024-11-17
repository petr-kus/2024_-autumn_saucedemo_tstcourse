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
AtCs=driver.find_elements(By.CLASS_NAME, "btn_primary")
AtCs[random.randrange(1,len(AtCs))].click()
#enter the cart
driver.find_element(By.ID, "shopping_cart_container").click()

#--->cart page
#check for items in the cart
cartItems = driver.find_elements(By.CLASS_NAME, "cart_item")
assert len(cartItems) > 0
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
assert len(cartItems) > 0
#finish the checkout
driver.find_element(By.ID, "finish").click()

#--->confirmation page
#validate expected URL
assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

time.sleep(5)
driver.close()