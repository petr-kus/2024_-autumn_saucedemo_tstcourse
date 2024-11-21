from selenium import webdriver

#TODO Lektor - no tak :-) to je chyba v mém skriptu... . (zbytečný import šlo to odebrat)
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

Option = Options()
Option.add_argument("start-maximized")
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID,'user-name')

#TODO Lektor - no tak :-) to je chyba v mém skriptu... . (to je zbytecny krok)
username = driver.find_element(By.ID,'user-name')

username.send_keys('standard_user') 
password = driver.find_element(By.ID,'password')
password.send_keys('secret_sauce')
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

#TODO Lektor - lepsi je nemit tam sleepy nebo je mit parametrizovane. (ale chapu ze je to ucelne...)
time.sleep(5)

hamburger_menu = driver.find_element(By.ID,'react-burger-menu-btn')
hamburger_menu.click()

time.sleep(5)
#TODO Lektor - presne zde je ideali misto na WAIT!
logout = driver.find_element(By.ID,'logout_sidebar_link')
logout.click()

time.sleep(5)

driver.close()

#TODO Lektor - Oki, takove minimalistice odevzdani úlohy, chválím za odevzdaní a dostání se do tohto stavu!
# na lekci si řekneme příklady co se dalo, udělat na víc... A pokročíme dál.
# není tam nikde assert! (test toho zase tolik neověří...)
