*** Settings ***
Library                          Browser

*** Variables ***
${CART_URL} =                    https://www.saucedemo.com/cart.html
# ${NUMBER_OF_ITEMS_IN_CART} =     xpath=//div[@class='cart_list']//div[@class='cart_quantity']

*** Keywords ***
# Check number of items in cart
#     ${count}     Get Element Count    selector=${NUMBER_OF_ITEMS_IN_CART}
#     log     ${count}