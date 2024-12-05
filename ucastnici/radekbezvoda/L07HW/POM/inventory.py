from POM.common import click_on_element, get_elements_by_xpath, get_element_by_id, get_element_by_class_name
import random
from .base import LoggedInPage

class InventoryPage(LoggedInPage):
    page_url = 'inventory.html'
    id_cart_icon = "shopping_cart_link"
    checkout_id = 'checkout'
    add_to_cart_xpath = "//button[contains(text(),'Add to cart')]"
    add_to_cart_class_name = 'shopping_cart_link'

    def __init__(self, driver, screenshot_folder, logger) -> None:
        super().__init__(driver, screenshot_folder, logger)
        self.logger.info(f'At Inventory page')
        self.check_page_url(self.page_url)

    def add_to_cart_random(self):
        random_integer = random.randint(1, 6)
        random_indexes = random.sample(list(range(6)), random_integer)
        self.logger.info(f'trying to add {str(random_integer)} of elements to cart at random indexes')
        elements = get_elements_by_xpath(self.driver, self.add_to_cart_xpath, self.logger)
        for index in random_indexes:
            click_on_element(self.driver, elements, index)
        self.take_screenshot()
        return random_integer # expected number of items in the cart
    
    def click_cart_icon(self):
        get_element_by_class_name(self.driver, self.add_to_cart_class_name, 'cart icon').click()

    def logout(self):
        self.click_logout_link()

    def click_checkout(self):
        get_element_by_id(self.driver, self.checkout_id, 'checkout').click()
        
    
