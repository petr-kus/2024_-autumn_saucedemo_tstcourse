import allure

@allure.title("Product detail - view the content")
@allure.description("Verify that clicking on a product in product category displays its detailed information and purchase button.")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TC_003_product")
def test_view_product_detail(logger, login_page, product_category_page, product_detail_page):
        
    # Step 1: Log in
    login_page.login()

    # Step 2: View product detail by clicking on chosed product image
    product_id_image = (product_category_page.PRODUCT_ID_IMAGE)
    product_category_page.show_product_detail(product_id_image)

    # Verify, if the product details page loads with corresponding URL, displaying name, product photo, price, description and purchase button.
    expected_product_id = 4
    actual_product_id = product_detail_page.get_product_id_from_url()

    assert expected_product_id == actual_product_id, f"Expected product ID '{expected_product_id}', but got product ID '{actual_product_id}' reflected in URL."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_NAME), f"Element 'Product name' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PHOTO), f"Element 'Product photo' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_PRICE), f"Element 'Product price' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_DESCRIPTION), f"Element 'Product description' is not visible on the page."
    assert product_detail_page.is_element_visible(product_detail_page.PRODUCT_ADD_CART_BUTTON), f"Element 'Purchase button' is not visible on the page."

    logger.info("Product details page is displayed correctly.")