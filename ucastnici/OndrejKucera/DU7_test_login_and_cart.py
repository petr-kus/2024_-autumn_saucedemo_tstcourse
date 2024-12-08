# test_login_and_cart.py

import logging
from selenium import webdriver
from DU7_POM.OK_page_objects.login_page import LoginPage
from DU7_POM.OK_page_objects.product_page import ProductPage
from selenium.common.exceptions import NoSuchElementException
import time

# Configure logging
logging.basicConfig(filename='OKDU7_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_login_and_cart_operations():
    """Test login and cart operations on the application."""
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Login
        login_page = LoginPage(driver)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login()
        
        logging.info('User logged in successfully.')

        # Add products to cart
        product_page = ProductPage(driver)
        
        for i in range(6):
            product_page.add_product_to_cart(i)
        
        badge_count = product_page.get_cart_badge_count()
        
        if badge_count == 6:
            logging.info('All products added to cart successfully.')
        else:
            logging.warning(f'Expected 6 items in cart but found {badge_count}.')

        # Remove products from cart
        for i in range(6):
            product_page.remove_product_from_cart(i)

        try:
            element = product_page.get_cart_badge()
            if element.is_displayed():
                logging.warning('Remove from cart does NOT work fine.')
        except NoSuchElementException:
            logging.info('Remove from cart works fine.')
        
        # Logout

        try:
            element = login_page.click_logout()
            if element.is_displayed():
                logging.info('Logout works fine.')
        except NoSuchElementException:
            logging.warning('Logout seems to DO NOT work fine.')

        #except Exception as e:
        #    logging.error(f'Error while checking cart badge: {e}')
      

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_and_cart_operations()