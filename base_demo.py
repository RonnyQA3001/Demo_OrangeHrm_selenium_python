from test_fill_form import OrangeHRMTestCases

def test_OrangeHRMTestSuite(setup_login): # Create an instance of the test class with the fixture setup_login
    tc = OrangeHRMTestCases(setup_login)
    rows = tc.connect_and_get_data()

    for row in rows:
        name, middle_name, last_name = row
        tc.add_employee(name,middle_name,last_name)

    for row in rows:
        name, middle_name, last_name = row
        tc.edit_personal_details(name)

