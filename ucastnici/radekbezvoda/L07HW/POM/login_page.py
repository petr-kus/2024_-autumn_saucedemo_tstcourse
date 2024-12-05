from selenium.webdriver.common.keys import Keys
import logging
import random
from .common import get_element_by_id, get_element_by_css_selector
from .base import BasePage

class LoginPage(BasePage):
    page_url = ''
    username_id = 'user-name'
    password_id = 'password'
    login_button_id = 'login-button'
    error_message_container_id = 'error-message-container'
    error_message_container_css = '.error-message-container > h3:nth-child(1)'
    error_message = 'Username and password do not match any user'

    def __init__(self, driver, screenshot_folder, logger) -> None:
        super().__init__(driver, screenshot_folder, logger)
        self.check_page_url( self.page_url)
        self.logger = logger

    def login(self,credentials):
        self.logger.info(f'LoginPage.login: Attempting to login with username {credentials.username} and password {credentials.password}')
        get_element_by_id(self.driver, self.username_id, 'username').send_keys(credentials.username)
        get_element_by_id(self.driver, self.password_id, 'password').send_keys(credentials.password)
        choice = random.choice((0,1))
        if choice:
            get_element_by_id(self.driver, self.login_button_id, 'Login button').click()
        else:
            get_element_by_id(self.driver, self.password_id, 'password').send_keys(Keys.ENTER)
    
    def check_failed_login_state(self):
        container = get_element_by_css_selector(self.driver, self.error_message_container_css, "error message box", self.logger)
        if self.error_message in container.text:
            return True
        else:
            return False

