import logging

from selenium.webdriver.common.by import By

from common import Base
from TestData import TestData


class Cart(Base):
    def __init__(self, driver):
        super().__init__(driver)

##### VARIABLEs ---------------------------------
    
    number_of_items_in_cart = (By.XPATH, "//div[@class='cart_list']//div[@class='cart_quantity']")
    tested_item_in_cart = (By.XPATH, f"//div[@class='cart_list']//div[contains(@class, 'inventory_item_name') and contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{TestData.inventory_items[TestData.chosen_item].lower()}')]")
    tested_item = TestData.inventory_items[TestData.chosen_item]
    class Buttons:
        checkout = (By.XPATH, '//*[translate(text(), "CHECKOUT", "checkout")="checkout" and name()="button"]')
        all_remove_buttons_in_cart = (By.XPATH, "//div[@class='cart_list']//button[contains(translate(text(), 'remove', 'REMOVE'), 'REMOVE')]")
        remove_chosen_item = (By.XPATH, f"//div[@class='cart_list']//div[contains(@class, 'cart_item') and .//div[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{TestData.inventory_items[TestData.chosen_item].lower()}')]]//button[contains(translate(text(), 'REMOVE', 'remove'), 'remove')]")

##### KEYWORDs ----------------------------------

    def go_to(self):
        self.driver.get(TestData.urls["cart"])
        logging.info(f"Redirected to '{TestData.urls["cart"]}'.")

    def check_needed_url(self):
        if self.driver.current_url != {TestData.urls["cart"]}:
            logging.info(f"Not on the correct URL. Navigating to '{TestData.urls["cart"]}'.")
            self.driver.get(TestData.urls["cart"])

    def click_checkout(self):
        self.wait_and_click(Cart.Buttons.checkout)
        logging.info(f"Clicked the checkout button in Cart.")
    
    def check_number_of_items(self) -> int:
        self.check_needed_url()
        quantities = self.driver.find_elements(*Cart.number_of_items_in_cart)
        total_quantity = sum(int(number.text) for number in quantities)
        logging.info(f"{total_quantity} item(s) in cart.")
        return total_quantity

    def check_if_chosen_item_is_in_cart(self):
        self.check_needed_url()
        item_in_cart = self.driver.find_elements(*Cart.tested_item_in_cart)
        if item_in_cart:
            logging.info(f"'{Cart.tested_item}' is in cart.")
        else:
            logging.error(f"Item '{Cart.tested_item}' is NOT in cart.'")
    
    def make_empty(self):
        self.check_needed_url()
        remove_buttons = self.driver.find_elements(*Cart.Buttons.all_remove_buttons_in_cart)
        for each in remove_buttons:
            each.click()
            logging.info(f"Clicked the 'remove' button in cart.")

    def remove_chosen_item(self):
        self.check_needed_url()
        self.wait_and_click(Cart.Buttons.remove_chosen_item)
        logging.info(f"Clicked the 'remove' button for '{Cart.tested_item}' cart.")