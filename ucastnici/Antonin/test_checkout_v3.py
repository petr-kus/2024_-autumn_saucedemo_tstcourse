import logging
from Assets.tests import setup, loginTest, addToCartTest, cartTest, checkoutTest, teardown

result = "Test completed successfully!"
#TODO - Lektor: vetsinu jsme komentovali na lekci. Takze moje komentare nemusi / nebudou uplne.
#TODO - Lektor: nebal bych se uz na teto urovni tu mit nakou hlavni parametrizaci... jako treba jaka webova stranka se testuje.
#TODO - Lektor: ty testovaci data uplne zmizeli na vsech urovnich. To neni dobre. Je fajn pouzite POM ale testovaci data cloveka zajimaji, jako heslo jmeno, ktery web... .

#Test execution

try:
    setup()

    loginTest()

    addToCartTest()

    cartTest()

    checkoutTest()

except Exception as err:
    result = f"Test failed!"

finally:
    teardown()
    
    logging.warning(f"Test finsihed. Result: {result}")