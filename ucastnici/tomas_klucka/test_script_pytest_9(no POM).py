from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest

@pytest.fixture(scope='function')
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
    self.username_field = WebDriverWait(self.driver, 3).until(
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
    self.about_page_id = 'about_sidebar_link'
    self.logout_id = 'logout_sidebar_link'
    
  def open_menu(self):
    try:
      self.menu_button = WebDriverWait(self.driver, 3).until(
        EC.element_to_be_clickable((By.ID, self.menu_button_id))
      )
      self.menu_button.click()
      logging.info(f"menu opened successfully")

    except Exception as error:
      logging.error(f"error during clicking on '{self.menu_button}': '{error}'")
      raise

  def open_about_page(self):
    try:
      self.about_page_button = WebDriverWait(self.driver, 3).until(
        EC.element_to_be_clickable((By.ID, self.about_page_id))
      )
      self.about_page_button.click()
      logging.info(f"clicked on menu item '{self.about_page_button}'")
      
    except Exception as error:
      logging.error(f"error while clicking on menu item '{self.about_page_button}': {error}")
      raise
    
  def perform_logout(self):
    try:
      self.logout_button = WebDriverWait(self.driver, 3).until(
        EC.element_to_be_clickable((By.ID, self.logout_id))
      )
      self.logout_button.click()
      logging.info(f"successfully performed logout'")
      
    except Exception as error:
      logging.error(f"error while performing logout': {error}")
      raise

@pytest.mark.parametrize("username, password", [
  ("standard_user", "secret_sauce"),
  ("problem_user", "secret_sauce"),
  ("error_user", "secret_sauce"),
])

def test_user_login(browser, username, password):
  login_page = LoginPage(browser)
  login_page.perform_login(username, password)
  assert "inventory.html" in browser.current_url, f"login failed for '{username}'"

@pytest.mark.parametrize("username, password", [
  ("standard_user", "secret_sauce"),
  ("problem_user", "secret_sauce"),
  ("error_user", "secret_sauce"),
])

def test_login_and_about_page(browser, username, password):
  # login
  login_page = LoginPage(browser)
  login_page.perform_login(username, password)
  assert "inventory.html" in browser.current_url, f"login failed for '{username}'"
  
  # navigation to about page
  navigation = Navigation(browser)
  navigation.open_menu()
  navigation.open_about_page()
  assert "404 Not Found" not in browser.page_source, f"navigation to About page failed"

@pytest.mark.parametrize("username, password", [
  ("standard_user", "secret_sauce"),
  ("problem_user", "secret_sauce"),
  ("error_user", "secret_sauce"),
])

def test_user_login_logout(browser, username, password):
  # login
  login_page = LoginPage(browser)
  login_page.perform_login(username, password)
  assert "inventory.html" in browser.current_url, f"login failed for '{username}'"
  
  #logout
  navigation = Navigation(browser)
  navigation.open_menu()
  navigation.perform_logout()
  assert "saucedemo.com" in browser.current_url, f"logout failed"
  