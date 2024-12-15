from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import logging

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)

class Browser:
 def __init__(self, test_page):
  logging.info("Initializing browser setup")
  self.test_page = test_page

 def setup(self):
  Option = Options()
  Option.add_argument("--disable-features=PasswordManager")
  Option.add_argument("start-maximized")
  self.driver = webdriver.Chrome(options=Option)
  self.driver.get(self.test_page)
  logging.info(f"browser opened at '{self.test_page}'")
  return self.driver
  
 def close(self):
  logging.info("closing browser")
  time.sleep(5)
  self.driver.quit()

class User:
 def __init__(self, user_name, password):
  self.user_name = user_name
  self.password = password

 def login(self, driver):
  try:
   logging.info(f"logging in as user: '{self.user_name}'")
   username_field = driver.find_element(By.ID, 'user-name')
   password_field = driver.find_element(By.ID, 'password')
   login_button = driver.find_element(By.ID, 'login-button')

   username_field.send_keys(self.user_name)
   password_field.send_keys(self.password)
   login_button.click()
   logging.info("login successfull")

  except Exception as error:
   logging.error(f"error during login: '{error}'")
   raise

class Nav:
 def __init__(self, **menu_items):
  self.menu_items = menu_items

 def open_menu(self, driver, menu_button):
  try:
   menu_button = driver.find_element(By.ID, menu_button)
   menu_button.click()
   logging.info(f"menu '{menu_button}' clicked successfully")

  except Exception as error:
    logging.error(f"error during clicking on '{menu_button}': '{error}'")
    raise

 def open_menu_item(self, driver, menu_item_name):
  try:
   if menu_item_name not in self.menu_items:
    logging.error(f"menu item '{menu_item_name}' does not exist")
    raise ValueError(f"invalid menu item: '{menu_item_name}'")

   # waiting until hamburger menu opens
   driver.implicitly_wait(2)

   menu_item_id = self.menu_items[menu_item_name]
   menu_item = driver.find_element(By.ID, menu_item_id)
   menu_item.click()

   logging.info(f"successfully clicked on menu item '{menu_item}'")

  except Exception as error:
   logging.error(f"error while clicking on menu item '{menu_item}': {error}")
   raise
  
def main():
 # URL for testing
 test_page = "https://www.saucedemo.com/"

 # all menu options available
 menu_button = 'react-burger-menu-btn'
 menu_items = {
  "inventory": "inventory_sidebar_link",
  "about_page": "about_sidebar_link",
  "logout": "logout_sidebar_link"
 }
 
 browser = Browser(test_page)
 browser.setup()

 user = User('problem_user', 'secret_sauce')
 user.login(browser.driver)

 nav = Nav(**menu_items)
 nav.open_menu(browser.driver, menu_button)
 nav.open_menu_item(browser.driver, "about_page")

 browser.close()
 
if __name__ == "__main__":
 main()



