from base.base_Driver import BaseDriver
from selenium.webdriver.common.by import By 



class (BaseDriver):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    
    

    def get_dashboard_title(self):
        return self.FindElement(By.XPATH,self.dashbord_welcome_title)
            

    
