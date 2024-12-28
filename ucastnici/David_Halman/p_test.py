import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni jak test automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre... )

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#TODO Lektor -chtelo by to nekam nastavit soubor pro logovani at je hned vedle / v nake slozkove strukture
logger = logging.getLogger()
#TODO Lektor -jo muzes pouzivat instanci loggeru. Ale fungovalo by to i bez toho. Chválim pritomnost timestampu a info uroven.

class PrihlasovaciStranka:
    #TODO Lektor - zde staticka property tridy:
    # username_field = (By.ID, 'user-name')

    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        #TODO Lektor -username, password a ostatni mohlo byt definovano az na driver. Mohlo bzt definovano jako property tridy ne initu.
        #TODO Lektor - __init__ se vola pri iniciaci instance tridy.. ale tyhle property na tom nezavisi zda instance existuje nebo ne... .
        #TODO Lektor - co se tyka driveru v selfu. Dobre reseni... da se ale usetrit psani kdyz to udelas jako sperae singltton. Viz example reseni od lektora.

    def otevrit(self, url):
        logger.info(f"Otevírám URL: {url}")
        self.driver.get(url)

    def prihlasit(self, username, password):
        logger.info(f"Přihlašuji se s uživatelským jménem: {username} a heslem.")
        #TODO Lektor -tady bych si klidne heslo zalogoval taky. Vimze to jde proti nake bezpecnostni politice... ale stejne ho mas v kodu a je testovaci... .
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        #TODO Lektor - libi se mi ze je to parametrizovany one linere. Pochvala... . (hodne kolegu to nemelo...)

class InventarniStranka:
    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.CLASS_NAME, 'inventory_item_name')

    def jsou_produkty_zobrazeny(self):
        logger.info("Kontroluji, zda jsou zobrazeny produkty.")
        product_element = self.driver.find_element(*self.product_name)
        #TODO Lektor - tady se ti ale vrati jen prvni/posledni ne cele pole... . Blbe se to jmenuje jako metoda mluvi se tam v mnoznem.... 
        #TODO Lektor -  self.driver.find_elements(*self.product_name) - toto by vratilo pole
        return product_element.is_displayed()

@pytest.fixture(scope="module")
def driver():
    logger.info("Inicializace WebDriveru.")
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    logger.info("Ukončuji WebDriver.")
    #TODO Lektor -  super ze jsi pouzil logovani jako info... celkove... .
    driver.quit()
    #TODO Lektor -  pochvala za pouziti pytetsu a fixture a yelidu... .

def test_prihlaseni_uspesne(driver):
    prihlasovaci_stranka = PrihlasovaciStranka(driver)
    inventarni_stranka = InventarniStranka(driver)
     #TODO Lektor - tohto se dalo take zbavit... (dva radky inicalizace) . Viz priklad od lektora.

    prihlasovaci_stranka.otevrit("https://www.saucedemo.com/")
    prihlasovaci_stranka.prihlasit("standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(
        EC.url_contains('inventory.html')
    )
    

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL není správná!"
    logger.info("Úspěšně přihlášeno a stránka se načetla.")

    assert inventarni_stranka.jsou_produkty_zobrazeny(), "Produkty nejsou zobrazeny!"
    logger.info("Produkty jsou zobrazeny!")
    #TODO Lektor - jednoduchy test super je ze jsou pouzity asserty. 
    #TODO Lektor - celkove dobra uroven ulohy. Jen POM mohlo byt oddelneo do separatnich souboru v separatni slozce. 