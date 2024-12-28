from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import pytest

#TODO Lektor - ukol jen proletim a dam par komentaru. Vetsinu jsem odpovedel/komentoval na lekci.
#TODO Lektor - Take pridavam priklad jak by to slo napsat s lektorksymi komentari, abych uzavrel tuto 7 ulohu kde by mel byt vrchol umeni 
# jak test automatizovat bez Test Frameworku, coz pro tebe plne neplati mas tu uz pytest :-), ale principy jsou podobne.
#TODO Lektor - Priklad je v 1_lektor_petr_kus/Python_OOP_POM_Lectors_example/ i s komentarema co si z toho kde odnest... . 
# A je tam pouzity pattern singleton pro predani driveru (odpoved na otazku z lekci ja to udelat dobre s predanim driveru v pyhtonu... )
    
@pytest.fixture(scope='module')
def browser():
  Option = Options()
  Option.add_argument("--disable-features=PasswordManager")
  Option.add_argument("start-maximized")
  driver = webdriver.Chrome(options=Option)
  driver.get("https://www.saucedemo.com/")
  #TODO Lektor - tohle bz chtelo nak parametrizovat z venku. 
  #predstav si ze to najednou terba budes zkouset proti nake zkusebni verzi toho webu na jine adrese...
  yield driver
  driver.quit()

class LoginPage:
  #TODO Lektor - zde by melo byt...
  #login_btn = (By.ID, 'login-button')

  def __init__(self, driver):
    self.driver = driver

  def perform_login(self, username, password):
    self.username = username
    self.password = password
    #TODO Lektor - tohle s eme vyjmecne libi, u vetsiny jsme rekl ze to ma byt v property classy 
    #ale tady je to jinak - uklada se to do instance objektu s jakym user accountem jsme zalogovani a drzi to stav.
    #to je dobre...
    self.username_field = WebDriverWait(self.driver, 5).until(
    EC.presence_of_element_located((By.ID, 'user-name'))
)
    #TODO Lektor -tohle cekani zde je zbytecne. Imlicitne se ten priklad provede az po nacteni stranky... 

    self.password_field = self.driver.find_element(By.ID, 'password')
    self.login_button = self.driver.find_element(By.ID, 'login-button')
    #TODO Lektor - tohle (By.ID, 'login-button') by uz ale v property classy byt melo. Jde o statickou vec.
    # kterou je treba menit na jednom miste a zde pak by melo byt... 
    #self.login_button = self.driver.find_element(*self.login_btn)

    try:
      #TODO Lektor - nevidim duvod proc v try neni uz i hledani elementu...
      logging.info(f"logging in as user: '{self.username}'")

      self.username_field.send_keys(self.username)
      self.password_field.send_keys(self.password)
      self.login_button.click()
      logging.info("login successfull")
      #TODO Lektor - to jehodne silne tvrzeni na to ze jsi jen klikl na prihlasit...

    except Exception as error:
      logging.error(f"error during login as user '{self.username}': '{error}'")
      raise
      #TODO Lektor - super ze se error neschovava a jeste se zaloguje a vyraisuje... .

class Navigation:
  def __init__(self, driver):
    self.driver = driver
    self.menu_button_id = 'react-burger-menu-btn'
    self.menu_items = {
       "inventory": "inventory_sidebar_link",
      "about_page": "about_sidebar_link",
       "logout": "logout_sidebar_link"
    }
    #TODO Lektor - toto z vetsiny meli byt property tridy...

  def open_menu(self):
    try:
      menu_button = WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable((By.ID, self.menu_button_id))
      )
      #TODO Lektor - tady je ten explicitini wait zbytecny...
      menu_button.click()
      logging.info(f"menu opened successfully")

    except Exception as error:
      logging.error(f"error during clicking on '{menu_button}': '{error}'")
      raise

  def open_menu_item(self, menu_item):
    if menu_item not in self.menu_items:
      logging.error(f"menu item '{menu_item}' does not exist")
      raise ValueError(f"invalid menu item: '{menu_item}'")
      #TODO Lektor - to je silne tvrzeni na to ze to vycitas ze sveho statickeho seznamu a ne dynamicky z webove stranky...
      #ale je to dobra myslenka... . ja bych si to klidne vycetl dynamicky... . a pak klikal na dany popisek...

    try:
      menu_item_id = self.menu_items[menu_item]
      menu_element = WebDriverWait(self.driver, 5).until(
        EC.element_to_be_clickable((By.ID, menu_item_id))
      )
      #TODO Lektor - tady ten explicitin wait zbytecny neni! Super
      menu_element.click()
      logging.info(f"clicked on menu item '{menu_item}'")
      
    except Exception as error:
      logging.error(f"error while clicking on menu item '{menu_item}': {error}")
      raise
    
@pytest.mark.parametrize("username, password", [
  ("problem_user", "secret_sauce"),
])
#TODO Lektor - super ze se pouziva parametrize... jen tady je to trosku jednotvarny. Zadnych vic moznosti...
def test_user_login(browser, username, password):
  login_page = LoginPage(browser)
  login_page.perform_login(username, password)
  assert "inventory.html" in browser.current_url, f"login failed for '{username}'"

@pytest.mark.parametrize("menu_item", [
  "about_page",
])

def test_menu_navigation(browser, menu_item):
  navigation = Navigation(browser)
  navigation.open_menu()
  navigation.open_menu_item(menu_item)
  assert "about.html" in browser.current_url, f"navigation to '{menu_item}' failed"
  #TODO Lektor -tady to overeni vzhledem k parametrizaci neni zrovna dynamicke... kde jsou dva prvky... :-) (jednou selze podruhe projde... pokud by melo sanci)
  #neni tam totiz implementovan ani navrat...

#TODO Lektor - celkove hezke pouziti pytestu. Chtelo by to vic ho vyuzit. A skutecne pouzit parametrize nak prakticky.
# Page Object Model by to chtelo odelit do separe souboru. A klidne udelat vic testiku. 
# prace s driverem jde prevest na ten pattern singlton tim by odpadlo par radku a zvysilo to citelnost. 
# nakonec jsem nikde neivdel vyuziti self.password self.username ktere jsem na zacatku chvalil. Klidne to mohla byt tim padem property...