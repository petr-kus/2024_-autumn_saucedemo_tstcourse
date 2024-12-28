from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pytest

#standartni python logging
import logging

#LOAD PAGE OBJECTS
from PageObjects.LoginPage import LoginPage
from PageObjects.Menu import Menu
from PageObjects.Browser import Browser
# TODO Lektor - Browser zde neni pouzity... snazime se minimalizovat importy... kadzy import zere cas a pamet, takze pokud import neni potreba odebira se... .

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni 
# jak test automatizovat bez Test Frameworku, coz pro tebe plne neplati mas tu uz pytest :-), ale principy jsou podobne.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . 
# A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre s predanim driveru v pyhtonu... )

def slowdown():
    sleep_time = 0.5
    if sleep_time > 0:
        logging.debug(f"slowdown and sleep {sleep_time}s to be visible during test development")
        time.sleep(sleep_time)

#OLD FIXTURES
"""
@pytest.fixture
def webpage():
    return "https://www.saucedemo.com/"

@pytest.fixture
def credentials():
    return {"password"   : "secret_sauce", "login_name" : "standart_user"}
"""

# Used constrution wit global variable and autouse=True 
# Why? -  I don't have to pass it now as fixture/object to each test...
# TODO Lektor - yes good, solution but still jsut in this module (fixtures need to be define in same file as tests). 
# TODO Lektor - Better would be use singlton pattern and import browser - see example from lector. 

@pytest.fixture(autouse=True, scope="session")
def Browser():
    global browser
    logging.debug(f"Starting browser chrome...")
    browser = webdriver.Chrome()
    logging.info(f"Browser started")
    yield browser
    logging.debug(f"Ending browser chrome...")
    browser.close()
    browser.quit()
    logging.info(f"Browser closed")
    # TODO Lektor - dobre deleni logovani info/debug :-)

@pytest.fixture()
def login_page():
    login_page = "https://www.saucedemo.com/"
    # TODO Lektor - to by chtelo parametrizovat tu stranku externe te fixture. 
    # Predstav si ze, by nkede byla testovaci instance a melo by se to prehodit... . 
    logging.debug(f"Going to login page '{login_page}'")
    browser.get(login_page)
    logging.info(f"Login page '{login_page}' loaded already.")
    yield
    current_page = browser.current_url
    try:
        logging.debug(f"Going make user logoff via page menu from page '{current_page}'")
        menu = Menu(browser)
        menu.logout()
        logging.info(f"Logoff from '{current_page}' already done.")
    except:
        logging.warn(f"The page '{current_page}' was not logged in!")
    # TODO Lektor - libi se mi tebto automaticky logout, je to krasne premysleni a vyuziti fixtures.

# TODO Lektor - fixtures mohli bt definovany v nakem jinem spuboru treba v conftest.py kde s nimi defaultne pocita pytest... a nebo uplne jinde a importnout.

class TestWebPage:

    test_page = "https://www.saucedemo.com/"
    # TODO Lektor - znovu tu parametrizujes test page coz je spravne ale do driveru si to nepredavas... .
    test_page_inventory = "https://www.saucedemo.com/inventory.html"
    # TODO Lektor -tady se dalo vyuzit slouceni adress... at se to nemusi pak prepisovat rucne...
    login_error_box = (By.XPATH,"//h3[@data-test='error']")

    # TODO Lektor - libi se mi docela rozumne oddeleni tetsovacich dat... .

    @pytest.mark.parametrize("loginame, password", 
                            [("standard_user", "secret_sauce"), 
                            ("problem_user", "secret_sauce"), 
                            ("performance_glitch_user", "secret_sauce"), 
                            ("error_user", "secret_sauce"), 
                            ("visual_user", "secret_sauce")])
    def test_Successful_Login_and_Logout(self, loginame, password):
        """ This is testing successful login and logout to the page"""

        loginPage = LoginPage(browser)
        menu = Menu(browser)

        #DIFFERENT SOLUTION - possible add drver also to Page Object Model
        #browser = Browser(driver)
        #browser.go_to_page(test_page)
        # TODO Lektor - jo jo... to by bylo fajn a kdyz uvnitr toho browseru to vytvoris jako singlton pattern (mrkni na priklad)
        # tak by jsi byl presne v tom lektroskem reseni... a mohl by jsi kompletne vynechat jak tyto radky co tam mas ted i ty navrhovane... 
        # stacil by ti import nahore. 

        browser.get(self.test_page)
        slowdown()
        # TODO Lektor - pochvala za extrakci slowdownu aspon takto :-) ve finalnim odevzdani bych to klidne odebral.
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" in browser.current_url
        slowdown()
        menu.logout()
        assert self.test_page == browser.current_url
        browser.get(self.test_page_inventory)
        assert self.test_page == browser.current_url
        assert browser.find_element(*self.login_error_box)

        #TODO: passing also for performance glitch user - shoudl not - have to be added verifictaion for performance
        # TODO Lektor -  ano ano, celkove... krasne vyuziti parametrizace! (premyslim jestli jsi to dokonce nekde nezkopiroval z minuleho kurzu odemne :-) )

    @pytest.mark.parametrize("loginame, password", [("locked_out_user", "secret_sauce")])
    def test_Unsuccessful_Login(self, loginame, password):
        """ This is testing unsuccessful login to the page"""

        loginPage = LoginPage(browser)
        browser.get(self.test_page)
        slowdown()
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" not in browser.current_url
        assert browser.find_element(*self.login_error_box)

     # TODO Lektor jo jo najednou se to rychle pise. Krasa... . Jen bych to pojmenoval mozna nak. invalid login, locked user... protoze to je obsah co se testuje.

    #Approach with usage fixture nad yield for teardown (logout) # TODO Lektor - pecka! co vic dodat... . Krasne vyuziti sily pytestu!
    @pytest.mark.parametrize("loginame, password", 
                            [("standard_user", "secret_sauce"), 
                            ("problem_user", "secret_sauce"), 
                            ("performance_glitch_user", "secret_sauce"), 
                            ("error_user", "secret_sauce"), 
                            ("visual_user", "secret_sauce")])
    def test_Successful_Login(self, login_page, loginame, password):
        """ This is testing successful login to the page"""
        loginPage = LoginPage(browser)
        slowdown()
        loginPage.login(loginame, password)
        slowdown()
        assert "inventory" in browser.current_url

# TODO Lektor - celkove dobre, skoda ze testujes jen login. Na kterem jsme si to vse vlastne ukazovali. 
# Lepsi by bylo zkusit neco jineho jeste.
#take tu nikde neviidm zadne nastavovani logingu a treba timstapmu a mista vystupniho souboru, zadne scrennshoty a tak. Coz by bylo fajn pouzit.
#celkove to logovani je slabsi... jinak struktury a zpusoby testu jsou fajn.