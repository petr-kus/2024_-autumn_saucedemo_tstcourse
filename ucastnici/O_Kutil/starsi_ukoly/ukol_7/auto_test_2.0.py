#1. dávám tomu strukturu -funkce
#2. přidávám logování 
#3. OOP raději ne, protože ho vlastně moc nechápu
#4. spuštění přes try
#5. funkce testu je stejná - přidat batoh do košíku a zkontrolovat, že se tam správně přidal
#6. Jak provést kontrolu, že se skutečně přidal
#7. dávám pryč explicitní waity protože nejsou potřeba
#8. odkazuji raději přes xpath
#9. přidat try a except
#10. přidat co kde udlal a přidpaně aby bylo jasné kde se zaseknul přes assert
#
#

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

import logging
import time

import logging

# logování
import logging

# logování do MOJÍ složky
log_file = "ucastnici/O_Kutil/okutil_log.log"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    filemode="w",  # Přepisuje soubor při každém spuštění
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Starting test execution")


# Globální proměnné
test_page = "https://www.saucedemo.com/"

def setup(test_page):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome()
    logging.debug("Starting Chrome browser...")
    driver.get(test_page)
    time.sleep(2) 
    return driver
    

def login_test(driver, username, password):
    #username
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)
    logging.debug(f"Entered username: {username}")
    time.sleep(2)  

    # password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    logging.debug(f"Entered password: {password}")
    time.sleep(2)  

    # Click on "Login" button
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    logging.debug("Clicked login button")
    time.sleep(2)  

def add_backpack_to_cart_test(driver):
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div").click()
    logging.debug("Clicked on backpack item")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    logging.debug("Clicked 'Add to cart'")
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a/span").click()
    logging.debug("Opened shopping cart")
    time.sleep(2)

def teardown(driver):
    driver.close()
    driver.quit()

# Spuštění testu
if __name__ == "__main__":
    driver = setup(test_page)
    try:
        login_test(driver, "standard_user", "secret_sauce")
    except Exception as e:
        logging.error(f"Test failed: {e}")
    finally:
        teardown(driver)
