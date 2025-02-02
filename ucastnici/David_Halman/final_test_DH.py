import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#TODO Lektor - jsou tu zbytecne a nepouzite importy

#TODO Lektor - vetsinu komentatru k pytetsu jsme uz daval v predchozich ulohach a na lekci. Tak budu strucny. 

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        #TODO Lektor - to meal byt property tridy

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        #TODO Lektor - to melo byt parametrizovano z venku.

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, "inventory_item")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_item_to_cart(self):
        items = self.driver.find_elements(*self.add_to_cart_button)
        if items:
            items[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

#TODO Lektor - tridy meli byt v jinych souborech.

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    service = Service("chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    #TODO Lektor - chvalim vypnuti vyskakovaciho okna. Nicmene pro instalaci sluzby jako service as je potreba admin prava.
    driver.maximize_window()
    yield driver
    driver.quit()
    #TODO Lektor - zde mohl byt pouzit singleton pattern
    #TODO Lektor - mohlo byt v jinem souboru.


def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    #TODO Lektor - to melo byt parametrizovano z venku.
    assert "inventory" in driver.current_url

def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    #TODO Lektor - to melo byt parametrizovano z venku a take prepouzity predchozi test case... .
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) > 0

def test_proceed_to_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    #TODO Lektor - to melo byt parametrizovano z venku a take prepouzity predchozi test case... .
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()
    cart_page.proceed_to_checkout()

    assert "checkout-step-one" in driver.current_url

#TODO Lektor - je tu velmi malo logovani.p