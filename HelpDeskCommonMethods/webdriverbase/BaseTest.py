import os
import atexit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class BaseTest:
    def __init__(self):
        self.driver = None

    def beforeSuite(self):
        chrome_driver_path = "C:\\Users\\test\\Desktop\\D drive\\automation\\Chrome driver\\chromedriver.exe"
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximize window on start
        service = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
    def afterSuite(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

    def getDriver(self):
        return self.driver

# Instantiate BaseTest and set up driver before suite
base_test = BaseTest()
base_test.beforeSuite()

# Ensure driver is closed and quit after suite
atexit.register(base_test.afterSuite)

# Usage example:
# driver = base_test.getDriver()
# driver.get("https://www.example.com")
