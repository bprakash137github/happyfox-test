from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import os
import platform
import time

class AppPage:
    PATH_TO_TEST_DATA_FILE = "src/main/resources/"
    WINDOWS_PATH_TO_TEST_DATA_DIR = "src/main/resources/"
    WAIT_TIME_SEC = 60

    def __init__(self, driver):
        self.driver = driver
        self.javaScriptExecutor = None
        self.waitImplicitly()
        self.maximizeWindow()

    def getDriver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def getCurrentUrl(self):
        return self.driver.current_url

    def maximizeWindow(self):
        self.driver.maximize_window()

    def waitImplicitly(self, timeOutInSeconds=WAIT_TIME_SEC):
        self.driver.implicitly_wait(timeOutInSeconds)

    def clearAndType(self, element, text):
        element.clear()
        element.send_keys(text)

    def switchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def switchToFrame(self, frame):
        self.driver.switch_to.frame(frame)

    def hoverOverElementUsingJS(self, element):
        js = """
            var evObj = document.createEvent('MouseEvents');
            evObj.initEvent('mouseover', true, false);
            arguments[0].dispatchEvent(evObj);
        """
        self.getJavaScriptExecutor().execute_script(js, element)

    def getJavaScriptExecutor(self):
        if self.javaScriptExecutor is None:
            self.javaScriptExecutor = self.driver
        return self.javaScriptExecutor

    def scrolltoElement(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
            self.scrolltoElement(element)
        except Exception as ex:
            pass

    def scrolltoElement(self, element):
        self.getJavaScriptExecutor().execute_script("arguments[0].scrollIntoView(false)", element)
        time.sleep(1)

    def waitForVisible(self, element):
        wait = WebDriverWait(self.driver, self.WAIT_TIME_SEC)
        wait.until(EC.element_to_be_clickable(element))

    def getCurrentWorkingDirectory(self):
        return os.getcwd()

    def getTestDataFullDirPath(self, fileName):
        path = self.PATH_TO_TEST_DATA_FILE
        if self.getOperatingSystemType() == 'Windows':
            path = self.WINDOWS_PATH_TO_TEST_DATA_DIR
        return os.path.join(self.getCurrentWorkingDirectory(), path, fileName)

    def getOperatingSystemType(self):
        return platform.system()
