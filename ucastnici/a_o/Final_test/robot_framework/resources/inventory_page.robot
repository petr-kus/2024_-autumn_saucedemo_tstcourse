*** Keywords ***
Verify Page Title
    [Arguments]    ${expected_title}
    ${actual_title}=    Get Text    class:title
    Should Be Equal    ${actual_title}    ${expected_title}

Verify Error Message
    Element Should Contain    xpath://div[@class='error-message-container']    "lock"