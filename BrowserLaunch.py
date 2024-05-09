from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver_path = 'drivers/chromedriver'
chrome_options = Options()

driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Open a website
driver.get('https://www.flipkart.com/')  # Replace with the URL you want to visit
driver.maximize_window()

# Close the browser when done
driver.quit()



