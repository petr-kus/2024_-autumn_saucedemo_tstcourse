from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging

def get_element_by_id(driver, id, str_name):
    try:
        element=driver.find_element(By.ID, id)
        return element
    except NoSuchElementException:
        logging.error(f'{str_name} element not found')
        raise


def get_elements_by_xpath(driver, xpath_str, str_name):
    try:
        elements=driver.find_elements(By.XPATH, xpath_str)
        return elements
    
    except NoSuchElementException:
        logging.error(f'{str_name} element not found')
        raise


def get_element_by_css_selector(driver, css_selector, str_name, logger):
    try:
        element=driver.find_element(By.CSS_SELECTOR, css_selector)
        return element
    
    except NoSuchElementException:
        logger.error(f'{str_name} element not found by CSS selector')
        raise


def get_element_by_class_name(driver, class_name, logger):
    try:
        element=driver.find_element(By.CLASS_NAME, class_name)
        return element
    
    except NoSuchElementException:
        logger.error(f'{str_name} element not found by class name.')
        raise

def click_on_element(driver, elements, element_index):
    if element_index < len(elements):
        elements[element_index].click()
    else:
        logging.error(f"No element found at index {element_index}. Total elements found: {len(elements)}")



