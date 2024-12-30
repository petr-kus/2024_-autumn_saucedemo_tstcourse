import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    #TODO Lektor - neustale prepouzivas zalogovani uzivatele. Mohla to byt parametricka fixture... nebo tak neco.
    assert "inventory.html" in driver.current_url
    #TODO Lektor - error message...

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("invalid_user", "invalid_password")
    assert "Epic sadface" in login_page.get_error_message()
    #TODO Lektor - error message...
