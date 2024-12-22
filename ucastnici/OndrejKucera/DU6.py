
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import logging
import time

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam

# Configure logging
logging.basicConfig(filename='OK_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    """Set up the Chrome WebDriver."""
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

    #TODO Lektor - username_str mohl byt jen username
def login(driver, username_str, password_str):
    """Log in to the application."""
    driver.get("https://www.saucedemo.com/")
    
    username = driver.find_element(By.ID, 'user-name')
    username.send_keys(username_str)
    #TODO Lektor - username_str mohl byt jen "one liner" driver.find_element(By.ID, 'user-name').send_keys(username_str)
    #TODO Lektor - (By.ID, 'user-name') - slo oddelit a definovat bokem.

    password = driver.find_element(By.ID, 'password')
    password.send_keys(password_str)
    
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    logging.info('User logged in successfully.')
    #TODO Lektor - tady mohlo byt overeni assertem ze se nacetla treba naka stranka - protoze tohle ti to vyhodi i kdyz se neprihlasis

def add_to_cart(driver):
    """Add items to the cart."""
    item_ids = [f'item_{i}_title_link' for i in range(6)]
    
    for item_id in item_ids:
        try:
            select_product = driver.find_element(By.ID, item_id)
            select_product.click()
            add_to_cart_button = driver.find_element(By.ID, 'add-to-cart')
            add_to_cart_button.click()
            time.sleep(1)  # Wait for the action to complete
            #TODO Lektor - waity jsou antipatern meli byt parametrizovany bokem
            back_to_main_page = driver.find_element(By.ID, 'back-to-products')
            back_to_main_page.click()
        except NoSuchElementException:
            logging.error(f'Could not find or interact with {item_id}.')
            #TODO Lektor - super chvalim try and except a dobry log...
    
    # Check the shopping cart badge
    shopping_cart_badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
    badge_count = int(shopping_cart_badge.text)
    
    if badge_count >= 6:
        logging.info('Add to cart works fine.')
    else:
        logging.warning('Add to cart does NOT work fine.')

def remove_from_cart(driver):
    """Remove items from the cart."""
    item_ids = [f'item_{i}_title_link' for i in range(6)]
    
    for item_id in item_ids:
        try:
            select_product = driver.find_element(By.ID, item_id)
            select_product.click()
            remove_from_cart_button = driver.find_element(By.ID, 'remove')
            remove_from_cart_button.click()
            time.sleep(1)  # Wait for the action to complete
            back_to_main_page = driver.find_element(By.ID, 'back-to-products')
            back_to_main_page.click()
        except NoSuchElementException:
            logging.error(f'Could not find or interact with {item_id}.')

    # Check if cart is empty
    try:
        element = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge[data-test='shopping-cart-badge']")
        if element.is_displayed():
            logging.warning('Remove from cart does NOT work fine.')
    except NoSuchElementException:
        logging.info('Remove from cart works fine.')

def logout(driver):
    """Log out from the application."""
    main_menu_icon = driver.find_element(By.ID, 'react-burger-menu-btn')
    main_menu_icon.click()
    #TODO Lektor - tady neni wait takze test selze... :-( aspon staticky wait tady mohl byt. I kdyz je to antipatern.

    logout_button = driver.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()
    
    try:
        element = driver.find_element(By.ID, 'login-button')
        if element.is_displayed():
            logging.info('Logout works fine.')
    except NoSuchElementException:
        logging.warning('Logout does NOT work fine.')

def main():
    """Main function to execute the test."""
     #TODO tady mohl byt global driver a nemuse jsi si to predavat ve funkcich
    driver = setup_driver()
    
    try:
        login(driver, 'standard_user', 'secret_sauce')
        add_to_cart(driver)
        remove_from_cart(driver)
        logout(driver)
        #TODO Lektor - chvalim za krasne oddeleni struktury testu!
        #TODO tady chybel driv konec exceptu!
    finally:
        driver.quit()
    
    

if __name__ == "__main__":
    main()