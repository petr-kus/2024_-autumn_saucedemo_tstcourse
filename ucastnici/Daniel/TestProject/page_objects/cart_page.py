from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    CART_PAGE_URL = "cart.html"
    
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    ADD_BUTTON = (By.ID, "add-to-cart_button")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CONTINUE_TO_CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the cart page."""
        self.open_url(self.CART_PAGE_URL)
        self.logger.info(f"Cart page was opened.")

    def remove_item_from_cart(self, item_remove_button = REMOVE_BUTTON):
        """Removes product item from the cart"""
        self.logger.info(f"Process of removing the item from the cart initiated.")
        self.click(item_remove_button)
        self.logger.info(f"Clicked on the 'Remove' button.")
    
    def proceed_to_checkout(self):
        """Clicks on the "Checkout button" and continues to the checkout page."""
        self.logger.info(f"Process of proceeding to the checkout initiated.")
        self.click(self.CONTINUE_TO_CHECKOUT_BUTTON)
        self.logger.info(f"Clicked on the 'Checkout' button.")
    
    def continue_shopping(self):
        """Clicks on the "Continue Shopping" button and continues to the product category page / homepage."""
        self.logger.info(f"Continue shopping process initiated.")
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        self.logger.info(f"Clicked on the 'Continue Shopping' button.")