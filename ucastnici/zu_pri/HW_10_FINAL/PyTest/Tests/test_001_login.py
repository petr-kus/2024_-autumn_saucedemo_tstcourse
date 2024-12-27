import logging
import pytest
import traceback

from selenium.common.exceptions import TimeoutException
from ..TestData import TestData

try:
    @pytest.mark.parametrize("username, password", [
    (TestData.users["standard_user"]["name"], TestData.users["standard_user"]["password"]),
    (TestData.users["locked_out_user"]["name"], TestData.users["locked_out_user"]["password"]),
    ])
    def test_login(driver, base, login_page, inventory_page, username, password):
        base.log_start()
        
        driver.get(TestData.urls["landing_page"])
        logging.info(f"Going to '{TestData.urls['landing_page']}'")
        
        login_page.fill_in_username(username)
        login_page.fill_in_password(password)
        login_page.click_login()
        assert inventory_page.is_loaded(), f"Login failed or not redirected to Inventory page. Login failed for user: {username}"


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