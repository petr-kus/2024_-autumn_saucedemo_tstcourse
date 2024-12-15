from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

#TODO Lektor - Komentovano na lekci tak, z rychliku...
#TODO Lektor - velmi podobne Kristyne :-) is chybkama... .
#TODO Lektor - Super je ze skript jede a selhava s error_user do konzole!

Option = Options()
Option.add_argument("--disable-features=PasswordManager")
Option.add_argument("start-maximized")

driver = webdriver.Chrome(options=Option)
driver.get("https://www.saucedemo.com/")
username = driver.find_element(By.ID, 'user-name')
#TODO Lektor - ID melo byt oddeleno nekam jinam do promene treba nahoru...
username.send_keys('problem_user')
#TODO Lektor - mohl byt one liner s oddelenim do dictionary! driver.find_element(*username).send_keys(user['name'])

password = driver.find_element(By.ID, 'password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
menu_button.click()

driver.implicitly_wait(2) #TODO Lektor - krasna zmena sleepu za imlicit wait pozdeji po odevzdani :-)! Pochvala!
about_page = driver.find_element(By.ID, 'about_sidebar_link')
about_page.click()
#TODO Lektor - diky chybejejicmu assertu nevis ze te to zavedlo an spatnou stranku... proste chybejici asserty

time.sleep(5)
#TODO Lektor - to je moc na tvrdo ten sleep... mohlo to byt i nekde v prubehu testu a navrchu parametrizovany...

driver.quit()
