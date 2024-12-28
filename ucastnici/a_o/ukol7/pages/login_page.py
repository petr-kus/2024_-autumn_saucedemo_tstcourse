from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        #TODO Lektor - toto mohlo byt definovano jako property tridy 
        # a nebo jde o testovaci data co by spis meli byt parametrizovane... .

    def open(self):
        self.driver.get(self.url)
        logging.info(f"Stránka otevřena: {self.url}")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        ).send_keys(username)
        #TODO Lektor - rekl bych ze tu chybi *pred self a take... ze je to ceknai zbytecne... 
        # dalsi prikaz se totiz implicitne spusti az po nacteni stranky...
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        logging.info(f"Pokus o přihlášení uživatelem: {username}")
        #TODO Lektor - je fajn ze messsage nerika nic co neni pravda :-). 
        # Nejlepsi by bylo zalogovat si na zacatku i na konci te metody... 
