from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    
    CHECKOUT_BUTTON = (By.XPATH, "//button[@name='checkout']")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEMS)
    
    def checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()