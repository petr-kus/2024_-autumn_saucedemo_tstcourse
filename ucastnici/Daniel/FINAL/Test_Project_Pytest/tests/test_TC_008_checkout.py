import pytest
import allure

from tests.test_TC_004_cart import test_add_to_cart

@allure.title("Checkout - proceed to checkout")
@allure.description("Verify that a user can successfully complete an order after entering valid details.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_008_checkout")
@pytest.mark.dependency(depends=["test_add_to_cart"])
def test_proceed_to_checkout(driver, logger, base_page, login_page, product_detail_page, cart_page, checkout_page):

    # Step 1-2: Follow all the steps of the case TC_004_cart - dependency to "test_add_to_cart"
    login_page.login()
    product_detail_page.open()
    product_detail_page.add_product_to_cart()
    product_detail_page.go_to_cart()

    # Step 3:
    cart_page.proceed_to_checkout()

    # Verify, if the expected url is the same as the current url.
    expected_url = f"{base_page.BASE_URL}{checkout_page.CHECKOUT_STEP_ONE_URL}"
    current_url = driver.current_url
    logger.info(f"Expected URL = {expected_url}, Current URL = {current_url}")

    assert current_url == expected_url, f"Expected URL {expected_url}, but got {current_url}"
    logger.info(f"Checkout page step one loaded succesfully.")
    
    assert product_detail_page.is_element_visible(checkout_page.CHECKOUT_CUSTOMER_FORM), f"Expected checkout page step one URL: {expected_url}, but got URL: {current_url}"
    logger.info(f"Checkout customer form is visible.")

    logger.info(f"Checkout process starts successfully.")