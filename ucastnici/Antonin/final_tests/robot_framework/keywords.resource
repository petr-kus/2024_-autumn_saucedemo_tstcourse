*** Settings ***
Library   Browser
Library      custom_library.py

*** Keywords ***
Populate field ${id} with ${text}
    Type Text    input#${id}    ${text}
Add random item to Cart
    @{items}=    Get Elements    .inventory_item >> ../.. >> "Add to cart"
    ${randomAtC}=    Random Item Generator    ${items}
    Scroll To Element    ${randomAtC}
    Highlight Elements   ${randomAtC}    duration=200ms
    Take Screenshot
    Click    ${randomAtC}
    Get Text     span.shopping_cart_badge  ==  1
Enter the Cart
    Click        a.shopping_cart_link
    Get Url      contains  cart
Confirm Checkout
    Get Text     h2    contains    Thank you
Login ${output} 
    Run Keyword If    '${output}'=='positive'     Get Url      contains  inventory
    ...    ELSE IF    '${output}'=='negative'     Get Text     h3    contains    Epic sadface