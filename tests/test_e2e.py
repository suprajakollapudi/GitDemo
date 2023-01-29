import time
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

class TestFramework(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("Getting Items")
        products = checkOutPage.Product_Items()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            #productName = product.checkOutPage.Product_Item().text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button[@class='btn btn-info']").click()
                self.driver.execute_script("window.scrollTo(0, 0)")
                break
        checkOutPage.CheckOut_AddtoCart().click()
        confirmPage = checkOutPage.CheckOut_FinalCheckout()
        confirmPage.Enter_Country().send_keys("India")
        self.verifyLinkedTextPresence("India")
        confirmPage.PurChansing().click()
        confirmPage.Terms_And_Conditions().click()
        confirmPage.Confirm_Submit().click()
        time.sleep(5)
        alertMessage = confirmPage.Alert_Message().text
        log.info(alertMessage)
        assert "Success! Thank you!1" in alertMessage
        log.info("Execution completed successfully")
        print("For Git Demo")
