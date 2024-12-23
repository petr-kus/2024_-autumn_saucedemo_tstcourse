*** Settings ***
Library    SeleniumLibrary
Resource   variables.robot

*** Keywords ***
Perform Login
    [Arguments]   ${username}          ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Text    ${PASSWORD_FIELD}    ${password}
    Click Button  ${LOGIN_BUTTON}

Verify Login Successful
    Wait Until Location Contains   inventory.html
