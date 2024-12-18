import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_item_count(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_item_count() > 0
