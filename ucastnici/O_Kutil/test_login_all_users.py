import pytest
from OOP.setup import Setup
from OOP.login import Login
from OOP.screenshot import Screenshot
from OOP.timer import Timer

@pytest.mark.usefixtures("driver")
class TestLogin(Setup):
    @pytest.mark.parametrize("username", [
        "standard_user",
        "locked_out_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user"
    ])
    def test_login_all_users(self, driver, username):
        driver.get("https://www.saucedemo.com")
        
        login_page = Login(driver)
        screenshot = Screenshot(driver)
        timer = Timer()
        
        timer.start()
        login_page.perform_login(username, "secret_sauce")
        timer.stop()
        
        screenshot.take_screenshot(f"login_{username}")
        
        inventory = driver.find_element("id", "inventory_container")
        assert inventory.is_displayed(), f"Login failed for user: {username}"
        timer.verify_duration(3)  # Fail if login takes more than 3 seconds
