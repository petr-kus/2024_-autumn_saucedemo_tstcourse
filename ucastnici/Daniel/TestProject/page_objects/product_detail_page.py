from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailPage(BasePage):

    PRODUCT_ID = 4
    PRODUCT_DETAIL_PAGE_URL = f"inventory-item.html?id={PRODUCT_ID}"
    
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