import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class Global_functions():

    def __init__(self, driver):
        self.driver = driver

    def browse(self, url, timer):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            t = time.sleep(timer)
            return t

        except Exception as ex:
            print(ex.msg)
            print("Element not found" + url)

    def mixed_text(self, type, selector, text, timer):
        if type == "xpath":
            try:
                val = self.select_xpath(selector)
                val.clear()
                val.send_keys(text)
                print("By typing in the field {} the text -> {} ".format(selector, text))
                t = time.sleep(timer)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not found" + selector)

        elif type == "id":
            try:
                val = self.select_id(selector)
                val.clear()
                val.send_keys(text)
                print("By typing in the field {} the text -> {} ".format(selector, text))
                t = time.sleep(timer)
                return t

            except TimeoutException as ex:
                print(ex.msg)
                print("Element not found" + selector)

    ########################################################################################################################
    # Click actions section
    ########################################################################################################################
    def click_id_check(self, id, timer):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            t = time.sleep(timer)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + id)

    def click_xpath_check(self, xpath, timer):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(timer)
            return t

        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + xpath)

    def click_xpath_no_scroll(self, xpath, timer):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
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
        time.sleep(3)

    ########################################################################################################################
    # Select values section
    ########################################################################################################################
    def select_xpath(self, element):
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, element)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.XPATH, element)
        return val

    def select_id(self, selector, element):
        val = self.select_xpath(selector)
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.ID, element)
        return val

    def select_xpath_type(self, xpath, type, dato, timer):
        try:
            val = self.select_xpath(xpath)
            val = Select(val)
            if type == "text":
                val.select_by_visible_text(dato)
            elif type == "index":
                val.select_by_index(dato)
            elif type == "value":
                val.select_by_value(dato)
            print("The field selected is {} ".format(dato))
            t = time.sleep(timer)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("The element was not found: " + xpath)


