from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):

    SEARCH_PAGE_URL = "index.html"
    
    SEARCH_FIELD = (By.ID, "search-field")
    SEARCH_BUTTON = (By.ID, "search-button")

    SEARCH_QUERY = "product name"
    SEARCH_PAGE_RESULT_URL = f"search.html?id={SEARCH_QUERY}"

    SEARCH_RESULTS = (By.CLASS_NAME, "search-result-item")
    NO_RESULTS_MESSAGE = (By.ID, "no-results-message")

    def __init__(self, driver):
        super().__init__(driver)
    
    def open(self):
        """Opens the search page."""
        self.open_url(self.SEARCH_PAGE_URL)
        self.logger.info(f"Product search page was opened.")
    
    def enter_search_query(self, query=SEARCH_QUERY):
        """Enters a query into the search input field."""
        self.logger.info(f"Entering search query: {query}")
        self.send_keys(self.SEARCH_FIELD, query)
    
    def click_search_button(self):
        """Clicks the search button to execute the search."""
        self.logger.info("Clicking the search button.")
        self.click(self.SEARCH_BUTTON)
    
    def search_for(self, query):
        """Performs a complete search operation."""
        self.logger.info(f"Searching for: {query}")
        self.enter_search_query(query)
        self.click_search_button()
    
    def get_search_results(self):
        """Retrieves the list of search results."""
        self.logger.info("Getting search results.")
        results = self.find_elements(self.SEARCH_RESULTS)
        return [result.text for result in results]

    def is_no_results_message_displayed(self):
        """Checks if the 'no results' message is displayed."""
        self.logger.info("Checking if 'No Results' message is displayed.")
        return self.is_element_visible(self.NO_RESULTS_MESSAGE)