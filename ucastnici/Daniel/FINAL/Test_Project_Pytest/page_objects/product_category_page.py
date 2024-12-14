from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductCategoryPage(BasePage):

    PRODUCT_CATEGORY_PAGE_URL = "inventory.html"

    PRODUCT_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_ADD_CART_BUTTON = (By.ID, "btn_inventory")

    PRODUCT_ID_IMAGE = (By.ID, "item_4_img_link")
    PRODUCT_ID_ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")


    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the product category page."""
        self.open_url(self.PRODUCT_CATEGORY_PAGE_URL)
        self.logger.info(f"Product category page was opened.")
    
    def show_product_detail(self, product_id_image = None):
        """Shows product detail by clicking on the product image by its locator name by ID."""
        self.logger.info(f"Process of showing product detail initiated.")
        product_id_image = product_id_image or self.PRODUCT_ID_IMAGE
        self.click(product_id_image)
        self.logger.info(f"Clicked on the product image.")

    def add_product_to_cart(self, product_id_add_to_cart_button = None):
        """Adds the product to the cart by clicking on the "Add to cart" button by ID."""
        self.logger.info(f"Process of adding the product to the cart initiated.")
        product_id_add_to_cart_button = product_id_add_to_cart_button or self.PRODUCT_ID_ADD_TO_CART_BUTTON
        self.click(self.PRODUCT_ADD_CART_BUTTON)
        self.logger.info(f"Clicked on the 'Add to cart' button.")
    
