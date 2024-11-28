from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

class Test:
  def __init__(self):
    Option = Options()
    Option.add_argument("start-maximized")
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.saucedemo.com/")

  def test_login(self, user:str, password_user:str):
    username = self.driver.find_element(By.ID,'user-name')
    username.send_keys(user) 
    password = self.driver.find_element(By.ID,'password')
    password.send_keys(password_user)
    login_button = self.driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Špatná URL"
    time.sleep(3)

  def test_cart(self):
    # Kliknutí na ikonu košíku (vpravo nahoře)
    cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
    time.sleep(3)

  def test_burger_menu(self):
    # Kliknutí na burger menu
    burger_menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(3)

  def test_logout(self):
    # Kliknutí na Logout v burger menu
    logout = self.driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    time.sleep(3)

  def close_driver(self):
    self.driver.close()

test = Test()

test.test_login("standard_user", "secret_sauce")
test.test_cart()
test.test_burger_menu()
test.test_logout()
test.test_login("problem_user", "secret_sauce")
test.test_burger_menu()
test.test_logout()
test.close_driver()
