*** Settings ***
Documentation                  FINAL Homework Test Suite
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
    [Documentation]            Login test with valid user
    [Tags]                     001
    saucedemoApp.Load Page     https://www.saucedemo.com/
    saucedemoApp.Login using   USERNAME=standard_user    PASSWORD=secret_sauce
    saucedemoApp.Logout

Try Login with Locked Out User
    [Documentation]            Login test with user who cannot log in; FAIL is expected
    [Tags]                     002
    saucedemoApp.Load Page     https://www.saucedemo.com/
    saucedemoApp.Login using   USERNAME=locked_out_user    PASSWORD=secret_sauce
    saucedemoApp.Logout

Add item to cart and remove it
    [Documentation]            Test adding and removing items to Cart from Inventory page
    [Tags]                     003
    [Setup]                    standard_user is logged in
    saucedemoApp.Add Backpack to cart
    saucedemoApp.Go to Checkout
    saucedemoApp.Remove all items from Cart


*** Keywords ***
${user} is logged in
    ${cart_present} =   Get Element States  ${CART_LINK}
    Run Keyword If      'visible' not in ${cart_present}       saucedemoApp.Login using   USERNAME=${user}    PASSWORD=secret_sauce