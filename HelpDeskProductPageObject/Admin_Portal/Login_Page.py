from selenium.webdriver.common.by import By
from webdriverbase import AppPage

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgotPassword(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyHomePage(self):
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise RuntimeError("Not on the home page")

    def navigateToProfile(self):
        self.driver.find_element(By.ID, "profileLink").click()

class TablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")

    def retrieveRowTexts(self):
        rows = self.driver.find_elements(self.rowLocator)
        for i, row in enumerate(rows):
            rowText = row.text
            print(f"Row {i} Text: {rowText}")
