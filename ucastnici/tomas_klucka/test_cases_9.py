import pytest
from POM.login_page import LoginPage  
from POM.navigation_page import NavigationPage 

# test case for login
@pytest.mark.parametrize("username, password", [
 ("standard_user", "secret_sauce"),
 ("problem_user", "secret_sauce"),
 ("error_user", "secret_sauce"),
])

def test_user_login(browser, username, password):
 login_page = LoginPage(browser)
 login_page.perform_login(username, password)
 assert "inventory.html" in browser.current_url, f"login failed for '{username}'"

# test case for login and about page
@pytest.mark.parametrize("username, password", [
 ("standard_user", "secret_sauce"),
 ("problem_user", "secret_sauce"),
 ("error_user", "secret_sauce"),
])

def test_login_and_about_page(browser, username, password):
 login_page = LoginPage(browser)
 login_page.perform_login(username, password)
 assert "inventory.html" in browser.current_url, f"login failed for '{username}'"

 navigation = NavigationPage(browser)
 navigation.open_menu()
 navigation.open_about_page()
 assert "404 Not Found" not in browser.page_source, "navigation to about page failed"

# test case for login and logout
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
])
def test_user_login_logout(browser, username, password):
    login_page = LoginPage(browser)
    login_page.perform_login(username, password)
    assert "inventory.html" in browser.current_url, f"Login failed for '{username}'"
  
    navigation = NavigationPage(browser)
    navigation.open_menu()
    navigation.perform_logout()
    assert "saucedemo.com" in browser.current_url, "logout failed"
