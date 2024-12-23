*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Open Browser To Login Page
    [Arguments]    ${url}
    Open Browser   ${url}    Chrome
    Maximize Browser Window

Close Browser
    Close All Browsers
