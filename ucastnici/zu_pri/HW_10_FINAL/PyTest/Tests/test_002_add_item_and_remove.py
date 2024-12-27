import logging
import pytest
import traceback

from selenium.common.exceptions import TimeoutException

try:
    @pytest.mark.usefixtures("login_standard")
    def test_add_item_from_inventory_page_and_empty_cart(base, inventory_page, cart):
        base.log_start()
        
        inventory_page.add_chosen_item_to_cart()
        cart.check_if_chosen_item_is_in_cart()
        cart.click_checkout()
        cart.make_empty()
        cart.check_number_of_items()

except TimeoutException as timeout_error:
    logging.error(timeout_error)
    full_terminal_error = traceback.format_exc()
    logging.error(full_terminal_error)
    assert False

except Exception as error:
    logging.error(f"Fatal ERROR: '{error}'")
    full_terminal_error = traceback.format_exc()
    logging.error(full_terminal_error)
    assert False

finally:
    print("...Test finished")