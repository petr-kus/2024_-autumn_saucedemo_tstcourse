from common import HamburgerMenu
from common import get_element_by_id

class Cart():
    page_url = ''
    def __init__(self, driver) -> None:
        self.driver = driver
        self.hamburger_menu = HamburgerMenu(self.driver)

    def get_number_items(self):
        pass