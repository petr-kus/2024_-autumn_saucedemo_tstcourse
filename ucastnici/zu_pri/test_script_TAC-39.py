from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

## Setup
Option = Options()
Option.add_argument("start-maximized")
driver = webdriver.Chrome()

url = "https://www.saucedemo.com/"
valid_user_name = "standard_user"
valid_password = "secret_sauce"

try:

    ## Step 1: Go to and load page
    driver.get(url)
    time.sleep(1)

    # Is landing page loaded successfully: Does title include "Swag Labs"?
    #assert "Swag Labs" in driver.title, "Invalid title of landing page"
    assert "LOL" in driver.title, "Invalid title of landing page"

except AssertionError as error:
    print(f"Selhání: {error}")

try:
    ## Step 2: Valid login
    username = driver.find_element(By.ID,'user-name')
    username.send_keys(valid_user_name)
    time.sleep(1)

    password = driver.find_element(By.ID,'password')
    password.send_keys(valid_password)
    time.sleep(1)

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    time.sleep(1)

    # Check if successfuly redirected to Inventory page
    #assert "inventory" in driver.current_url, "Login failed or not redirected to Inventory page"
    assert "LOL" in driver.current_url, "Login failed or not redirected to Inventory page"

except AssertionError as error:
    print(f"Selhání: {error}")

try:
    ## Step 3: Add 4 items to cart (*** In PROGRESS ***)
    # Add item Sauce labs backpack to the cart by clicking on the button
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    time.sleep(1)

    #Is item in the cart?
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "Sauce Labs Backpack was not added to the cart"
    print("Sauce Labs Backpack successfully added to the cart")
    

except AssertionError as error:
    print(f"Selhání: {error}")

## Exit
finally:
    driver.close()