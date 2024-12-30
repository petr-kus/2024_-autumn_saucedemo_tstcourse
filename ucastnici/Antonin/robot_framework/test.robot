*** Settings ***
Library   Browser
#TODO Lektor - nevidim tu nikde readme nebo requiremnts ktere by splnili co je potreba pro pusteni takovehoto testu.
#spoleha se jen na to ze vim jak to udelat :-) - ja to vim... ale nekdo jiny uz nemusi!
#Vzdy by melo byt pohromade i neco co pripravi to testovaci prostredi (skript dobre citelny navod treba v md souboru)!

#TODO Lektor - hlavni komentar k RF je asi v posledni koznultaci nahrany. 
# take jsme komentoval na lekci.
# zde plati vse co je v te konzultaci a na lekci receno, dam par poznamek i sem.


*** Test Cases ***
Checkout Test
    Login Page Test    standard_user    secret_sauce
    Varify Login
    Add Item to Cart Test    backpack
    Checkout Test    Joe    Doe    111
    [Teardown]    #TODO Lektor - poku tu neni step je ten teardown zbytecny 

Denied Login Information 
    #TODO Lektor podle nazvu test casu mi neni moc jasny co se tim testuje... 
    Login Page Test    locked_out_user    secret_sauce
    Varify Denied Login
    [Teardown]

*** Keywords ***
Login Page Test
    [Arguments]    ${login}    ${password}
    #TODO Lektor - argumenty mohli byt s vyhodou RF pouziti zevnitr nazvu, napriklad:
    # Login  ${user} with ${password}
    # a neni to test ale spis step ze?
    New Page     https://www.saucedemo.com/
    #TODO Lektor - toto (ta stranka) urcite melo byt parametrizovano z venku.
    Type Text    input#user-name     ${login}
    Type Text    input#password  ${password}
    Click        id=login-button
Varify Login
    Get Url      contains  inventory
Varify Denied Login
    Get Text     h3    contains    Epic sadface
Add Item to Cart Test
    [Arguments]    ${item}
    Click        id=add-to-cart-sauce-labs-${item}
    Get Text     span.shopping_cart_badge  ==     1 

Checkout Test
    #TODO Lektor - toto neni test... je to step... nepojmenovavat test.
    #mozna by ten keyword sel rozdelit ze... 
    [Arguments]    ${first_name}    ${last_name}    ${zip}
    Click        a.shopping_cart_link
    Get Url      contains  cart
    Click        "Checkout"
    Type Text    input#first-name     ${first_name}
    Type Text    input#last-name  ${last_name}
    Type Text    input#postal-code  ${zip}
    Click        "Continue"
    Click        "Finish"
    Get Text     h2    contains    Thank you
    #TODO Lektor - id mohou byt stale v POM strukture mimo samotny predpis testu a test stepu. 
    #je to vyhoda a metoda pouzitelna v libovolnym tets frameworku a ma svuj duvod.
    #zde jsou ID opet na tvrdo napsany zde... .

#TODO Lektor - nejsou nidke zadne screnshoty/video z pruchodu testu. Mohlo by byt... .