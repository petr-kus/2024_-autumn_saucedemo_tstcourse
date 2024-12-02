from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    LOGIN_PAGE_URL = "/"

    LOGIN_USERNAME_FIELD = (By.ID, "user-name")
    LOGIN_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    LOGIN_USERNAME = "standard_user"
    LOGIN_PASSWORD = "secret_sauce"

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the login page."""
        self.open_url(self.LOGIN_PAGE_URL)
        self.logger.info(f"Login page was opened.")

    def login(self, username = None, password = None):
        """Logs in the user with given username and password."""
        try:
            username = username or self.LOGIN_USERNAME
            password = password or self.LOGIN_PASSWORD

            self.logger.info(f"Login process initiated.")
            self.open()
            self.logger.info(f"Login page was opened on url: {self.LOGIN_PAGE_URL}")

            self.send_keys(self.LOGIN_USERNAME_FIELD, username)
            self.logger.info(f"Login username entered: '{username}'")

            self.send_keys(self.LOGIN_PASSWORD_FIELD, password)
            self.click(self.LOGIN_BUTTON)
            self.logger.info(f"Login password entered: '{password}'")

            self.logger.info(f"User '{username}' attempted to log in.")
        except Exception as e:
            self.logger.error(f"Failed to complete login process. Error: {str(e)}")
            self.take_screenshot()
            raise

