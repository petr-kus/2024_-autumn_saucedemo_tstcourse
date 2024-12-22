*** Settings ***
Library                     Browser

*** Keywords ***
Start tests - Open browser
    New Browser             ${BROWSER}     headless=False
    New Context
    New Page

Finish tests - Close browser
    Close browser