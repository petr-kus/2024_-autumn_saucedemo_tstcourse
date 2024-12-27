For both frameworks (Pytest and Robotframework) there are two test cases:
* Test Adding Items To Cart Directly And Placing Order
* Test Adding Items To Cart Via Detail Page And Placing Order

Each test case is execited three times:
* Twice using standard_user - Pests Pass
* Once using error_user - Test Fails

For tests using robotframework following needs to be installed:
* nodejs
* npm

Other prerequisities are specified in Install_prerequisities.ps1 file