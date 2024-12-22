import pytest
from playwright.sync_api import sync_playwright
from order_test import OrderTest

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page
        context.close()
        browser.close()

@pytest.mark.parametrize("username, item_button_ids, expected_item_total_price", [
    (
        "standard_user",
        ["add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)", "add-to-cart-sauce-labs-fleece-jacket"],
        65.98
    ),
    (
        "standard_user",
        ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt"],
        45.98
    ),
    (
        "error_user",
        ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt"],
        45.98
    )
])
def test_adding_items_to_cart_directly_and_placing_order(page, username, item_button_ids, expected_item_total_price):
    order_test = OrderTest(page)
    order_test.case_1_add_items_to_cart_directly_and_place_order(username, item_button_ids, expected_item_total_price)


@pytest.mark.parametrize("username, item_link_ids, expected_item_total_price", [
    (
        "standard_user",
        ["item_0_title_link", "item_1_title_link", "item_4_title_link"],
        55.97
    ),
    (
        "standard_user",
        ["item_4_title_link", "item_1_title_link"],
        45.98
    ),
    (
        "error_user",
        ["item_4_title_link", "item_1_title_link"],
        45.98
    )
])
def test_adding_items_to_cart_via_detail_page_and_placing_order(page, username, item_link_ids, expected_item_total_price):
    order_test = OrderTest(page)
    order_test.case_2_add_items_to_cart_via_detail_page_and_place_order(username, item_link_ids, expected_item_total_price)
