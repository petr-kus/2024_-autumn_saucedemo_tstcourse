*** Keywords ***

Login With Credentials
    [Arguments]    ${username}    ${password}
    New Page    ${BASE_URL}
    Fill Text      ${user_name_id}    ${username}
    Fill Text      ${password_id}    ${password}
    Click          ${login_button}
    Log    Login in with ${username}    INFO    ${False}    ${True}

Logout
    Click    ${burger_menu}
    Click    ${logout}
    Log    Attempted to log out, User = ${username}    INFO    ${False}    ${True}

Add Item to cart
    [Arguments]    ${item_name}
    Click    ${item_name}

Get Cart Badge Number
    ${badge_number}=    Get Text    ${shopping_cart_badge}
    RETURN    ${badge_number}
