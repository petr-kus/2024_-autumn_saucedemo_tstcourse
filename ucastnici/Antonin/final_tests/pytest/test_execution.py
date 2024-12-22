from selenium import webdriver
import pytest, logging, random
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True, scope="session")
def setup():
    global driver
    logging.debug("Starting driver")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("login, password", [("standard_user", "secret_sauce")])
def test_loginTest(login, password):
    driver.get("https://www.saucedemo.com/")
    login_page.fillUserName(login)
    login_page.fillPassword(password)
    login_page.clickLoginBtn()

def test_addToCartTest():
    inventory_page.add_random_items_to_cart(6)

@pytest.mark.parametrize("name, last_name, zip", [("Joe", "Doe", "111")])
def test_checkoutTest(name, last_name, zip):
    checkout_page.startCheckout()
    checkout_page.fillFirstName(name)  
    checkout_page.fillSecondName(last_name)
    checkout_page.fillZip(zip)
    checkout_page.clickConfirmBtn()
    checkout_page.clickFinishBtn()

#############################----------POM----------#############################

class login_page():
    userNameField = (By.ID, "user-name")
    passwordField = (By.ID, "password")
    loginBtn = (By.ID, "login-button")

    def fillUserName(user_name):
        fillField(login_page.userNameField, user_name)
    def fillPassword(user_password):
        fillField(login_page.passwordField, user_password)
    def clickLoginBtn():
        clickBtn(login_page.loginBtn)
        assert "inventory.html" in driver.current_url, logging.error(f"Logging in failed.")

class inventory_page():
    cartBadge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_random_items_to_cart(amount):
        AtCFun(amount)
        cart_badge = driver.find_element(*inventory_page.cartBadge)
        assert int(cart_badge.text) == amount, logging.error(f"There were {inventory_page.cartBadge} items added to the cart during this test. Expected amount was {amount}")
    
class checkout_page():
    cartBtn = (By.ID, "shopping_cart_container")
    firstCheckoutBtn = (By.ID, "checkout")
    secondCheckoutBtn = (By.ID, "continue")
    lastCheckoutBtn = (By.ID, "finish")
    firstNameField = (By.ID, "first-name")
    lastNameField = (By.ID, "last-name")
    zipField = (By.ID, "postal-code")
    checkoutComplete =  (By.XPATH, "//*[contains(., 'Thank you')]")
    
    def startCheckout():
        if "cart.html" not in driver.current_url:   
            clickBtn(checkout_page.cartBtn)
            clickBtn(checkout_page.firstCheckoutBtn)
        else:
            clickBtn(checkout_page.firstCheckoutBtn)
    def fillFirstName(first_name):
        fillField(checkout_page.firstNameField,first_name)
    def fillSecondName(last_name):
        fillField(checkout_page.lastNameField,last_name)
    def fillZip(zip):
        fillField(checkout_page.zipField,zip)
    def clickConfirmBtn():
        clickBtn(checkout_page.secondCheckoutBtn)
    def clickFinishBtn():
        clickBtn(checkout_page.lastCheckoutBtn)
        assert "checkout-complete.html" in driver.current_url, logging.error(f"Checkout failed.")



#############################----------FUNCTIONS----------#############################

def fillField(fillTarget, value):
    try:
        driver.find_element(*fillTarget).send_keys(value)
    except Exception as err:
        logging.error(f"Field '{fillTarget}' was NOT found. {err}")

def clickBtn(clickTarget):
    try:
        driver.find_element(*clickTarget).click()
    except Exception as err:
        logging.error(f"Button '{clickTarget}' was NOT found.{err}")

def AtCFun(numItemsToOrder):
    numAddedItems = 0 #Keeps track of products added during the test
    for x in range(numItemsToOrder): 
        AtCs=driver.find_elements(By.CLASS_NAME, "btn_primary")
        randomAtC = AtCs[random.randrange(0,len(AtCs)-1)] if len(AtCs) > 1 else AtCs[0] 
        try:
            randomAtC.click()
        except Exception as err:
            logging.error(f"Error occured while adding{randomAtC}: {err}!")
        numAddedItems += 1
    assert numAddedItems == numItemsToOrder, logging.error(f"There were {numAddedItems} items added to the cart during this test. Expected amount was {numItemsToOrder}")