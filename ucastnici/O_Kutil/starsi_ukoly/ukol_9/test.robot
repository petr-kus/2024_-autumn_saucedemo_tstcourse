*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PASSWORD}    secret_sauce
${URL}         https://www.saucedemo.com
@{USERS}       standard_user    locked_out_user    problem_user    performance_glitch_user    error_user    visual_user

*** Test Cases ***
Test Login For All Users
    FOR    ${USERNAME}    IN    @{USERS}
        Run Login Test And Continue    ${USERNAME}
        Close Browser
    END

*** Keywords ***
Run Login Test And Continue
    [Arguments]    ${USERNAME}
    Run Keyword And Continue On Failure    Run Login Test    ${USERNAME}

Run Login Test
    [Arguments]    ${USERNAME}
    Open Browser    ${URL}    Chrome
    Input Text      id:user-name    ${USERNAME}
    Input Text      id:password     ${PASSWORD}
    Click Element   id:login-button
    Verify Login Successful
    Capture Page Screenshot

Verify Login Successful
    Element Should Be Visible    id:inventory_container
    Log    Login was successful
