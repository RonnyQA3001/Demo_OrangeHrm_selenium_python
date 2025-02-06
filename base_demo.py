from test_fill_form import OrangeHRMTestCases


def test_OrangeHRMTestSuite(setup_login): # Create an instance of the test class with the fixture setup_login
    tc = OrangeHRMTestCases(setup_login)
    print("Instance successfully created.")

    user_rows = tc.connect_and_get_data()
    print(f"User data obtained: {user_rows}")

    contact_rows = tc.get_contact_info()
    print(f"Contact details obtained: {contact_rows}")

    # We check that both lists have data
    if not user_rows or not contact_rows:
        print("Error: No data were found in one of the databases.")
        return

    for user, contact in zip(user_rows, contact_rows):
        name, middle_name, last_name = user
        street1, city, state, zip_code, mobile_number, work_number, work_email, other_email = contact

        tc.add_employee(name, middle_name, last_name)
        tc.edit_personal_details(
            f"{name}",
            street1,
            city,
            state,
            zip_code,
            mobile_number,
            work_number,
            work_email,
            other_email
        )

