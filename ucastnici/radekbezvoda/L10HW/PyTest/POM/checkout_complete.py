from .base import LoggedInPage

class CheckoutComplete(LoggedInPage):
    page_url = 'checkout-step-two.html'
    btn_id = 'back-to-products'

    def __init__(self, driver, screenshot_folder, logger) -> None:
        logger.info('at the checkout complete page.')
        super().__init__(driver, screenshot_folder, logger)

    def click_back(self):
        self.get_elements_by('ID', self.btn_id, "finish button").click()
