from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pathlib
from selenium.webdriver.chrome.options import Options

FOLDER_SCREENSHOTS = pathlib.Path('screenshots')


def prepare_folder(folder_name: pathlib.Path) -> None:
    if folder_name.exists(): # clear old content
        for item in folder_name.iterdir():
            if item.is_file():
                item.unlink()
    else:
        folder_name.mkdir(parents=True)


def prepare_driver() -> webdriver:
    Option = Options()
    Option.add_argument("start-maximized")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver


def run_test(folder_path: pathlib.Path, driver: webdriver) -> None:
    
    driver.get("https://www.saucedemo.com/")
    driver.save_screenshot(folder_path / pathlib.Path('login_page.png'))
    username = driver.find_element(By.ID,'user-name')
    username.send_keys('standard_user') 
    password = driver.find_element(By.ID,'password')
    password.send_keys('secret_sauce')
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    # time.sleep(5)
    driver.save_screenshot(folder_path / pathlib.Path('inventory_page.png'))
    hamburger_btn = driver.find_element(By.ID,'react-burger-menu-btn')
    hamburger_btn.click()
    time.sleep(2) # waiting for animation
    driver.save_screenshot(folder_path / pathlib.Path('hamburger_clicked.png'))
    logout_link = driver.find_element(By.ID,'logout_sidebar_link')
    logout_link.click()
    driver.save_screenshot(folder_path / pathlib.Path('logout.png'))


if __name__ == "__main__":
    driver = prepare_driver()
    prepare_folder(FOLDER_SCREENSHOTS)
    run_test(FOLDER_SCREENSHOTS, driver)
    driver.close()

