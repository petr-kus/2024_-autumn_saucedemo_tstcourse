*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PASSWORD}    secret_sauce
${URL}         https://www.saucedemo.com
@{USERS}       standard_user    locked_out_user    problem_user    performance_glitch_user    error_user    visual_user

# TODO Lektor - test je moc hezky a funguje. Ocenuji prilozene screenshoty v logach.
#mame zjevne odlisne verze pythonu, takze v reamde by to chtelo zminit verzi pythonu. (mel jsme problem s tvyma balickama)
# TODO Lektor - lepsi pro implementaci takovehoto test casu by byl Data Driven apraoch. 
# Coz je zjevne to co jsi se tu snazil po svem implementovat... . RF pro to ma primo konstrukci.
# podrobny priklad je zde... https://docs.robotframework.org/docs/testcase_styles/datadriven
# tam by slo i krasne nastavit overeni zda ma nebo nema byt uzivatel prihlasen...

*** Test Cases ***
Test Login For All Users
    FOR    ${USERNAME}    IN    @{USERS}
        Run Login Test And Continue    ${USERNAME}
        Close Browser
    END

*** Keywords ***
Run Login Test And Continue
    [Arguments]    ${USERNAME}
    Run Keyword And Continue On Failure    Run Login Test    ${USERNAME}

Run Login Test
    [Arguments]    ${USERNAME}
    Open Browser    ${URL}    Chrome
    Input Text      id:user-name    ${USERNAME}
    Input Text      id:password     ${PASSWORD}
    Click Element   id:login-button
    Verify Login Successful
    Capture Page Screenshot

Verify Login Successful
    Element Should Be Visible    id:inventory_container
    Log    Login was successful

#TODO Lektor - celkove je to obdobne tomu kdyz jsme ze zacatku psali skripty a nepouzivali zadne zovbecneni.
# i zde neni pouzit zadne POM ... a klidne by mohlo :-). RF samozrejmne dela spoustu veci za tebe, takze bytrvalo dele nez by se ti to vymstilo.
# ale i zde je dobre tu id mit deinovane nekde zvlast... .

#TODO Lektor - ja osobne bych si i jinak pojmenoval keywordy... treba
# 'Run Login Test And Continue' bych pojmenoval 'Try ${USERNAME} login'
# a tim zvysoval citelnost testu... .