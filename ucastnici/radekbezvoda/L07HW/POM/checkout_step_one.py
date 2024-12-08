from .base import LoggedInPage

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
        self.get_elements_by('ID',self.btn_id, "continue button").click()
    
    def fill_out_personal_data(self, personal_data):
        self.get_elements_by('ID', self.first_name_id, 'first name').send_keys(personal_data.first_name)
        self.get_elements_by('ID', self.last_name_id, 'last name').send_keys(personal_data.last_name)
        self.get_elements_by('ID', self.postal_code_id, 'postal-code').send_keys(personal_data.postal_code)
    

        
