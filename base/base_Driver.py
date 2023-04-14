from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

'''In base class we wrapup all the driver method to minimize the complexibility of the framework'''
'''All the Driver Methods will be written here and this this class will he inherited from the other class to use the Methods'''

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver


    def wait_till_element_clickable(self,locator_type, Locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((locator_type,Locator))) # --> Explicit Wait Syntax. We Pass Arguments in the form of tuple
        return element
    
    def wait_till_element_present(self,locator_type, Locator):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_element_located((locator_type,Locator))) # --> Explicit Wait Syntax. We Pass Arguments in the form of tuple
        return element
    
    def Find_Element(self,locator_type,locator):
        element = self.driver.find_element((locator_type,locator))
    
    def handleAlearts(self,ResponseAlert):
        alert = Alert(self.driver)
        return alert.text

