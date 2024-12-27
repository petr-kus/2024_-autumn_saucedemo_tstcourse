import logging

from selenium.webdriver.common.by import By

from common import Base
from TestData import TestData


class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver) 
        #TODO Lektor - vidim ze se tu asi snazis vyvtorit singleton konstrukci. to je fajn a spravne reseni na problem s predavanim driveru ale asi to neni uplne.

##### VARIABLEs ---------------------------------

    tested_username = TestData.users[TestData.chosen_user]["name"]
    tested_password = TestData.users[TestData.chosen_user]["password"]

    #TODO Lektor - strceni tohoto do podtrid proc ne. Jen me prijde ze by stacilo to rozdelit spise jmenem pokud to je potreba. 
    #ale jak rikam proc ne... . SuperS
    class Fields:
        username = (By.XPATH,'//*[translate(@placeholder, "USERNAME", "username")="username"]')
        password = (By.XPATH,'//*[translate(@placeholder, "PASSWORD", "password")="password"]')
    class Buttons:
        login = (By.XPATH, '//*[translate(@value, "LOGIN", "login")="login"]')

##### KEYWORDs ----------------------------------

    def fill_in_username(self):
        self.driver.find_element(*LoginPage.Fields.username).send_keys(LoginPage.tested_username)
        logging.info(f"Filled in username: '{LoginPage.tested_username}'.")
        
    def fill_in_password(self):
        self.driver.find_element(*LoginPage.Fields.password).send_keys(LoginPage.tested_password)
        logging.info(f"Filled in password: '{LoginPage.tested_password}'.")
    
    def click_login(self):
        self.wait_and_click(LoginPage.Buttons.login)
        logging.info(f"Login button clicked.")