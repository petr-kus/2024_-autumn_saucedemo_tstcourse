from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#TODO Lektor - zbytecny nepouzity import (snazime se minimalizovat importy kazdy import je alokace, pametia zdrzeni...)
from selenium.webdriver.common.by import By

import time
#TODO Lektor - zbytecny nepouzity import (snazime se minimalizovat importy kazdy import je alokace, pametia zdrzeni...)
from selenium.webdriver.chrome.options import Options
import logging

import pytest

logging.basicConfig(filename='pytest.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#TODO Lektor - pochvala za time stamp.

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni jak test automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre... )

class LoginPage:
    #TODO Lektor - username_field = (By.ID, "user-name")  
    def __init__(self, driver):
        self.driver = driver
        #TODO Lektor - predani driveru zrovna v tomt testu mohlo byt pres Global Driver variable. 
        #TODO Lektor - ale chvalim ze je pouzite OOP pro to a init. Ale lepsi by byl ten singlton pattern. 
        #TODO Lektor - A kdyz uz je to takhle... mohlo to byt kazdy ten page object oddelen separe do souboru.

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        #TODO Lektor - (By.ID, "user-name") a pod. melo byt definovano nahore jako parametr. Viz priklad.
        #self.driver.find_element(*self.username_field).send_keys(username)
        logging.info("User succesfuly logged in")
        #TODO Lektor - nejspis je, ale jiste to nevis... tak to neloguj takto. Ale treba should nebo neco oc je jasne... .


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        
    def add_to_cart(self, item_button_id):
        self.driver.find_element(By.ID, item_button_id).click()
        logging.info(f"Item {item_button_id} added to cart directly.")
        
    def go_to_detail(self, item_link_id):
        self.driver.find_element(By.ID, item_link_id).click()
        logging.info(f"Going to item {item_link_id} detail page.")
    
    def get_cart_badge_count(self):
        product_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        logging.info(f"there are {product_count} items on cart badge.")
        return product_count

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        logging.info("Going to cart.")
        #TODO Lektor - obecne se me libi ze vsude neco logujes a docela hezky. 
        
class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        
    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart").click()
        logging.info("Item added to cart directly.")
        
    def go_back_to_inventory(self):
        self.driver.find_element(By.ID, "back-to-products").click()
        logging.info("Going back to inventory page.")
        
        
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        
    def get_product_count(self):
        product_count = len(self.driver.find_elements(By.CLASS_NAME, "cart_item"))
        logging.info(f"there are {product_count} items in cart.")
        return product_count
    
    def go_to_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        logging.info("Going back to checkout page.") 
        
        
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
      
    def fill_in_form(self, first_name, last_name, postal_code):
        first_name_input = self.driver.find_element(By.ID, "first-name")
        first_name_input.click()
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)

        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys(postal_code)
        logging.info(f"Filling in order form - first name: {first_name}, last name: {last_name}, postal code: {postal_code}.")
        
    def go_to_summary_page(self):
        self.driver.find_element(By.ID, "continue").click()
        logging.info("Going to summary page.")
      
      
class SummaryPage:
    def __init__(self, driver):
        self.driver = driver
                           
    def get_item_total_label(self):
        itemtotal_label = self.driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
        logging.info(f"Item total label is {itemtotal_label}.")
        return itemtotal_label   
    
    def go_to_final_page(self):
        self.driver.find_element(By.ID, "finish").click()
        logging.info("Going to final page.")
        
        
class FinalPage:
    def __init__(self, driver):
        self.driver = driver
               
    def get_message(self):
        checkout_complete_container = self.driver.find_element(By.ID, "checkout_complete_container")
        final_message = checkout_complete_container.find_element(By.CLASS_NAME, "complete-header").text
        logging.info(f"Final message is \"{final_message}\"")
        return final_message
    
    def go_back_home(self):
        self.driver.find_element(By.ID, "back-to-products").click()
        logging.info("Going back to inventory page.")
    
    
class OrderTest:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.product_detail_page = ProductDetailPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.summary_page = SummaryPage(driver)
        self.final_page = FinalPage(driver)
        self.login_page.login("standard_user", "secret_sauce") 
        
        #TODO: toto uz je test step a je to sem schovane... cekal bych to nekde viditelneji... .
        #v pytestu by bylo faj  pro toto udelat zvlas fixture ... user_is_logged napriklad...
        
    def add_items_to_cart_directly_and_place_order(self, item_button_ids, expected_item_total_price):
        for idx, item_button_id in enumerate(item_button_ids):
            self.inventory_page.add_to_cart(item_button_id)
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, f"Item count in cart is incorrect." 

        self.inventory_page.go_to_cart()
        expected_product_count = len(item_button_ids)   
        actual_product_count = self.cart_page.get_product_count()
        assert actual_product_count == expected_product_count, f"Expected product count is {expected_product_count}, actual product count is {actual_product_count}"
            
        self.cart_page.go_to_checkout()
        self.checkout_page.fill_in_form("Kris", "Tyna", "tady")
        self.checkout_page.go_to_summary_page()
        
        expected_item_total_label = f"Item total: ${expected_item_total_price}"
        actual_item_total_label = self.summary_page.get_item_total_label()
        assert actual_item_total_label == expected_item_total_label,  f"Expected item total label is {expected_item_total_label}, actual item total label is {actual_item_total_label}"
            
        self.summary_page.go_to_final_page()
        expected_message = "Thank you for your order!"
        actual_message = self.final_page.get_message()
        assert actual_message == expected_message, f"Expected message is {expected_message}, actual message is {actual_message}"
            
        self.final_page.go_back_home()
    
    def add_items_to_cart_via_detail_page_and_place_order(self, item_link_ids, expected_item_total_price):
        for idx, item_link_id in enumerate(item_link_ids):
            self.inventory_page.go_to_detail(item_link_id)
            self.product_detail_page.add_to_cart()
            self.product_detail_page.go_back_to_inventory()
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, f"Item count in cart is incorrect." 

        self.inventory_page.go_to_cart()
        expected_product_count = len(item_link_ids)   
        actual_product_count = self.cart_page.get_product_count()
        assert actual_product_count == expected_product_count, f"Expected product count is {expected_product_count}, actual product count is {actual_product_count}"
            
        self.cart_page.go_to_checkout()
        self.checkout_page.fill_in_form("Kris", "Tyna", "tady")
        self.checkout_page.go_to_summary_page()
        
        expected_item_total_label = f"Item total: ${expected_item_total_price}"
        actual_item_total_label = self.summary_page.get_item_total_label()
        assert actual_item_total_label == expected_item_total_label,  f"Expected item total label is {expected_item_total_label}, actual item total label is {actual_item_total_label}"
            
        self.summary_page.go_to_final_page()
        expected_message = "Thank you for your order!"
        actual_message = self.final_page.get_message()
        assert actual_message == expected_message, f"Expected message is {expected_message}, actual message is {actual_message}"
            
        self.final_page.go_back_home()


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    #TODO Lektor - parametrizace by mela byt vyvedena ven...
    yield driver
    driver.close()
    driver.quit()
    

def test_adding_items_to_cart_directly_and_placing_order(driver):
    order_test = OrderTest(driver)
    order_test.add_items_to_cart_directly_and_place_order(["add-to-cart-test.allthethings()-t-shirt-(red)", "add-to-cart-sauce-labs-fleece-jacket"], 65.98)
    #TODO Lektor - ty id by mela byt nekam schovana za pom... . a asi i ty ceny by meli byt nekam vyextrahovany mimo ... a ne napsany takto.
    #TODO Lektor - jde cititi jak je to necitelne... .
    #TODO Lektor - ty kroky co jsou schovane add_items_to_cart_directly_and_place_order by meli byt spis vvedene sem vcetne toho loginu... aby to tady bylo vic citelne. 
    #TODO Lektor - jinak se to tu jen prevolava ale nema to pridanou hodnotu citelnosti testu... .


def test_adding_items_to_cart_via_detail_page_and_placing_order(driver):
    order_test = OrderTest(driver)
    order_test.add_items_to_cart_via_detail_page_and_place_order(["item_1_title_link", "item_4_title_link", "item_0_title_link"], 55.97)

 #TODO Lektor - chvalim ze uz zde je pouzit pytest!
