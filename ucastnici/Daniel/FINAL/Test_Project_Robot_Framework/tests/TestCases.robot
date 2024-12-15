*** Settings ***
Library     Browser
Library    ../venv/Lib/site-packages/robot/libraries/XML.py
Resource    ../resources/BrowserSetup.robot
Resource    ../resources/Keywords.robot
Resource    ../resources/Variables.robot

Suite Setup    Setup Browser
Suite Teardown    Teardown Browser

*** Test Cases ***
Test Valid Login
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    
    ${expected_url}=    Set Variable    https://www.saucedemo.com/inventory.html
    ${current_url}=     Get Url
    Should Be Equal     ${current_url}    ${expected_url}
    Log    The result login page was loaded succesfully -> ${current_url}    INFO    ${False}    ${True}

Test logout
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    Logout

    ${expected_url}=    Set Variable    ${BASE_URL}
    ${current_url}=     Get Url
    Should Be Equal     ${current_url}    ${expected_url}
    Log    The result logout page was loaded succesfully -> ${current_url}

Test Add Item To Cart
    Login With Credentials   ${USERNAME}    ${PASSWORD}
    Add Item to cart    ${ITEM_NAME}

    ${cart_badge_number}=    Get Cart Badge Number
    Should Be Equal    ${cart_badge_number}    1
    Log    The cart badge number is ${cart_badge_number}    INFO    ${False}    ${True}

#HODNOCENI: (100 bodu je maximum - pokud někdo nebude fakt dobrej*á) 
# + 50 bodu za funkčnost (jde spustit, standard_user prochází a na uživateli locked_out_user failuje). 
# - 5 bodu zapomnel jsi na call rfbrowser init pro iniciaci Browser Library v readme nebo prerequisities scriptu... :-)
# + 10 bodu za použití jiné technologie než selenium a jiným způsobem než importem py souborů z pythonu
# + 7 bodu za readme markdown file!
# + 5 bodu odddeleni keywordu do souboru i dat

#=> 67 bodů TEST V RF splněn! 

# mohl jsi dostat další body kdyby třeba... (easy tip pro ostatní):
# - jsi použil Screenshot library pro dělaní obrázků dodatečně (technologie o které jsme nemluvili)
# - jsi použil recording videa pro robot framework (technologie o které jsme nemluvili)
# - mohl jsi vyuzit silne vlastnosti RF a mít proměnou uvnitř jména keywordu
# - mohl jsi lepe vyuzit pojmenovani dat a nepouzit jen prejmenovani v promene (OOP object napr ${user.valid_name} ... nebo jinak... a jeste lepe)
# - mohl jsi něják pracovat s POM (page obeject modelem)
# - mohl jsi odevzdat výsledek logů i v Allure (technologie o které jsme nemluvili)
# - mohl jsi použít nějaký listener pro něco
# - mohl jsi "pochlebovat lektrovi" a použít balíček pytest-in-robotoframework a využít parametrizace pytestu z roboto frameworku
# - mohl jis použít BDD zápis!
# - mohl jis použít data driven zápis pro Roboto Framework (něco jako parametrizace v pytestu)
# - mohli si tu mít rovnou test case co failuje a ukázal by že s jinýma datama pro stejný test case to odhaluje chybu..
# ... 
