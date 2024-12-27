import POM.cart
import POM.checkout_complete
import POM.checkout_step_one
import POM.checkout_step_two
import POM.inventory
import POM.login_page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import test_data
import POM

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni jak test automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre... )
#TODO Lektor - dost se me libi struktura cele tve slozky ... jde videt ze jsi zvykli si v tom drzet poradek coz hodne chvalim!

def prepare_logging(logger_name: str):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=logger_name, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S')

    return logger

def prepare_driver(logger):
    logger.info(f'creating the chromedriver')
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def prepare_screenshot_folder(folder_name):
    if folder_name.exists(): # clear old content
        logger.info(f'folder {folder_name} already exists, attempting to erase its content')
        for item in folder_name.iterdir():
            if item.is_file():
                item.unlink()
    else:
        logger.info(f'folder {folder_name} does not exist yet, attempting to create it')
        folder_name.mkdir(parents=True)

def teardown(driver):
    driver.close()
    driver.quit()

def test_unhappy_login(driver,  credentials, screenshot_folder, logger):
    logger.info(f'starting unhappy login test with invalid credentials {str(credentials)}.')
    login(driver, logger, credentials, screenshot_folder)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)
    result = login_page.check_failed_login_state()
    if result:
        logger.info(f'Unhappy login failed as expected, test passed.')
    else:
        logger.info(f'Unhappy login test failed.')
 




def login(driver, logger, credentials, screenshot_folder):
    driver.get(test_data.MAIN_PAGE_URL)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)
    login_page.login(credentials)
    


def test_random_login(driver, screenshot_folder, logger):
    logger.info(f'starting login test with random data')
    driver.get(test_data.MAIN_PAGE_URL)
    credentials = test_data.generate_random_credentials()
    login(driver, logger, credentials, screenshot_folder)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)

    try:
        assert login_page.check_failed_login_state() == True
    except AssertionError as error:
        logging.error(f'Login page is probably not displaying error message. Test login with random data failed')
    else:
        logging.info(f'Login page is  displaying login error message. Test login with random data passed')

def test_happy_login(driver, credentials, screenshot_folder, logger):
    logger.info(f'starting login test with valid credentials {credentials}.')
    login(driver, logger, credentials, screenshot_folder)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, logger)
    inventory_page.logout()
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)
    #TODO Lektor - te iniciaci se da vyhnout... ke vsemu zere fakt hodne parametru na muj vkus... coz snizuje citelnost.
    logger.info(f'Happy login test succeeded.')
    #TODO Lektor - neni spatne ale furt je to trosku necitelne. To logovani bych mozna schoval... nekam bud do logovani tech akci... 
    # a nebo bych proto pouzil dekorator nejlepe pomuze k tomuto pochopeni s ekouknout na lektorsky priklad. 



def test_cart_checkout(driver, credentials, screenshot_folder, logger):
    logger.info(f'Starting test of cart and checkout with user {credentials}.')
    login(driver, logger, credentials, screenshot_folder)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, logger)
    items_added_to_cart = inventory_page.add_to_cart_random()
    inventory_page.click_cart_icon()
    cart_page = POM.cart.Cart(driver, screenshot_folder, logger)
    try:
        assert items_added_to_cart == len(cart_page.get_cart_items())
    except AssertionError as err:
        logger.error(f'The cart item number is wrong, {err}')
        raise
    else:
        logger.info(f'Cart item number check passed.')    
    cart_page.click_checkout()
    checkout_first_page = POM.checkout_step_one.CheckoutStepOne(driver, screenshot_folder, logger)
    checkout_first_page.fill_out_personal_data(test_data.personal_data)
    checkout_first_page.click_checkout()
    checkout_second_page = POM.checkout_step_two.CheckoutStepTwo(driver, screenshot_folder, logger)
    checkout_second_page.click_finish()
    checkout_complete_page = POM.checkout_complete.CheckoutComplete(driver, screenshot_folder, logger)
    checkout_complete_page.click_back()
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, logger)
    inventory_page.click_logout_link()
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)
    logger.info('Checkout test passed..')




if __name__ == '__main__':
    logger = prepare_logging(test_data.LOG_FILE_NAME)
    #TODO Lektor -  ten logger pouziva pattern singleton interne takze ho staci nastavit z jednoho mista a nemusis si ho dal predavat. 
    #cela ta konstrukce okolo je vlastne zbytecna. Koukni se do prikladoveho skriptu od lektora a nebo ke kolegum.
    # to predavani musis delat je proto ze to nevolas z hlavniho skriptu ale z funkce nejspis.. .
    # ale stacil by asi import logovani do tech pod modululu (v pomku..)

    driver = prepare_driver(logger)
    for item in test_data.SCREENSHOT_FOLDERS:
        prepare_screenshot_folder(item)

    try:
        logger.info('starting main test procedure')
        test_happy_login(driver, test_data.standard_user, test_data.FOLDER_HAPPY_SCREENSHOTS, logger)
        #TODO Lektor - happy je takove hovorove... positiv scenario negativ scenario... je lepsi.
        test_unhappy_login(driver,test_data.bad_password, test_data.FOLDER_UNHAPPY_SCREENSHOTS,logger)
        #TODO opravdu to zere dost parametru a cca pulka je imlicitni... jako logger a driver... takze obou se da zbavit pkmoci pouziti vlastnosti sinlgtton patternu.
        test_random_login(driver, test_data.FOLDER_RANDOM_SCREENSHOTS, logger)
        test_cart_checkout(driver, test_data.standard_user, test_data.FOLDER_CART_SCREENSHOTS, logger)
    except Exception as error:
        
        logger.error(f'An error{error} occurred', exc_info=True)
    else:
        logger.info(f'Success! All tests passed.')

    finally:
        teardown(driver)

#TODO Lektor - tve logovani vypada dost dobre! Zatim asi nejlepsi z tech co jsem opravoval. Jde vylepsit samozrejmne... . ale dobry.
# jak jde vylepsit... hod oko na priklad od lektora.

#TODO Lektor - hodne chvalim delani screenshotu! Cesty bych generoval dynamicky... pomoci dekoratoru (to jsme neprobirali..) a nedelal si staticky list... a nebo bych pouzil Test Framework... jo jo. 
#narazis zde uz na to zeby se ti vlastne testovaci framework desne hodil... ale jeste ho nepouzivas... .