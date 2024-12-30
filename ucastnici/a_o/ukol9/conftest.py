import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    #TODO Lektor - co logy? Nak zmizeli mezi ulohou 7 a touto :-)
