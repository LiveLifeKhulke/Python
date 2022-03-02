import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Baseclass import BaseClass


class Test_PHP(BaseClass):

    def test_php(self,dataload):
        self.driver.refresh()

        self.driver.find_element_by_name("name").send_keys(dataload["name"])

        self.driver.find_element_by_name("email").send_keys(dataload["email"])
        dropdown=Select(self.driver.find_element_by_xpath("//select[@class='form-control']"))
        dropdown.select_by_index(1)
        self.driver.find_element_by_css_selector("[type='submit']").click()
        message=self.driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text
        print(message)


    @pytest.fixture(params=[{"name":"Deepak","email":"Deepak.147392"},{"name":"Akshay","email":"xyz"}])
    def dataload(self,request):
        return request.param