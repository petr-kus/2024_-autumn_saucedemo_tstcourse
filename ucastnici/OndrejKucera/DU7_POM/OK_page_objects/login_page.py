# OK_page_objects/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Page Object for the Login Page of the application."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.main_menu_icon = (By.ID, 'react-burger-menu-btn')
        self.logout_button = (By.ID, 'logout_sidebar_link')

    def enter_username(self, username: str):
        """Enter username into the username field."""
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password: str):
        """Enter password into the password field."""
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.login_button).click()
    
    def click_logout(self):
        """Click the logout button."""
        self.driver.find_element(*self.main_menu_icon).click()
        WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(self.logout_button)
        )
        self.driver.find_element(*self.logout_button).click()
        element = self.driver.find_element(*self.login_button)
        return element