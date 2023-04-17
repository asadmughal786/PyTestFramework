import logging
import time
from selenium.webdriver.common.by import By
from base.base_Driver import BaseDriver
from utilities.utils import Utils
from selenium.webdriver.common.alert import Alert

# Implementation file All the technical functionality here
# best Practise is as for POM (Page Object Model file) all the dependencies should be listed in the same file and class

class launchPage(BaseDriver):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)  # this will initialize the base class as well as the object of this class will be created
        self.driver = driver
        # self.wait = wait

    # Locators / XPATH's for the fields
    first_name_field = "//input[@placeholder='First Name']"
    last_name_field = "//input[@placeholder='Last Name']"
    business_name_field = "//input[@placeholder='Business Name']"
    email_field = "//input[@placeholder='Email']"
    num1 = "//span[@id='numb1']"
    num2 = "//span[@id='numb2']"
    result = "//input[@id='number']"
    submit_button =  "//button[@id='demo']"
    message = "//strong[normalize-space()='Thank you!']"
    demo_form = "//a[@class='jfHeader-menuListLink']"

    # Getting the Fields 
    def getFirstNameField(self):
        return self.wait_till_element_clickable(By.XPATH, self.first_name_field)
    
    def getLastNameField(self):
        return self.wait_till_element_clickable(By.XPATH, self.last_name_field)
    
    def getBusinessNameField(self):
        return self.wait_till_element_clickable(By.XPATH, self.business_name_field)

    def getEmailField(self):
        return self.wait_till_element_clickable(By.XPATH, self.email_field)
    
    def getResultField(self):
        return self.wait_till_element_clickable(By.XPATH, self.result)

    def getCaptchaNum1(self):
        return self.wait_till_element_present(By.XPATH,self.num1)

    def getCaptchaNum2(self):
        return self.wait_till_element_present(By.XPATH,self.num2)

    def getMessages(self):
        return self.wait_till_element_present(By.XPATH,self.message)
    
    def getSubmitButtonField(self):
        return self.wait_till_element_clickable(By.XPATH, self.submit_button)

    def getDemoScreen(self):
        return self.wait_till_element_clickable(By.XPATH,self.demo_form)

    # end def

    # Actions / Operations
    def EnterFirstName(self, Firstname):
        self.getFirstNameField().click()
        self.getFirstNameField().send_keys(Firstname)
        
    def EnterLastName(self, lastname):
        self.getLastNameField().click()
        self.getLastNameField().send_keys(lastname)
    
    def EnterBusinessName(self, businessname):
        self.getBusinessNameField().click()
        self.getBusinessNameField().send_keys(businessname)
    
    def EnterEmail(self, email):
        self.getEmailField().click()
        self.getEmailField().send_keys(email)
    
    def EnterResult(self, result):
        self.getResultField().click()
        self.getResultField().send_keys(result)

    def clickSubmitButton(self):
        self.getSubmitButtonField().click()
        time.sleep(5)  # import time

    def clickDemoButton(self):
        self.getDemoScreen().click()
        time.sleep(5)  # import time


    def FormFunctionalityverification(self, first_name , last_name, business_name, email):
        alert = Alert(self.driver)
        try:
            self.EnterFirstName(first_name)
            self.log.info(f"Successfully Typed the First Name: {first_name}")
            self.EnterLastName(last_name)
            self.log.info(f"Successfully Typed the Last Name: {last_name}")
            self.EnterBusinessName(business_name)
            self.log.warning(f"Successfully Typed the Business Name: {business_name}")
            self.EnterEmail(email)
            self.log.warning(f"Successfully Typed the Email: {email}")
            result = int(self.getCaptchaNum1().text) + int(self.getCaptchaNum2().text)
            self.EnterResult(result)
            self.log.warning(f"Successfully Typed the Result: {result}")
            self.clickSubmitButton()
            self.log.warning(f"Successfully Clicked the Button Name")
        except:
            print(alert.text)
        finally:
            alert.accept()
            print(f"Successfully Accepted the Alert: {result}")
            ut = Utils()
            message= self.getMessages()
            self.log.info(message)
            self.log.warning(f"Test Executed")
            ut.assert_Element_Text(message,"Thank you!")
            self.clickDemoButton()

