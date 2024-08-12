from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriverbase import AppPage
import time

class AdminPortalTest1stPage(AppPage):
    def __init__(self, driver):
        super().__init__(driver)

    def clickStatus(self):
        self.hoverOverElementUsingJS(self.Title())
        self.Title().click()
        self.Statuses().click()

    def clickPriorities(self):
        self.sleep()
        self.hoverOverElementUsingJS(self.Title())
        self.Title().click()
        self.hoverOverElementUsingJS(self.Priorities())
        self.Priorities().click()

    def clickNewStatus(self):
        self.NewStatus().click()

    def enterStatusName(self, text):
        self.StatusName().send_keys(text)

    def clickStatusColourInner(self):
        self.StatusColourInner().click()

    def enterStatusColour(self, text):
        self.clickStatusColourInner()
        self.StatusColour().clear()
        self.StatusColour().send_keys(text)
        self.clickStatusColourInner()

    def enterBehavior(self, text):
        self.Behavior().click()
        self.Behavior().send_keys(text)
        self.Behavior().send_keys(Keys.ENTER)

    def enterStatusDescription(self, text):
        self.StatusDescription().clear()
        self.StatusDescription().send_keys(text)

    def clickAddStatus(self):
        self.AddStatus().click()

    def clickStatusesSection(self):
        self.scrolltoElement(self.StatusesSection())
        self.StatusesSection().click()

    def setDefaultStatus(self, xpath):
        status_xpath = f"//div[contains(text(),'{xpath}')]//following::td[3]"
        abc = self.driver.find_element(By.XPATH, status_xpath)
        self.hoverOverElementUsingJS(abc)
        abc.click()

    def clickPrioritySection(self):
        self.PrioritySection().click()

    def clickNewPriority(self):
        self.NewPriority().click()

    def enterPriorityName(self, text):
        self.PriorityName().clear()
        self.PriorityName().send_keys(text)

    def enterPriorityDescription(self, text):
        self.PriorityDescription().clear()
        self.PriorityDescription().send_keys(text)

    def enterPriorityHelpText(self, text):
        self.PriorityHelpText().clear()
        self.PriorityHelpText().send_keys(text)

    def clickAddPriority(self):
        self.AddPriority().click()

    def setDefaultPriority(self, xpath):
        priority_xpath = f"//span[contains(text(),'{xpath}')]//following::td[3]"
        pqr = self.driver.find_element(By.XPATH, priority_xpath)
        self.hoverOverElementUsingJS(pqr)
        pqr.click()
        self.sleep()
        self.sleep()

    def ClickAddedPriority(self, xpath):
        self.sleep()
        priority_xpath = f"//span[contains(text(),'{xpath}')]"
        self.scrolltoElement(priority_xpath)
        self.driver.find_element(By.XPATH, priority_xpath).click()

    def clickPriorityDeleteLink(self):
        self.scrolltoElement(self.PriorityDeleteLink())
        self.PriorityDeleteLink().click()

    def setNewDefaultPriority(self):
        self.hoverOverElementUsingJS(self.NewDefaultPriority())
        self.NewDefaultPriority().click()
        self.ChoosingNewDefaultPriority().click()
        self.ChoosingNewDefaultPriority().send_keys("Low")
        self.ChoosingNewDefaultPriority().send_keys(Keys.ENTER)

    def clickDeleteConfirm(self):
        self.DeleteConfirm().click()
        time.sleep(5)

    def ClickAddedStatus(self, xpath):
        self.sleep()
        status_xpath = f"//div[contains(text(),'{xpath}')]"
        self.scrolltoElement(status_xpath)
        self.driver.find_element(By.XPATH, status_xpath).click()

    def clickStatusDeleteLink(self):
        self.scrolltoElement(self.StatusDeleteLink())
        self.StatusDeleteLink().click()

    def setNewDefaultStatus(self):
        self.hoverOverElementUsingJS(self.NewDefaultStatus())
        self.NewDefaultStatus().click()
        self.NewDefaultStatus().send_keys(Keys.DOWN)
        self.NewDefaultStatus().send_keys(Keys.ENTER)

    def switchToFrames(self):
        self.switchToFrame(self.ToFrames())

    def switchToDefaultPage(self):
        self.switchToDefaultContent()

    def clickProfile(self):
        self.sleep()
        self.waitForVisible(self.Profile())
        self.Profile().click()

    def clickLogout(self):
        self.Logout().click()

    def sleep(self):
        time.sleep(2)

    def Title(self):
        return self.driver.find_element(By.XPATH, "//span[@class='hf-top-bar_title_text hf-font-light']")

    def Statuses(self):
        return self.driver.find_element(By.LINK_TEXT, "Statuses")

    def Priorities(self):
        return self.driver.find_element(By.LINK_TEXT, "Priorities")

    def NewStatus(self):
        return self.driver.find_element(By.XPATH, "//button[@class='hf-mod-create']")

    def StatusName(self):
        return self.driver.find_element(By.XPATH, "//input[@aria-label='Status Name']")

    def StatusColourInner(self):
        return self.driver.find_element(By.XPATH, "//div[@class='sp-preview-inner']")

    def StatusColour(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter any valid color code format.']")

    def Behavior(self):
        return self.driver.find_element(By.XPATH, "//div[@aria-label='Behavior']")

    def StatusDescription(self):
        return self.driver.find_element(By.XPATH, "//textarea[@aria-label='Description']")

    def AddStatus(self):
        return self.driver.find_element(By.XPATH, "//button[@data-test-id='add-status']")

    def StatusesSection(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='manage-statuses-left-nav']")

    def NewDefaultPriority(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Choose Priority')]")

    def ChoosingNewDefaultPriority(self):
        return self.driver.find_element(By.XPATH, "//input[contains(@class,'ember-power-select-search-input')]")

    def PriorityDeleteLink(self):
        return self.driver.find_element(By.XPATH, "//a[@data-test-id='priority-delete-trigger']")

    def NewDefaultStatus(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Choose Status')]")

    def ToFrames(self):
        return self.driver.find_element(By.XPATH, "//iframe[@id='hfc-frame']")

    def Profile(self):
        return self.driver.find_element(By.XPATH, "//div[@class='hf-avatar-image-container ember-view']//img[@class='hf-avatar-image hf-avatar-image_show']")

    def Logout(self):
        return self.driver
