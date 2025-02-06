# locators.py
class AddEmployeeLocators:
    PIM_BUTTON = "//span[normalize-space()='PIM']"
    ADD_EMPLOYEE_BUTTON = "//a[normalize-space()='Add Employee']"
    FIRST_NAME_FIELD = "//input[@placeholder='First Name']"
    MIDDLE_NAME_FIELD = "//input[@placeholder='Middle Name']"
    LAST_NAME_FIELD = "//input[@placeholder='Last Name']"
    SAVE_EMPLOYEE_BUTTON = "//button[normalize-space()='Save']"
    USER_ADDED_POPUP = "//div[@class='oxd-toast oxd-toast--success oxd-toast-container--toast']"

class EditPersonalDetails:
    EMPLOYEE_LIST_BUTTON = "//a[normalize-space()='Employee List']"
    EMPLOYEE_NAME_FIELD = "//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]"
    EMPLOYEE_ID_FIELD = "//div[@class='oxd-input-group oxd-input-field-bottom-space']/div/input[@class='oxd-input oxd-input--active']"
    SEARCH_BUTTON = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    EDIT_EMPLOYEE_PENCIL_BUTTON = "//div/div[@class='oxd-table-cell oxd-padding-cell']/div/button[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-pencil-fill']"
    OTHER_ID_FIELD = "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/input[1]"
    LICENSE_EXPIRY_DATE_FIELD = "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    NATIONALITY_DROPDOWN = "//body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
    MARITAL_STATUS_DROPDOWN = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-text oxd-select-text--active']"
    GENDER_RADIO = "//label[normalize-space()='Male']"
    SAVE_PERSONAL_DETAILS = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']"
    SAVE_PERSONAL_POPUP = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"
    BLOOD_TYPE = "//div[@class='orangehrm-custom-fields']//div[@class='orangehrm-card-container']//form[@class='oxd-form']//div[@class='oxd-form-row']//div[@class='oxd-grid-3 orangehrm-full-width-grid']//div[@class='oxd-grid-item oxd-grid-item--gutters']//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div[@class='oxd-select-text oxd-select-text--active']"
    SAVE_CUSTOM_FIELDS = "//div[@class='orangehrm-custom-fields']//button[@type='submit'][normalize-space()='Save']"
    SAVE_CUSTOM_FIELDS_POPUP = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"
    CONTACT_DETAILS = "//a[@class='orangehrm-tabs-item'][contains(text(),'Contact Details')]"
    STREET1_FIELD = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//div[1]//div[1]//div[1]//div[1]//div[2]//input"
    CITY_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[3]/div[1]/div[2]/input[@class='oxd-input oxd-input--active']"
    STATE_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/input[1]"
    ZIP_CODE_FIELD = "//form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/input[1]"
    MOBILE_NUMBER_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]"
    WORK_NUMBER_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[3]/div[1]/div[2]/input[1]"
    WORK_EMAIL_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]"
    PERSONAL_EMAIL_FIELD = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]"






