from selenium.webdriver.common.by import By
import random, logging
from Assets.test_data import Driver as driver


logging.basicConfig(
    filename="myLogFile.log",
    level=logging.INFO,
    filemode="w",  # Přepisuje soubor při každém spuštění
    format="%(asctime)s - %(levelname)s - %(message)s")

class Fields():
    userNameField = (By.ID, "user-name")
    passwordField = (By.ID, "password")
    firstNameField = (By.ID, "first-name")
    lastNameField = (By.ID, "last-name")
    zipField = (By.ID, "postal-code")

    def fillField(fieldAttr, value):
        try:
            fillTarget = getattr(Fields, fieldAttr, None)
            driver.find_element(*fillTarget).send_keys(value)
            logging.info(f"Filling the {fieldAttr} with '{value}'.")
        except Exception as err:
            logging.error(f"Field '{fieldAttr}' was NOT found. {err}")


class Btns():
    loginBtn = (By.ID, "login-button")
    addToCartBtn = (By.CLASS_NAME, "btn_primary")
    cartBtn = (By.ID, "shopping_cart_container")
    firstCheckoutBtn = (By.ID, "checkout")
    secondCheckoutBtn = (By.ID, "continue")
    lastCheckoutBtn = (By.ID, "finish")

    def clickBtn(BtnAttr):
        try:
            clickTarget = getattr(Btns, BtnAttr, None)
            driver.find_element(*clickTarget).click()
        except Exception as err:
            logging.error(f"Button '{BtnAttr}' was NOT found.{err}")

    def AtCFun(numItemsToOrder):
        numAddedItems = 0 #Keeps track of products added during the test
        for x in range(numItemsToOrder): 
            AtCs=driver.find_elements(*Btns.addToCartBtn)
            randomAtC = AtCs[random.randrange(0,len(AtCs)-1)] if len(AtCs) > 1 else AtCs[0] 
            try:
                randomAtC.click()
            except Exception as err:
                logging.error(f"Error occured while adding{randomAtC}: {err}!")
            numAddedItems += 1
            logging.info(f"{randomAtC} was added to the cart!")
        assert numAddedItems == numItemsToOrder, logging.error(f"There were {numAddedItems} items added to the cart during this test. Expected amount was {numItemsToOrder}")
        

class OtherEls():
    itemsInCartAmount =  (By.CLASS_NAME, "cart_quantity")
    checkoutComplete =  (By.XPATH, "//*[contains(., 'Thank you')]")

    def countItemsInCart(numItemsToOrder):
        cartItems = driver.find_elements(*OtherEls.itemsInCartAmount)
        cartAmount = 0
        for item in cartItems: #Checks for the amount of items currently in the cart
            itemAmount = int(item.get_attribute("innerText"))
            cartAmount += itemAmount
        assert cartAmount == numItemsToOrder, logging.error(f"There were {cartAmount} in cart. Expected amount was {numItemsToOrder}.")