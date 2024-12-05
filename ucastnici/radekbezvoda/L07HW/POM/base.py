import os
from .common import get_element_by_id
import time

class BasePage():
    def __init__(self, driver, screenshot_folder, logger):
        self.driver = driver
        self.screenshot_folder = screenshot_folder
        self.logger = logger
        self.take_screenshot()
    
    def take_screenshot(self):
        url = self.driver.current_url
        page_name = os.path.basename(url)
        file_name = f"{page_name}_screenshot.png"
        full_path = os.path.join(self.screenshot_folder, file_name)
        self.driver.save_screenshot(full_path)
    
    def check_page_url(self,page_name):
        """
        Checks whether we are at the expected page
        """
        current_url = self.driver.current_url
        current_page_name = current_url.split("/")[-1]
        try:
            assert current_page_name == page_name
        except AssertionError as error:
            self.logger.error(f'Current page name: {current_page_name} differs from expected apge name: {page_name}. Youu seem to be at an unexpected page.')
            raise
        else:
            return True

class LoggedInPage(BasePage):
    hamburger_menu_btn_id = 'react-burger-menu-btn'
    logout_link_id = 'logout_sidebar_link'

    def __init__(self, driver, screenshot_folder, logger):
        super().__init__(driver, screenshot_folder, logger)

    def get_hamburger_icon(self):
        return get_element_by_id(self.driver, self.hamburger_menu_btn_id, "Hamburger menu icon")
    
    def click_hamburger_icon(self):
        self.get_hamburger_icon().click()
    
    def click_logout_link(self):
        self.logger.info('trying to log out through hamburger menu link')
        self.click_hamburger_icon()
        time.sleep(1)
        get_element_by_id(self.driver, self.logout_link_id, "Logout link").click()