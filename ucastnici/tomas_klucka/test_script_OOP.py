from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import logging

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam

logging.basicConfig(filename='my_log.log', level=logging.DEBUG)
#TODO Lektor - chvalim logovani bokem... 

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
  #TODO Lektor - hard sleepy jsou antipatern - melo by byt parametrizovano bokem... .
  self.driver.quit()

class LoginPage:
 #TODO Lektor - zde to má správně být! (koukni níže)
 #user_name = user_name
 #password = password
 #username_field = self.driver.find_element(By.ID, 'user-name')
 #password_field = self.driver.find_element(By.ID, 'password')
 #login_button = self.driver.find_element(By.ID, 'login-button')
 #...

 def __init__(self, driver):
  self.driver = driver

 def login(self, user_name, password):
  self.user_name = user_name
  self.password = password
  self.username_field = self.driver.find_element(By.ID, 'user-name')
  self.password_field = self.driver.find_element(By.ID, 'password')
  self.login_button = self.driver.find_element(By.ID, 'login-button')
  #TODO Lektor - chavlim nice POM! ale ma to byt nahore jako parametry toho objektu!

  try:
   logging.info(f"logging in as user: '{self.user_name}'")
   #TODO Lektor - chvalim logovani!

   self.username_field.send_keys(self.user_name)
   self.password_field.send_keys(self.password)
   self.login_button.click()
   logging.info("login successfull")
   #TODO Lektor - no to uplne bez assertu tict neumime ze? Co kdyz jsme zadali invalid udaje!

  except Exception as error:
   logging.error(f"error during login as user '{self.user_name}': '{error}'")
   raise
  #TODO Lektor - trosku me stve tovje zarovnavani... pouzival bych aspon 4 mezery jako tab... . at se vse nejevi na stejne urovni! v Pythonu je to dulezity!

class Navigation:
 def __init__(self, driver, menu_button, **menu_items):
  self.menu_items = menu_items
  self.menu_button = menu_button
  self.driver = driver

 def open_menu(self):
  try:
   menu_button = self.driver.find_element(By.ID, self.menu_button)
   menu_button.click()
   logging.info(f"menu '{menu_button}' clicked successfully")

  except Exception as error:
    logging.error(f"error during clicking on '{menu_button}': '{error}'")
    raise

 def open_menu_item(self, menu_item_name):
  try:
   if menu_item_name not in self.menu_items:
    logging.error(f"menu item '{menu_item_name}' does not exist")
    raise ValueError(f"invalid menu item: '{menu_item_name}'")

   # waiting until hamburger menu opens
   self.driver.implicitly_wait(2)

   menu_item_id = self.menu_items[menu_item_name]
   menu_item = self.driver.find_element(By.ID, menu_item_id)
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
 #TODO Lektor - chvalim oddeleni testovacich dat...  nicmene  menu_items melo byt asi spis definovany v navigation clase.. .

 browser = Browser(test_page)
 browser.setup()
 #TODO Lektor - a co kdyby initi bylo uz v setupu a setup se jmenoval open_page ...  global browser = Browser.open_page(test_page)
 #TODO kdyz by byl global ani by jsi si to dal nemusel predavat

 try:
  login_problem_user = LoginPage(browser.driver)
  login_problem_user.login('problem_user', 'secret_sauce')

  nav = Navigation(browser.driver, menu_button, **menu_items)
  nav.open_menu()
  nav.open_menu_item("about_page")

  #TODO Lektor - pokud by to bylo vse definovano jak jsme se snazil naznacit vyse a na leck... tento zapis by se dal udelat lepsi treba..
  #
  #login_page.login('problem_user', 'secret_sauce')
  #menu.go_to("about_page")
  #
  #jen 2 radky a srozumitelnejsi... a delaji to stejny...

 finally:
  browser.close()
 
if __name__ == "__main__":
 main()

 #TODO Lektor - celkove prochazi/selhava s heslem bez hesla... no docela dobre. Neoveruje se nactena stranka about.. projde se spatnyma udajama ale jen do dalsiho stepu. Not bad.. .