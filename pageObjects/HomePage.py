from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    shop = (By.XPATH, "//a[text()='Shop']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkme = (By.ID, "exampleCheck1")
    name = (By.CSS_SELECTOR, "input[name='name']")
    gender = (By.CSS_SELECTOR, "input[value='option2']")
    empstatus = (By.CSS_SELECTOR, "#inlineRadio1")
    databind = (By.XPATH, "(//input[@type='text'])[3]")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME, "alert-success")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def findEmail(self):
        return self.driver.find_element(*HomePage.email)

    def findPassword(self):
        return self.driver.find_element(*HomePage.password)

    def findchechMeOut(self):
        return self.driver.find_element(*HomePage.checkme)

    def findName(self):
        return self.driver.find_element(*HomePage.name)

    def findGender(self):
        return self.driver.find_element(*HomePage.gender)

    def findEmpStatus(self):
        return self.driver.find_element(*HomePage.empstatus)

    def findDatabind(self):
        return self.driver.find_element(*HomePage.databind)

    def findsubmot(self):
        return self.driver.find_element(*HomePage.submit)

    def findAlert(self):
        return self.driver.find_element(*HomePage.alert)








        #self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()