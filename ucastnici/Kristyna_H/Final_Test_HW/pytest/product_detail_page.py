import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class ProductDetailPage(LoggedInPage):
    def add_to_cart(self):
        self.page.click("#add-to-cart")
        logger.info("Item added to cart via detail page.")

    def go_back_to_inventory(self):
        self.page.click("#back-to-products")
        logger.info("Going back to inventory page.")