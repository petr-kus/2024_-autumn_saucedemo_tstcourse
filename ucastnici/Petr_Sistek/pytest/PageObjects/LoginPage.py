from selenium.webdriver.common.by import By

class LoginPage:
    password_field = (By.ID,'password')
    login_name_field = (By.ID,'user-name')
    login_button = (By.ID,'login-button')

    def __init__(self,driver):
        self.driver = driver
        # TODO Lektor - toho bych se zbavil singlton patternem a importem browseru...
        
    def login(self,name,password):
        self.driver.find_element(*self.login_name_field).send_keys(name)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        # TODO Lektor - tady bych urcite udelal naky logovani. V kazde metode se to hodi! Na zacatek a na konec!

# TODO Lektor - jinak krasa...

