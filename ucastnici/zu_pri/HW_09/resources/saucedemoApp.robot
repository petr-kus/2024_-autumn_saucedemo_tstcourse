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
    loginPage.Fill in password   ${PASSWORD}
    loginPage.Click Login Button

Logout
    header.Open burger menu
    header.Click Logout

Add Backpack to cart
    inventoryPage.Add Backpack to cart
    ${CART_COUNT} =     header.Check number of items in cart
    IF  "${CART_COUNT} == 1"
        log   Backpack succesfully added.
    ELSE    
        Fail    Expected 1 item in the cart, but found ${CART_COUNT}.
    END
