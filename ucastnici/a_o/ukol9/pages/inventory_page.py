from selenium.webdriver.common.by import By

class InventoryPage:
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))
