import logging
from Assets.tests import setup, loginTest, addToCartTest, cartTest, checkoutTest, teardown

result = "Test completed successfully!"

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