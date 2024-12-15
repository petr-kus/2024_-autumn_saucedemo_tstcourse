*** Settings ***
Library    Browser
Library    DateTime

*** Variables ***
${BROWSER}    chromium
${HEADLESS}    False
${BASE_URL}    https://www.saucedemo.com/

*** Keywords ***
Setup Browser
    New Browser    ${BROWSER}    ${HEADLESS}
    New Context    viewport={'width': 1920, 'height': 1080}
    Set Browser Timeout    3 sec

Teardown Browser
    [Teardown]
    Close Browser

    