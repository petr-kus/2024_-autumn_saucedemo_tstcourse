import logging
import requests

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from TestData import TestData


class Base:
    def __init__(self, driver=None):
        self.url = TestData.urls["landing_page"]
        if driver is None:
            self.driver = self.setup_driver()
        else:
            self.driver = driver
    
    def setup_driver(self):
        option = Options()
        option.add_argument("--start-maximized")
        driver = TestData.browsers[TestData.chosen_webdriver](option)
        driver.implicitly_wait(2)
        logging.info(f"...initiating {TestData.chosen_webdriver} browser")
        driver.get(self.url)
        return driver
    
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