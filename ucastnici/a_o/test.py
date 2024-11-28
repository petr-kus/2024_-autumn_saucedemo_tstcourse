
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 

Option = Options()
Option.add_argument("start-maximized")
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#Přihlašovací jméno
username_field = driver.find_element(By.ID, 'user-name')  
username_field.send_keys('problem_user')  

#Heslo
password_field = driver.find_element(By.ID, 'password')  
password_field.send_keys('secret_sauce') 

#Tlačítko pro přihlášení
login_button = driver.find_element(By.ID, 'login-button')  
login_button.click() 

# Čekání, aby se stránka načetla po přihlášení
time.sleep(3)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Kliknutí na dropdown
filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")

actions = ActionChains(driver)
actions.move_to_element(filter_dropdown).click().perform()

# Počkáme, až se zobrazí možnosti v dropdownu
wait = WebDriverWait(driver, 10)
filter_options = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'option')))  # Možnosti v dropdownu jsou <option> tagy

# Seznam hodnot pro jednotlivé možnosti 
options_values = ['az', 'za', 'lohi', 'hilo']
for option in filter_options:
    value = option.get_attribute('value')
    if value in options_values:
        option.click()
        print(f"Kliknuto na možnost: {option.text}")

        # Po kliknutí na filtr počkáme, až se stránka přepne
        time.sleep(2)  
        
        products = driver.find_elements(By.CLASS_NAME, 'product')

        # Získáme názvy produktů, abychom ověřili, zda došlo ke změně
        product_names_before = [product.text for product in products]

        # Získáme produkty po aplikování filtru
        products_after = driver.find_elements(By.CLASS_NAME, 'product')
        product_names_after = [product.text for product in products_after]

        # Kontrolní hlášky
        if product_names_before != product_names_after:
            print(f"Po kliknutí na '{option.text}' se položky změnily.")
        else:
            print(f"Po kliknutí na '{option.text}' se položky nezměnily.")

# Zavření prohlížeče po dokončení testuu
driver.quit()



