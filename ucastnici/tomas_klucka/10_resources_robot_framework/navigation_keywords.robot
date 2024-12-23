*** Settings ***
Library    SeleniumLibrary
Resource   variables.robot

*** Keywords ***
Open Menu
    Wait Until Element Is Visible    id=react-burger-menu-btn    3s
    Click Element    ${MENU_BUTTON}
    Wait Until Element Is Visible    ${ABOUT_LINK}

Navigate To About Page
    Wait Until Element Is Visible    id=about_sidebar_link    3s
    Click Element    ${ABOUT_LINK}
    Page Should Not Contain    404 Not Found

Perform Logout
    Click Element    ${LOGOUT_LINK}
    Wait Until Page Contains Element    ${USERNAME_FIELD}
