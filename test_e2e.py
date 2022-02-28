import pytest

from Baseclass import BaseClass
from homepage import Homepage
from homepage2 import HomePage2


class TestCase(BaseClass):

    def test_e2e(self):

        homepage=Homepage(self.driver)
        homepage.insert().send_keys("Deepak")
        homepage.insert1().send_keys("Email")
        homepage.insert2().send_keys("qwerty")
        homepage.insert3().click()
        homepage.insert4().click()
        assert "Success" in self.driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text
        homepage.insert5().click()
        self.driver.implicitly_wait(6)
        homepage2=HomePage2(self.driver)
        Option = homepage2.insert6()
        for choose in Option:
                choose.click()
        homepage2.insert8().click()
        homepage2.insert9().click()
        homepage2.insert10().send_keys("ind")
        country = homepage2.insert11()
        for c in country:
            if c.text == 'India':
                c.click()
                break
        homepage2.insert12().click()
        assert "Success" in homepage2.insert13().text



