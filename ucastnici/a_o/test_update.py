from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    filename='my_log.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('Konfigurace logování úspěšná.')

login_button = (By.ID, 'login-button')
user_name = (By.ID, 'user-name')
password = (By.ID, 'password')
test_page = "https://www.saucedemo.com" 

def setup(test_page):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(test_page)
    logging.info("Driver inicializován a stránka otevřena.")
    return driver

def login_test(driver, username_value, password_value):
    username = driver.find_element(*user_name)
    username.send_keys(username_value)
    password_field = driver.find_element(*password) 
    password_field.send_keys(password_value)
    login = driver.find_element(*login_button)
    login.click()
    logging.info("Přihlášení proběhlo.")
  
    time.sleep(3)

def filter_test(driver):
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    actions = ActionChains(driver)
    actions.move_to_element(filter_dropdown).click().perform()
    
    wait = WebDriverWait(driver, 10)
    filter_options = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'option')))

    options_values = ['az', 'za', 'lohi', 'hilo']
    for option in filter_options:
        value = option.get_attribute('value')
        if value in options_values:
            option.click()
            logging.info(f"Kliknuto na možnost: {option.text}")
            time.sleep(2)

def teardown(driver):
    driver.close()
    driver.quit()
    logging.info("Driver ukončen.")

driver = setup(test_page)
try:
    login_test(driver, 'problem_user', 'secret_sauce')
    filter_test(driver)
finally:
    teardown(driver)
