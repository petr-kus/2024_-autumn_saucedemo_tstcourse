from Assets.page_objs import startSite, loginPage, inventoryPage, cartPage, checkoutPage
from Assets.test_data import Driver as driver

def setup():
    startSite.loadPage

def loginTest():
    loginPage.fillUserName
    loginPage.fillPassword
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