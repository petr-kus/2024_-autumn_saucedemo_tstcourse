from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pathlib
from selenium.webdriver.chrome.options import Options
import logging

#TODO Lektor -  Oprava úkolu 5 + 6 dohromady. 
#TODO Lektor -  Mohlo to být už v POM/OOP aspoň :-) 
#TODO Lektor -  cením si verifikace typů ve funkcích
#TODO Lektor -  super že test jede ale do konzole nedá vědět, že zalogovanbí selhalo když dám usra locked_out_user
#TODO Lektor -  ulohu si pamatuji ze jsem podrobne komentoval na lekci... . Tak jen v rychlosti nejdulezitejsi body.


FOLDER_SCREENSHOTS = pathlib.Path('screenshots')
SITE_URL = "https://www.saucedemo.com/"
LOGIN_PAGE_FILE_NAME = 'login_page.png'
INVENTORY_PAGE_FILE_NAME = 'inventory_page.png'
HAMBURGER_CLICKED_FILE_NAME = 'hamburger_clicked.png'
LOGOUT_PAGE_FILE_NAME = 'logout.png'
LOG_FILE_NAME = 'saucedemo-tests.log'
LOGIN_CREDENTIALS = ('locked_out_user','secret_sauce')
#TODO Lektor -  pro cesty k obraykum bz bzl lepsi generator ney je tu vsechny uvadet.


def prepare_folder(folder_name: pathlib.Path) -> None:
    if folder_name.exists(): # clear old content
        logger.info(f'folder {folder_name} already exists, attempting to its content')
        for item in folder_name.iterdir():
            if item.is_file():
                item.unlink()
    else:
        logger.info(f'folder {folder_name} does not exist yet, attempting to create it')
        folder_name.mkdir(parents=True)


def prepare_driver() -> webdriver:
    logger.info(f'creating the chromedriver')
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver


def prepare_logger(logger_name: str):
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename=logger_name, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
    datefmt='%Y-%m-%d %H:%M:%S')

    return logger


def run_test(folder_path: pathlib.Path, driver: webdriver) -> None:
    logger.info(f'run of tests')
    
    logger.info(f'visiting site {SITE_URL}')
    try:

        driver.get(SITE_URL)
        driver.save_screenshot(folder_path / pathlib.Path(LOGIN_PAGE_FILE_NAME))
        logger.info(f'run of tests')
        logger.info(f'login attempt')

        username = driver.find_element(By.ID,'user-name')
        #TODO Lektor -  to id  by to chctelo nekam oddelit
        username.send_keys(LOGIN_CREDENTIALS[0]) 
        password = driver.find_element(By.ID,'password')
        password.send_keys(LOGIN_CREDENTIALS[1])
        #TODO Lektor -  password pouzijes jen jendou mohl to byt one liner...treba: driver.find_element(password).send_keys(credentials['password'])
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()
        # time.sleep(5)
        driver.save_screenshot(folder_path / pathlib.Path(INVENTORY_PAGE_FILE_NAME))
        logger.info(f'visiting the inventory page, looking at hamburger menu')
        hamburger_btn = driver.find_element(By.ID,'react-burger-menu-btn')
        hamburger_btn.click()
        time.sleep(2) # waiting for animation
        driver.save_screenshot(folder_path / pathlib.Path(HAMBURGER_CLICKED_FILE_NAME))
        logger.info(f'logout attempt')
        logout_link = driver.find_element(By.ID,'logout_sidebar_link')
        logout_link.click()
        driver.save_screenshot(folder_path / pathlib.Path(LOGIN_PAGE_FILE_NAME))
    except Exception as excp:
        logger.error(f'Exception {excp} triggered.')
        #TODO Lektor -  super ze logujes cely error - me to ale do konuzole neselhalo diky odchytu erroru... .


def teardown(driver):
    driver.close()
    driver.quit()


if __name__ == "__main__":
    logger = prepare_logger(LOG_FILE_NAME)
    driver = prepare_driver()
    prepare_folder(FOLDER_SCREENSHOTS)
    run_test(FOLDER_SCREENSHOTS, driver)
    teardown(driver)
