from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

from urllib.parse import urlparse, parse_qs

class ProductDetailPage(BasePage):

    PRODUCT_ID = 4
    PRODUCT_DETAIL_PAGE_URL = f"inventory-item.html?id={PRODUCT_ID}"
    
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
    PRODUCT_PHOTO = (By.CLASS_NAME, "inventory_details_img")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_details_price")
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, "inventory_details_desc")
    PRODUCT_ADD_CART_BUTTON = (By.ID, "add-to-cart")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self, product_id = None):
        """Opens the product detail page by product ID."""
        product_id = product_id or self.PRODUCT_ID
        self.open_url(self.PRODUCT_DETAIL_PAGE_URL)
        self.logger.info(f"Product detail page was opened.")
    
    def add_product_to_cart(self):
        """Adds the product to the cart by clicking on the "Add to cart" button."""
        self.logger.info(f"Process of adding the product to the cart initiated.")
        self.click(self.PRODUCT_ADD_CART_BUTTON)
        self.logger.info(f"Clicked on the 'Add to cart' button.")
    
    def get_product_id_from_url(self):
        """Extracts product ID from URL of the product detail page as an number (integer)."""
        url = self.get_current_url()
        self.logger.info(f"Extracting product ID from actual URL: '{url}'")
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        product_id = int(query_params.get('id', [None])[0])

        if product_id is None:
            self.logger.error("Product ID not found in the URL. URL is missing the 'id' parameter.")
        else:
            self.logger.info(f"Extracted product ID: '{product_id}'")

        return product_id
    
    def verify_product_id_in_url(self, product_id = None):
        """
        Verifies if the given product ID is present in the URL.

        :param product_id: The ID of the product to check in the URL.
        :return: True if the product ID is in the URL, False otherwise.
        """
        product_id = product_id or self.get_product_id_from_url()

        if product_id is None:
            self.logger.error("Cannot verify product ID as it is missing from the URL.")
            return False