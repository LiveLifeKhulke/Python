from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):
        self.driver=driver

    A =(By.NAME,"name")
    B=(By.NAME,"email")
    C=(By.ID,"exampleInputPassword1")
    D=(By.CSS_SELECTOR,"[class='form-check-input']")
    E=(By.CSS_SELECTOR,"[class='btn btn-success']")
    F=(By.XPATH,"//a[text()='Shop']")



    def insert(self):
        return self.driver.find_element(*Homepage.A)
    def insert1(self):
        return self.driver.find_element(*Homepage.B)
    def insert2(self):
        return self.driver.find_element(*Homepage.C)
    def insert3(self):
        return self.driver.find_element(*Homepage.D)
    def insert4(self):
        return self.driver.find_element(*Homepage.E)
    def insert5(self):
        return self.driver.find_element(*Homepage.F)



