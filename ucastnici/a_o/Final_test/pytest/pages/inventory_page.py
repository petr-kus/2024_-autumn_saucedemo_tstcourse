from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title").text