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
import pytest
import pathlib

@pytest.fixture(scope='module')
def test_logger():
    logger_name = 'pytest.log'
    log_obj = logging.getLogger(__name__)
    log_obj.setLevel(logging.INFO)

    file_handler = logging.FileHandler(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    log_obj.addHandler(file_handler)

    yield log_obj

    log_obj.removeHandler(file_handler)
    file_handler.close()


@pytest.fixture(scope='module')
def driver(test_logger):
    test_logger.info(f'creating the chromedriver')
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope='module')
def screenshot_folder(test_logger, folder_name='screenshots'):
    folder_name = pathlib.Path(folder_name)
    if folder_name.exists(): # clear old content
        test_logger.info(f'folder {folder_name} already exists, attempting to erase its content')
        for item in folder_name.iterdir():
            if item.is_file():
                item.unlink()
    else:
        test_logger.info(f'folder {folder_name} does not exist yet, attempting to create it')
        folder_name.mkdir(parents=True)
    return folder_name


@pytest.mark.parametrize('credentials', test_data.wrong_credentials)
def test_unhappy_login(driver,  credentials, screenshot_folder, test_logger):
    test_logger.info(f'starting unhappy login test with invalid credentials {str(credentials)}.')
    login(driver, test_logger, credentials, screenshot_folder)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, test_logger)
    result = login_page.check_failed_login_state()
    if result:
        test_logger.info(f'Unhappy login failed as expected, test passed.')
    else:
        test_logger.info(f'Unhappy login test failed.')
 




def login(driver, test_logger, credentials, screenshot_folder):
    driver.get(test_data.MAIN_PAGE_URL)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, test_logger)
    login_page.login(credentials)
    


def test_random_login(driver, screenshot_folder, test_logger):
    test_logger.info(f'starting login test with random data')
    driver.get(test_data.MAIN_PAGE_URL)
    credentials = test_data.generate_random_credentials()
    login(driver, test_logger, credentials, screenshot_folder)
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, test_logger)

    try:
        assert login_page.check_failed_login_state() == True
    except AssertionError as error:
        test_logger.error(f'Login page is probably not displaying error message. Test login with random data failed')
    else:
        test_logger.info(f'Login page is  displaying login error message. Test login with random data passed')

@pytest.mark.parametrize('credentials', test_data.ok_credentials)
def test_happy_login(driver, credentials, screenshot_folder, test_logger):
    test_logger.info(f'starting login test with valid credentials {credentials}.')
    login(driver, test_logger, credentials, screenshot_folder)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, test_logger)
    inventory_page.logout()
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, test_logger)
    test_logger.info(f'Happy login test succeeded.')


def clear_cart(driver, screenshot_folder, test_logger):
    POM.inventory.InventoryPage(driver, screenshot_folder, test_logger).click_cart_icon()
    cart_page = POM.cart.Cart(driver, screenshot_folder, test_logger)
    cart_page.remove_items()
    cart_page.click_continue_shopping()


@pytest.mark.parametrize('credentials', test_data.ok_credentials)
def test_cart_checkout(driver, credentials, screenshot_folder, test_logger):
    test_logger.info(f'Starting test of cart and checkout with user {credentials}.')
    login(driver, test_logger, credentials, screenshot_folder)
    clear_cart(driver, screenshot_folder, test_logger)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, test_logger)
    items_added_to_cart = inventory_page.add_to_cart_random()
    inventory_page.click_cart_icon()
    cart_page = POM.cart.Cart(driver, screenshot_folder, test_logger)
    try:
        assert items_added_to_cart == len(cart_page.get_cart_items())
    except AssertionError as error:
        test_logger.error(f'The cart item number is wrong, {error}')
        raise
    else:
        test_logger.info(f'Cart item number check passed.')    
    cart_page.click_checkout()
    checkout_first_page = POM.checkout_step_one.CheckoutStepOne(driver, screenshot_folder, test_logger)
    checkout_first_page.fill_out_personal_data(test_data.personal_data)
    checkout_first_page.click_checkout()
    checkout_second_page = POM.checkout_step_two.CheckoutStepTwo(driver, screenshot_folder, test_logger)
    checkout_second_page.click_finish()
    checkout_complete_page = POM.checkout_complete.CheckoutComplete(driver, screenshot_folder, test_logger)
    checkout_complete_page.click_back()
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, test_logger)
    inventory_page.click_logout_link()
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, test_logger)
    test_logger.info('Checkout test passed..')





