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
    # TODO Lektor... to je zajimave pouziti... cekla bych zde metody a property a ty misto toho pouzijes property ktery se naplni jako metody...
    # urcite bych to tak nedelal... mas moc zanoreni a schvoana testovaci data az prilis... . a moc souboru!
    # obecne...snazis se minimalizovat pocet souboru... a zaroven mit dost velkou obecnost... a data co k sobe patri mit na jednom miste... .
    #rozbijis tim dva posledni principy... zkratil jsi to hezky ... ale moc... . Nicmene hezky no... jen moc rozbite pres moc souboru... . ty ID patri sem!
    fillUserName = Fields.fillField("userNameField",testUser.userName)
    fillPassword = Fields.fillField("passwordField",testUser.password)
    clickLoginBtn = Btns.clickBtn("loginBtn")
    #id_pro_user_filed = (neco, neco)

    # TODO fill user name je naka akce... koukej...
    #def fillUserName(self, user):
        # ... 
        # a tady klidne muzes pouzit nake filed a btn tridy pokdu mas tu potrebu (taky ji mit nemusis)...
        # ale id bych tam plnil uz odsud...
        # fields.fillField(id_pro_user_filed, user)
    #def fillPassword(self,password):
        # ... 
        # a tady klidne muzes pouzit nake filed a btn tridy pokdu mas tu potrebu (taky ji mit nemusis)...
        # ale id bych tam plnil uz odsud...
        # fields.fillField(id_pro_password, password)

    #zde si povsimni ze zeru z vyzsi paramtericaze jmeno a heslo...  a neschovavam to az zde... jinak bych pouzil oddeleni dat podobne tobe... 
    #def Login(self, user,password):
        #self.fillUserName(user)
        #self.fillPassword(password)
        #click...


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