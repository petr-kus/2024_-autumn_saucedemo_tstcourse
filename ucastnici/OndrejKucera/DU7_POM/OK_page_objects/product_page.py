# page_objects/product_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ProductPage:
    """Page Object for the Product Page of the application."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.product_selector_template = 'item_{}_title_link'
        self.add_to_cart_button = (By.ID, 'add-to-cart')
        self.back_to_products_button = (By.ID, 'back-to-products')
        self.cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
        self.remove_button = (By.ID, 'remove')

    def add_product_to_cart(self, product_index: int):
        """Add a product to the cart by its index."""
        product_id = self.product_selector_template.format(product_index)
        self.driver.find_element(By.ID, product_id).click()
        self.driver.find_element(*self.add_to_cart_button).click()
        self.driver.find_element(*self.back_to_products_button).click()

    def remove_product_from_cart(self, product_index: int):
        """Remove a product from the cart by its index."""
        product_id = self.product_selector_template.format(product_index)
        self.driver.find_element(By.ID, product_id).click()
        self.driver.find_element(*self.remove_button).click()
        self.driver.find_element(*self.back_to_products_button).click()
    
    def get_cart_badge(self):
        """Get the icon of items in the shopping cart."""
        element = self.driver.find_element(*self.cart_badge)
        return element


    def get_cart_badge_count(self) -> int:
        """Get the number of items in the shopping cart."""
        return int(self.driver.find_element(*self.cart_badge).text)