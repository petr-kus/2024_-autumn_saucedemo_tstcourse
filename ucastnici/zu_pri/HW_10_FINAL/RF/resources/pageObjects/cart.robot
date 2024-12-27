*** Settings ***
Library                          Browser

*** Variables ***
${CART_URL} =                    https://www.saucedemo.com/cart.html
${CART_ICON} =                   xpath=//div[@id='shopping_cart_container']
${CHECKOUT_BUTTON} =             xpath=//*[text()="Checkout"]
${REMOVE_BUTTONS}=               xpath=//button[text()='Remove']
${NUMBER_OF_ITEMS_IN_CART} =     xpath=//div[@class='cart_list']//div[@class='cart_quantity']

*** Keywords ***
Check number of items in cart
    ${count}     Get Element Count    ${NUMBER_OF_ITEMS_IN_CART}
    log     ${count}

Go to Cart by clicking Cart Icon
    click                        ${CART_ICON}

Click Checkout Button
    Click                        "Checkout"

Click all Remove buttons
    FOR    ${button}    IN   ${REMOVE_BUTTONS}
        Click  ${button}
    END
