import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class InventoryPage(LoggedInPage):
    def add_to_cart(self, item_button_id):
        self.page.click(f"#{item_button_id}")
        logger.info(f"Item \"{item_button_id}\" added to cart directly.")

    def go_to_detail(self, item_link_id):
        self.page.click(f"#{item_link_id}")
        logger.info(f"Going to item \"{item_link_id}\" detail page.")