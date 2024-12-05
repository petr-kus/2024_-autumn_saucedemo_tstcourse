from collections import namedtuple
import random
import string
import pathlib

MAIN_PAGE_URL = 'https://www.saucedemo.com/'
FOLDER_SCREENSHOTS = pathlib.Path('screenshots')
FOLDER_HAPPY_SCREENSHOTS = FOLDER_SCREENSHOTS / pathlib.Path('happy-test')
FOLDER_UNHAPPY_SCREENSHOTS = FOLDER_SCREENSHOTS / pathlib.Path('unhappy-test')
FOLDER_RANDOM_SCREENSHOTS = FOLDER_SCREENSHOTS / pathlib.Path('random-login-test')
FOLDER_CART_SCREENSHOTS = FOLDER_SCREENSHOTS / pathlib.Path('cart-checkout-test')
SCREENSHOT_FOLDERS = [FOLDER_HAPPY_SCREENSHOTS, FOLDER_UNHAPPY_SCREENSHOTS, FOLDER_RANDOM_SCREENSHOTS, FOLDER_CART_SCREENSHOTS]
LOG_FILE_NAME = 'test.log'


Credentials = namedtuple('Credentials', ['username', 'password'])

standard_user = Credentials(username='standard_user', password='secret_sauce')
bad_password = Credentials(username='error_user', password='sauce')


PersonalData = namedtuple('PersonalData', ['first_name', 'last_name', 'postal_code'])
personal_data = PersonalData(first_name='Jan', last_name='Novák', postal_code='15687')


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string


def generate_random_credentials():
    return Credentials(username=generate_random_string(random.randint(1,15)), password=generate_random_string(random.randint(1,15)))
