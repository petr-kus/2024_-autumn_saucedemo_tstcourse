from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_list = (By.CLASS_NAME, "inventory_item_name")

    def apply_filter(self, filter_value):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.filter_dropdown)
        )
        dropdown.click()
        option = self.driver.find_element(By.XPATH, f"//option[@value='{filter_value}']")
        option.click()
        logging.info(f"Filtr '{filter_value}' byl aplikován.")

    def get_product_names(self):
        return [product.text for product in self.driver.find_elements(*self.product_list)]
