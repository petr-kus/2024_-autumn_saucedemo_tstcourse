import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
Lector's Note: 
Logging is essential for tracking application behavior. The log level is set to INFO for general practicality. 
During debugging, switch the log level to DEBUG to capture more detailed information. 
Including a timestamp in your logs is crucial for debugging. 
It helps to track the exact timing of events, making it easier to pinpoint issues and understand the sequence of actions.

Principle behind:
The logging of the test should be detailed enough that you can identify the issue without having to rerun the test. 
You can automatically attach screenshots, application logs, and other relevant information to help diagnose the problem quickly and efficiently.
'''

logging.basicConfig(filename='test_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Logging is set!')

def slowdown(seconds=2):
        time.sleep(seconds)

class Browser():
        driver = None
        #Lector's Note: The Singleton pattern is implemented here using __init__ (it can also be implemented using __new__).
        #Lector's Note: Only a single instance of the object (browser/driver) is used throughout.
        #Lector's Note: A key feature of this implementation is that the Browser class is accessed directly, rather than through an instance.

        def __init__(self): 
            if Browser.driver is None:
                # Initialize the browser only once
                option = Options()
                option.add_argument("start-maximized")
                Browser.driver = webdriver.Chrome(options=option)
                Browser.driver.implicitly_wait(2)
                logging.debug("Starting browser chrome...")

        def __del__(self):
            self.driver.quit()
            logging.debug(f"Closing browser.")

browser_instance = Browser()
# Lector's Note: This instance will be imported into all tests.
# Lector's Note: If anyone creates a new instance, they will receive the same browser instance!

browser = browser_instance.driver
# Lector's Note: The correct import statement to access the browser instance is:
# 'from tstkit import browser'

def exception():
      logging.info('Test Case Failed!')
      logging.error('ERROR:')
      logging.error(exception)
      logging.info('Test continue to next test case!')

def page_is_loaded(page):
       assert page in browser.current_url, "The current url doesn't contain '{page}'"
       logging.info(f"Current url is '{browser.current_url}' and contains '{page}'")
       # Lector's TIP: The single quotes ('') around the variable values 
       # in the log help easily identify if the variable is empty.