from .base import LoggedInPage
from .common import get_element_by_id

class CheckoutComplete(LoggedInPage):
    page_url = 'checkout-step-two.html'
    btn_id = 'back-to-products'

    def __init__(self, driver, screenshot_folder, logger) -> None:
        logger.info('at the checkout complete page.')
        super().__init__(driver, screenshot_folder, logger)

    def click_back(self):
        get_element_by_id(self.driver, self.btn_id, "finish button").click()