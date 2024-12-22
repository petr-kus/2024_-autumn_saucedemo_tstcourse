import logging
import requests
import inspect

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from .TestData import TestData

class Base:
    def __init__(self, driver):
        self.url = TestData.urls["landing_page"]
        self.driver = driver
  
    def log_start(self):
        test_name = inspect.currentframe().f_back.f_code.co_name
        logging.info(f"Starting test: {test_name}")
    
    def check_landing_page_loaded(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            logging.info(f"Page '{self.url}' loaded successfully.")
            return True
        else:
            logging.error(f"Page returned status code {response.status_code}. Test execution SUSPENDED.")
            return False
    
    def teardown(self):
        self.driver.quit()
        logging.info(f"Browser closed.")

    def click(self, locator, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException as error:
            print(f"ERROR while waiting on element: {error}.")

    def wait_and_click(self, locator, timeout=3):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
        except TimeoutException as error:
            print(f"ERROR while waiting on element: {error}.")