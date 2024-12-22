import pytest
from selenium import webdriver
from pytest_lib.pages.login_page import LoginPage
from pytest_lib.pages.inventory_page import InventoryPage
from pytest_lib.pages.cart_page import CartPage

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_and_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert "Swag Labs" in driver.title

    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()
    assert len(cart_items) > 0, "No items in the cart"

def test_login_invalid_creedentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("invalid_user", "wrong_password")

    assert "Epic sadface" in login_page.error_message(), "Error message not found"