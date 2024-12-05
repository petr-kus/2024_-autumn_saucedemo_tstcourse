from common import HamburgerMenu

class Checkout():
    page_url = ''
    def __init__(self, driver) -> None:
        self.driver = driver
        self.hamburger_menu = HamburgerMenu(self.driver)