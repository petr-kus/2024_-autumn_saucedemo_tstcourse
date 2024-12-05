from selenium.webdriver.common.by import By
import logging

class AddToBackpack:
    def __init__(self, driver):
        self.driver = driver
        self.product_locators = {
            "Sauce Labs Backpack": (By.XPATH, "//a[@id='item_4_title_link']/div"),
            "Sauce Labs Bike Light": (By.XPATH, "//a[@id='item_0_title_link']/div"),
            "Sauce Labs Bolt T-Shirt": (By.XPATH, "//a[@id='item_1_title_link']/div"),
            "Sauce Labs Fleece Jacket": (By.XPATH, "//a[@id='item_5_title_link']/div"),
            "Sauce Labs Onesie": (By.XPATH, "//a[@id='item_2_title_link']/div"),
            "Test.allTheThings() T-Shirt (Red)": (By.XPATH, "//a[@id='item_3_title_link']/div"),
        }
        self.add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
        self.cart_icon = (By.XPATH, "//div[@id='shopping_cart_container']/a/span")
        self.cart_item_name = (By.XPATH, "//div[@class='inventory_item_name']")

    def add_product(self, product_name):
        """Add a product to the cart by its name."""
        logging.info(f"Adding product: {product_name}")
        if product_name not in self.product_locators:
            raise ValueError(f"Locator for product '{product_name}' not found.")
        
        product_locator = self.product_locators[product_name]
        self.driver.find_element(*product_locator).click()
        logging.debug(f"Clicked on product: {product_name}")

        self.driver.find_element(*self.add_to_cart_button).click()
        logging.debug(f"Clicked 'Add to cart' for product: {product_name}")

        self.driver.find_element(*self.cart_icon).click()
        logging.debug("Opened the shopping cart")

        cart_item_name = self.driver.find_element(*self.cart_item_name).text
        assert cart_item_name == product_name, f"Expected '{product_name}', but got '{cart_item_name}'"
        logging.info(f"Product '{product_name}' successfully added to cart.")