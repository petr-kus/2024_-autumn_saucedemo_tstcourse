import logging
import inspect

from common import Base
from TestData import TestData
from PageObjects.Cart import Cart
from PageObjects.Header import Header
from PageObjects.InventoryPage import InventoryPage
from PageObjects.LoginPage import LoginPage

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol jak tets automatizovat bez Test Frameworku.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... .

class Tests(Base):
    def __init__(self, driver):
        super().__init__(driver) #TODO Lektor - toto moc nechapu. V kazdem pade to zavani z ejsi chtela delat pattern singleton ale nedodelala.
        #TODO Lektor - pattern singloton jde pomoci init udelat treba tak jak jsem ho napsal ja v prikladu. Resi to prave ten dotaz z lekce, jak si predat driver a nemuset psat jeho predani.
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart = Cart(self.driver)
        self.header = Header(self.driver)
        #TODO Lektor - celkove je to prestrukturovany. Tahle trida by mozna nemusela byt trida. (nevidim v tom specificky ucel)
        #TODO Lektor - ukladat do selfu instance jinych objektu je zbytecne moc slozity pristup. Ale chapu z ejsi musela vytvorit jejich instance nekde.
        #V tvem reseni bych to tvoril az v tom danem testu vyhla by jsi se opkaovani self... a mohla si to vhodne pojmenovat. Sice zbytecne radek na vic... ale aspon neco z toho.
        # ale pak by jsi bez globalu mela provlem s predanim driveru. Hm. No mrkni na priklad. Bude to jasnejsi snad.. .
    
    def log_start(self):
        test_name = inspect.currentframe().f_back.f_code.co_name
        logging.info(f"Starting test: {test_name}")
        
        #TODO Lektor - toto je moc hezke ze jsi na to logovani myslela jak to zalogovat! K tomu slouzi prave frameworky aby jsi to nemusela delat.
        #lepsi by pro teto ucel bylo v pythonu pouzit asi dekoratory! Ale je fajn ze jsi si nasla cestu!

##### TESTs ----------------------------------

    def login_test(self):
        """
        #TODO Lektor - moc hezke ze je to nachystane na komentare ale neco by zde mohlo byt
        """
        self.log_start()
        self.login_page.fill_in_username()  #TODO Lektor - zde bych rad videl co se teda vyplnuje za udaje... . Uz je zde prilisne oddeleni dat a testu samotneho.
        self.login_page.fill_in_password()
        self.login_page.click_login()
        #TODO Lektor - hezky napsany assert libi s emi ze je hlavne logika presunuta do POMka inventory_page!
        assert self.inventory_page.is_loaded(), "Login failed or not redirected to Inventory page."

    def add_item_from_inventory_page_to_buy_test(self):
        """
        WIP, would continue checkout, but for now it removes all items
        """
        self.log_start()
        self.inventory_page.add_chosen_item_to_cart()
        self.cart.check_if_chosen_item_is_in_cart()
        self.cart.click_checkout()
        self.cart.make_empty()
        self.cart.check_number_of_items()
    
    def add_random_number_of_items_and_than_remove_all_test(self):
        """
        """
        self.log_start()
        self.inventory_page.add_random_number_of_items_to_cart()
        self.cart.check_number_of_items()
        self.cart.make_empty()
        items_in_cart = self.cart.check_number_of_items()
        if items_in_cart == 0:
            logging.info(f"Test successfull - number of items in cart is '{items_in_cart}'.")
        else:
            logging.error(f"Test FAILED - number of items in cart is '{items_in_cart}'.")
    
    def add_random_number_of_items_and_count_them_in_cart_test(self):
        """
        """
        self.log_start()
        number_of_random_items_added = self.inventory_page.add_random_number_of_items_to_cart()
        items_in_cart = self.cart.check_number_of_items()
        if  items_in_cart == number_of_random_items_added:
            logging.info(f"Number of items in cart ('{items_in_cart}') does equal number of items chosen for adding ('{number_of_random_items_added}').")
        else:
            logging.error(f"Check for number of items in cart being the same as number of items added FAILED: Expected '{number_of_random_items_added}' items in the cart, but found '{items_in_cart}'.")
        
    def logout_test(self):
        self.log_start()
        self.header.logout()

    def burger_menu_open_close_test(self):
        """
        """
        self.log_start()
        self.header.burger_menu.open()
        self.header.burger_menu.close()
        self.header.burger_menu.check_if_closed()
    
    def burger_menu_links_test(self):
        """
        """
        self.log_start()
        self.cart.go_to()
        self.header.burger_menu.open()
        self.header.go_to_inventory_page_by_link_in_menu()
        self.header.go_to_inventory_page_by_link_in_menu()
        self.header.go_to_about_page_by_link_in_menu()
        self.inventory_page.go_to()
        logging.info(f"Redirected back to '{TestData.urls["inventory_page"]}'.")