import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#TODO Lektor - super z eje pouzity conf tests

logging.basicConfig(
    filename="my_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

#TODO Lektor - super ze je zde configurovany logging a s time stampam!
#mohla jsi si tam nastavit zobrazeni jen INFO at ten log pro logovani nemas tak plny a necitelny... 
# na debug si to pakprepnes jen kdyz potrebujes...

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    logging.info("Driver úspěšně ukončen.")

#TODO Lektor - super ze je zde driver a ze je to fixtures a ze je pouzti yield.
#TODO Lektor - jen by bylo fajn zde provolat ten singlton pattern a tim si zajistit ze bude pouzit vsude bez predavani si ho.
#TODO Lektor - a pouzit scope=session nbeo scope-module + autorun=True aby jsi si ho nemusela predavat... .
