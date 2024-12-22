from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#TODO Lektor - toto je zbytecny nepouzity import. Cim vic importu tim vic to brzdi script... .
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options
import logging

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam
#TODO Lektor - na prvni pohled se me ukol moc libi jak je rozdelen do funkci jako test steptu/test casu. Je prehledny!

#TODO Lektor - zde mohly byt parametry pro test! Vstup i stranka atp., 

logging.basicConfig(filename='OK_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#TODO Lektor - chvalim logovani do souboru bokem!


def setup():
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    #TODO Lektor - stranka mohl byt parametrizovana paramtrem funkce setup
    return driver


def login(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    #TODO Lektor - toto mohl byt one liner... driver.find_element(By.ID, "user-name").send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    #TODO By.ID, "password" - to mohlo byt v POM strukture mimo hlavni skript... .

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    logging.info("User succesfuly logged in")
    #TODO tohle ale nevis... primpomina mi to jendoho z kolegu... neni tu assert. Toto ti to napise i kdyz budes mit invalid udaje... .


def add_item_to_cart_directly(driver, item_id: str):
    add_to_cart_button = driver.find_element(By.ID, item_id)
    add_to_cart_button.click()
       
    logging.info(f"Item {item_id} added to cart directly.")
    #TODO tohle ale nevis... primpomina mi to jendoho z kolegu... neni tu assert. Toto ti to napise i kdyz budes mit invalid udaje... .


def add_item_to_cart_via_detail_page(driver, item_id: str):
    inventory_item = driver.find_element(By.ID, item_id)
    inventory_item.click()

    add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
    add_to_cart_button.click()

    back_to_products_button = driver.find_element(By.ID, "back-to-products")
    back_to_products_button.click()
       
    logging.info(f"Item {item_id} added to cart via detail page.")
    #TODO tohle ale nevis... primpomina mi to jendoho z kolegu... neni tu assert. Toto ti to napise i kdyz budes mit invalid udaje... .


def go_to_cart(driver, expected_item_count):
    cart_container_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_container_button.click()

    items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
    actual_item_count = len(items_in_cart)
    assert actual_item_count == expected_item_count, f"Expected item count is {expected_item_count}, actual item count is {actual_item_count}"
    logging.info("Went to cart. Item count is correct.")
   

def checkout(driver, expected_subtotal_price):
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    
    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.click()
    first_name_input.send_keys("Kris")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Tyna")

    postal_code_input = driver.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("tady")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    expected_subtotal_label = f"Item total: ${expected_subtotal_price}"
    actual_subtotal_label = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    assert actual_subtotal_label == expected_subtotal_label,  f"Expected subtotal label is {expected_subtotal_label}, actual subtotal label is {actual_subtotal_label}"
    logging.info("Checked out. Subtotal price is correct.")


def finalize_order(driver):
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    checkout_complete_container = driver.find_element(By.ID, "checkout_complete_container")
    actual_final_message = checkout_complete_container.find_element(By.CLASS_NAME, "complete-header").text
    expected_final_message = "Thank you for your order!"
    assert actual_final_message == expected_final_message, f"Expected message is {expected_final_message}, actual message is {actual_final_message}"
    logging.info("Order finalized. Message is correct.")
    
    
def go_back_home(driver):
    back_home_button = driver.find_element(By.ID, "back-to-products")
    back_home_button.click()


def assert_item_count_on_cart_badge(driver, expected_count):
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert int(cart_badge.text) == expected_count, f"Item count in cart is incorrect."


def test_adding_items_directly(driver, item_ids, expected_subtotal_price):
    for idx, item_id in enumerate(item_ids):
        add_item_to_cart_directly(driver, item_id)
        assert_item_count_on_cart_badge(driver, idx + 1)
    go_to_cart(driver, len(item_ids))
    checkout(driver, expected_subtotal_price)
    finalize_order(driver)
    go_back_home(driver)


def test_adding_items_via_detail_page(driver, item_ids, expected_subtotal_price):
    for idx, item_id in enumerate(item_ids):
        add_item_to_cart_via_detail_page(driver, item_id)
        assert_item_count_on_cart_badge(driver, idx + 1)
    go_to_cart(driver, len(item_ids))
    checkout(driver, expected_subtotal_price)
    finalize_order(driver)
    go_back_home(driver)
    

def teardown(driver):
    time.sleep(10)
    driver.close()


def run_test_scenario():
    driver = setup()
    #TODO driver mohl byt global driver a nemusis si ho pak predavat v parametrech funkci.. .

    login(driver)
    test_adding_items_directly(driver, ["add-to-cart-test.allthethings()-t-shirt-(red)", "add-to-cart-sauce-labs-fleece-jacket"], 65.98)
    #TODO Lektor -zde bych doporucil bud rozsirit nazev funkce o to ze verifikujes i cenu a nebo pridat price=65.98 (pouzit spravne pojmenovane vstupni parametry)
    test_adding_items_via_detail_page(driver, ["item_1_title_link", "item_4_title_link", "item_0_title_link"], 55.97)
    teardown(driver)

    #TODO Lektor - libi se mi moc ze mas test case co prehravas vlastne za sebou jako naky scenar. 
    #TODO Lektor - to je velmi spravne premysleni! Dost pokrocile! a perfektni... . Presne tak by to totiz melo fungovat!
    #TODO Lektor - v kazdem pade je evidentni ze potrebujes zapracovat na Domain Languge aby to bylo orpavdu srozumitelne... a na vzajmenem predavani dat... . 

    #TODO Lektor -kdyz by jsi jednotlive metody napsala jeste obecneji a jeste vic parametricky a predaval si treba objekt stranky... umoznil by ti to napsat to lepe. 
    #TODO Lektor -takove jednoduche vylepseni by bylo navrhu si vytvorit dictionary a v nem jednoltive produkty a jednotlive ceny... a ID... tim by jsi tu pak nemusel amit ty dlouhe texty jako... "add-to-cart-sauce-labs-fleece-jacket"
    #TODO Lektor - proste jsi malo pouzila POM a oddeleni dat od testu...

run_test_scenario()

