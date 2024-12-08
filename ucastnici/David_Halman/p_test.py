import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class PrihlasovaciStranka:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def otevrit(self, url):
        logger.info(f"Otevírám URL: {url}")
        self.driver.get(url)

    def prihlasit(self, username, password):
        logger.info(f"Přihlašuji se s uživatelským jménem: {username} a heslem.")
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class InventarniStranka:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.CLASS_NAME, 'inventory_item_name')

    def jsou_produkty_zobrazeny(self):
        logger.info("Kontroluji, zda jsou zobrazeny produkty.")
        product_element = self.driver.find_element(*self.product_name)
        return product_element.is_displayed()

@pytest.fixture(scope="module")
def driver():
    logger.info("Inicializace WebDriveru.")
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    logger.info("Ukončuji WebDriver.")
    driver.quit()

def test_prihlaseni_uspesne(driver):
    prihlasovaci_stranka = PrihlasovaciStranka(driver)
    inventarni_stranka = InventarniStranka(driver)

    prihlasovaci_stranka.otevrit("https://www.saucedemo.com/")
    prihlasovaci_stranka.prihlasit("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains('inventory.html')
    )
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL není správná!"
    logger.info("Úspěšně přihlášeno a stránka se načetla.")

    assert inventarni_stranka.jsou_produkty_zobrazeny(), "Produkty nejsou zobrazeny!"
    logger.info("Produkty jsou zobrazeny!")