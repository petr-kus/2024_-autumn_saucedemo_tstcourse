from Assets.page_objs import startSite, loginPage, inventoryPage, cartPage, checkoutPage
from Assets.test_data import Driver as driver

def setup():
    startSite.loadPage

def loginTest():
    loginPage.fillUserName
    loginPage.fillPassword
    #TODO - Lektor: krasne POM/OOP! pokud ale ty data zapadly takto moc... pak pouzit fillValidUserName a nebo to zde pouzit jako parametr... cely test muze byt parametrizovan... user, password, valid...
    #moc jsi veci rozbil a moc je schoval. Chces obecnost ale zaroven mit vse na jednom miste co to jde... ty jsi moc zafocusoval to deleni... az moc.
    #coz vede celkove i k tomu ze kdyz test selze neni uplne jasne kde a co se stalo... z logu jsou jasne akce ale ne stranky napriklad... .
    #errorovy vystup do comannd liny ti taky moc nepomuze... .
    #a vlasten s emi tezko dohledavaji logy a chyb9 tam asi timestamp.
    loginPage.clickLoginBtn

def addToCartTest():
    inventoryPage.addItemsToCart

def cartTest():
    cartPage.enterCart
    cartPage.checkNumAddedItems

def checkoutTest():
    checkoutPage.startCheckout
    checkoutPage.fillFirstName   
    checkoutPage.fillSecondName
    checkoutPage.fillZip
    checkoutPage.clickConfirmBtn
    checkoutPage.clickFinishBtn
    
def teardown():
    driver.close()
    driver.quit()