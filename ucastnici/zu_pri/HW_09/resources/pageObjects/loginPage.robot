*** Settings ***
Library                          Browser

*** Variables ***
${LOGIN_PAGE_TITLE} =            Swag Labs
${USERNAME_FIELD} =              xpath=//input[@placeholder="Username"]
${PASSWORD_FIELD} =              xpath=//input[@placeholder="Password"]
${LOGIN_BUTTON} =                xpath=//*[text()="Login"]

*** Keywords ***
Check Login Page is loaded
    Wait For Elements State      text=${LOGIN_PAGE_TITLE}

Click Login Button
    Click                        "Login"

Fill in username
    [Arguments]    ${USERNAME}
    Fill Text    selector=${USERNAME_FIELD}    txt=${USERNAME}

Fill in password
    [Arguments]    ${PASSWORD}
    Fill Text    selector=${PASSWORD_FIELD}    txt=${PASSWORD}

#TODO Lektor - krasa tak nak bych ocekaval vnitrni implementaci.

