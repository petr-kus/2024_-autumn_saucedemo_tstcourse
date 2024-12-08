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
        elements = self.get_elements_by('XPATH', self.add_to_cart_xpath,  'add to cart buttons', multiple=True)
        for index in random_indexes:
            self.click_on_element(elements, index)
        self.take_screenshot()
        return random_integer # expected number of items in the cart
    
    def click_cart_icon(self):
        self.get_elements_by('CLASS_NAME', self.add_to_cart_class_name, 'cart icon').click()

    def logout(self):
        self.click_logout_link()

    def click_checkout(self):
        self.get_elements_by('ID', self.checkout_id, 'checkout').click()
        
    
