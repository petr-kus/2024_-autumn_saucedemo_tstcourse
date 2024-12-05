from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging 


login_btn = (By.ID,'login-button')
LoginPage = {'username':(By.ID,'user-name')}
field_password = 'password'

class login_page():
      login_button = (By.ID,'login-button')
      password = (By.ID,'password')
      username = (By.ID,'user-name')

# základ myšlenky pro použití POM - page object modelu:
# (všimněte si nápovědy přes tečku při použití!)
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

def slowdown(seconds=2):
        time.sleep(seconds)

class page:

    driver = None

    def Load_page(self, page):
        Option = Options()
        Option.add_argument("start-maximized")
        self.driver = webdriver.Chrome()
        logging.info(f"Starting browser chrome...")
        self.driver.get(page)
    
    def Login_user(self, username, password):
        user = self.driver.find_element(*LoginPage['username'])
        user.send_keys(username)
        slowdown()
        user_password = self.driver.find_element(By.ID, field_password)
        user_password.send_keys(password)
        slowdown()
        login_button = self.driver.find_element(*login_btn)
        login_button.click()

    def Browser_is_opened(self):
        if self.driver == None:
            Option = Options()
            Option.add_argument("start-maximized")
            self.driver = webdriver.Chrome()
            logging.info("openening browser")
        else:
             logging.info("Browser is already opened")
        return self.driver
    
    def Close_Browser(self):
            self.driver.close()
            self.driver.quit()