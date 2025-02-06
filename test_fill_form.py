import sqlite3
import time
from selenium.common import TimeoutException
from utils.generate_random import generate_random_number
from utils.functions import Global_functions
from data_handler import get_nationality, get_marital_status, get_blood_type
from locators import AddEmployeeLocators, EditPersonalDetails


class OrangeHRMTestCases:
    def __init__(self, driver):
        # Initialises the driver
        self.driver = driver

    def connect_and_get_data(self, name=None, middle_name=None, last_name=None):
        try:
            conn = sqlite3.connect('database/data.db')
            print("Successful connection to the database")
            cursor = conn.cursor()

            if name and middle_name and last_name:

                cursor.execute('SELECT name, middle_name, last_name FROM users WHERE name = ? AND middle_name = ? AND last_name = ?',
                               (name, middle_name, last_name))

            else:
                cursor.execute('SELECT name, middle_name, last_name FROM users')

            rows = cursor.fetchall()

            return rows

        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

        finally:
            if 'conn' in locals():
                conn.close()

    def get_contact_info(self, name=None, middle_name=None, last_name=None):
        try:
            conn = sqlite3.connect('database/contact_details.db')
            cursor = conn.cursor()

            if name and middle_name and last_name:

                cursor.execute('''
                                     SELECT street1, city, state, zip_code, mobile_number, work_number, work_email, other_email'
                                     FROM contact_table '
                                     WHERE name = ? AND middle_name = ? AND last_name = ?''',
                               (name, middle_name, last_name))

            else:
                cursor.execute('SELECT street1, city, state, zip_code, mobile_number, work_number, work_email, other_email FROM contact_table')

            rows = cursor.fetchall()
            return rows

        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

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

    def edit_personal_details(self,name, street1, city, state, zip_code, mobile_number, work_number, work_email, other_email):

        f = Global_functions(self.driver)
        nationality = get_nationality()
        marital_status = get_marital_status()
        blood_type = get_blood_type()
        random_number = generate_random_number()

        try:
            f.click_xpath_check(AddEmployeeLocators.PIM_BUTTON, .3)
            f.click_xpath_check(EditPersonalDetails.EMPLOYEE_LIST_BUTTON, 2)
            f.select_xpath(EditPersonalDetails.EMPLOYEE_NAME_FIELD)
            f.mixed_text("xpath", EditPersonalDetails.EMPLOYEE_NAME_FIELD, name, .5)
            f.select_xpath(EditPersonalDetails.EMPLOYEE_ID_FIELD)
            f.click_xpath_no_scroll(EditPersonalDetails.SEARCH_BUTTON, .5)
            f.click_xpath_no_scroll(EditPersonalDetails.EDIT_EMPLOYEE_PENCIL_BUTTON, .3)
            f.mixed_text("xpath", EditPersonalDetails.OTHER_ID_FIELD, str(random_number), 3)
            f.mixed_text("xpath", EditPersonalDetails.LICENSE_EXPIRY_DATE_FIELD, "2025-10-09", 3)
            f.click_js(EditPersonalDetails.NATIONALITY_DROPDOWN)
            f.click_xpath_no_scroll(
                f"//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div/div/div[@class='oxd-select-option']/span[contains(text(), '{nationality}')]",
                .5)
            f.click_js(EditPersonalDetails.MARITAL_STATUS_DROPDOWN)
            f.click_xpath_no_scroll(
                f"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --positon-bottom']/div/span[contains(text(),'{marital_status}')]",
                .3)
            f.click_xpath_no_scroll(EditPersonalDetails.GENDER_RADIO, .3)
            f.click_js(EditPersonalDetails.SAVE_PERSONAL_DETAILS)
            f.select_xpath(EditPersonalDetails.SAVE_PERSONAL_POPUP)
            f.click_js(EditPersonalDetails.BLOOD_TYPE)
            f.click_xpath_no_scroll(
                f"//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div/div[@class='oxd-select-dropdown --positon-bottom']/div/span[contains(text(),'{blood_type}')]",
                .5)
            f.click_js(EditPersonalDetails.SAVE_CUSTOM_FIELDS)
            f.select_xpath(EditPersonalDetails.EMPLOYEE_ID_FIELD)
            f.click_xpath_check(EditPersonalDetails.CONTACT_DETAILS,1)
            f.mixed_text("xpath", EditPersonalDetails.STREET1_FIELD, street1, .5)
            f.mixed_text("xpath", EditPersonalDetails.CITY_FIELD, city, .5)
            f.mixed_text("xpath", EditPersonalDetails.STATE_FIELD, state, .5)
            f.mixed_text("xpath", EditPersonalDetails.ZIP_CODE_FIELD, zip_code, .5)
            f.mixed_text("xpath", EditPersonalDetails.MOBILE_NUMBER_FIELD, mobile_number, .5)
            f.mixed_text("xpath", EditPersonalDetails.WORK_NUMBER_FIELD, work_number, .5)
            f.mixed_text("xpath", EditPersonalDetails.WORK_EMAIL_FIELD, work_email, 3)
            f.mixed_text("xpath", EditPersonalDetails.PERSONAL_EMAIL_FIELD, other_email, 3)
            f.click_xpath_check("//button[normalize-space()='Save']",1)
            f.select_xpath("//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']")
            time.sleep(3)

        except TimeoutException as ex:
            print(ex.msg)
            print("Element is not displayed: {ex}")