import os  # For manipulation with files and folders
from datetime import datetime
from urllib.parse import urlparse
import re

from utilities.logger import get_logger # For logging
from utilities.wait import wait_for_element # For explicit waiting

from utilities.driver_factory import get_driver #    VYMAZAT!!!
from utilities.logger import get_logger # For logging

from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage

import time

from selenium.webdriver.common.by import By

driver = get_driver()
logger = get_logger("TEST")

login_page = LoginPage(driver)

login_page.logger.info("Login page instance created.")

login_page.open_url("https://www.saucedemo.com/")

login_page.login()

time.sleep(5)

driver.quit()