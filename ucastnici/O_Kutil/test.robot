*** Settings ***
Library    SeleniumLibrary
Library    DateTime

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
    ${start_time}=    Get Time    epoch
    Open Browser    ${URL}    Chrome
    Input Text      id:user-name    ${USERNAME}
    Input Text      id:password     ${PASSWORD}
    Click Element   id:login-button
    Verify Login Successful
    ${end_time}=    Get Time    epoch
    ${duration}=    Evaluate    ${end_time} - ${start_time}
    Run Keyword And Continue On Failure    Should Be True    ${duration} <= 3    Login took too long: ${duration} seconds (maximum allowed: 3 seconds)
    Capture Page Screenshot

Verify Login Successful
    Element Should Be Visible    id:inventory_container
    Log    Login was successful
