from selenium import webdriver

# TODO Lektor: zbytecny import... 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")

# Přihlášení uživatele
username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

# Čekání, než se načte stránka po přihlášení
# TODO Lektor: velká pochvala za myšlení na tuto věc... ale je to zbytečné udělá to za tebe Seleium samo... . 
WebDriverWait(driver, 10).until(
    EC.url_contains('inventory.html')
)

# Ověření, zda se správně načetla stránka
# TODO Lektor: velká pochvala za Assert, errorovou hlášku i za pozitivní case log! 
assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL není správná!"
print("Úspěšně přihlášeno a stránka se načetla!")

# Ověření, že produkty jsou zobrazeny
product_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
assert product_name.is_displayed(), "Produkt není zobrazen!"
print("Produkty jsou zobrazeny!")

# Zavření prohlížeče
driver.quit()
# TODO Lektor: pochvala za silnejsi verzi quit a ne close... .
print("Dobrej test Dejve!")
# TODO Lektor: :-)))) - jo jo. Vice na lekci. 