*** Settings ***
Resource    10_resources_robot_framework/variables.robot
Resource    10_resources_robot_framework/browser_keywords.robot
Resource    10_resources_robot_framework/login_keywords.robot
Resource    10_resources_robot_framework/navigation_keywords.robot

*** Variables ***
@{USERS}      ${STANDARD_USER}    ${PROBLEM_USER}    ${ERROR_USER}

*** Test Cases ***
Test User Login
    FOR    ${user}    IN    @{USERS}
        Perform Login And Verify Success    ${user}    ${PASSWORD}
    END

Test Login And Navigate To About Page
    FOR    ${user}    IN    @{USERS}
        Perform Login And Navigate To About Page    ${user}    ${PASSWORD}
    END

Test User Login And Logout
    FOR    ${user}    IN    @{USERS}
        Perform Login And Logout    ${user}    ${PASSWORD}
    END

*** Keywords ***
Perform Login And Verify Success
    [Arguments]      ${username}    ${password}
    Open Browser To Login Page      ${BASE_URL}
    Perform Login    ${username}    ${password}
    Verify Login Successful
    Close Browser

Perform Login And Navigate To About Page
    [Arguments]      ${username}    ${password}
    Open Browser To Login Page      ${BASE_URL}
    Perform Login    ${username}    ${password}
    Verify Login Successful
    Open Menu
    Navigate To About Page
    Close Browser

Perform Login And Logout
    [Arguments]      ${username}    ${password}
    Open Browser To Login Page      ${BASE_URL}
    Perform Login    ${username}    ${password}
    Verify Login Successful
    Open Menu
    Perform Logout
    Location Should Be              ${BASE_URL}
    Close Browser
