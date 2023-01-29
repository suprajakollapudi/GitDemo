from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    Items = (By.XPATH, "//div[@class='card h-100']")
    Item = (By.XPATH, "div/h4/a")
    CheckOut = (By.PARTIAL_LINK_TEXT, "Checkout")
    FinalCheckOut = (By.XPATH, "//button[@class='btn btn-success']")


    def Product_Items(self):
        return self.driver.find_elements(*CheckOutPage.Items)

    def Product_Item(self):
        return self.driver.find_elements(*CheckOutPage.Item)

    def CheckOut_AddtoCart(self):
        return self.driver.find_element(*CheckOutPage.CheckOut)

    def CheckOut_FinalCheckout(self):
        self.driver.find_element(*CheckOutPage.FinalCheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage