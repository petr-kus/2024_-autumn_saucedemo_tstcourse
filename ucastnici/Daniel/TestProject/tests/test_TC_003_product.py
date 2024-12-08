def test_view_product_detail(login_page, product_category_page, product_detail_page):
        
    # Step 1: Log in
    login_page.login()

    # Step 2: View product detail
    product_category_page.show_product_detail()

    # Verify, if the product details page loads, displaying name, product photo, price, description and purchase button.
    assert product_detail_page.verify_product_id_in_url(product_detail_page.PRODUCT_ID)
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_NAME)
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PHOTO)
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PRICE)
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_DESCRIPTION)
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_ADD_CART_BUTTON)

    product_detail_page.logger.info("Product details page is displayed correctly.")