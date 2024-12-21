import os
from datetime import datetime
import logging

class Screenshot:
    def __init__(self, driver):
        self.driver = driver
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    def take_screenshot(self, name, status=""):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/{name}_{status}_{timestamp}.png"
        self.driver.save_screenshot(screenshot_path)
        logging.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path
