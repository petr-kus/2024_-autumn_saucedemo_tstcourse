import logging
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import Base
from TestData import TestData


class InventoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

##### VARIABLEs ---------------------------------
    
    url_keyword = "inventory"
    tested_item = TestData.inventory_items[TestData.chosen_item]
    class Buttons:
        class AddItem:
            chosen_item = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., '{TestData.inventory_items[TestData.chosen_item]}')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            backpack = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Backpack')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            bike_light = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Light')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            bolt_t_shirt = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Bolt')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            fleece_jacket = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Jacket')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            onesie = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Onesie')]//button[contains(translate(text(),'A','a'),'add to cart')]")
            red_t_shirt = (By.XPATH, f"//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Red')]//button[contains(translate(text(),'A','a'),'add to cart')]")
    
##### KEYWORDs ----------------------------------

    def go_to(self):
        self.driver.get(TestData.urls["inventory_page"])
        logging.info(f"Redirected to '{TestData.urls["inventory_page"]}'.")

    def check_needed_url(self):
        if self.driver.current_url != TestData.urls["inventory_page"]:
            logging.info(f"Not on the correct URL. Navigating to '{TestData.urls["inventory_page"]}'.")
            self.driver.get(TestData.urls["inventory_page"])
    
    def is_loaded(self)-> bool:
        logging.info(f"Redirected to Inventory page.")
        return WebDriverWait(self.driver, 2).until(EC.url_contains(InventoryPage.url_keyword))
  
    def add_chosen_item_to_cart(self):
        self.check_needed_url()
        self.click(InventoryPage.Buttons.AddItem.chosen_item)
        logging.info(f"Added '{InventoryPage.tested_item}' to the cart.")

    def add_random_number_of_items_to_cart(self)-> int:
        self.check_needed_url()
        number_of_items = random.randint(1,len(TestData.inventory_items))
        items = [x for x in range(1, len(TestData.inventory_items) + 1)]
        chosens = random.sample(items, k=number_of_items)
        for each in chosens:
            self.click((By.XPATH, f"//div[@class='inventory_container']//div[contains(text(),'{TestData.inventory_items[each]}')]//following::button[contains(text(),'Add to cart')]"))
            logging.info(f"Clicked the 'add to cart' button for '{TestData.inventory_items[each]}'.")
        items_added = sum([1 for each in chosens])
        logging.info(f"Added '{items_added}' random item(s) to the cart.")
        return items_added

