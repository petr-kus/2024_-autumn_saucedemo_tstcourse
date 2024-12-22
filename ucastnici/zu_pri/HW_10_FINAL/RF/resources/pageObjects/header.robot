*** Settings ***
Library                           Browser

*** Variables ***
${OPEN_BURGER_MENU} =             id=react-burger-menu-btn
${LOGOUT_BUTTON} =                xpath=//*[text()="Logout"]
${CART_LINK} =                    xpath=//*[@id="shopping_cart_container"]/a
${CART_BADGE} =                   //*[@class="shopping_cart_badge"]

*** Keywords ***
Open burger menu
    Click                         ${OPEN_BURGER_MENU}

Click Logout
    Click                         ${LOGOUT_BUTTON}

Check number of items in cart
    ${NUMBER_OF_ITEMS_IN_CART} =    Get Text    selector=${CART_BADGE}
    RETURN     ${NUMBER_OF_ITEMS_IN_CART}