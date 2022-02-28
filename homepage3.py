from selenium.webdriver.common.by import By


class homepage3:
    def __init__(self,driver):
        self.driver = driver

    a = (By.CSS_SELECTOR,"[class='radioButton']")
    b = (By.CSS_SELECTOR,"[type='checkbox']")
    c=(By.NAME,"enter-name")

    def pull_data1(self):
        return self.driver.find_elements(*homepage3.a)
    def pull_data2(self):
        return self.driver.find_elements(*homepage3.b)
    def pull_data3(self):
        return self.driver.find_element(*homepage3.c)