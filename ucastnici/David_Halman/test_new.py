from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam

def setup_driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

#TODO Lektor - klidne tu mohlo byt open_page - to je lepsi ne? Vic srozumitelny i neprogramatrovi...

def open_url(driver, url):
    driver.get(url)

def login(driver, username, password):
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    #TODO Lektor - mohl byt one liner... driver.find_element(By.ID, 'user-name').send_keys(username)
    password_field = driver.find_element(By.ID, 'password')

    #TODO Lektor - mohlo byt oddeleno bokem... (By.ID, 'password') ... do pom nebo nekde...
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains('inventory.html')
    )
     #TODO Lektor - tady tento wait neni potreba nicmene chvalim za nastudoivani... v kazdem pade stacil by imlicit wait a nehyzdilo bz to tu kod... .

def verify_login_success(driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL není správná!"
    print("Úspěšně přihlášeno a stránka se načetla!")
    #TODO Lektor - no mozna to nepouzijes jen pri prihlasovani takze bych dle toho zmenil komentar... . jinak pochvala... .

def verify_products_are_displayed(driver):
    product_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert product_name.is_displayed(), "Produkt není zobrazen!"
    print("Produkty jsou zobrazeny!")

def close_driver(driver):
    driver.quit()
    print("Test dokončen a prohlížeč byl zavřen.")

if __name__ == "__main__":
    driver = setup_driver()
    #TODO Lektor - kdby byl pouzit global driver nemusis si to furt predavat
    try:
        open_url(driver, "https://www.saucedemo.com/")
        login(driver, 'standard_user', 'secret_sauce')
        verify_login_success(driver)
        verify_products_are_displayed()
        #TODO Lektor - posledni vefikace nema drvier... nefunguje...
        #TODO Lektor - krasny zapis ze? celkove...mohlo byt jeste pouzito logovani do souboru treba nebo vic oddelit POM...
    finally:
        close_driver(driver)