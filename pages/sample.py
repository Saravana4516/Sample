import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from steps import conftest

conftest.init_driver()

driver = webdriver.Chrome('drivers/chromedriver')
driver.get("http://rahulshettyacademy.com")
driver.title()
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, "email").send_keys()
driver.find_element(By.CSS_SELECTOR, ".Password").send_keys()
driver.find_element()
driver.current_url()
driver.refresh()
driver.forward()
driver.back()
driver.minimize_window()
