import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

#TODO Lektor - za me dobre zpracovani dost minimalisticke teda. Ale je to dobre.  
#TODO Lektor - par poznamek preci jen budu mit... celkove chtelo by to vic logovani!
#TODO Lektor - a mohla jsi si predat nekde driver aby jsi nemusela znovu otvirat browser. Skoda ze to tu nemas.
#TODO Lektor - pak by jsi musela zacit premyslet jak to udelat. a to by byl nejlepsi ten signlton pattern z prikladu z ukolu 7.
#TODO Lektor - pochvala za pouziti conftestu!
#TODO Lektor - pochvala za hezkou strukturu slozek!
#TODO Lektor - velka nepochvala za v podstate chybejejici reseni logovani!
#TODO Lektor - velka nepochvala za neaktualni requirements.txt (chybi me pro spusteni testu nake balicky...)

def test_inventory_item_count(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    #TODO Lektor - to melo byt parametrizovane z venku.

    inventory_page = InventoryPage(driver)
    assert inventory_page.get_item_count() > 0
    #TODO Lektor - hmm nice :-) co error message?
