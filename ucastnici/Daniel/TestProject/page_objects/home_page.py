from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    HOME_PAGE_URL = "/inventory.html"

    NAVIGATION_MENU_OPEN = (By.ID, "react-burger-menu-btn")
    NAVIGATION_MENU_ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    NAVIGATION_MENU_ABOUT = (By.ID, "about_sidebar_link")
    NAVIGATION_MENU_LOGOUT = (By.ID, "logout_sidebar_link")
    NAVIGATION_MENU_RESET = (By.ID, "reset_sidebar_link")
    NAVIGATION_MENU_CLOSE = (By.ID,"react-burger-cross-btn")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Opens the home page."""
        self.open_url(self.HOME_PAGE_URL)
        self.logger.info(f"Home page was opened.")

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



