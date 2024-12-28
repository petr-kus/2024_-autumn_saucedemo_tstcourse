import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import logging

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni 
# jak test automatizovat bez Test Frameworku, coz pro tebe plne neplati mas tu uz pytest :-), ale principy jsou podobne.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . 
# A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre s predanim driveru v pyhtonu... )

@pytest.mark.parametrize("filter_value", ["az", "za", "lohi", "hilo"])
def test_inventory_filters(driver, filter_value):
    #TODO Lektor - skoda ze test je napsan dohromady s evsim is prihlasenim a tak dale.
    # dela hot o vyrazne mene prepouzitelnym a automatizace jakehokoli dalsiho testu se stava komplikovanejsi
    # prvni co bych udelal je rozseakni na mensi pod testy (tets zalogovani uzivatele, atd..)
    """Test filtrování produktů."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    #TODO Lektor - tohle se dalo prave obejti tim kdby v tom driveru/fixture byl pouzity singlton patern (viz priklad lektora)

    login_page.open()
    #TODO Lektor - tady by se hodilo rict jakoustranku ma otevrit ze?
    login_page.login("problem_user", "secret_sauce")

    product_names_before = inventory_page.get_product_names()
    inventory_page.apply_filter(filter_value)
    product_names_after = inventory_page.get_product_names()

    if filter_value == "az":
        assert product_names_after == sorted(product_names_before), f"Filtr {filter_value} selhal!"
        #TODO Lektor - nebal bych se tu nekde zalogovat cele to pole... .
    elif filter_value == "za":
        assert product_names_after == sorted(product_names_before, reverse=True), f"Filtr {filter_value} selhal!"
    elif filter_value == "lohi" or filter_value == "hilo":
        assert product_names_before != product_names_after, f"Filtr {filter_value} selhal!"
    #TODO Lektor - ps co kdyby tam bylo vic produktunez na jednu stranku?
    logging.info(f"Test pro filtr '{filter_value}' proběhl úspěšně.")
