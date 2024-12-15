
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
#TODO Lektor - zbytecny imporet nepouziteho random... ale super ze se chtel nekde pouzit...!
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 


#TODO Lektor - Bylo hodne komentovane na lekci tak jen par poznamek. Neni zmineno vse... .

Option = Options()
Option.add_argument("start-maximized")
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


#Přihlašovací jméno
username = driver.find_element(By.ID, 'user-name')  
#TODO Lektor - ID melo byt oddeleno nekam jinam do promene treba nahoru...
username.send_keys('problem_user')  
#TODO Lektor - mohl byt one liner s oddelenim do dictionary! driver.find_element(*username).send_keys(user['name'])

#Heslo
password = driver.find_element(By.ID, 'password')  
password.send_keys('secret_sauce') 

#Tlačítko pro přihlášení
login_button = driver.find_element(By.ID, 'login-button')  
login_button.click() 

# Čekání, aby se stránka načetla po přihlášení
time.sleep(3)
#TODO Lektor - to cekani na nacteni je zbytecny. Ono si to samo pocka na nacteni a spusti se to a bezi to. 
#TODO Lektor - jedine pro c to tu mit je tyo videt. Sleep by zde vubec na tvrdo napsan byt nemel. Melo by to nak byt parametrizovane nahore treba... .
 
# Kliknutí na dropdown
filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")

actions = ActionChains(driver)
actions.move_to_element(filter_dropdown).click().perform()
#TODO Lektor - je super ze jsi pouzila action chains. Ale tady to nema zrovna duvod jen ti to prodluzuje zapis. 
#TODO Lektor - bez action chains se neobejdes kdyz chces treba pracovat s gestama mysi. Coz tu nikdo nezkousel...

# Počkáme, až se zobrazí možnosti v dropdownu
wait = WebDriverWait(driver, 10)
filter_options = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'option')))  # Možnosti v dropdownu jsou <option> tagy
#TODO Lektor - super ze cekas! Uspornejsi by byl imlicitwait. Ale i takto to jde... . 

# Seznam hodnot pro jednotlivé možnosti 
options_values = ['az', 'za', 'lohi', 'hilo']
for option in filter_options:
    value = option.get_attribute('value')
    if value in options_values:
        option.click()
        print(f"Kliknuto na možnost: {option.text}")

        # Po kliknutí na filtr počkáme, až se stránka přepne
        time.sleep(2)  
        #TODO Lektor - toto mel byt naky wait! NE Sleep! 
        
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
        #TODO Lektor - toto mel byt spis assert. Ale super jak logujes a ze to overujes!
        #TODO Lektor - aspon by melo byt vyhodnoceno co je chyba a co ne.
        #TODO Lektor - poprve se ti nezmeni ani na originalni funkcni strance protoze je to serazeno od a-z!
        #TODO Lektor - na standart usrovi to selze! Takze jsi to tam vlastne netestovala... . Testovat musis obe varianty... .


# Zavření prohlížeče po dokončení testuu
driver.quit()



