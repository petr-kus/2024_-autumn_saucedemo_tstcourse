#!/bin/bash

# Aktivace virtuálního prostředí
# source venv/bin/activate

# Aktualizace pipu na nejnovější verzi
# python3 -m pip install --upgrade pip

# Instalace závislostí z requirements.txt
# python3 -m pip install -r requirements.txt

# Aktualizace requirements.txt (uložení nainstalovaných balíčků)
# python3 -m pip freeze > requirements.txt


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

time.sleep(3)

driver.close()