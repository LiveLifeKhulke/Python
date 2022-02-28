from Baseclass import BaseClass


class TestGreen(BaseClass):
    def test_greencart(self):
        self.driver.implicitly_wait(6)
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        Option=self.driver.find_elements_by_css_selector("[class='btn btn-info']")
        for choose in Option:
            if "Black" in choose.find_element_by_xpath("parent::div/parent::div/div/h4").text:
                choose.click()
                break
        self.driver.find_element_by_css_selector("[class='nav-link btn btn-primary']").click()
        self.driver.find_element_by_css_selector("[class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        country= self.driver.find_elements_by_css_selector("[class='suggestions'] a")
        for c in country:
            if c.text=='India':
                c.click()
                break
        self.driver.find_element_by_css_selector("[class='btn btn-success btn-lg']").click()
        assert "Success" in self.driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text


