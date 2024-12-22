import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class FinalPage(LoggedInPage):
    def get_message(self):
        final_message = self.page.inner_text(".complete-header")
        logger.info(f"Final message is \"{final_message}\".")
        return final_message

    def go_back_home(self):
        self.page.click("#back-to-products")
        logger.info("Going back to inventory page.")