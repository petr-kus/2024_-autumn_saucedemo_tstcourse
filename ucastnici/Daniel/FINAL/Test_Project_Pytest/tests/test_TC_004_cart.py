import pytest
import allure

@allure.title("Product detail - add product to cart")
@allure.description("Verify that a user can add a product to the cart from the product details page.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_004_cart")
@pytest.mark.dependency()
def test_add_to_cart(driver, logger, login_page, product_detail_page, cart_page):

    # Step 0: Log in
    login_page.login("standard_user", "secret_sauce")
    
    # Step 1: Navigate to the product details page.
    product_detail_page.open()
    
    # Step 2: Click on "Add to Cart" button
    product_detail_page.add_product_to_cart()

    # Step 3: Verify if cart icon badge updates
    cart_badge_number = product_detail_page.get_cart_badge_number()
    expected_cart_badge_number = 1

    assert expected_cart_badge_number == cart_badge_number, f"Expected '{expected_cart_badge_number}' item in the cart, but found '{cart_badge_number}'."
    logger.info(f"Expected cart badge number '{expected_cart_badge_number}' corresponds to actual cart badge number '{cart_badge_number}'.")

    # Step 4: Navigate to the cart page.
    product_detail_page.go_to_cart()

    # Verify if cart item is visible in the cart and if the count corresponds with the number of added products to the cart before.
    assert cart_page.is_element_visible(cart_page.CART_ITEM), "Product item is not visible in the cart page."
    logger.info(f"Product item is visible in the cart page.")

    cart_items_number = cart_page.get_cart_items_count()
    expected_cart_items_number = 1

    assert cart_page.is_element_visible(cart_page.CART_ITEM), "Product item is not visible in the cart page."
    assert expected_cart_items_number == cart_items_number, f"Expected '{expected_cart_items_number}' item(s) in the cart page, but found '{cart_items_number}'."
    logger.info(f"Expected cart items number count of '{expected_cart_items_number}' corresponds to actual cart items number count of '{cart_items_number}'.")

    # Step 5: Close and reopen browser and load homepage.
    cart_page.logout()
    login_page.login("standard_user", "secret_sauce")

    # Step 6: Navigate to the cart page.
    cart_page.open()

    # Verify, if the cart page remembered cart products added before browser closure.
    cart_items_number = cart_page.get_cart_items_count()
    cart_badge_number = product_detail_page.get_cart_badge_number()
    expected_cart_badge_number = 1

    assert cart_page.is_element_visible(cart_page.CART_ITEM), "Product item is not visible in the cart page after reopening."
    logger.info(f"Product item element is visible in the cart after reopening.")
    assert expected_cart_items_number == cart_items_number, f"Expected '{expected_cart_items_number}' item(s) in the cart page, but found '{cart_items_number}'."
    logger.info(f"Expected cart items number '{expected_cart_items_number}' corresponds to actual cart items number '{cart_items_number}'.")
    assert expected_cart_badge_number == cart_badge_number, f"Expected '{expected_cart_badge_number}' item in the cart, but found '{cart_badge_number}'."
    logger.info(f"Expected cart badge number '{expected_cart_badge_number}' corresponds to actual cart badge number '{cart_badge_number}'.")
    
    logger.info("Product item is successfully displayed in the cart after reopening the browser.")