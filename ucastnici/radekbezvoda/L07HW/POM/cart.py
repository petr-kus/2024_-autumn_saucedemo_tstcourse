from .base import LoggedInPage

class Cart(LoggedInPage):
    page_url = 'cart.html'
    checkout_id = 'checkout'
    cart_item_id = 'cart_item'
    def __init__(self, driver, screenshot_folder, logger) -> None:
        logger.info('at the cart page')
        super().__init__(driver, screenshot_folder, logger)


    def click_checkout(self):
        self.get_elements_by('ID', self.checkout_id, "checkout button").click()

    def get_cart_items(self):
        return self.get_elements_by('CLASS_NAME', self.cart_item_id, "cart item block", multiple=True)
