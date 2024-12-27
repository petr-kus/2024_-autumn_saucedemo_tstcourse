*** Settings ***
Library                      Browser

*** Variables ***
${ADD_BACKPACK_TO_CART} =    xpath=//div[@class='inventory_container']//div[@class='inventory_item_description' and contains(., 'Backpack')]//button[contains(translate(text(),'A','a'),'add to cart')]


*** Keywords ***
Add Backpack to cart
    Click                    ${ADD_BACKPACK_TO_CART}