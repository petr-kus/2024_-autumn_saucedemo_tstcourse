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
def logger():
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
def driver(logger):
    logger.info(f'creating the chromedriver')
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.fixture(scope='module')
def screenshot_folder(logger, folder_name='screenshots'):
    folder_name = pathlib.Path(folder_name)
    if folder_name.exists(): # clear old content
        logger.info(f'folder {folder_name} already exists, attempting to erase its content')
        for item in folder_name.iterdir():
            if item.is_file():
                item.unlink()
    else:
        logger.info(f'folder {folder_name} does not exist yet, attempting to create it')
        folder_name.mkdir(parents=True)
    return folder_name


@pytest.mark.parametrize('credentials', test_data.wrong_credentials)
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
        logger.error(f'Login page is probably not displaying error message. Test login with random data failed')
    else:
        logger.info(f'Login page is  displaying login error message. Test login with random data passed')

@pytest.mark.parametrize('credentials', test_data.ok_credentials)
def test_happy_login(driver, credentials, screenshot_folder, logger):
    logger.info(f'starting login test with valid credentials {credentials}.')
    login(driver, logger, credentials, screenshot_folder)
    inventory_page = POM.inventory.InventoryPage(driver, screenshot_folder, logger)
    inventory_page.logout()
    login_page = POM.login_page.LoginPage(driver, screenshot_folder, logger)
    logger.info(f'Happy login test succeeded.')






