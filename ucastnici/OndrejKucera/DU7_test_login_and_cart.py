# test_login_and_cart.py

import logging
from selenium import webdriver
from DU7_POM.OK_page_objects.login_page import LoginPage
from DU7_POM.OK_page_objects.product_page import ProductPage
from selenium.common.exceptions import NoSuchElementException
import time

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni jak test automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre... )

# Configure logging
logging.basicConfig(filename='OKDU7_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#TODO Lektor - super z eje tam timestamp... a chvalim i info logging

def test_login_and_cart_operations():
    """Test login and cart operations on the application."""
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com/")
        #TODO Lektor - mohlo byt parametrizovano nak externe...
        
        # Login
        login_page = LoginPage(driver)
        #TODO Lektor - super predani driveru jen. lepsi by bylo pouzit singltton patern - viz priklad od lektora vyse.
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
        
        #TODO Lektor - tohle je vlasne moc hezke tyto if else a logovani. Ja bych se to snazil schovat a mit tu jeste min kodu.
        # ale ... to uz je hodne o stylu. Blby je ze to je warrning ja bych cekal spis selhani... nebo neco.
        #proste warningy realne na konci nikdo necte... . Musi to selhat kdyz je neco blbe.

        # Remove products from cart
        for i in range(6):
            product_page.remove_product_from_cart(i)

        try:
            element = product_page.get_cart_badge()
            if element.is_displayed():
                logging.warning('Remove from cart does NOT work fine.')
                #TODO Lektor - tady ma byt error a selhani...
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
    
    #TODO Lektor - celkove struktura docela fajn ale mohlo by byt o dost citelnejsi ten kod... .

if __name__ == "__main__":
    test_login_and_cart_operations()