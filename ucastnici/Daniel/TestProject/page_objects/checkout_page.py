from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    #Checkout step one page
    CHECKOUT_STEP_ONE_URL = "/checkout-step-one.html"
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")

    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ADDRESS_FIELD = (By.ID, "postal-code")

    FIRST_NAME = "Daniel"
    LAST_NAME = "Hladík"
    ADDRESS = "Praha 6"

    #Checkout step two page
    CHECKOUT_STEP_TWO_URL = "/checkout-step-two.html"
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")

    #Checkout complete page
    CHECKOUT_COMPLETE_URL = "/checkout-complete.html"
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Opens the checkout page."""
        self.open_url(self.CHECKOUT_STEP_ONE_URL)
        self.logger.info(f"Checkout page step one was opened.")
    
    def fill_customer_details(self, first_name=None, last_name=None, address=None):
        """Fills in the customer information form."""
        try:
            first_name = first_name or self.FIRST_NAME
            last_name = last_name or self.LAST_NAME
            address = address or self.ADDRESS

            self.logger.info("Filling in customer information.")
            self.send_keys(self.FIRST_NAME_FIELD, first_name)
            self.logger.info(f"First name entered: {first_name}")
            self.send_keys(self.LAST_NAME_FIELD, last_name)
            self.logger.info(f"Last name entered: {last_name}")
            self.send_keys(self.ADDRESS_FIELD, address)
            self.logger.info(f"Address entered: {address}")
        except Exception as e:
            self.logger.error(f"Error while filling customer details: {str(e)}")
            self.take_screenshot()
            raise

    def click_continue(self):
        """Clicks the 'Continue' button to proceed to the next checkout step."""
        self.logger.info("Clicking 'Continue' button.")
        self.click(self.CONTINUE_BUTTON)
        self.logger.info("Attempted to proceed to the next checkout step.")

    def click_cancel(self):
        """Clicks the 'Cancel' button to go back to the previous page."""
        self.logger.info("Clicking 'Cancel' button to go back.")
        self.click(self.CANCEL_BUTTON)
        self.logger.info("Cancellation in checkout was attempted.")

    def finish_checkout(self):
        """Clicks the 'Finish' button to complete the checkout."""
        self.logger.info("Finishing the checkout process.")
        self.click(self.FINISH_BUTTON)
        self.logger.info("Checkout process completed.")

    def go_back_home(self):
        """Clicks the 'Back Home' button on the checkout complete page."""
        self.logger.info("Clicking 'Back Home' button.")
        self.click(self.BACK_HOME_BUTTON)
        self.logger.info("Returned to the home page.")
    