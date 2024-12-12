import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import datetime

class BasePage():
    def __init__(self, driver, screenshot_folder, logger):
        self.driver = driver
        self.screenshot_folder = screenshot_folder
        self.logger = logger
        self.take_screenshot()
    
    def take_screenshot(self):
        url = self.driver.current_url
        page_name = os.path.basename(url)
        now = datetime.datetime.now()
        if not page_name:
            page_name = 'root'
        file_name = f"{page_name}_{now.isoformat().replace(':', '-')}screenshot.png"
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
    
    def get_elements_by(self, by_type:str, identifier, str_name, multiple=False):
        by = getattr(By, by_type.upper())
        try:
            if multiple:
                elements = self.driver.find_elements(by, identifier)
            else:
                elements = self.driver.find_element(by, identifier)            
            return elements
        except NoSuchElementException:
            self.logger.error(f'{str_name} element not found')
            raise

    def click_on_element(self, elements, element_index):
        if element_index < len(elements):
            elements[element_index].click()
        else:
            self.logger.error(f"No element found at index {element_index}. Total elements found: {len(elements)}")

class LoggedInPage(BasePage):
    hamburger_menu_btn_id = 'react-burger-menu-btn'
    logout_link_id = 'logout_sidebar_link'

    def __init__(self, driver, screenshot_folder, logger):
        super().__init__(driver, screenshot_folder, logger)

    def get_hamburger_icon(self):
        return self.get_elements_by('ID',self.hamburger_menu_btn_id, "Hamburger menu icon")
    
    def click_hamburger_icon(self):
        self.get_hamburger_icon().click()
    
    def click_logout_link(self):
        self.logger.info('trying to log out through hamburger menu link')
        self.click_hamburger_icon()
        time.sleep(1)
        self.get_elements_by('ID',self.logout_link_id,  "Logout link").click()
