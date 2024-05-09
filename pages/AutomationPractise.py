import time
from datetime import date
import sys
import os

import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

sys.path.append(os.path.dirname("C:/Users/nagap/PycharmProjects/pythonProject/utility"))
from utility import GlobalVariables

class AutomationPractise:

    Shopxpath = "//a[text()='Shop']"

    def __init__(self,driver):
        self.driver = driver

    def HomemenuCLick(self):
        self.driver.find_element(by=By.XPATH, value = self.Shopxpath).click()
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(), name="HomemenuCLick",attachment_type=AttachmentType.PNG)
