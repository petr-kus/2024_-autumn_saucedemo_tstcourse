import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class CheckoutPage(LoggedInPage):
    def fill_in_form(self, first_name, last_name, postal_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)
        logger.info(f"Filling in order form - first name: \"{first_name}\", last name: \"{last_name}\", postal code: \"{postal_code}\".")

    def go_to_summary_page(self):
        self.page.click("#continue")
        logger.info("Going to summary page.")