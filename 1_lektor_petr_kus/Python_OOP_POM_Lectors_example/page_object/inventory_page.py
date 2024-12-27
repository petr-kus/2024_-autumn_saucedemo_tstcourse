import tstkit
import logging
from tstkit import browser 
from selenium.webdriver.common.by import By

class inventory_page:
      class_items_names = 'inventory_item_name'
      class_price = 'pricebar'
      class_items = 'inventory_item'
      descripton_add_cart_button = 'Add to cart'
      items = (By.CLASS_NAME, class_items_names)
      password_filed = (By.ID,'password')
      username_filed = (By.ID,'user-name')
      page='inventory.html'

      def is_loaded():
        tstkit.page_is_loaded(inventory_page.page)
      
      def get_all_showed_items_names():
         # Lector's Note: This method retrieves all the item names that are visible to the user.
         # Lector's TIP: The principle here is that we work with the same names/texts that the user sees, making the test closer to the user experience.
         logging.info(f"Inventory_Page - These items are showed :")
         items = browser.find_elements(*inventory_page.items)
         items_names = []
         for item in items:
             items_names.append(item.text)
             logging.info(f"Inventory_Page - Item name: '{item.text}'")
         logging.info(f"Inventory_Page - Items are returned for next use.")
         # Lector's TIP: Always include the source page (e.g., 'Inventory_Page') from the POM in the log message for enhanced traceability and easier debugging.
         # TIP: If logging patterns like this are used frequently, consider creating a dedicated logging utility or function in tstkit to centralize and standardize these messages.
         # TIP: Follow the principle: "When you press Ctrl+C, think!"—repeated or copied code is often a sign that you should abstract it into a reusable function, method, or class for improved maintainability and scalability.
         return items_names
      
      def add_item_to_cart(name):
         logging.info(f"Inventory_Page - Try to add item '{name}' to cart")
         # Lector's Note: This approach simplifies the code by using a relative XPath.
         # We locate the "Add to cart" button by identifying the product name (which is visible to the user!) and the button's description (which is visible to the user!).
         relative_xpath_to_button = f"//div[contains(@class,'{inventory_page.class_items_names}') and text()='{name}']/ancestor::div[contains(@class,'{inventory_page.class_items}')]/div[@class='{inventory_page.class_price}']/button[text()='{inventory_page.descripton_add_cart_button}']"
         logging.info(f"Inventory_Page - cliking to button add for xpath: '{relative_xpath_to_button}'")
         # Lector's TIP: This XPath directly verifies the text of the "Add to cart" button, ensuring we are interacting with the correct button for the specified item.
         # Lector's TIP: If you have trouble defining a relative XPathlike this, you can use the browser's Developer Tools (F12) to inspect the HTML structure. 
         # In the console, you can test XPath expressions directly with the $x() function. Additionally, AI tools can help you generate accurate XPath by analyzing the HTML snippet you provide.
         browser.find_element(By.XPATH, relative_xpath_to_button).click()
         logging.info(f"Inventory_Page - Item '{name}' should be added to cart.")