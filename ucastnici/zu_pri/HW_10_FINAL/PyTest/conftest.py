import logging
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from .TestData import TestData
from .common import Base
from .PageObjects.Cart import Cart
from .PageObjects.Header import Header
from .PageObjects.InventoryPage import InventoryPage
from .PageObjects.LoginPage import LoginPage

@pytest.fixture (autouse=True, scope="session")
def driver():
    option = Options()
    option.add_argument("--start-maximized")
    driver = TestData.browsers[TestData.chosen_webdriver](option)
    driver.implicitly_wait(2)
    logging.info(f"...initiating {TestData.chosen_webdriver} browser")
    yield driver
    driver.quit()

@pytest.fixture
def base(driver):
    return Base(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def header(driver):
    return Header(driver)

@pytest.fixture
def cart(driver):
    return Cart(driver)

@pytest.fixture
def login_standard(driver, base, login_page, inventory_page):
    """
    """
    base.log_start()
    driver.get(TestData.urls["landing_page"])
    logging.info(f"Going to '{TestData.urls['landing_page']}'")
    
    login_page.fill_in_username(TestData.users["standard_user"]["name"])
    login_page.fill_in_password(TestData.users["standard_user"]["password"])
    login_page.click_login()
    assert inventory_page.is_loaded(), "Login failed or not redirected to Inventory page."