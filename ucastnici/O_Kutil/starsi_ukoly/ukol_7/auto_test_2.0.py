#1. dávám tomu strukturu -funkce
#2. přidávám logování 
#3. OOP raději ne, protože ho vlastně moc nechápu
#TODO Lektor - skoda... . Ale vidim tam pokusy. Urcite je potreba se OOP naucit. Dost to pomuze obecechapat vyvojare... .
#4. spuštění přes try
#5. funkce testu je stejná - přidat batoh do košíku a zkontrolovat, že se tam správně přidal
#TODO Lektor - no ani ne... . (spis je to jen login...)
#6. Jak provést kontrolu, že se skutečně přidal
#7. dávám pryč explicitní waity protože nejsou potřeba
#TODO Lektor - super... jeste ty sleepy :-)
#8. odkazuji raději přes xpath
 #TODO Lektor - xpath je hodne silne a da se samo pouzit k verifikaci. Viz prikaldovy test. Takze xpath neni na skodu... . Jen se musi umet vyuzit... .
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
#TODO Lektor - zbytecne opakovane importuje logovani... . staci jednou!

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorskymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni jak test automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre... )

# logování do MOJÍ složky
log_file = "ucastnici/O_Kutil/okutil_log.log"
#TODO Lektor - ta cesta zavisi na miste spousteni... a spousteni by melo byt s interni slozky tve... . Takze ta cesta musi byt but nak relativni a nebo jen pojmenovat ssoubor?
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
    #TODO Lektor - time sleepy jso antipatern. sleep by tu nemel byt na tvrdo. Mel by byt nekam parametrizovany. 
    # jediny proc ho tu chces je aby jsi videl jak se to proklikava ve finalni implementaci nema co delat... .
    return driver
    

def login_test(driver, username, password):
    #username
    username_field = driver.find_element(By.ID, "user-name")
    #TODO Lektor - (By.ID, "user-name") - melo byt nekam oddeleno bokem... . 
    #TODO Lektor - (By.ID, "user-name") - cele to mohl byt one liner... . driver.find_element(By.ID, "user-name").send_keys(username)
    username_field.send_keys(username)
    logging.debug(f"Entered username: {username}")
    time.sleep(2)  

    # password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    logging.debug(f"Entered password: {password}")
    time.sleep(2)  

    # Click on "Login" button 
    # TODO Lektor - komentare nejsou potreba, snazime se o to aby nebyli treba piseme kod co nejsrozumitelneji. 
    # Pripadne jde/mel by byt pro to pouzit logging... aby to slo videt i ve vysledku testu.
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    logging.debug("Clicked login button")
    time.sleep(2)  

def add_backpack_to_cart_test(driver):
    driver.find_element(By.XPATH, "//a[@id='item_4_title_link']/div").click()
    logging.debug("Clicked on backpack item") 
    # TODO Lektor - to z eje to zrovna backpack item neni moc parametricky... pri zmene prodkutu musis zmenit i logging. To neni dobry, mel to byt parametr... .
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    logging.debug("Clicked 'Add to cart'")
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a/span").click()
    logging.debug("Opened shopping cart")
    # TODO Lektor - vic bych pouzival uroven INFO nez debug...
    time.sleep(2)

def teardown(driver):
    driver.close()
    driver.quit()

# Spuštění testu
if __name__ == "__main__":
    driver = setup(test_page)
    # TODO Lektor - co kdyz selze setup?
    try:
        login_test(driver, "standard_user", "secret_sauce")
    except Exception as e:
        logging.error(f"Test failed: {e}")
         # TODO Lektor - super ze se nepohcje chyba!
    finally:
        teardown(driver)
# TODO Lektor - krasne vyuzita konstrukce try/except final. Skoda ze je tam jen jeden test :-)
