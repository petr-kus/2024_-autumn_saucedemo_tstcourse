import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..common import Base
from ..TestData import TestData


class Header(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.burger_menu = Header.BurgerMenu(driver)

##### VARIABLEs ---------------------------------

    burger_menu_class = By.CLASS_NAME, "bm-menu"
    class Icons:
        cart = (By.CLASS_NAME, "shopping_cart_link")
        burger_menu = (By.CLASS_NAME,'bm-burger-button')
    class Badges:
        cart = (By.CLASS_NAME, "shopping_cart_badge")

    class BurgerMenu(Base):
        def __init__(self, driver):
            super().__init__(driver)
            self.driver = driver

        open_button = (By.ID,'react-burger-menu-btn')
        cross_close = (By.ID,'react-burger-cross-btn')
        all_items_link = (By.XPATH, "//a[contains(translate(text(), 'AL ITEMS', 'al items'), 'all items')]")
        about_link = (By.XPATH, "//a[contains(translate(text(), 'ABOUT', 'about'), 'about')]")
        logout_link = (By.XPATH,"//a[contains(translate(text(), 'LOGUT', 'logut'), 'logout')]")
        reset_app_state_link = (By.XPATH, "//a[contains(translate(text(), 'REST AP', 'rest ap'), 'reset app')]")

##### KEYWORDs ----------------------------------

        def open(self):
            self.wait_and_click(Header.BurgerMenu.open_button)
            logging.info(f"Opened burger menu.")

        def close(self):
            self.wait_and_click(Header.BurgerMenu.cross_close)
            logging.info(f"Closed burger menu.")

        def check_if_closed(self):
            WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located((Header.burger_menu_class)))
            if self.driver.find_element(*Header.burger_menu_class).is_displayed():
                logging.error(f"Burger menu is NOT closed.")
            else:
                logging.info("Burger menu is not open.")

        
    def go_to_cart_by_clicking_cart_icon(self):
        self.wait_and_click(Header.Icons.cart)
        logging.info(f"Clicked the cart icon.")
        current_url = self.driver.current_url
        if current_url == TestData.urls["cart"]:
            logging.info(f"Clicking the cart icon was successful - current url is '{current_url}'.")
        else:
            logging.error(f"Clicking the cart icon was NOT successful - current url is '{current_url}', but should be '{TestData.urls["cart"]}'.")

    def go_to_about_page_by_link_in_menu(self):
        self.burger_menu.open()
        self.wait_and_click(Header.BurgerMenu.about_link)
        logging.info(f"Clicked the About link in menu.")
        current_url = self.driver.current_url
        if current_url == TestData.urls["about"]:
            logging.info(f"Clicking the About link was successful - current url is '{current_url}'.")
        else:
            logging.error(f"Clicking the About link was NOT successful - current url is '{current_url}', but should be '{TestData.urls["about"]}'.")

    def go_to_inventory_page_by_link_in_menu(self):
        self.burger_menu.open()
        self.wait_and_click(Header.BurgerMenu.all_items_link)
        logging.info(f"Clicked the All items link in menu.")
        current_url = self.driver.current_url
        if current_url == TestData.urls["inventory_page"]:
            logging.info(f"Clicking the All items link was successful - current url is '{current_url}'.")
        else:
            logging.error(f"Clicking the All items link was NOT successful - current url is '{current_url}', but should be '{TestData.urls["inventory_page"]}'.")

    def logout(self):
        self.burger_menu.open()
        self.wait_and_click(Header.BurgerMenu.logout_link)
        if self.driver.current_url == TestData.urls["landing_page"]:
            logging.info(f"Logout successful, back on '{TestData.urls["landing_page"]}'.")
        else:
            logging.error(f"Logout FAILED, not back on '{TestData.urls["landing_page"]}'.")