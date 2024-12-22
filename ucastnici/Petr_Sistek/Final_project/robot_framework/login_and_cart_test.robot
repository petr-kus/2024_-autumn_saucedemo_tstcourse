*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}          https://www.saucedemo.com
${USERNAME}     standard_user
${PASSWORD}     secret_sauce
${PRODUCT}      Sauce Labs Backpack

*** Test Cases ***
Test Login And Add To Cart
    Open Browser    ${URL}  chrome
    Maximize Browser Window
    Login To SauceDemo
    Add Product To Cart
    Verify Product In Cart
    Close Browser

*** Keywords ***
Login To SauceDemo
    Input Text                  id = user-name  ${USERNAME}
    Input Text                  id = password   ${PASSWORD}
    Click Button                id = login-button
    Wait Until Page Contains    Products

Add Product To Cart
    Click Button            xpath = //div[@class="inventory_item"][.//div[text()="${PRODUCT}"]]//button
    Wait Until Page Contains     1

Verify Product In Cart
    Click Link                  class = shopping_cart_link
    Wait Until Page Contains    ${PRODUCT}
    Page Should Contain         ${PRODUCT}