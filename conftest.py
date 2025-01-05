import pytest
import time
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.functions import Global_functions

#Conftest: File needed to define fixtures and make them global

@pytest.fixture(scope='module')
def setup_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    f = Global_functions(driver)
    f.mixed_text("xpath", "//input[@placeholder='Username']", "Admin", 5)
    f.mixed_text("xpath", "//input[@placeholder='Password']", "admin123", 5)
    f.click_xpath_check("//button[@type='submit']", .3)
    time.sleep(5)
    print("Logging in")
    yield driver # Returns the driver to test functions that use this fixture.
    driver.quit() # Close the browser at the end of the test module.