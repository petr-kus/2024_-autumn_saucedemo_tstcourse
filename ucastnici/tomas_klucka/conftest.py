import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

@pytest.fixture(scope='function')
def browser():
 options = Options()
 options.add_argument("--disable-features=PasswordManager")
 options.add_argument("start-maximized")
 driver = webdriver.Chrome(options=options)
 driver.get("https://www.saucedemo.com/")
 yield driver
 driver.quit()

def pytest_configure():
 logging.basicConfig(
 filename='my_log_pytest.log',
  level=logging.DEBUG,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
 )