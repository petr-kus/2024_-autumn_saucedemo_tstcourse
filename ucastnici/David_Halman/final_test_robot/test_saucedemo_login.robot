*** Settings ***
Library         SeleniumLibrary
Library         Browser
Library         Collections

*** Variables ***
${URL}          https://www.saucedemo.com/
${USERNAME}     standard_user
${PASSWORD}     secret_sauce

*** Test Cases ***

# Testovací případ pomocí SeleniumLibrary
Login Test with Selenium Library
    [Documentation]    Test validního přihlášení pomocí Selenium Library.
    SeleniumLibrary.Open Browser     ${URL}    Chrome
    Input Text                      id:user-name    ${USERNAME}
    Input Text                      id:password     ${PASSWORD}
    Click Button                    id:login-button
    Should Contain                  title           Products
    SeleniumLibrary.Close Browser

Failed Login Test with Selenium Library
    [Documentation]    Test neplatného přihlášení pomocí Selenium Library.
    SeleniumLibrary.Open Browser     ${URL}    Chrome
    Input Text                      id:user-name    invalid_user
    Input Text                      id:password     wrong_password
    Click Button                    id:login-button
    Should Contain                  xpath://div[contains(@class, 'error-message')]    Epic sadface:
    SeleniumLibrary.Close Browser

# Testovací případ pomocí Browser Library
Login Test with Browser Library
    [Documentation]    Test validního přihlášení pomocí Browser Library.
    Browser.Open Browser             ${URL}    Chromium
    Browser.Fill Text                [data-test="username"]    ${USERNAME}
    Browser.Fill Text                [data-test="password"]    ${PASSWORD}
    Browser.Click                    [data-test="login-button"]
    Browser.Wait For Elements State   text="Products"    visible
    Browser.Close Browser

Failed Login Test with Browser Library
    [Documentation]    Test neplatného přihlášení pomocí Browser Library.
    Browser.Open Browser             ${URL}    Chromium
    Browser.Fill Text                [data-test="username"]    invalid_user
    Browser.Fill Text                [data-test="password"]    wrong_password
    Browser.Click                    [data-test="login-button"]
    Browser.Wait For Elements State   text="Epic sadface:"    visible
    Browser.Close Browser
