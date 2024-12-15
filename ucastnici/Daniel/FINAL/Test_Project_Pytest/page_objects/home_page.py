from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    HOME_PAGE_URL = "inventory.html"

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Opens the home page."""
        self.open_url(self.HOME_PAGE_URL)
        self.logger.info(f"Home page was opened.")



