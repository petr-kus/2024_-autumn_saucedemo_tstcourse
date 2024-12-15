*** Settings ***
Library   Browser

*** Test Cases ***
Checkout Test
    Login Page Test    standard_user    secret_sauce
    Varify Login
    Add Item to Cart Test    backpack
    Checkout Test    Joe    Doe    111
    [Teardown]    

Denied Login Information
    Login Page Test    locked_out_user    secret_sauce
    Varify Denied Login
    [Teardown]

*** Keywords ***
Login Page Test
    [Arguments]    ${login}    ${password}
    New Page     https://www.saucedemo.com/
    Type Text    input#user-name     ${login}
    Type Text    input#password  ${password}
    Click        id=login-button
Varify Login
    Get Url      contains  inventory
Varify Denied Login
    Get Text     h3    contains    Epic sadface
Add Item to Cart Test
    [Arguments]    ${item}
    Click        id=add-to-cart-sauce-labs-${item}
    Get Text     span.shopping_cart_badge  ==     1 
Checkout Test
    [Arguments]    ${first_name}    ${last_name}    ${zip}
    Click        a.shopping_cart_link
    Get Url      contains  cart
    Click        "Checkout"
    Type Text    input#first-name     ${first_name}
    Type Text    input#last-name  ${last_name}
    Type Text    input#postal-code  ${zip}
    Click        "Continue"
    Click        "Finish"
    Get Text     h2    contains    Thank you
    