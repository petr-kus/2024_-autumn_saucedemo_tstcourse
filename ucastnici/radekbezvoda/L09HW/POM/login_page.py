from selenium.webdriver.common.keys import Keys
import random
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
        self.get_elements_by('ID', self.username_id, 'username').send_keys(credentials.username)
        self.get_elements_by('ID', self.password_id, 'password').send_keys(credentials.password)

        choice = random.choice((0,1))
        if choice:
            self.get_elements_by('ID', self.login_button_id, 'Login button').click()

        else:
            self.get_elements_by('ID', self.password_id, 'Login button').send_keys(Keys.ENTER)
    
    def check_failed_login_state(self):
        container = self.get_elements_by('CSS_SELECTOR', self.error_message_container_css, "error message box")
        if self.error_message in container.text:
            return True
        else:
            return False

