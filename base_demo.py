from test_fill_form import OrangeHRMTestCases

def test_OrangeHRMTestSuite(setup_login): # Create an instance of the test class with the fixture setup_login
    tc = OrangeHRMTestCases(setup_login)
    tc.add_employee("Carlos","Lopez","Loria")

