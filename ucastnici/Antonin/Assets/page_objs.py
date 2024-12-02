from Assets.test_data import testData
from Assets.page_nav import Fields, Btns, OtherEls
from Assets.test_data import Driver as driver

class User:
    def __init__(self, userName, password, firstName, secondName, zip):
        self.userName = userName
        self.password = password
        self.firstName = firstName
        self.secondName = secondName
        self.zip = zip
        
testUser = User(testData.user.userName, testData.user.password, testData.user.firstName, testData.user.lastName, testData.user.zip)

numItemsToOrder = testData.numItemsToOrder

class startSite():
    loadPage = driver.get(testData.testPage)

class loginPage():
    fillUserName = Fields.fillField("userNameField",testUser.userName)
    fillPassword = Fields.fillField("passwordField",testUser.password)
    clickLoginBtn = Btns.clickBtn("loginBtn")

class inventoryPage():
    addItemsToCart = Btns.AtCFun(numItemsToOrder)

class cartPage():
    enterCart = Btns.clickBtn("cartBtn")
    checkNumAddedItems = OtherEls.countItemsInCart(numItemsToOrder)
    
class checkoutPage():
    startCheckout = Btns.clickBtn("firstCheckoutBtn")
    fillFirstName = Fields.fillField("firstNameField",testUser.firstName)
    fillSecondName = Fields.fillField("lastNameField",testUser.secondName)
    fillZip = Fields.fillField("zipField",testUser.zip)
    clickConfirmBtn = Btns.clickBtn("secondCheckoutBtn")
    clickFinishBtn = Btns.clickBtn("lastCheckoutBtn")