from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#TODO Lektor - toto je tepotrebny import. Snazime se ty nepotrebne tam nemit. Protoze load importu zbytecne zdrzuje skript!
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.options import Options

#TODO Lektor - komentovano na lekci takze jen prolitnu a okomentuji co tam vidim... .
#TODO Lektor - nemusi / nebude to uplny seznam

#TODO Lektor - libi se mi pouziti OOP a ale mohl jsi pouzit rovnou POM a nemit to pojmenovane jako test ale mit nekolik trid podle toho na jakou stranku pristupujes.
class Test:
  #TODO Lektor - staticke prvky a jejich misto mohlo byt zde... 
  #password_field = (By.ID,'password')
  # ...

  def __init__(self):
    Option = Options()
    Option.add_argument("start-maximized")
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.saucedemo.com/")
    #TODO Lektor - tady mohla byt ta stranka oparamatrizovana a mohla se zrat v initu jako parametr... .

  #TODO Lektor - typova kontrola je nice... .
  def test_login(self, user:str, password_user:str):
    username = self.driver.find_element(By.ID,'user-name')
    username.send_keys(user) 
    #TODO Lektor - toto mohl byt one liner... .
    #TODO Lektor - self.driver.find_element(By.ID,'user-name').send_keys(user) 

    password = self.driver.find_element(By.ID,'password')
    password.send_keys(password_user)
    #ID mohli byt nekm oddelene... mrkni nahoru... By.ID,'password'... aspon jako parametry objektu... pouziti pak... self.password_field

    login_button = self.driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert self.driver.current_url == "https://www.saucedemo.com/inventory.html", "Špatná URL"
    time.sleep(3)
    #TODO Lektor - staticky sleep fakt ne je to anitpattern... mel byt nahore celkove nak parametrizovan

  def test_cart(self):
    # Kliknutí na ikonu košíku (vpravo nahoře)
    cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
    time.sleep(3)

  def test_burger_menu(self):
    # Kliknutí na burger menu
    burger_menu = self.driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(3)

  def test_logout(self):
    # Kliknutí na Logout v burger menu
    logout = self.driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()
    time.sleep(3)

  def close_driver(self):
    self.driver.close()

#TODO Lektor - mohlo tady byt vic assertu.

test = Test()

test.test_login("standard_user", "secret_sauce")
test.test_cart()
test.test_burger_menu()
#TODO Lektor - tadz by ti v metodach chybel implicit wait ... pokud by jsi odebral ty staticke waity... .
test.test_logout()
test.test_login("problem_user", "secret_sauce")
test.test_burger_menu()
test.test_logout()
test.close_driver()

#TODO strasne opakovani test. - je to wwaste znaku :-) mohlo mit vyznam treba pouzitim POM. Viz výše... .
#TODO použití oop je to heyke ale nepouzil jsi vubec property objektu coz je skoda... .