*** Settings ***
Library           Browser
Resource          keywords.resource

*** Test Cases ***
Smoke Checkout Test
    [Tags]    happy_path
    Load https://www.saucedemo.com/
    Test log in standard_user with password secret_sauce
    Confirm positive login
    Add random item to Cart Test
    Checkout Test    Joe    Doe    111    

Denied Login Information
    [Tags]    negative
    Load https://www.saucedemo.com/
    Test log in locked_out_user with password secret_sauce
    Confirm negative login

*** Keywords ***
Load ${page}
    New Page     ${page}
Test log in ${login} with password ${password}
    Populate field user-name with ${login}
    Populate field password with ${password}
    Click        "Login"
Confirm ${output} login
    Login ${output}   
Add random item to Cart Test
    Add random item to Cart
Checkout Test
    [Arguments]    ${first_name}    ${last_name}    ${zip}
    Enter the Cart
    Click        "Checkout"
    Populate field first-name with ${first_name}
    Populate field last-name with ${last_name}
    Populate field postal-code with ${zip}
    Click        "Continue"
    Click        "Finish"
    Confirm Checkout