import time

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
            f.mixed_text("xpath","//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]",name,5)
            f.select_xpath("//div[@class='oxd-input-group oxd-input-field-bottom-space']/div/input[@class='oxd-input oxd-input--active']")
            f.click_xpath_no_scroll("//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']",5)
            f.click_xpath_check("//div/div[@class='oxd-table-cell oxd-padding-cell']/div/button[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-pencil-fill']",3)
            f.mixed_text("xpath","//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]","3001",3)
            f.mixed_text("xpath","//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]","2025-10-09",3)
            f.click_js("//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
            f.click_xpath_no_scroll("//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div/div/div[@class='oxd-select-option']/span[contains(text(),'American')]",5)
            f.click_xpath_no_scroll("//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div/div/div[@class='oxd-select-option']/span[contains(text(),'American')]",5)

        except TimeoutException as ex:
            print(ex.msg)
            print(f"Element is not displayed: {ex}")








