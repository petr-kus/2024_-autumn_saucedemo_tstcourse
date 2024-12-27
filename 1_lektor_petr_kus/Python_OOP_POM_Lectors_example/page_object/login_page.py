import tstkit
from tstkit import browser
import logging
from selenium.webdriver.common.by import By

class login_page:
      login_button = (By.ID,'login-button')
      password_field = (By.ID,'password')
      username_field = (By.ID,'user-name')
      page = "www.saucedemo.com"

      # Lector's Note: Different approaches are used to address the class (`cls`/`login_page`) and its elements.

      def is_loaded():
         # Lector's TIP: Page load checks are often repeated across multiple pages, so the logic is centralized in the `tstkit.page_is_loaded()` function.
         # This promotes code reuse and reduces duplication, making the code more maintainable and easier to update.
         tstkit.page_is_loaded(login_page.page)
         # Lector's TIP: This centralization approach can be applied to other common actions/elements that are used across multiple pages.
         # For example, actions like taking screenshots, interacting with fields or buttons, etc., can be abstracted into helper functions or methods.
         # This helps maintain a clean code structure and makes modifications easier when such actions need to be updated or changed.
      
      def fill_user(username):
        logging.info(f"Login_Page - Filling user name '{username}'")
        browser.find_element(*login_page.username_field).send_keys(username)
      
      @classmethod
      def fill_password(cls, password):
        logging.info(f"Login_Page - Filling password '{password}'")
        browser.find_element(*cls.password_field).send_keys(password)

      @classmethod
      def click_login(cls):
         logging.info(f"Login_Page - clicking to login")
         browser.find_element(*cls.login_button).click()