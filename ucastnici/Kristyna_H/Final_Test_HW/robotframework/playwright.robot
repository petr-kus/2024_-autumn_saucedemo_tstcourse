*** Settings ***
Resource   keywords.robot
Library    Browser
Library    Collections
Library    OperatingSystem
Library    String
Suite Setup    New Browser    browser=${BROWSER_TYPE}   headless=${HEADLESS}
Test Setup    New Context    viewport={'width': 1920, 'height': 1080}
Test Teardown    Close Context
Suite Teardown    Close Browser

*** Variables ***
${HEADLESS}                     False
${BROWSER_TYPE}                 chromium
${BASE_URL}                     https://www.saucedemo.com
${USERNAME_FIELD}               user-name
${PASSWORD_FIELD}               password
${LOGIN_BUTTON}                 login-button
${CART_CONTAINER}               shopping_cart_container
${CART_BADGE}                   .shopping_cart_badge
${ADD_TO_CART_BUTTON}           add-to-cart
${BACK_TO_PRODUCTS_BUTTON}      back-to-products
${CHECKOUT_BUTTON}              checkout
${LOGOUT_BUTTON}                logout_sidebar_link
${BURGER_MENU}                  react-burger-menu-btn
${FIRST_NAME_FIELD}             first-name
${LAST_NAME_FIELD}              last-name
${POSTAL_CODE_FIELD}            postal-code
${CONTINUE_BUTTON}              continue
${FINISH_BUTTON}                finish
${ITEM_TOTAL_LABEL}             .summary_subtotal_label
${COMPLETE_HEADER}              .complete-header


*** Test Cases ***

Test Adding Items To Cart Directly And Placing Order
    [Template]    Add Items To Cart Directly And Place Order
    standard_user   65.98   add-to-cart-test.allthethings()-t-shirt-(red)   add-to-cart-sauce-labs-fleece-jacket
    standard_user   45.98   add-to-cart-sauce-labs-backpack     add-to-cart-sauce-labs-bolt-t-shirt
    error_user      45.98   add-to-cart-sauce-labs-backpack     add-to-cart-sauce-labs-bolt-t-shirt

Test Adding Items To Cart Via Detail Page And Placing Order
    [Template]    Add Items To Cart Via Detail Page And Place Order
    standard_user    55.97      item_0_title_link   item_1_title_link   item_4_title_link
    standard_user    45.98      item_4_title_link   item_1_title_link
    error_user       45.98      item_4_title_link   item_1_title_link