from selenium.webdriver.common.by import By
from webdriverbase import AppPage
import time

class SupportPortalPage(AppPage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigateToHappyFoxSupportPortalURL(self, url):
        self.driver.get(url)

    def enterSubject(self, text):
        self.Subject().send_keys(text)

    def enterMessage(self, text):
        self.Message().send_keys(text)

    def clickAddCC(self):
        self.AddCC().click()

    def clickAddBCC(self):
        self.AddBCC().click()

    def enterCC(self, text):
        self.CC().send_keys(text)

    def enterBCC(self, text):
        self.BCC().send_keys(text)

    def addingScreenshot(self, abc):
        self.BrowseFile().send_keys(self.getTestDataFullDirPath(abc))

    def enterFullName(self, text):
        self.sleep()
        self.FullName().send_keys(text)

    def enterEmail(self, text):
        self.sleep()
        self.Email().send_keys(text)

    def enterPhone(self, text):
        self.Phone().send_keys(text)

    def clickCreateTicket(self):
        self.CreateTicket().click()
        return AdminPortalTest2ndPage(self.driver)

    def sleep(self):
        time.sleep(1)

    def Subject(self):
        return self.driver.find_element(By.ID, "id_subject")

    def Message(self):
        return self.driver.find_element(By.XPATH, "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")

    def AddCC(self):
        return self.driver.find_element(By.ID, "add-cc")

    def AddBCC(self):
        return self.driver.find_element(By.ID, "add-bcc")

    def CC(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_cc']")

    def BCC(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_bcc']")

    def BrowseFile(self):
        return self.driver.find_element(By.XPATH, "//a[@class='hf-attach-file_link']")

    def FullName(self):
        return self.driver.find_element(By.ID, "id_name")

    def Email(self):
        return self.driver.find_element(By.ID, "id_email")

    def Phone(self):
        return self.driver.find_element(By.ID, "id_phone")

    def CreateTicket(self):
        return self.driver.find_element(By.XPATH, "//button[@id='submit']")
