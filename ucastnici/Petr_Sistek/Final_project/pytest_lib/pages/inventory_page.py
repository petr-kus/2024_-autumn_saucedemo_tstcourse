from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
    
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()