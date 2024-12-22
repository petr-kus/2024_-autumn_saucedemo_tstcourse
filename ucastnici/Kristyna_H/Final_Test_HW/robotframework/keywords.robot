*** Keywords ***

Open Page
    New Page    ${BASE_URL}

Login
    [Arguments]    ${username}
    Type Text    input#${USERNAME_FIELD}    ${username}
    Type Text    input#${PASSWORD_FIELD}    secret_sauce
    Click    id=${LOGIN_BUTTON}
    Log To Console    User logged in as ${username}.

Checkout
    [Arguments]     ${expected_product_count}
    Click    id=${CART_CONTAINER}
    ${actual_product_count} =   Get Element Count    .cart_item
    Should Be Equal As Integers     ${expected_product_count}   ${actual_product_count}     Product count mismatch.
    Click   id=${CHECKOUT_BUTTON}

Continue To Summary
    Type Text   input#${FIRST_NAME_FIELD}   Kris
    Type Text   input#${LAST_NAME_FIELD}    Tyna
    Type Text   input#${POSTAL_CODE_FIELD}  tady
    Click   id=${CONTINUE_BUTTON}

Finalize Order
    [Arguments]     ${expected_item_total_price}
    ${expected_item_total_label} =  Set Variable    Item total: $${expected_item_total_price}
    ${actual_item_total_label} =  Get Text    ${ITEM_TOTAL_LABEL}
    Should Be Equal     ${expected_item_total_label}    ${actual_item_total_label}      Item total mismatch.
    Click   id=${FINISH_BUTTON}

Go Back Home
    ${expected_message} =   Set Variable    Thank you for your order!
    ${actual_message} =     Get Text    ${COMPLETE_HEADER}
    Should Be Equal     ${expected_message}    ${actual_message}    Order completion message mismatch.

Place Order
    [Arguments]     ${expected_product_count}   ${expected_item_total_price}
    Checkout    ${expected_product_count}
    Continue To Summary
    Finalize Order  ${expected_item_total_price}
    Go Back Home

Logout
    Click    id=${BURGER_MENU}
    Click    id=${LOGOUT_BUTTON}
    Log To Console    Logged out.

Add Items To Cart Directly And Place Order
    [Arguments]    ${username}    ${expected_item_total}    @{item_button_ids}
    Open Page
    Login    ${username}
    FOR     ${index}    ${item_button_id}    IN ENUMERATE    @{item_button_ids}
        Click    id=${item_button_id}
        Log To Console    Item ${item_button_id} added to cart directly
        ${expected_count}=  Evaluate    ${index} + 1
        ${actual_count}=    Get Text    ${CART_BADGE}
        Should Be Equal As Integers    ${expected_count}    ${actual_count}     Item count in cart is incorrect.
    END
    ${expected_product_count}=  Get Length      ${item_button_ids}
    Place Order     ${expected_product_count}   ${expected_item_total}
    Logout

Add Items To Cart Via Detail Page And Place Order
    [Arguments]    ${username}    ${expected_item_total}    @{item_link_ids}
    Open Page
    Login    ${username}
    FOR    ${index}    ${item_link_id}    IN ENUMERATE   @{item_link_ids}
        Click    id=${item_link_id}
        Click    id=${ADD_TO_CART_BUTTON}
        Click    id=${BACK_TO_PRODUCTS_BUTTON}
        ${expected_count}=  Evaluate    ${index} + 1
        ${actual_count}=    Get Text    ${CART_BADGE}
        Should Be Equal As Integers    ${expected_count}    ${actual_count}     Item count in cart is incorrect.
    END
    ${expected_product_count}=  Get Length      ${item_link_ids}
    Place Order     ${expected_product_count}   ${expected_item_total}
    Logout
