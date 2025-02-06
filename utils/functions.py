import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys



class Global_functions():

    def __init__(self, driver):
        self.driver = driver

#Access to the page via URL
    def browse(self, url, timer):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            t = time.sleep(timer)
            return t

        except Exception as ex:
            print(ex.msg)
            print("Element not found" + url)

    # Function to search for a selector by Xpath or ID
    def mixed_text(self, type, selector, text, timer):
        """
              Types text into a field identified by an XPath selector.

              Parameters:
              type (str): Locator type (can support xpath and ID).
              selector (str): XPath string to locate the element.
              text (str): The text to input.
              timer (float): Delay (in seconds) after entering text.

              Returns:
              None
        """

        if type == "xpath":
            try:
                val = self.select_xpath(selector)

                # Clear the input field
                val.send_keys(Keys.CONTROL + "a")
                val.send_keys(Keys.DELETE)

                # Enter the new text
                val.send_keys(text)
                print("By typing in the field {} the text -> {} ".format(selector, text))

                # Wait for the specified time
                t = time.sleep(timer)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not found" + selector)

        elif type == "id":
            try:
                val = self.select_id(selector)

                # Clear the input field
                val.send_keys(Keys.CONTROL + "a")
                val.send_keys(Keys.DELETE)

                # Enter the new text
                val.send_keys(text)
                print("By typing in the field {} the text -> {} ".format(selector, text))

                # Wait for the specified time
                t = time.sleep(timer)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not found" + selector)

    ########################################################################################################################
    # Click actions section
    ########################################################################################################################
    def click_id_check(self, id, timer):
        """
                      Click the element via ID

                      Parameters:
                      id (str): Selector to identify the element.
                      timer (float): Delay (in seconds) after click the element.
        """
        try:
            # Wait until the selector is visible.
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, id)))

            # Ensures the element is fully visible before interacting
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", val)
            val = self.driver.find_element(By.ID, id)
            val.click()

            # Wait for the specified time
            t = time.sleep(timer)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + id)

    def click_xpath_check(self, xpath, timer):
        """
                             Click the element via XPATH

                             Parameters:
                             xpath (str): Selector xpath to identify the element.
                             timer (float): Delay (in seconds) after click the element.
        """
        try:
            # Wait until the selector is visible.
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))

            # Ensures the element is fully visible before interacting
            val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()

            # Wait for the specified time
            t = time.sleep(timer)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + xpath)

    def click_xpath_no_scroll(self, xpath, timer):
        """
                             Click on the element via xpath but do not scroll to the element.

                             Parameters:
                             xpath (str): Selector to identify the element.
                             timer (float): Delay (in seconds) after click the element
        """
        try:
            # Wait until the selector is visible.
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()

            # Wait for the specified time
            t = time.sleep(timer)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + xpath)

    def double_click(self, element):
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, element)))
        val = self.driver.find_element(By.XPATH, element).double_click()

    def click_js(self, element):
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, element)))
        val = self.driver.find_element(By.XPATH, element)
        val.click()
        self.driver.execute_script("arguments[0].setAttribute('style', 'display: block;')", val)
        time.sleep(1)

    ########################################################################################################################
    # Select values section
    ########################################################################################################################
    def select_xpath(self, element):
        # Wait until the selector is visible.
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, element)))

        # Ensures the element is fully visible before interacting
        val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", val)
        val = self.driver.find_element(By.XPATH, element)
        return val

    def select_id(self, selector, element):
        val = self.select_xpath(selector)
        val = self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", val)
        val = self.driver.find_element(By.ID, element)
        return val

    def select_xpath_type(self, xpath, type, dato, timer):
        """
            Selects an option from a dropdown menu located by an XPath.

            Parameters:
            xpath (str): XPath locator of the dropdown element.
            type (str): Selection method ('text', 'index', or 'value').
            dato (str/int): The data to select (text, index, or value depending on 'type').
            timer (float): Delay (in seconds) after selection.

            Returns:
            None
            """

        try:
            # Locate the dropdown element using XPath
            val = self.select_xpath(xpath)

            # Convert the element into a Select object
            val = Select(val)

            # Choose selection method based on 'type' argument
            if type == "text":
                val.select_by_visible_text(dato) # Select by visible text
            elif type == "index":
                val.select_by_index(dato) # Select by index (0-based)
            elif type == "value":
                val.select_by_value(dato) # Select by option value
            print("The field selected is {} ".format(dato))

            # Pause execution for the specified time
            t = time.sleep(timer)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("The element was not found: " + xpath)


