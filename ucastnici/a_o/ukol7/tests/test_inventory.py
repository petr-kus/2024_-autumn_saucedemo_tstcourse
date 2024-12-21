import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

@pytest.mark.parametrize("filter_value", ["az", "za", "lohi", "hilo"])
def test_inventory_filters(driver, filter_value):
    """Test filtrování produktů."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open()
    login_page.login("problem_user", "secret_sauce")

    product_names_before = inventory_page.get_product_names()
    inventory_page.apply_filter(filter_value)
    product_names_after = inventory_page.get_product_names()

    if filter_value == "az":
        assert product_names_after == sorted(product_names_before), f"Filtr {filter_value} selhal!"
    elif filter_value == "za":
        assert product_names_after == sorted(product_names_before, reverse=True), f"Filtr {filter_value} selhal!"
    elif filter_value == "lohi" or filter_value == "hilo":
        assert product_names_before != product_names_after, f"Filtr {filter_value} selhal!"
    
    logging.info(f"Test pro filtr '{filter_value}' proběhl úspěšně.")
