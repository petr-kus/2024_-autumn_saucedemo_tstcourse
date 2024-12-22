import logging
from login_page import LoginPage
from inventory_page import InventoryPage
from product_detail_page import ProductDetailPage
from cart_page import CartPage
from checkout_page import CheckoutPage
from summary_page import SummaryPage
from final_page import FinalPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class OrderTest:
    def __init__(self, page):
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.product_detail_page = ProductDetailPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.summary_page = SummaryPage(page)
        self.final_page = FinalPage(page)

    def login(self, username):
        self.login_page.login(username, "secret_sauce")

    def checkout(self, expected_product_count):
        self.inventory_page.go_to_cart()
        actual_product_count = self.cart_page.get_product_count()
        assert actual_product_count == expected_product_count, "Product count mismatch."
        self.cart_page.go_to_checkout()

    def continue_to_summary(self):
        self.checkout_page.fill_in_form("Kris", "Tyna", "tady")
        self.checkout_page.go_to_summary_page()

    def finalize_order(self, expected_item_total_price):
        expected_item_total_label = f"Item total: ${expected_item_total_price}"
        actual_item_total_label = self.summary_page.get_item_total_label()
        assert actual_item_total_label == expected_item_total_label, "Item total mismatch."
        self.summary_page.go_to_final_page()

    def go_back_home(self):
        expected_message = "Thank you for your order!"
        actual_message = self.final_page.get_message()
        assert actual_message == expected_message, "Order completion message mismatch."
        self.final_page.go_back_home()

    def place_order(self, expected_product_count, expected_item_total_price):
        self.checkout(expected_product_count)
        self.continue_to_summary()
        self.finalize_order(expected_item_total_price)
        self.go_back_home()

    def logout(self):
        self.inventory_page.logout()

    def case_1_add_items_to_cart_directly_and_place_order(self, username, item_button_ids, expected_item_total_price):
        self.login(username)

        for idx, item_button_id in enumerate(item_button_ids):
            self.inventory_page.add_to_cart(item_button_id)
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, "Item count in cart is incorrect."

        self.place_order(len(item_button_ids), expected_item_total_price)

        self.logout()

    def case_2_add_items_to_cart_via_detail_page_and_place_order(self, username, item_link_ids, expected_item_total_price):
        self.login(username)

        for idx, item_link_id in enumerate(item_link_ids):
            self.inventory_page.go_to_detail(item_link_id)
            self.product_detail_page.add_to_cart()
            self.product_detail_page.go_back_to_inventory()
            expected_count = idx + 1
            assert int(self.inventory_page.get_cart_badge_count()) == expected_count, "Item count in cart is incorrect."

        self.place_order(len(item_link_ids), expected_item_total_price)

        self.logout()