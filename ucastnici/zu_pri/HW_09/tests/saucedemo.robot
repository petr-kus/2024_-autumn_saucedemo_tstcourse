*** Settings ***
Documentation                  About this test suite
Resource                       ../resources/saucedemoApp.robot
Resource                       ../resources/common.robot
Suite Setup                    Start tests - Open browser
Suite Teardown                 Finish tests - Close browser

# text spouštěcího scriptu:
# robot -d results tests/saucedemo.robot
# TODO Lektor - nebal bych se to dat jako poznamku do dokumentace nahore. 
# TODO Lektor - V kazdem pade hned po otevreni jsem impressed jak adresarovou strukturu, tak oddlenim do souboru tak pouzitim Suite Setup a Suite teardown!

*** Variables ***
${BROWSER} =                   chromium

*** Test Cases ***
Can Login with valid credentials
    [Documentation]            About test no. 001
    # TODO Lektor - ty dokumentacni texty by to opravdu chtelo vylepsit... . Tohle nic nerika... .
    [Tags]                     001
    saucedemoApp.Load Page     https://www.saucedemo.com/
    saucedemoApp.Login using   USERNAME=standard_user    PASSWORD=secret_sauce
    # TODO Lektor tady by to slo i bez pojmenovani parametru staci poradi.. ale otazka je srozumitelnost pouzil bych to ze to muze byt soucasti nazvu.
    #saucedemoApp.Login standard_user with secret_sauce
    saucedemoApp.Logout
    # TODO Lektor - vidim ze mas pozuite "dve" page obejktove struktury zanorene do sebe.
    # hele neni to spatny, libi se mi to. Otazka zni zda by spis nestacilo jen jedno zanoreni! 
    # pri jendom zanoreni by lepe sel videt obsah a prubeh testu, takhle je to dost prazdne a zanorene...

Add item to cart
    [Documentation]            About test no. 002
    [Tags]                     002
    [Setup]                    standard_user is logged in
    # TODO Lektor - chvalim pousiti takoveho krasneho setu keywordu :-), jde videt ze poslouchas lektora... 
    saucedemoApp.Add Backpack to cart
    # TODO Lektor - tady uz je to fakt jen prevolani... nema smysl druha struktura...

*** Keywords ***
${user} is logged in
    ${cart_present} =   Get Element States  ${CART_LINK}
    Run Keyword If      'visible' not in ${cart_present}       saucedemoApp.Login using   USERNAME=${user}    PASSWORD=secret_sauce
    # TODO Lektor - hezka implementace. Ale to by mimochodem slo zjistit z objektu stranky pokud by jis si ji nekde drzela, kdo je zalogovany. 
    # jde o pokrocili trik kdy si kontext testu drzis v property python objektu v prubehu testu ... a methody z neho je pres self. ci jinak.. nastavuji/ctou.
    # v tom trikcu jde o kombinaci pythonu a robot frameworku... . Da se to nahradit pres globalni promene ale to pak neni tak ciste a hezke. 
    # ze si nekde vytvoris globalni promenou kterou nastavujes dle toho jakeho uzivatele by jsi zalogovala. 
    # Jak vidis ... tady v tve implementaci nevis ze jde o standart usra nebo nekoho jineho.
    # Dalsi cesta nez si to pmaatovat je take ze by se to asi dalo vycist z cokiies souboru... .

#TODO Lektor a co ta nahravka nebo obrazky z testovani? :-)