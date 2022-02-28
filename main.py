from selenium import webdriver
import pytest

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.implicitly_wait(6)

driver.get("https://rahulshettyacademy.com/angularpractice/")