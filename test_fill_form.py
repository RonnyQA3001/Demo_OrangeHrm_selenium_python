import pytest
import sqlite3
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from utils.functions import Global_functions

class OrangeHRMTestCases:
    def __init__(self, driver):
        # Initialises the driver
        self.driver = driver

    def connect_and_get_data(self):
        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()

        cursor.execute('SELECT name, middle_name, last_name FROM users')
        rows = cursor.fetchall()

        conn.close()

        return rows

    def add_employee(self, name, middle_name, last_name):
        f = Global_functions(self.driver)

        try:
            #Go to PIM to generate a new user
            f.click_xpath_check("//span[normalize-space()='PIM']",.3)
            f.click_xpath_check("//a[normalize-space()='Add Employee']",.3)

            try:
                f.mixed_text("xpath","//input[@placeholder='First Name']",name,.3)
            except Exception as e:
                print("Error entering name: {e}")

            try:
                f.mixed_text("xpath","//input[@placeholder='Middle Name']",middle_name,.3)
            except Exception as e:
                print("Error entering name: {e}")

            try:
                f.mixed_text("xpath", "//input[@placeholder='Last Name']", last_name, .3)
            except Exception as e:
                print("Error entering name: {e}")

            f.click_xpath_check("//button[normalize-space()='Save']",.5)
            f.select_xpath("//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")
            print("New user added correctly: " + name)

        except TimeoutException as ex:
            print(ex.msg)
            print("Element is not displayed")

    def edit_personal_details(self, name):
        f = Global_functions(self.driver)

        try:
            f.click_xpath_check("//span[normalize-space()='PIM']", .3)
            f.click_xpath_check("//a[normalize-space()='Employee List']",2)
            f.select_xpath("//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
            f.mixed_text("xpath","//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]",name,2)
            f.click_xpath_check("//button[normalize-space()='Search']",2)
            f.click_xpath_check("//div[contains(text(),'Riccardo')]",.3)

        except TimeoutException as ex:
            print(ex.msg)
            print(f"Element is not displayed: {ex}")








