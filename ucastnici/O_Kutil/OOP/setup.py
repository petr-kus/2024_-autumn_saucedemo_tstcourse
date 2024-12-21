import pytest
from selenium import webdriver
import logging

class Setup:
    @pytest.fixture
    def driver(self):
        logging.info("Starting WebDriver")
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver  # Return the driver to the test
        logging.info("Closing WebDriver")
        driver.quit()