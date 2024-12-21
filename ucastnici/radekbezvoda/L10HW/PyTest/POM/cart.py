from .base import LoggedInPage

class Cart(LoggedInPage):
    page_url = 'cart.html'
    checkout_id = 'checkout'
    cart_item_id = 'cart_item'
    remove_xpath = "//button[contains(text(),'Remove')]"
    continue_shopping_id = 'continue-shopping'
    def __init__(self, driver, screenshot_folder, logger) -> None:
        logger.info('at the cart page')
        super().__init__(driver, screenshot_folder, logger)


    def click_checkout(self):
        self.get_elements_by('ID', self.checkout_id, "checkout button").click()

    def get_cart_items(self):
        return self.get_elements_by('CLASS_NAME', self.cart_item_id, "cart item block", multiple=True)
    
    def remove_items(self):
        self.logger.info(f'removing items from cart')
        elements = self.get_elements_by('XPATH', self.remove_xpath,  'add to cart buttons', multiple=True)
        self.logger.info(f'found {len(elements)} in cart, attempting to remove them')

        for index in range(len(elements)):
            self.click_on_element(elements, index)
        self.take_screenshot()

    def click_continue_shopping(self):
        self.get_elements_by('ID', self.continue_shopping_id, "continue shopping button").click()
