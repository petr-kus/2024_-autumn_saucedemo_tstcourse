
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tstkit import browser

class menu():
    all_items = (By.XPATH, "//a[text()='All Items']")
    about = (By.XPATH,"//a[text()='About']")
    logout = (By.XPATH,"//a[text()='Logout']")
    reset_app = (By.XPATH,"//a[text()='Reset App State']")
    cross_close = (By.ID,'react-burger-cross-btn')
    open_button = (By.ID,'react-burger-menu-btn')

    # Lector's Note: The object itself is used, rather than an instance. This approach avoids transferring any live context for testing, simplifying test writing.
    # Lector's Note: By using the class directly, we save one line in test code initialization, making tests more readable.
    # Lector's Note: If a live context of the object is needed for testing (e.g., instance-specific data), it's better to use an instance approach!

    def open():
        logging.info('menu - Opening burger menu')
        # Lector's TIP: The '*' operator unpacks the tuple (By.ID, 'react-burger-menu-btn') into separate arguments for the find_element method.
        # This approach allows us to combine the locator strategy (By.ID) with the value ('react-burger-menu-btn') in a more readable and flexible way.
        browser.find_element(*menu.open_button).click()
        # Wait for the menu to open
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(menu.cross_close))
        # Lector's Note: This open method demonstrates the first approach to access the class directly (menu is referenced everywhere).
        # This approach is simple, but renaming the class requires changing all references.

    @classmethod
    def logingout(cls):
        logging.info('menu - Logging out user')
        browser.find_element(*cls.logout).click()
        # Lector's TIP: This logingout method demonstrates the second approach to access the class directly.
        # Using 'cls' allows the class to be referenced generically, making it easier to rename the class without breaking the code.