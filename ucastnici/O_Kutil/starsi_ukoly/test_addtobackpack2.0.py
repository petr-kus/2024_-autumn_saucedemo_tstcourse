#1. dávám tomu strukturu - funkce
#2. přidávám logování 
#3. OOP raději ne, protože ho vlastně moc nechápu
#4. spuštění přes try 
#5. funkce testu je stejná - přidat batoh do košíku a zkontrolovat, že se tam správně přidal
#6. Jak provést kontrolu, že se skutečně přidal
#7. dávám pryč explicitní waity protože nejsou potřeba
#8. odkazuji raději přes xpath
#9. Přidávám try a except aby bylo jasné kde se zaseknul
#10. Přidávám jasnou hlášku, že test je bud pass nebo fail přes asert


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging

# Nastavení logování
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
    """Nastavení prohlížeče a spuštění stránky."""
    print("Setting up browser and opening test page...")
    logging.debug("Setting up browser...")
    try:
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome()
        driver.get(test_page)
        logging.debug(f"Opened test page: {test_page}")
        return driver
    except Exception as e:
        logging.error(f"Setup failed: {e}")
        print(f"Setup failed: {e}")
        raise

def login_test(driver, username, password):
    """Přihlášení na stránku."""
    print("Logging in...")
    logging.debug("Starting login test...")
    try:
        driver.find_element(By.ID, "user-name").send_keys(username)
        logging.debug("Entered username")
        driver.find_element(By.ID, "password").send_keys(password)
        logging.debug("Entered password")
        driver.find_element(By.ID, "login-button").click()
        logging.debug("Clicked login button")
    except Exception as e:
        logging.error(f"Login test failed: {e}")
        print(f"Login test failed: {e}")
        raise

def add_backpack_to_cart_test(driver):
    """Test přidání batohu do košíku."""
    print("Adding backpack to cart...")
    logging.debug("Starting add backpack to cart test...")
    try:
        driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div").click()
        logging.debug("Clicked on backpack item")
        driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
        logging.debug("Clicked 'Add to cart'")
        driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a/span").click()
        logging.debug("Opened shopping cart")

        # Kontrola, že je batoh v košíku
        item_name = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text
        assert item_name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack', but got '{item_name}'"
        logging.debug("Backpack is in the cart")
        print("Test is OK. Sauce Labs Backpack was correctly added to cart.")
    except AssertionError as e:
        logging.error(f"Assertion failed: {e}")
        print(f"Assertion failed: {e}")
        raise
    except Exception as e:
        logging.error(f"Add backpack to cart test failed: {e}")
        print(f"Add backpack to cart test failed: {e}")
        raise

def teardown(driver):
    """Ukončení testu a zavření prohlížeče."""
    print("Closing browser...")
    logging.debug("Tearing down browser...")
    try:
        driver.close()
        driver.quit()
        logging.debug("Browser closed")
    except Exception as e:
        logging.error(f"Teardown failed: {e}")
        print(f"Teardown failed: {e}")
        raise

# Spuštění testu
if __name__ == "__main__":
    test_failed = False
    driver = None
    try:
        driver = setup(test_page)
        login_test(driver, "standard_user", "secret_sauce")
        add_backpack_to_cart_test(driver)
    except Exception as e:
        logging.error(f"Test execution failed: {e}")
        print(f"Test execution failed: {e}")
        test_failed = True
    finally:
        if driver:
            teardown(driver)

    # Výstup o celkovém výsledku testu
    if test_failed:
        print("Test FAILED. See logs for details.")
        logging.info("Test FAILED.")
    else:
        print("Test PASSED successfully!")
        logging.info("Test PASSED.")
