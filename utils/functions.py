import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Global_functions():

    def __init__(self,driver):
        self.driver = driver

    def browse(self,url,timer):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            t = time.sleep(timer)
            return t

        except Exception as ex:
            print(ex.msg)
            print("No se encontro el elemento" + url)

    def mixed_text(self, set, selector, text, timer):
        if set == "xpath":
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

        elif set == "id":
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


    def click_id_check(self,id,tiempo):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID,id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + id)

    def click_xpath_check(self,xpath,tiempo):
        try:
            val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("Element was not found" + xpath)

    def select_xpath(self,element):
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, element)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.XPATH, element)
        return val

    def select_id(self,element):
        val = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.ID, element)))
        val = self.driver.execute_script("arguments[0].scrollIntoView()", val)
        val = self.driver.find_element(By.ID, element)
        return val

