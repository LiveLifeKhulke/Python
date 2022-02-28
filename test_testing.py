import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Baseclass import BaseClass
from homepage3 import homepage3


class TestAutomation(BaseClass):
    def test_automation(self,getData):

        log = self.getlogger()
        homepage=homepage3(self.driver)
        RadioButton=homepage.pull_data1()
        for option in RadioButton:
            if option.get_attribute("value")=="radio2":
                option.click()
                break
        CheckBox = homepage.pull_data2()
        for option1 in CheckBox:
            if option1.get_attribute("value")=="option2":
                option1.click()
                break
        log.info("First name"+getData["First Name"])
        homepage.pull_data3().send_keys(getData["First Name"])
        name = homepage.pull_data3().get_attribute("value")
        log.error("The value typed is"+name)
        self.driver.refresh()


    @pytest.fixture(params=[{"First Name":"Deepak"}])
    def getData(self, request):
        return request.param