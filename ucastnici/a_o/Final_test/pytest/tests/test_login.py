import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
@pytest.mark.parametrize("username, password, expected_title", [
    ("standard_user", "secret_sauce", "Products"),
    ("locked_out_user", "secret_sauce", "")
])
def test_login(standard_user, username, password, expected_title):
    login_page = LoginPage(standard_user)
    inventory_page = InventoryPage(standard_user)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    if expected_title:
        assert inventory_page.get_title() == expected_title, "Login failed for standard_user"
    else:
        assert "error" in standard_user.page_source, "Locked out user should not log i"