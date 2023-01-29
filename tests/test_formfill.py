import time

import pytest
# Edge Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


"""
class TestFormFill(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.findEmail().send_keys(getData[0])  # Using Name
        homePage.findPassword().send_keys(getData[1])  # Using ID
        homePage.findchechMeOut().click()
        homePage.findName().send_keys(getData[2])  # using CSS
        homePage.findGender().click()
        homePage.findEmpStatus().click()
        homePage.findDatabind().send_keys(getData[3])
        homePage.findsubmot().click()  # using xpath
        alert_text = homePage.findAlert().text  # using classname
        print(alert_text)
        assert "Success" in alert_text
        homePage.findDatabind().clear()
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=[("supraja@gmail.com", "welcome_123", "Hello", "Hello again"), ("Tanu@gmail.com", "welcome_123", "Smile", "Hello Smile")])
    def getData(self, request):
        return request.param
"""

"""
#parametized data
class TestFormFill(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        homePage.findEmail().send_keys(getData["EmailID"])  # Using Name
        homePage.findPassword().send_keys(getData["Pwd"])  # Using ID
        homePage.findchechMeOut().click()
        homePage.findName().send_keys(getData["Name"])  # using CSS
        homePage.findGender().click()
        homePage.findEmpStatus().click()
        homePage.findDatabind().send_keys(getData["DataBind"])
        homePage.findsubmot().click()  # using xpath
        alert_text = homePage.findAlert().text  # using classname
        print(alert_text)
        assert "Success" in alert_text
        homePage.findDatabind().clear()
        time.sleep(5)
        self.driver.refresh()

    @pytest.fixture(params=[
        {"EmailID" : "supraja@gmail.com", "Pwd" : "welcome_123", "Name" : "Hello", "DataBind": "Hello again"},
        {"EmailID" : "Tanuz@gmail.com", "Pwd" : "welcome_123", "Name" : "Tanuz", "DataBind": "Hello Smile"}])
    def getData(self, request):
        return request.param
"""

#calling data from separate file
class TestFormFill(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)
        log = self.getLogger()
        log.info("Email ID is" + getData["EmailID"])
        homePage.findEmail().send_keys(getData["EmailID"])  # Using Name
        log.info("Email ID is" + getData["Pwd"])
        homePage.findPassword().send_keys(getData["Pwd"])  # Using ID
        homePage.findchechMeOut().click()
        log.info("Email ID is" + getData["Name"])
        homePage.findName().send_keys(getData["Name"])  # using CSS
        homePage.findGender().click()
        homePage.findEmpStatus().click()
        log.info("Email ID is" + getData["DataBind"])
        homePage.findDatabind().send_keys(getData["DataBind"])
        homePage.findsubmot().click()  # using xpath
        alert_text = homePage.findAlert().text  # using classname
        log.info(alert_text)
        assert "Success" in alert_text
        homePage.findDatabind().clear()
        time.sleep(5)
        self.driver.refresh()

    #@pytest.fixture(params=HomePageData.test_HomePage_Data)
    @pytest.fixture(params=HomePageData.get_testdata("Form_fill"))
    def getData(self, request):
        return request.param

