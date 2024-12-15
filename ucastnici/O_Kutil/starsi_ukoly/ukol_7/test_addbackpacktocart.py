# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddbackpacktocart():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addbackpacktocart(self):
    self.driver.find_element(By.XPATH, "//a[@id=\'item_4_title_link\']/div").click()
    self.driver.find_element(By.XPATH, "//button[@id=\'add-to-cart\']").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'shopping_cart_container\']/a/span").click()
    self.driver.find_element(By.XPATH, "//div[@id=\'page_wrapper\']/footer").click()
  
