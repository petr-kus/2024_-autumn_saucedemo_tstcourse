from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    SEARCH_PAGE_URL = "/index.html"
    
    SEARCH_QUERY = "product name"
    SEARCH_PAGE_RESULT_URL = f"/search.html?id={SEARCH_QUERY}"
    
    SEARCH_FIELD = (By.ID, "search-field")
    SEARCH_BUTTON = (By.ID, "search-button")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Opens the search page."""
        self.open_url(self.SEARCH_PAGE_URL)
        self.logger.info(f"Product search page was opened.")