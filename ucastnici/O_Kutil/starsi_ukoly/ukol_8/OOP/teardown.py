import logging

class Teardown:
    def __init__(self, driver):
        self.driver = driver

    def close_browser(self):
        logging.info("Zavírám browser - teardown ")
        self.driver.quit()
        
