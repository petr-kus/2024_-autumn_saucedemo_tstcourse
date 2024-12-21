*** Settings ***
Resource         resources.robot
Suite Teardown   Close All Browsers

*** Test Cases ***
Unhappy Login Test
    [Tags]    unhappy
    [Setup]    Setup Test Environment
    FOR    ${credential}    IN    @{INVALID_CREDENTIALS}
        @{parts}=    Split String    ${credential}    :
        ${username}=    Set Variable    ${parts[0]}
        ${password}=    Set Variable    ${parts[1]}
        Login With Credentials    ${username}    ${password}
        Check Failed Login
    END
    Close Browser

Happy Login Test
    [Tags]    happy
    [Setup]    Setup Test Environment

    FOR    ${credential}    IN    @{VALID_CREDENTIALS}
        @{parts}=    Split String    ${credential}    :
        ${username}=    Set Variable    ${parts[0]}
        ${password}=    Set Variable    ${parts[1]}
        Login With Credentials    ${username}    ${password}
        Check Successful Login
        Logout
    END
    Close Browser





