import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class CartPage(LoggedInPage):
    def get_product_count(self):
        product_count = len(self.page.query_selector_all(".cart_item"))
        logger.info(f"There are {product_count} items in the cart.")
        return product_count

    def go_to_checkout(self):
        self.page.click("#checkout")
        logger.info("Going to checkout page.")