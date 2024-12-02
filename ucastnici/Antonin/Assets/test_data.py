#Test data
from selenium import webdriver

class testData():
    testPage = "https://www.saucedemo.com/"
    numItemsToOrder = 1
    class user():
        userName = "standard_user"
        password = "secret_sauce"
        firstName = "Joe"
        lastName = "Doe"
        zip = "111"
    
Driver = webdriver.Chrome()
    
