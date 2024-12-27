# Lector's note: This code follows the Page Object Model (POM) pattern, where elements, actions, and other common functionalities 
# related to a page or module (like the menu) are encapsulated within separate classes and/or files for better organization and decressing maintatance needs.
from page_object.menu import menu
from page_object.inventory_page import inventory_page
from page_object.login_page import login_page
import random
# Lector's note: The `tstkit` module contains shared testing functions and utilities that are not specific to the test subject. This helps keep the test code clean and readable.
import tstkit 
from tstkit import browser

# Lector's note: Important test data, such as URLs and credentials, are declared here or in a separate configuration file for easy parameterization in tests.
# Lector's note: Non-relevant details like UI IDs are hidden behind the Page Object Model (POM), making the tests more readable and easier to maintain.
test_page = "https://www.saucedemo.com/"

username = "standard_user"
password = "secret_sauce"
validity = "valid"

def login_test(username,password,validity):
    # Lector's TIP: Parameterizing the test enhances reusability across various test scenarios, offering greater flexibility and reducing code duplication.
    # TIP: While designing test parameterization, consider the knowledge and expectations of the end user for input data. This user-centric approach improves abstraction from a technical perspective.
    # TIP: Technical details of parameterization should be abstracted and encapsulated within the POM to maintain clean and readable test code.
    try: #Lector's note: TRY / EXCEPT block used to handle any errors that may occur during the test. 
         #This structure can be improved by creating custom decorators for cleaner test code, similar to how pytest handles test functions.
        browser.get(test_page)
        login_page.fill_user(username)
        login_page.fill_password(password)
        login_page.click_login()
        inventory_page.is_loaded()
    except Exception as exception:
        #Lector's note: Log the exception for better vidibility and error tracing!
        tstkit.exception(exception)

def logout_test():
    try:
        menu.open()
        menu.logingout()
        login_page.is_loaded()
    except Exception as exception:
        tstkit.exception(exception)

def test_scanario_standart_customer(username,password,validity):
        login_test(username,password,validity)
        first_page_items = inventory_page.get_all_showed_items_names()
        random_item = random.choice(first_page_items)
        inventory_page.add_item_to_cart(random_item)
        # Lector's TIP: Use full descriptive variable and method names with 'snake_case' convention for clarity.
        # Lector's TIP: The test steps are broken into multiple lines (variables first_page_items, random_item) for better readability and to clearly reflect the flow of actions.
        # Lector's TIP: Tests should be self-explanatory and readable without requiring extra documentation or technical knowledge.
        # Lector's note: This readability is achieved through descriptive naming, modular steps, POM, OOP, and a clear logical flow—not dependent on specific tools or frameworks (it is style of thinking).

        # Principle: The main tests or test scenarios should be written in a way that is clear and readable, 
        # making it obvious what is being tested and how, even without technical knowledge.
        # Lector's note: This approach is not just for non-technical roles (a common misconception) 
        # but also to facilitate quick debugging and human understanding, even for those with strong programming skills.
        # Reminder: Writing a test usually takes less time than reading and maintaining it later. Tests are more time readed than written!

        logout_test()

# Running the tests in sequence
login_test(username,password,validity)
logout_test()
test_scanario_standart_customer(username,password,validity)

# Lector's note: This structure makes it easy to add new tests or reuse existing ones in different scenarios.