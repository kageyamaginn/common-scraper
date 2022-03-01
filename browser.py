from json import JSONEncoder
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.common.exceptions import NoSuchElementException

class Browser:
    def __init__(self):
        self.driver:ChromiumDriver = None


    def Chrome():
        b = Browser()
        options = webdriver.ChromeOptions()
        options.add_argument("--log-levle=3")
        driver=webdriver.Chrome()
        b.driver=driver
        return b

    def go(self, uri):
        self.driver.get(uri)

    def find(self,xpath):
        hits = self.driver.find_elements_by_xpath(xpath)
        if len(hits)>1:
            return hits
        if len(hits)==1:
            return hits[0]

    def wait(self,xpath,expect=EC.presence_of_element_located,by=By.XPATH, timeout=10):
        try:
            WebDriverWait(self.driver,timeout).until(expect((by,xpath)))
        except NoSuchElementException as Ex:
            return False
        except:
            return False
        return True



    def focus_to(self, element):
        target=None
        if type(element)==type(''):
            target = self.find(element)
        else:
            target=element
        
        self.driver.execute_script("return arguments[0].scrollIntoView();",target)

            