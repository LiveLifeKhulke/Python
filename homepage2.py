from selenium.webdriver.common.by import By


class HomePage2:
    def __init__(self,driver):
        self.driver=driver

    a=(By.CSS_SELECTOR,"[class='btn btn-info']")

    c=(By.CSS_SELECTOR,"[class='nav-link btn btn-primary']")
    d=(By.CSS_SELECTOR,"[class='btn btn-success']")
    e=(By.ID,"country")
    f=(By.CSS_SELECTOR,"[class='suggestions'] a")
    g=(By.CSS_SELECTOR,"[class='btn btn-success btn-lg']")
    h=(By.CSS_SELECTOR,"[class='alert alert-success alert-dismissible']")

    def insert6(self):
        return self.driver.find_elements(*HomePage2.a)



    def insert8(self):
        return self.driver.find_element(*HomePage2.c)

    def insert9(self):
        return self.driver.find_element(*HomePage2.d)

    def insert10(self):
        return self.driver.find_element(*HomePage2.e)

    def insert11(self):
        return self.driver.find_elements(*HomePage2.f)

    def insert12(self):
        return self.driver.find_element(*HomePage2.g)

    def insert13(self):
        return self.driver.find_element(*HomePage2.h)