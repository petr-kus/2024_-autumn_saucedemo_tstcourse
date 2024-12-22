import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class LoggedInPage:
    def __init__(self, page):
        self.page = page

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")
        logger.info("Going to cart.")

    def get_cart_badge_count(self):
        product_count = self.page.inner_text(".shopping_cart_badge")
        logger.info(f"There are {product_count} items on the cart badge.")
        return product_count

    def logout(self):
        self.page.click("#react-burger-menu-btn")
        self.page.click("#logout_sidebar_link")