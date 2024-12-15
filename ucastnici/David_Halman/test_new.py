from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def open_url(driver, url):
    driver.get(url)

def login(driver, username, password):
    username_field = driver.find_element(By.ID, 'user-name')
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    WebDriverWait(driver, 10).until(
        EC.url_contains('inventory.html')
    )

def verify_login_success(driver):
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "URL není správná!"
    print("Úspěšně přihlášeno a stránka se načetla!")

def verify_products_are_displayed(driver):
    product_name = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert product_name.is_displayed(), "Produkt není zobrazen!"
    print("Produkty jsou zobrazeny!")

def close_driver(driver):
    driver.quit()
    print("Test dokončen a prohlížeč byl zavřen.")

if __name__ == "__main__":
    driver = setup_driver()
    try:
        open_url(driver, "https://www.saucedemo.com/")
        login(driver, 'standard_user', 'secret_sauce')
        verify_login_success(driver)
        verify_products_are_displayed()
    finally:
        close_driver(driver)