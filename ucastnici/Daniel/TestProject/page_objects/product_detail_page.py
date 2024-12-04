from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

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
    
    def open(self):
        """Opens the product detail page."""
        self.open_url(self.PRODUCT_DETAIL_PAGE_URL)
        self.logger.info(f"Product detail page was opened.")
    
    def add_product_to_cart(self, product_name_button = PRODUCT_ADD_CART_BUTTON):
        """Adds the product to the cart by clicking on the "Add to cart" button."""
        self.logger.info(f"Process of adding the product to the cart initiated.")
        self.click(product_name_button)
        self.logger.info(f"Clicked on the 'Add to cart' button.")
    
    def verify_product_id_in_url(self, product_id):
        """
        Verifies if the given product ID is present in the URL.

        :param product_id: The ID of the product to check in the URL.
        :return: True if the product ID is in the URL, False otherwise.
        """
        expected_url_part = f"?id={product_id}"
        current_url = self.get_current_url()

        self.logger.info(f"Verifying if URL contains the product ID '{product_id}'.")
        self.logger.debug(f"Expected URL part: '{expected_url_part}'. Current URL: '{current_url}'.")

        is_valid = expected_url_part in current_url
        if is_valid:
            self.logger.info(f"Product ID '{product_id}' is correctly reflected in the URL.")
        else:
            self.logger.error(f"Product ID '{product_id}' is missing or incorrect in the URL. Current URL: {current_url}")
        return is_valid