from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
import requests
import time

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam

logging.basicConfig(filename="test_logs.log", level=logging.DEBUG, filemode="w")


## Test Data
test_url = "https://www.saucedemo.com/"
# Pro účel testování testu:
#test_url = "http://httpstat.us/500"
tested_user_name = "standard_user"
tested_password = "secret_sauce"

# **** CHANGE for different item to be added (Backpack, Light, Onesie, Jacket, Bolt, Red) ****
item_to_be_added = "Backpack"

# ---------------------------
xpath_add_item_to_cart = f"//div[@class='inventory_container']//div[contains(text(),'{item_to_be_added}')]//following::button[contains(text(),'Add to cart')]"

## Login ---
#Fields
username_field = (By.XPATH,'//*[translate(@placeholder, "U", "u")="username"]')
password_field = (By.XPATH,'//*[translate(@placeholder, "P", "p")="password"]')
#Buttons
login_button = (By.XPATH, '//*[translate(@value, "L", "l")="login"]')

## Inventory page ---
#Add item buttons
add_sauce_labs_backpack = (By.XPATH, "//div[@class='inventory_container']//div[contains(text(),'Backpack')]//following::button[contains(text(),'Add to cart')]")
add_sauce_labs_bike_light = (By.XPATH, "//div[@class='inventory_container']//div[contains(text(),'Light')]//following::button[contains(text(),'Add to cart')]")
#Cart
cart_button = (By.CLASS_NAME, "shopping_cart_badge")
#TODO Lektor - super ze jsi oddelila adresaci super ze jsi si zkusila ruzne adressace ... ale absolutni je dost krehka tu pak nepouzivej.
#TODO Lektor - promene mohli byt oddelne do POM


def setup(url):
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    logging.info(f"...initiating Chrome browser")
    driver.get(url=url)
    
    #Check if page loaded successfully
    response = requests.get(url)
    if response.status_code == 200:
        logging.info(f"Page loaded successfully.")
        return driver
    else:
       logging.error(f"Page returned status code {response.status_code}. Tests SUSPENDED.")
       driver.quit()
       return None

def teardown():
    driver.quit()
    logging.info(f"Browser closed.")

def login_test(used_username, used_password):
            # Valid login
            username = driver.find_element(*username_field)
            username.send_keys(used_username)
            #TODO Lektor - mohl byt one liner... driver.find_element(*username_field).send_keys(used_username)

            password = driver.find_element(*password_field)
            password.send_keys(used_password)

            login_btn = driver.find_element(*login_button)
            login_btn.click()

            # Check if successfuly redirected to Inventory page
            assert "inventory" in driver.current_url, "Login failed or not redirected to Inventory page"
            #TODO Lektor - chvalim assert
            
            # Assert pro účel testování testu:
            #assert "LOL" in driver.current_url, "Login failed or not redirected to Inventory page"

def add_item_to_cart_test():
            try:
                # Add item to the cart by clicking on the button
                add_to_cart_button = driver.find_element(By.XPATH, xpath_add_item_to_cart)
                add_to_cart_button.click()

                # Is one item in the cart?
                cart_badge = driver.find_element(*cart_button)
                assert cart_badge.text == "1", "Item was not added to the cart"
                logging.info(f"1 item successfully present the cart")
            except AssertionError as error:
                print(f"Selhání: {error}")

def open_cart():
     '''Pro účel otestování testu'''
     #TODO Lektor - komentare test casu mohl byt pritomne i jinde... :-)
     driver.get("https://www.saucedemo.com/cart.html")
     time.sleep(5)
      #TODO Lektor - tvrdy sleep je antipatern mel byt parametrizovan nahore!

## EXECUTION
print("Starting...")
driver = setup(test_url)
if driver:

    try:
        login_test(tested_user_name, tested_password)
        add_item_to_cart_test()
        
        # Pro testování testu
        #open_cart()
        #TODO Lektor - chvalim krasnou strukturu testu... vyuziti a rozdeleni na pom by tomu pomohlo jeste vic...
    finally:
        print("...Testing finished")
        teardown()

else:
    logging.info(f"Setup selhal!")

#TODO Lektor - celkove krasna prace na lekci 6 .... jde videt ze nad tim premyslis.. .
#TODO Lektor - krasne prochazi a selhava kdyz ma... pecka!