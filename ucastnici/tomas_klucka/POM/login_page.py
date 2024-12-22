from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging

class LoginPage(BasePage):
 def __init__(self, driver):
  super().__init__(driver)
  self.username_field = (By.ID, 'user-name')
  self.password_field = (By.ID, 'password')
  self.login_button = (By.ID, 'login-button')

 def perform_login(self, username, password):
  try:
   logging.info(f"logging in as user: '{username}'")
   self.wait_for_element(*self.username_field).send_keys(username)
   self.wait_for_element(*self.password_field).send_keys(password)
   self.wait_for_clickable(*self.login_button).click()
   logging.info("login successful.")
   
  except Exception as error:
   logging.error(f"error during login as user '{username}': '{error}'")
   raise