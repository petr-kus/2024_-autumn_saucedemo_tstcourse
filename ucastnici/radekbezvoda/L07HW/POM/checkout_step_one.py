from .base import LoggedInPage
from .common import get_element_by_id

class CheckoutStepOne(LoggedInPage):
    page_url = 'checkout-step-one.html'
    first_name_id = 'first-name'
    last_name_id = 'last-name'
    postal_code_id = 'postal-code'
    btn_id = 'continue'

    def __init__(self, driver, screenshot_folder, logger) -> None:
        logger.info('at the checkout first page.')
        super().__init__(driver, screenshot_folder, logger)

    def click_checkout(self):
        get_element_by_id(self.driver, self.btn_id, "continue button").click()
    
    def fill_out_personal_data(self, personal_data):
        get_element_by_id(self.driver, self.first_name_id, 'first name').send_keys(personal_data.first_name)
        get_element_by_id(self.driver, self.last_name_id, 'last name').send_keys(personal_data.last_name)
        get_element_by_id(self.driver, self.postal_code_id, 'postal-code').send_keys(personal_data.postal_code)
    

        
