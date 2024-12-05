import pytest
from OOP.setup import Setup
from OOP.login import Login
from OOP.add_to_backpack import AddToBackpack
from OOP.teardown import Teardown


@pytest.mark.usefixtures("driver")
class TestCart(Setup):
    @pytest.mark.parametrize("product_name", [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ])
    def test_add_backpack_to_cart(self, driver,product_name):
        driver.get("https://www.saucedemo.com")
        
        login_page = Login(driver)
        login_page.perform_login("standard_user", "secret_sauce")

        product_page = AddToBackpack(driver)
        product_page.add_product(product_name)

        teardown = Teardown(driver)
        teardown.close_browser()