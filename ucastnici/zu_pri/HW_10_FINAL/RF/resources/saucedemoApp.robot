*** Settings ***
Library                          Browser
Resource                         ../resources/pageObjects/loginPage.robot
Resource                         ../resources/pageObjects/cart.robot
Resource                         ../resources/pageObjects/header.robot
Resource                         ../resources/pageObjects/inventoryPage.robot

*** Keywords ***
    
Load Page
    [Arguments]                  ${STARTING_PAGE}
    Go To                        ${STARTING_PAGE}   
    loginPage.Check Login Page is loaded

Login using
    [Arguments]                  ${USERNAME}    ${PASSWORD}
    Set Test Message             Test started with username: "${USERNAME}" and password: "${PASSWORD}"
    loginPage.Fill in username   ${USERNAME}
    Take Screenshot 
    loginPage.Fill in password   ${PASSWORD}
    Take Screenshot 
    loginPage.Click Login Button
    loginPage.Check if logged in

Logout
    header.Open burger menu
    header.Click Logout

Add Backpack to cart
    inventoryPage.Add Backpack to cart
    Take Screenshot
    ${CART_COUNT} =     header.Check number of items in cart
    IF  "${CART_COUNT} == 1"
        log     Backpack succesfully added.
    ELSE    
        Fail    Expected 1 item in the cart, but found ${CART_COUNT}.
    END

Go to Checkout
    cart.Go to Cart by clicking Cart Icon
    cart.Click Checkout Button

Remove all items from Cart
    cart.Go to Cart by clicking Cart Icon
    Take Screenshot
    cart.Click all Remove buttons
    Take Screenshot
    cart.Check number of items in cart
    IF    "${NUMBER_OF_ITEMS_IN_CART} == 0"
        Log   Cart successfully emptied.
    ELSE
        Fail  Expected 0 item in the cart, but found ${NUMBER_OF_ITEMS_IN_CART}.
    END
