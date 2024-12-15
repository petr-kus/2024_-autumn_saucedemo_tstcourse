*** Settings ***
Library     Browser
Library    ../venv/Lib/site-packages/robot/libraries/XML.py
Resource    ../resources/BrowserSetup.robot
Resource    ../resources/Keywords.robot
Resource    ../resources/Variables.robot

Suite Setup    Setup Browser
Suite Teardown    Teardown Browser

*** Test Cases ***
Test Valid Login
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    
    ${expected_url}=    Set Variable    https://www.saucedemo.com/inventory.html
    ${current_url}=     Get Url
    Should Be Equal     ${current_url}    ${expected_url}
    Log    The result login page was loaded succesfully -> ${current_url}    INFO    ${False}    ${True}

Test logout
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    Logout

    ${expected_url}=    Set Variable    ${BASE_URL}
    ${current_url}=     Get Url
    Should Be Equal     ${current_url}    ${expected_url}
    Log    The result logout page was loaded succesfully -> ${current_url}

Test Add Item To Cart
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    Add Item to cart    ${ITEM_NAME}

    ${cart_badge_number}=    Get Cart Badge Number
    Should Be Equal    ${cart_badge_number}    1
    Log    The cart badge number is ${cart_badge_number}    INFO    ${False}    ${True}