import pytest

from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage
from page_objects.search_page import SearchPage
from page_objects.home_page import HomePage
from page_objects.product_category_page import ProductCategoryPage
from page_objects.product_detail_page import ProductDetailPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage

from utilities.driver_factory import get_driver

@pytest.fixture
def driver():
    """Initializes the WebDriver based on the browser parameter."""
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def base_page(driver):
    """Initializes the base page."""
    return BasePage(driver)

@pytest.fixture
def login_page(driver):
    """Initializes the login page."""
    return LoginPage(driver)

@pytest.fixture
def search_page(driver):
    """Initializes the search page."""
    return SearchPage(driver)

@pytest.fixture
def home_page(driver):
    """Initializes the home page."""
    return HomePage(driver)

@pytest.fixture
def product_category_page(driver):
    """Initializes the product category page."""
    return ProductCategoryPage(driver)

@pytest.fixture
def product_detail_page(driver):
    """Initializes the product detail page."""
    return ProductDetailPage(driver)

@pytest.fixture
def cart_page(driver):
    """Initializes the cart page."""
    return CartPage(driver)

@pytest.fixture
def checkout_page(driver):
    """Initializes the checkout page."""
    return CheckoutPage(driver)