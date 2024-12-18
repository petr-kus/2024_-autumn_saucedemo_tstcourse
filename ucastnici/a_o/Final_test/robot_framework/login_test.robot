*** Settings ***
Library           SeleniumLibrary
Library           Screenshot
Resource          resources/login_page.robot
Resource          resources/inventory_page.robot
Variables         ucastnici\a_o\Final_test\robot_framework\variables\test_data.robot



*** Test Cases ***
Valid Login
    [Tags]    Valid
    Open Browser    ${URL}    Chrome
    Login To App    ${USER}    ${PASSWORD}
    Verify Page Title    ${EXPECTED_TITLE}
    Capture Page Screenshot
    Stop Video Recording
    [Teardown]    Close Browser

Invalid Login
    [Tags]    Invalid
    Open Browser    ${URL}    Chrome
    Login To App    ${LOCKED_USER}    ${PASSWORD}
    Verify Error Message
    Capture Page Screenshot
    Stop Video Recording
    [Teardown]    Close Browser