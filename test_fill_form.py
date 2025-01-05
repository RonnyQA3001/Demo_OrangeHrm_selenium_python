import pytest
from selenium.common import TimeoutException
from utils.functions import Global_functions

class OrangeHRMTestCases:
    def __init__(self, driver):
        # Initialises the driver
        self.driver = driver

    def add_employee(self):
        f = Global_functions(self.driver)
        try:
            #Go to PIM to generate a new user
            f.click_xpath_check("//span[normalize-space()='PIM']",3)
            f.click_xpath_check("//a[normalize-space()='Add Employee']",3)
            f.mixed_text("xpath","//input[@placeholder='First Name']","Miguel",.5)
            f.mixed_text("xpath","//input[@placeholder='Middle Name']","Jimenez",.5)
            f.mixed_text("xpath","//input[@placeholder='Last Name']","Torres",2)
            f.mixed_text("xpath","//div[@class='oxd-input-group oxd-input-field-bottom-space']/div/input[@class='oxd-input oxd-input--active']","0924",.5)


        except TimeoutException as ex:
            print(ex.msg)
            print("Element is not displayed")



