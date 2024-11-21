from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Nastavení prohlížeče
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


# Přihlášení
#TODO Lektor: dynamicky wait je nadherny, chvalim za pouziti !!! 
# par poznamek:
# - zde by stacil imlicitni wait
# - pokud tento wait tak ho furt vsude neopakovat a udelat si na to funkci
# - zde je pouziti waitu obecne uplne zbytecne... .

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'user-name'))
)
username.send_keys('standard_user')

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

# Přidání Sauce Labs Backpack do košíku
#TODO Lektor: Zde je krehkost testu spolehas na to ze je to prvni link... co kdyz ne?! 
backpack_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)
backpack_link.click()

#TODO Lektor: Vysoce ocenuji pouziti relativni XPATH, ktera se jeste odkazuje na text! 
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
)
add_to_cart_button.click()

# Přejde do košíku
shopping_cart_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
)
shopping_cart_link.click()

# Ověření, že košík obsahuje 'Sauce Labs Backpack'
item_name_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)
item_name = item_name_element.text
#TODO Lektor: konečně nějaké ověření. Za něji velká pochvala. Libí se mi ověření přesného porduktu. I komentař k assertu při selhání. 
# - v lekci nezapom,enout okomentovat jak test vlastně ověřuje
assert item_name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack', but got '{item_name}'"

# Výstup úspěšné hlášky
print("Test is OK. Sauce Labs Backpack was correctly added to cart.")
#TODO Lektor: Super! Jasny log ze test dobehl! (jen assert ani toto nemusi byt pravda pokud zustanes na strance produktu... - naznaceni krehkosti test automation)

# Zavření prohlížeče
#TODO Lektor: Super - quit je silnější než close. A je lepší...
driver.quit()

#TODO Lektor: Moc krasne zpracovaná úloha. 
# Chválím nepoužívaní waitů
# nechválím, že venv nebyl v ignor listu gitu a pushnul jsi ho do repa :-)!