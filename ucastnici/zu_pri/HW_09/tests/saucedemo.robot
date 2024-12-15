*** Settings ***
Documentation                  About this test suite
Resource                       ../resources/saucedemoApp.robot
Resource                       ../resources/common.robot
Suite Setup                    Start tests - Open browser
Suite Teardown                 Finish tests - Close browser

# text spouštěcího scriptu:
# robot -d results tests/saucedemo.robot

*** Variables ***
${BROWSER} =                   chromium

*** Test Cases ***
Can Login with valid credentials
    [Documentation]            About test no. 001
    [Tags]                     001
    saucedemoApp.Load Page     https://www.saucedemo.com/
    saucedemoApp.Login using   USERNAME=standard_user    PASSWORD=secret_sauce
    saucedemoApp.Logout

Add item to cart
    [Documentation]            About test no. 002
    [Tags]                     002
    [Setup]                    standard_user is logged in
    saucedemoApp.Add Backpack to cart


*** Keywords ***
${user} is logged in
    ${cart_present} =   Get Element States  ${CART_LINK}
    Run Keyword If      'visible' not in ${cart_present}       saucedemoApp.Login using   USERNAME=${user}    PASSWORD=secret_sauce