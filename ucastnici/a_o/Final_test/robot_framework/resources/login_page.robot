*** Keywords ***
Login To App
    [Arguments]    ${username}    ${password}
    Input Text      id:user-name    ${username}
    Input Text      id:password     ${password}
    Click Button    id:login-button