import logging
from logged_in_page import LoggedInPage

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class SummaryPage(LoggedInPage):
    def get_item_total_label(self):
        item_total_label = self.page.inner_text(".summary_subtotal_label")
        logger.info(f"Item total label is \"{item_total_label}\".")
        return item_total_label

    def go_to_final_page(self):
        self.page.click("#finish")
        logger.info("Going to final page.")
