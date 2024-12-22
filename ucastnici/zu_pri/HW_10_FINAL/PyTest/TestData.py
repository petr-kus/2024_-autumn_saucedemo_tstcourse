from selenium import webdriver

class TestData():
    
    urls = {
        "landing_page"   : "https://www.saucedemo.com/",
        "login_page"     : "https://www.saucedemo.com/",
        "inventory_page" : "https://www.saucedemo.com/inventory.html",
        "cart"           : "https://www.saucedemo.com/cart.html",
        "about"          : "https://saucelabs.com/",
        "checkout"       : "https://www.saucedemo.com/checkout-step-one.html"
    }
    
    # Pro účel testování testu:
    #"landing_page" : "http://httpstat.us/500"
    
    browsers = {
        "Chrome"  : webdriver.Chrome,
        "Firefox" : webdriver.Firefox,
        "Edge"    : webdriver.Edge,
        }
    
    ##### CHOOSE A BROWSER ---------------------------------
    chosen_webdriver = "Chrome"
    #-------------------------------------------------------

    users = {
        "standard_user"  : {
            "name"       : "standard_user",
            "password"   : "secret_sauce"
        },
        "locked_out_user": {
            "name"       : "locked_out_user",
            "password"   : "secret_sauce"
        },
        "problem_user"   : {
            "name"       : "problem_user",
            "password"   : "secret_sauce"
        },
        "performance_glitch_user": {
            "name"       : "performance_glitch_user",
            "password"   : "secret_sauce"
        },
        "error_user"     : {
            "name"       : "error_user",
            "password"   : "secret_sauce"
        },
        "visual_user"    : {
            "name"       : "visual_user",
            "password"   : "secret_sauce"
        }
        }

    ##### CHOOSE A USER ------------------------------------
    chosen_user = "standard_user"
    #-------------------------------------------------------

    inventory_items = {
        1: "Backpack", 
        2: "Bike Light",
        3: "Bolt T-Shirt",
        4: "Fleece Jacket",
        5: "Onesie",
        6: "T-Shirt (Red)",
        }
    
    ##### CHOOSE A TEST ITEM ---------------------------------
    chosen_item = 6
    #---------------------------------------------------------