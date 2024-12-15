from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utilities.logger import get_logger

def get_driver(browser="chrome"):
    """Initializes WebDriver for the given browser."""
    logger = get_logger("WebDriver")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
        logger.info(f"Driver was set to Chrome.")
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        logger.info(f"Driver was set to Firefox.")
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)
        logger.info(f"Driver was set to Edge.")
    else:
        logger.error(f"Driver for selected test browser '{browser}' is not supported. Supported browsers: Chrome, Firefox, Edge.")
        raise ValueError(f"Unsupported test browser: '{browser}'")
        

    driver.implicitly_wait(10)
    return driver