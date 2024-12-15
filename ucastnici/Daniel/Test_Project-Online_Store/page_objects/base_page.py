from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os  # For manipulation with files and folders
from datetime import datetime
from urllib.parse import urlparse
import re

from utilities.logger import get_logger # For logging

class BasePage():

    BASE_URL = "https://www.saucedemo.com/"

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ICON_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    NAVIGATION_MENU_OPEN = (By.ID, "react-burger-menu-btn")
    NAVIGATION_MENU_ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    NAVIGATION_MENU_ABOUT = (By.ID, "about_sidebar_link")
    NAVIGATION_MENU_LOGOUT = (By.ID, "logout_sidebar_link")
    NAVIGATION_MENU_RESET = (By.ID, "reset_sidebar_link")
    NAVIGATION_MENU_CLOSE = (By.ID,"react-burger-cross-btn")

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def open_url(self, url_path=""):
        """Opens a full URL by combining BASE_URL and given URL_PATH.
        
        :param url_path: URL path without symbol "/" in the beginning of the URL path. To combine BASE_URL and URL_PATH, BASE_URL should be specified first (should contain "/" in the end).
        """
        full_url = f"{self.BASE_URL}{url_path}"
        
        self.logger.info(f"Proceeding to open URL: {full_url}")

        try:
            self.driver.get(full_url)
            self.logger.info(f"Successfully opened URL: {full_url}")
        except Exception as e:
            self.logger.error(f"Failed to open URL: {full_url}. Error: {str(e)}")
            raise
    
    def find_element(self, locator, timeout=10, wait_for="presence"):
        """Finds an element with an explicit wait.

        :param locator: Tuple (By.<METHOD>, "value") for locating the element.
        :param timeout: Maximum time to wait for the element to appear.
        :param wait_for: Specify "presence" or "visibility" of elements to wait for.
        :return: WebElement object if element is found.
        :raises: Exception if element is not found within the timeout.
        """
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

    def find_elements(self, locator, timeout=10, wait_for="presence"):
        """
        Finds multiple elements with an explicit wait.

        :param locator: Tuple (By.<METHOD>, "value") for locating the elements.
        :param timeout: Maximum time to wait for the elements to appear.
        :param wait_for: Specify "presence" or "visibility" of elements to wait for.
        :return: List of WebElement objects if elements are found.
        :raises: Exception if elements are not found within the timeout.
        """
        try:
            if wait_for == "visibility":
                self.logger.debug(f"Waiting for visibility of elements: {locator}")
                elements = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
            else:
                self.logger.debug(f"Waiting for presence of elements: {locator}")
                elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

            self.logger.debug(f"Found {len(elements)} elements with locator: '{locator}'")
            return elements
        except Exception as e:
            self.logger.error(f"Elements with locator '{locator}' not found within {timeout} seconds. Error: {str(e)}")
            raise Exception(f"Elements with locator '{locator}' not found. Error: {str(e)}")
        
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

    def is_element_visible(self, locator, timeout=10):
        """
        Checks if an element is visible on the page.

        :param locator: Tuple (By.<METHOD>, "value") for locating the element.
        :param timeout: Maximum time to wait for the element to become visible.
        :return: True if the element is visible, False otherwise.
        """
        try:
            self.find_element(locator, timeout=timeout, wait_for="visibility")
            self.logger.debug(f"Element with locator '{locator}' is visible.")
            return True
        except Exception as e:
            self.logger.debug(f"Element with locator '{locator}' is not visible. Error: {str(e)}")
            return False

    def is_page_displayed(self):
        """
        Verifies that the page is displayed correctly.

        :return: True if the page is displayed, False otherwise.
        """
        try:
            self.find_element(self.PRODUCT_TITLE)  # Key element to verify the page
            return True
        except Exception as e:
            self.logger.error(f"Product Detail Page is not displayed. Error: {str(e)}")
            return False
    
    def get_current_url(self):
        """
        Returns the current URL of the page.

        :return: The current URL as a string.
        """
        current_url = self.driver.current_url
        self.logger.info(f"Current URL is: {current_url}")
        return current_url
    
    def go_to_cart(self):
        """Navigates to the shopping cart page by clicking on the cart icon."""
        self.logger.info(f"Navigating to the shopping cart.")
        self.click(self.CART_ICON)
        self.logger.info(f"Clicked on the shopping cart icon.")

    def get_cart_badge_number(self):
        """Finds the cart badge element and returns its numeric value."""
        try:
            # Find the cart badge element by class name
            cart_badge_element = self.find_element(self.CART_ICON_BADGE)
            cart_badge_text = cart_badge_element.text
            self.logger.info(f"Cart badge value was found: '{cart_badge_text}'")

            if cart_badge_text.isdigit():
                return int(cart_badge_text)
            else:
                self.logger.info(f"Cart badge value is not digit: '{cart_badge_text}'")
                return 0
            
        except Exception as e:
            self.logger.error(f"Failed to get cart badge number. Error: {str(e)}")
            return 0
    
    def open_menu(self):
        """Opens the navigation menu."""
        self.logger.info(f"Opening the navigation menu.")
        self.click(self.NAVIGATION_MENU_OPEN)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAVIGATION_MENU_CLOSE))
        self.logger.info(f"Navigation menu opened.")

    def logout(self):
        """Logs out the user."""
        self.logger.info(f"Logout process initiated.")
        self.open_menu()
        self.click(self.NAVIGATION_MENU_LOGOUT)
        self.logger.info(f"User attempted to logout.")