*** Settings ***
Documentation     A test suite for valid login.

Library           page.py

*** Variables ***

${count}  5

*** Test Cases ***
Login User with Password
    [Setup]  Browser is opened   
    Load page  https://www.saucedemo.com/
    Login standard_user with secret_sauce
    [Teardown]  Close Browser

*** Keywords ***

Login ${name} with ${password}
    Login user  ${name}  ${password}