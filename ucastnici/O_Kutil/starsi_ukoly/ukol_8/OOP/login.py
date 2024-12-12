from selenium.webdriver.common.by import By
import logging

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def perform_login(self, username, password):
        logging.info("Přihlašování uživatele")
        self.driver.find_element(*self.username_field).send_keys(username)
        logging.debug("Zadal uživatelské jméno")
        self.driver.find_element(*self.password_field).send_keys(password)
        logging.debug("Zadal heslo")
        self.driver.find_element(*self.login_button).click()
        logging.debug("Kliknul na tlačítko login")
