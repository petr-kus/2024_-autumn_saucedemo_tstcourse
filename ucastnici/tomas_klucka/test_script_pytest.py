from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest
    
@pytest.fixture(scope='module')
def browser():
  Option = Options()
  Option.add_argument("--disable-features=PasswordManager")
  Option.add_argument("start-maximized")
  driver = webdriver.Chrome(options=Option)
  driver.get("https://www.saucedemo.com/")
  yield driver
  driver.quit()

class LoginPage:
  def __init__(self, driver):
    self.driver = driver

  def perform_login(self, username, password):
    self.username = username
    self.password = password
    self.username_field = WebDriverWait(self.driver, 5).until(
    EC.presence_of_element_located((By.ID, 'user-name'))
)
    self.password_field = self.driver.find_element(By.ID, 'password')
    self.login_button = self.driver.find_element(By.ID, 'login-button')

    try:
      logging.info(f"logging in as user: '{self.username}'")

      self.username_field.send_keys(self.username)
      self.password_field.send_keys(self.password)
      self.login_button.click()
      logging.info("login successfull")

    except Exception as error:
      logging.error(f"error during login as user '{self.username}': '{error}'")
      raise

class Navigation:
  def __init__(self, driver):
    self.driver = driver
    self.menu_button_id = 'react-burger-menu-btn'
    self.menu_items = {
       "inventory": "inventory_sidebar_link",
      "about_page": "about_sidebar_link",
       "logout": "logout_sidebar_link"
    }

  def open_menu(self):
    try:
      menu_button = WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable((By.ID, self.menu_button_id))
      )
      menu_button.click()
      logging.info(f"menu opened successfully")

    except Exception as error:
      logging.error(f"error during clicking on '{menu_button}': '{error}'")
      raise

  def open_menu_item(self, menu_item):
    if menu_item not in self.menu_items:
      logging.error(f"menu item '{menu_item}' does not exist")
      raise ValueError(f"invalid menu item: '{menu_item}'")

    try:
      menu_item_id = self.menu_items[menu_item]
      menu_element = WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable((By.ID, menu_item_id))
      )
      menu_element.click()
      logging.info(f"clicked on menu item '{menu_item}'")
      
    except Exception as error:
      logging.error(f"error while clicking on menu item '{menu_item}': {error}")
      raise
    
@pytest.mark.parametrize("username, password", [
  ("problem_user", "secret_sauce"),
])

def test_user_login(browser, username, password):
  login_page = LoginPage(browser)
  login_page.perform_login(username, password)
  assert "inventory.html" in browser.current_url, f"login failed for '{username}'"

@pytest.mark.parametrize("menu_item", [
  "about_page",
])

def test_menu_navigation(browser, menu_item):
  navigation = Navigation(browser)
  navigation.open_menu()
  navigation.open_menu_item(menu_item)
  assert "about.html" in browser.current_url, f"navigation to '{menu_item}' failed"