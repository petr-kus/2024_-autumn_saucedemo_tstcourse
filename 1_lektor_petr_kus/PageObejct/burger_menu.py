
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class burger_menu():
      
      all_items = (By.XPATH, "//a[text()='All Items']")
      about = (By.XPATH,"//a[text()='About']")
      logout = (By.XPATH,"//a[text()='Logout']")
      reset_app = (By.XPATH,"//a[text()='Reset App State']")
      cross_close = (By.ID,'react-burger-cross-btn')
      open_button = (By.ID,'react-burger-menu-btn')
      
      def __init__(self, driver):
           self.driver = driver  

      def open(self):
           logging.info('Opening burger menu')
           self.driver.find_element(*burger_menu.open_button).click()
           #počkání až se otevře menu...
           WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(burger_menu.cross_close))