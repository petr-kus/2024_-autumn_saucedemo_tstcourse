from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

#TODO Lektor - Komentovano na lekci tak, z rychliku...
#TODO Lektor - Super je ze skript jede a selhava s error_user do konzole!

Option = Options()
Option.add_argument("start-maximized")
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
#TODO Lektor - ID melo byt oddeleno nekam jinam do promene treba nahoru...
username.send_keys("standard_user")

#TODO Lektor - mohl byt one liner s oddelenim do dictionary! driver.find_element(*username).send_keys(user['name'])

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

inventory_item = driver.find_element(By.ID, "item_4_title_link")
inventory_item.click()

add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
add_to_cart_button.click()

cart_container_button = driver.find_element(By.ID, "shopping_cart_container")
cart_container_button.click()

items_in_cart = driver.find_elements(By.CLASS_NAME, "cart_item")
expected_item_count = 1
actual_item_count = len(items_in_cart)
assert actual_item_count == expected_item_count, f"Expected item count is one, actual item count is {actual_item_count}"
#TODO Lektor - supoer ze je tu assert a ze krasne logujes...

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

first_name_input = driver.find_element(By.ID, "first-name")
first_name_input.click()
first_name_input.send_keys("Kristyna")

last_name_input = driver.find_element(By.ID, "last-name")
last_name_input.send_keys("Kris")

postal_code_input = driver.find_element(By.ID, "postal-code")
postal_code_input.send_keys("tady")

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()
checkout_complete_container = driver.find_element(By.ID, "checkout_complete_container")
actual_final_message = checkout_complete_container.find_element(By.CLASS_NAME, "complete-header").text
expected_final_message = "Thank you for your order!"
assert actual_final_message == expected_final_message, f"Expected message is {expected_final_message}, actual message is {actual_final_message}"

time.sleep(10)
#TODO Lektor - to je moc na tvrdo... mohlo to byt i nekde v prubehu testu a navrchu parametrizovany...
driver.close()