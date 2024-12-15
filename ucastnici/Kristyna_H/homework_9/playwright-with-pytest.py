import logging
import pytest
from playwright.sync_api import sync_playwright

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
        logger.info("User successfully logged in")


class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self, item_button_id):
        self.page.click(f"#{item_button_id}")
        logger.info(f"Item \"{item_button_id}\" added to cart directly.")

    def go_to_detail(self, item_link_id):
        self.page.click(f"#{item_link_id}")
        logger.info(f"Going to item \"{item_link_id}\" detail page.")

    def get_cart_badge_count(self):
        product_count = self.page.inner_text(".shopping_cart_badge")
        logger.info(f"There are {product_count} items on the cart badge.")
        return product_count

    def go_to_cart(self):
        self.page.click("#shopping_cart_container")
        logger.info("Going to cart.")


class ProductDetailPage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.click("#add-to-cart")
        logger.info("Item added to cart directly.")

    def go_back_to_inventory(self):
        self.page.click("#back-to-products")
        logger.info("Going back to inventory page.")


class CartPage:
    def __init__(self, page):
        self.page = page

    def get_product_count(self):
        product_count = len(self.page.query_selector_all(".cart_item"))
        logger.info(f"There are {product_count} items in the cart.")
        return product_count

    def go_to_checkout(self):
        self.page.click("#checkout")
        logger.info("Going to checkout page.")


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_in_form(self, first_name, last_name, postal_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)
        logger.info(f"Filling in order form - first name: \"{first_name}\", last name: \"{last_name}\", postal code: \"{postal_code}\".")

    def go_to_summary_page(self):
        self.page.click("#continue")
        logger.info("Going to summary page.")


class SummaryPage:
    def __init__(self, page):
        self.page = page

    def get_item_total_label(self):
        item_total_label = self.page.inner_text(".summary_subtotal_label")
        logger.info(f"Item total label is \"{item_total_label}\".")
        return item_total_label

    def go_to_final_page(self):
        self.page.click("#finish")
        logger.info("Going to final page.")


class FinalPage:
    def __init__(self, page):
        self.page = page

    def get_message(self):
        final_message = self.page.inner_text(".complete-header")
        logger.info(f"Final message is \"{final_message}\".")
        return final_message

    def go_back_home(self):
        self.page.click("#back-to-products")
        logger.info("Going back to inventory page.")


class OrderTest:
    def __init__(self, page):
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.product_detail_page = ProductDetailPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.summary_page = SummaryPage(page)
        self.final_page = FinalPage(page)
        self.login_page.login("standard_user", "secret_sauce")

    def place_order(self, expected_product_count, expected_item_total_price):
        self.inventory_page.go_to_cart()
        actual_product_count = self.cart_page.get_product_count()
        assert actual_product_count == expected_product_count, "Product count mismatch."

        self.cart_page.go_to_checkout()
        self.checkout_page.fill_in_form("Kris", "Tyna", "tady")
        self.checkout_page.go_to_summary_page()

        expected_item_total_label = f"Item total: ${expected_item_total_price}"
        actual_item_total_label = self.summary_page.get_item_total_label()
        assert actual_item_total_label == expected_item_total_label, "Item total mismatch."

        self.summary_page.go_to_final_page()
        expected_message = "Thank you for your order!"
        actual_message = self.final_page.get_message()
        assert actual_message == expected_message, "Order completion message mismatch."

        self.final_page.go_back_home()

    def add_items_to_cart_directly_and_place_order(self, item_button_ids, expected_item_total_price):
        for idx, item_button_id in enumerate(item_button_ids):
            self.inventory_page.add_to_cart(item_button_id)
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, "Item count in cart is incorrect."

        self.place_order(len(item_button_ids), expected_item_total_price)

    def add_items_to_cart_via_detail_page_and_place_order(self, item_link_ids, expected_item_total_price):
        for idx, item_link_id in enumerate(item_link_ids):
            self.inventory_page.go_to_detail(item_link_id)
            self.product_detail_page.add_to_cart()
            self.product_detail_page.go_back_to_inventory()
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, "Item count in cart is incorrect."

        self.place_order(len(item_link_ids), expected_item_total_price)


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page
        context.close()
        browser.close()


def test_adding_items_to_cart_directly_and_placing_order(browser):
    order_test = OrderTest(browser)
    order_test.add_items_to_cart_directly_and_place_order([
        "add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)",
        "add-to-cart-sauce-labs-fleece-jacket"
    ], 65.98)


def test_adding_items_to_cart_via_detail_page_and_placing_order(browser):
    order_test = OrderTest(browser)
    order_test.add_items_to_cart_via_detail_page_and_place_order([
        "item_1_title_link",
        "item_4_title_link",
        "item_0_title_link"
    ], 55.97)
