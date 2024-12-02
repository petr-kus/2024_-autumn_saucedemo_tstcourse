from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os  # For manipulation with files and folders
from datetime import datetime
from urllib.parse import urlparse
import re

from utilities.logger import get_logger # For logging

class BasePage():

    BASE_URL = "https://www.saucedemo.com"
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url_path=""):
        """Opens a full URL by combining BASE_URL and given URL_PATH."""
        full_url = f"{self.BASE_URL}{url_path}"
        self.logger.info(f"Attempting to open page URL: {full_url} .")
        try:
            self.driver.get(full_url)
            self.logger.info(f"Opening URL: {full_url}")
        except Exception as e:
            self.logger.error(f"Failed to open URL: {full_url}. Error: {str(e)}")
            raise
    
    def find_element(self, locator, timeout=10, wait_for="presence"):
        """Finds an element with an explicit wait."""
        try:
            if wait_for == "visibility":
                self.logger.debug(f"Waiting for visibility of the element: {locator}")
                element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            else:
                self.logger.debug(f"Waiting for presence of the element: {locator}")
                element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

            self.logger.debug(f"Element found with locator: '{locator}'")
            return element
        except Exception as e:
            self.logger.error(f"Element with locator '{locator}' not found within {timeout} seconds. Error: {str(e)}")
            raise Exception(f"Element with locator '{locator}' not found. Error: {str(e)}")

    def click(self, locator, timeout=10):
        """Clicks on the element."""
        try:
            element = self.find_element(locator, timeout)
            element.click()
            self.logger.debug(f"Clicked on element with locator: '{locator}'")
        except Exception as e:
            self.logger.error(f"Failed to click on element with locator '{locator}'. Error: {str(e)}")
            raise

    def send_keys(self, locator, text, timeout=10):
        """Sends keys to the input field. Clears the input field before sending the keys."""
        try:
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"Sent keys '{text}' to element with locator: '{locator}'")
        except Exception as e:
            self.logger.error(f"Failed to send keys '{text}' to element with locator '{locator}'. Error: {str(e)}")
            self.take_screenshot()
            raise
    
    def take_screenshot(self, folder_path="screenshots"):
        """Saves a screenshot of the page to a folder."""
        self.logger.info(f"Attempting to take a screenshot.")
        # Create a folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Get the current time and URL
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        parsed_url = urlparse(self.driver.current_url)
        page_name = parsed_url.path.replace("/", "_").strip("_") or "homepage"
        
        # Ensure page name is a valid filename by removing or replacing invalid characters
        page_name = re.sub(r'[<>:"/\\|?*]', '_', page_name)

        # File name
        file_name = f"{timestamp}_{page_name}.png"
        file_path = os.path.join(folder_path, file_name)

        # Saving a screenshot
        self.driver.save_screenshot(file_path)
        self.logger.info(f"Screenshot saved to '{file_path}'")

        return file_path
    
    def go_to_cart(self):
        """Navigates to the shopping cart page by clicking on the cart icon."""
        self.logger.info(f"Navigating to the shopping cart.")
        self.click(self.CART_ICON)
        self.logger.info(f"Clicked on the shopping cart icon.")
