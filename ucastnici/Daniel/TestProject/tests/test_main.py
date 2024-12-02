from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.product_category_page import ProductCategoryPage
from page_objects.product_detail_page import ProductDetailPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage

from utilities.driver_factory import get_driver

driver = get_driver("chrome")

login_page = LoginPage(driver)
product_category_page = ProductCategoryPage(driver)
product_detail_page = ProductDetailPage(driver)
home_page = HomePage(driver)
cart_page = CartPage(driver)
checkout_page = CheckoutPage(driver)

login_page.login()

product_category_page.show_product_detail()

product_detail_page.add_product_to_cart()
product_detail_page.go_to_cart()

cart_page.remove_item_from_cart()
cart_page.continue_shopping()

product_category_page.show_product_detail()

product_detail_page.add_product_to_cart()
product_detail_page.go_to_cart()

cart_page.proceed_to_checkout()

checkout_page.fill_customer_details()
checkout_page.take_screenshot()
checkout_page.click_continue()

checkout_page.take_screenshot()
checkout_page.finish_checkout()

home_page.take_screenshot()
checkout_page.go_back_home()

home_page.logout()
