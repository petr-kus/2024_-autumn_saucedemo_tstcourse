from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductCategoryPage(BasePage):

    PRODUCT_CATEGORY_PAGE_URL = "/inventory.html"

    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    PRODUCT_ADD_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the product category page."""
        self.open_url(self.PRODUCT_CATEGORY_PAGE_URL)
        self.logger.info(f"Product category page was opened.")
    
    def show_product_detail(self, product_name_image = PRODUCT_IMAGE):
        """Shows product detail by clicking on the product image."""
        self.logger.info(f"Process of showing product detail initiated.")
        self.click(self.PRODUCT_IMAGE)
        self.logger.info(f"Clicked on the product image.")

    def add_product_to_cart(self, product_name_button = PRODUCT_ADD_CART_BUTTON):
        """Adds the product to the cart by clicking on the "Add to cart" button."""
        self.logger.info(f"Process of adding the product to the cart initiated.")
        self.click(self.PRODUCT_ADD_CART_BUTTON)
        self.logger.info(f"Clicked on the 'Add to cart' button.")
    
