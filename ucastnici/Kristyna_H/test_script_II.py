from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(filename='OK_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup():
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    return driver


def login(driver):
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    logging.info("User succesfuly logged in")


def add_item_to_cart_directly(driver, item_id: str):
    add_to_cart_button = driver.find_element(By.ID, item_id)
    add_to_cart_button.click()
       
    logging.info(f"Item {item_id} added to cart directly.")


def add_item_to_cart_via_detail_page(driver, item_id: str):
    inventory_item = driver.find_element(By.ID, item_id)
    inventory_item.click()

    add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
    add_to_cart_button.click()

    back_to_products_button = driver.find_element(By.ID, "back-to-products")
    back_to_products_button.click()
       
    logging.info(f"Item {item_id} added to cart via detail page.")


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
    login(driver)
    test_adding_items_directly(driver, ["add-to-cart-test.allthethings()-t-shirt-(red)", "add-to-cart-sauce-labs-fleece-jacket"], 65.98)
    test_adding_items_via_detail_page(driver, ["item_1_title_link", "item_4_title_link", "item_0_title_link"], 55.97)
    teardown(driver)


run_test_scenario()

