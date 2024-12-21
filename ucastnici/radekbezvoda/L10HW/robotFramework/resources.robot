*** Settings ***
Library         SeleniumLibrary
Library         OperatingSystem
Library    String

*** Variables ***
${MAIN_PAGE_URL}    https://www.saucedemo.com/
${SCREENSHOT_FOLDER}    screenshots
${STANDARD_USER}        standard_user
${STANDARD_PASSWORD}    secret_sauce
${PROBLEM_USER}         problem_user
${PERFORMANCE_GLITCH_USER}    performance_glitch_user
${BAD_USERNAME}         error_user
${BAD_PASSWORD}         sauce
@{INVALID_CREDENTIALS}    ${BAD_USERNAME}:${BAD_PASSWORD} 
@{VALID_CREDENTIALS}      ${STANDARD_USER}:${STANDARD_PASSWORD}    ${PROBLEM_USER}:${STANDARD_PASSWORD}    ${PERFORMANCE_GLITCH_USER}:${STANDARD_PASSWORD}
${LOG_FILE}    robotframework-logs.txt
${screenshot_index}    0



*** Keywords ***

Open Browser And Maximize
  Open Browser    ${MAIN_PAGE_URL}    Chrome    maximize=True
  Set Selenium Implicit Wait    10s

Login With Credentials
    [Arguments]    ${username}    ${password}
    ${current_url}=    Get Location
    Log    Current URL: ${current_url}
    Should Be Equal As Strings    ${current_url}    ${MAIN_PAGE_URL}
    ${status}=    Run Keyword And Return Status    Input Text    id:user-name    ${username}
    IF    ${status} == False
        Fail    Could not input username.
    END
    ${status}=    Run Keyword And Return Status    Input Text    id:password    ${password}
    IF    ${status} == False
        Fail    Could not input password.
    END
    ${status}=    Run Keyword And Return Status    Click Button    id:login-button
    IF    ${status} == False
        Log    Could not click the login button. ERROR
        Fail    Could not click the login button.
    END

Check Failed Login
    ${current_url}=    Get Location
    Log    Testing failed login, Current URL: ${current_url}
    Should Be Equal As Strings    ${current_url}    ${MAIN_PAGE_URL}
    ${error_message}=    Set Variable    Epic sadface: Username and password do not match any user in this service 
    ${status}=    Run Keyword And Return Status    Page Should Contain    ${error_message}
    IF    not ${status}
        Log     Login error message was not displayed. ERROR
        Fail    Login error message was not displayed.
    END



Check Successful Login
    ${current_url}=    Get Location
    Log    Current URL: ${current_url}
    ${expected_url}=    Set Variable    ${MAIN_PAGE_URL}inventory.html
    Should Be Equal As Strings    ${current_url}    ${expected_url}
    ${status}=    Run Keyword And Return Status    Should Be Equal As Strings    ${current_url}    ${expected_url}
    IF    ${status} == False
        Log    Login was not successful. Current URL: ${current_url} ERROR
        Fail    Login was not successful. Current URL: ${current_url}
    END



Logout
    ${status}=    Run Keyword And Return Status    Click Element    id:react-burger-menu-btn
    IF    ${status} == False
        Fail    Could not click the menu button.
    END
    ${status}=    Run Keyword And Return Status    Wait Until Page Contains Element    id:logout_sidebar_link
    IF    ${status} == False
        Fail    Logout link was not found.
    END
    ${status}=    Run Keyword And Return Status    Click Element    id:logout_sidebar_link
    IF    ${status} == False
        Fail    Could not click the logout link.
    END
    ${current_url}=    Get Location
    ${status}=    Run Keyword And Return Status    Should Be Equal As Strings    ${current_url}    ${MAIN_PAGE_URL}
    IF    ${status} == False
        Fail    Logout was not successful. Current URL: ${current_url}
    END
    Log    Logout successful

Setup Test Environment
    ${screenshot_path}=    Set Variable    ${CURDIR}${/}screenshots
    ${folder_exists}=    Run Keyword And Return Status    Directory Should Exist    ${screenshot_path}
    IF    not ${folder_exists}
        Create Directory    ${screenshot_path}
        Log    Screenshot folder '${screenshot_path}' created.
    ELSE
        Log    Screenshot folder '${screenshot_path}' already exists.
    END
    Open Browser And Maximize

