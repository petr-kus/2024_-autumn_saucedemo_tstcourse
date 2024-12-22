from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

class NavigationPage(BasePage):
 def __init__(self, driver):
  super().__init__(driver)
  # id's for navigation and items in it
  self.menu_button = (By.ID, 'react-burger-menu-btn')
  self.about_page = (By.ID, 'about_sidebar_link')
  self.logout_button = (By.ID, 'logout_sidebar_link')

 def open_menu(self):
  try:
   logging.info("opening menu")
   self.wait_for_clickable(*self.menu_button).click()
  except Exception as error:
   logging.error(f"error while clicking on menu button '{error}'")
   raise

 def open_about_page(self):
  try:
   logging.info("opening about page")
   self.wait_for_clickable(*self.about_page).click()
  except Exception as error:
   logging.error(f"error while opening about page: '{error}'")
   raise

 def perform_logout(self):
  try:
   logging.info("performing logout")
   self.wait_for_clickable(*self.logout_button).click()
  except Exception as error:
   logging.error(f"error while logout: '{error}'")
   raise
