import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

@pytest.fixture(scope='function')
def browser():
 options = Options()
 options.add_argument("--disable-features=PasswordManager")
 options.add_argument("start-maximized")
 driver = webdriver.Chrome(options=options)
 driver.get("https://www.saucedemo.com/")
 yield driver
 driver.quit()

 #TODO Lektor - zvetsenim scopu fixture by slo docilit aby se predaval mezi testy a nemsuel se otvirat furt dokola
 #TODO Lektor - to je klicove pro rychlost testu, ktera je dulezity parametr.
 #TODO Lektor - take by se dal vyuzit Singlton Pattern aby se nemusel vsude ten browser importovat jako parametr funkce zaroven s autouse parametrem pytestu

def pytest_configure():
 logging.basicConfig(
 filename='my_log_pytest.log',
  level=logging.DEBUG,
   #TODO Lektor - tady by pro normalni provoz bylo lepsi nastavit info. aby logy byli ctielnejsi.
   #TODO Lektor - pripadne nekde v readme lepe popsat jak dane vysledky ukazat v allure...
   #TODO Lektor - proste na citelnosti a srozumitelnosti logovani by to zde chtelo zapracovat i co se tyka logovych message. 
   #TODO Lektor - Minule tu byly obrazky a ted tu nejsou skoda... .
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
 )