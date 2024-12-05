import logging
import traceback

from selenium.common.exceptions import TimeoutException

from common import Base
from tests import Tests as Tests

########################  LOG setup --------------------------------------------------

logging.basicConfig(filename="./HW_07/test_logs.log", 
                    level=logging.DEBUG, 
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Starting the execution:")

########################  SETUP -------------------------------------------------------
#TODO: ukazat priklad jak si predat driver bez toho abych musel pouzivat jeden objekt
def test_run():
    base_page = Base()
    driver = base_page.driver

    if base_page.check_landing_page_loaded():
        try:
            tests = Tests(driver)

########################  TESTs -------------------------------------------------------
            
            tests.login_test()          
            tests.add_random_number_of_items_and_than_remove_all_test()
            tests.add_item_from_inventory_page_to_buy_test()
            tests.add_random_number_of_items_and_count_them_in_cart_test()
            tests.burger_menu_open_close_test()
            tests.burger_menu_links_test()
            tests.logout_test()

########################  debugging ---------------------------------------------------

            # tests.header.go_to_cart_by_clicking_cart_icon()

########################  Exceptions handling & teardown ------------------------------
    	
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
            print("...Testing finished")
            base_page.teardown()

test_run()