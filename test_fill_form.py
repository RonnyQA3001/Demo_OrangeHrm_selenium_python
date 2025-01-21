import sqlite3
from selenium.common import TimeoutException
from utils.generate_random import generate_random_number
from utils.functions import Global_functions
from data_handler import get_nationality
from locators import AddEmployeeLocators, EditPersonalDetails


class OrangeHRMTestCases:
    def __init__(self, driver):
        # Initialises the driver
        self.driver = driver

    def connect_and_get_data(self):
        try:
            conn = sqlite3.connect('database/data.db')
            print("Conexión exitosa a la base de datos.")
            cursor = conn.cursor()

            cursor.execute('SELECT name, middle_name, last_name FROM users')
            rows = cursor.fetchall()

            conn.close()

            return rows

        finally:
            if 'conn' in locals():
                conn.close()

    def add_employee(self, name, middle_name, last_name):
        f = Global_functions(self.driver)

        try:
            # Go to PIM to generate a new user
            f.click_xpath_check(AddEmployeeLocators.PIM_BUTTON, .3)
            f.click_xpath_check(AddEmployeeLocators.ADD_EMPLOYEE_BUTTON, .3)

            try:
                f.mixed_text("xpath", AddEmployeeLocators.FIRST_NAME_FIELD, name, .3)
            except Exception as e:
                print("Error entering name: {e}")

            try:
                f.mixed_text("xpath", AddEmployeeLocators.MIDDLE_NAME_FIELD, middle_name, .3)
            except Exception as e:
                print("Error entering name: {e}")

            try:
                f.mixed_text("xpath", AddEmployeeLocators.LAST_NAME_FIELD, last_name, .3)
            except Exception as e:
                print("Error entering name: {e}")

            f.click_xpath_check(AddEmployeeLocators.SAVE_EMPLOYEE_BUTTON, .5)
            f.select_xpath(AddEmployeeLocators.USER_ADDED_POPUP)
            print("New user added correctly: " + name)

        except TimeoutException as ex:
            print(ex.msg)
            print("Element is not displayed")

    def edit_personal_details(self, name):

        f = Global_functions(self.driver)
        nationality = get_nationality()
        random_number = generate_random_number()

        try:
            f.click_xpath_check(AddEmployeeLocators.PIM_BUTTON, .3)
            f.click_xpath_check(EditPersonalDetails.EMPLOYEE_LIST_BUTTON, 2)
            f.select_xpath(EditPersonalDetails.EMPLOYEE_NAME_FIELD)
            f.mixed_text("xpath", EditPersonalDetails.EMPLOYEE_NAME_FIELD, name, 5)
            f.select_xpath(EditPersonalDetails.EMPLOYEE_ID_FIELD)
            f.click_xpath_no_scroll(EditPersonalDetails.SEARCH_BUTTON, 5)
            f.click_xpath_no_scroll(EditPersonalDetails.EDIT_EMPLOYEE_PENCIL_BUTTON, 3)
            f.mixed_text("xpath",EditPersonalDetails.OTHER_ID_FIELD,str(random_number), 3)
            f.mixed_text("xpath",EditPersonalDetails.LICENSE_EXPIRY_DATE_FIELD,"2025-10-09", 3)
            f.click_js(EditPersonalDetails.NATIONALITY_DROPDOWN)
            f.click_xpath_no_scroll(f"//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div/div/div[@class='oxd-select-option']/span[contains(text(), '{nationality}')]",5)


        except TimeoutException as ex:
            print(ex.msg)
            print("Element is not displayed: {ex}")
