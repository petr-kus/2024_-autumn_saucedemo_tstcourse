from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    CART_PAGE_URL = "cart.html"
    
    CART_ITEM = (By.CLASS_NAME, "cart_item")
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

    def get_cart_items_count(self):
        """Finds all items in the cart and returns the number of items found. If the empty cart message is visible, return 0."""
        try:
            """
            empty_cart_message = self.is_element_visible(self.EMPTY_CART_MESSAGE)
            if empty_cart_message:
                self.logger.info("Cart is empty, as indicated by the empty cart message.")
                return 0
            """
            cart_items = self.find_elements(self.CART_ITEM)
            number_of_cart_items = len(cart_items)
            self.logger.info(f"Found '{number_of_cart_items}' item(s) in the cart.")
            
            return number_of_cart_items
        
        except Exception as e:
            self.logger.error(f"Failed to get cart items count. Error: {str(e)}")
            return 0


    def remove_item_from_cart(self, item_remove_button = None):
        """Removes product item from the cart"""
        self.logger.info(f"Process of removing the item from the cart initiated.")
        item_remove_button = item_remove_button or self.REMOVE_BUTTON
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