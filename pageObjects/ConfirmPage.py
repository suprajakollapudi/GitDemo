from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver


    Country = (By.ID, "country")
    PurChase = (By.LINK_TEXT, "India")
    TermsConditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    Submit = (By.CSS_SELECTOR, "input[type='submit']")
    Alert = (By.CSS_SELECTOR, ".alert-success")

    def Enter_Country(self):
        return self.driver.find_element(*ConfirmPage.Country)

    def PurChansing(self):
        return self.driver.find_element(*ConfirmPage.PurChase)

    def Terms_And_Conditions(self):
        return self.driver.find_element(*ConfirmPage.TermsConditions)

    def Confirm_Submit(self):
        return self.driver.find_element(*ConfirmPage.Submit)

    def Alert_Message(self):
        return self.driver.find_element(*ConfirmPage.Alert)