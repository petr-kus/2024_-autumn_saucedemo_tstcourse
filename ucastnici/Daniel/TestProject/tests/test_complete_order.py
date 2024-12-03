def test_complete_order(base_page, login_page, product_category_page, product_detail_page, cart_page, checkout_page, home_page):
    
    # Step 1: Log in
    login_page.login()
    
    # Step 2: View product detail and add to cart
    product_category_page.show_product_detail()

    product_detail_page.add_product_to_cart()
    product_detail_page.go_to_cart()

    # Step 3: Remove item from cart and continue shopping
    cart_page.remove_item_from_cart()
    cart_page.continue_shopping()

    # Step 4: Show product detail again and add another product to cart
    product_category_page.show_product_detail()

    product_detail_page.add_product_to_cart()
    product_detail_page.go_to_cart()

    # Step 5: Proceed to checkout
    cart_page.proceed_to_checkout()

    # Step 6: Fill customer details and take screenshots
    checkout_page.fill_customer_details()
    checkout_page.take_screenshot()
    checkout_page.click_continue()

    # Step 7: Take another screenshot and finish the checkout
    checkout_page.take_screenshot()
    checkout_page.finish_checkout()

    # Step 8: Ensure we are back on the homepage and log out
    home_page.take_screenshot()
    checkout_page.go_back_home()

    home_page.logout()

    expected_url = base_page.BASE_URL
    current_url = base_page.driver.current_url
    assert current_url != expected_url, f"Expected URL {expected_url}, but got {current_url}"