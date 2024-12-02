import logging
import inspect

from common import Base
from TestData import TestData
from PageObjects.Cart import Cart
from PageObjects.Header import Header
from PageObjects.InventoryPage import InventoryPage
from PageObjects.LoginPage import LoginPage


class Tests(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart = Cart(self.driver)
        self.header = Header(self.driver)
    
    def log_start(self):
        test_name = inspect.currentframe().f_back.f_code.co_name
        logging.info(f"Starting test: {test_name}")

##### TESTs ----------------------------------

    def login_test(self):
        """
        """
        self.log_start()
        self.login_page.fill_in_username()
        self.login_page.fill_in_password()
        self.login_page.click_login()
        assert self.inventory_page.is_loaded(), "Login failed or not redirected to Inventory page."

    def add_item_from_inventory_page_to_buy_test(self):
        """
        WIP, would continue checkout, but for now it removes all items
        """
        self.log_start()
        self.inventory_page.add_chosen_item_to_cart()
        self.cart.check_if_chosen_item_is_in_cart()
        self.cart.click_checkout()
        self.cart.make_empty()
        self.cart.check_number_of_items()
    
    def add_random_number_of_items_and_than_remove_all_test(self):
        """
        """
        self.log_start()
        self.inventory_page.add_random_number_of_items_to_cart()
        self.cart.check_number_of_items()
        self.cart.make_empty()
        items_in_cart = self.cart.check_number_of_items()
        if items_in_cart == 0:
            logging.info(f"Test successfull - number of items in cart is '{items_in_cart}'.")
        else:
            logging.error(f"Test FAILED - number of items in cart is '{items_in_cart}'.")
    
    def add_random_number_of_items_and_count_them_in_cart_test(self):
        """
        """
        self.log_start()
        number_of_random_items_added = self.inventory_page.add_random_number_of_items_to_cart()
        items_in_cart = self.cart.check_number_of_items()
        if  items_in_cart == number_of_random_items_added:
            logging.info(f"Number of items in cart ('{items_in_cart}') does equal number of items chosen for adding ('{number_of_random_items_added}').")
        else:
            logging.error(f"Check for number of items in cart being the same as number of items added FAILED: Expected '{number_of_random_items_added}' items in the cart, but found '{items_in_cart}'.")
        
    def logout_test(self):
        self.log_start()
        self.header.logout()

    def burger_menu_open_close_test(self):
        """
        """
        self.log_start()
        self.header.burger_menu.open()
        self.header.burger_menu.close()
        self.header.burger_menu.check_if_closed()
    
    def burger_menu_links_test(self):
        """
        """
        self.log_start()
        self.cart.go_to()
        self.header.burger_menu.open()
        self.header.go_to_inventory_page_by_link_in_menu()
        self.header.go_to_inventory_page_by_link_in_menu()
        self.header.go_to_about_page_by_link_in_menu()
        self.inventory_page.go_to()
        logging.info(f"Redirected back to '{TestData.urls["inventory_page"]}'.")