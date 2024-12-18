import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.basicConfig(
    filename="my_log.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    logging.info("Driver úspěšně ukončen.")
