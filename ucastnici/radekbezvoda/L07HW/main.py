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
    logger.info(f'Happy login test succeeded.')


def test_cart_checkout(driver, credentials, screenshot_folder, logger):
    logger.info(f'Starting test of cart and checkout with user {credentials}.')
    login(driver, logger, credentials, screenshot_folder)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, logger)
    items_added_to_cart = inventory_page.add_to_cart_random()
    inventory_page.click_cart_icon()
    cart_page = POM.cart.Cart(driver, screenshot_folder, logger)
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
    driver = prepare_driver(logger)
    for item in test_data.SCREENSHOT_FOLDERS:
        prepare_screenshot_folder(item)

    try:
        logger.info('starting main test procedure')
        test_happy_login(driver, test_data.standard_user, test_data.FOLDER_HAPPY_SCREENSHOTS, logger)
        test_unhappy_login(driver,test_data.bad_password, test_data.FOLDER_UNHAPPY_SCREENSHOTS,logger)
        test_random_login(driver, test_data.FOLDER_RANDOM_SCREENSHOTS, logger)
        test_cart_checkout(driver, test_data.standard_user, test_data.FOLDER_CART_SCREENSHOTS, logger)
    except Exception as error:
        
        logger.error(f'An error{error} occurred', exc_info=True)
    else:
        logger.info(f'Success! All tests passed.')

    finally:
        teardown(driver)
