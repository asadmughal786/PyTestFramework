'''Utils file: This file contains all the assertion use in the Project'''
'''softest is use for soft assertion means the scripts will not stop execution it any of the test is failed'''



import inspect
import logging
import softest

class Utils(softest.TestCase):

    def VerifyListItemText(self,list,value):
        for i in list:
            print('Text is -> '+i.text())
            self.soft_assert(self.assertEqual,i.text,value)
            if i.text == value:
                print("Test Pass")
            else:
                print("Test Fail")
        self.assert_all()
    
    def assert_Element_Text(self,value1,verificationData):
            self.soft_assert(self.assertEqual,value1.text,verificationData)
            if value1.text == verificationData:
                print("Test Passed")
            else:
                print("Test Failed")

    def assert_Url(self,actualUrl,ExpectedUrl):
        self.soft_assert(self.assertEqual(actualUrl,ExpectedUrl))
        self.assert_all()
    

    def custom_logger(logLevel = logging.DEBUG):
        # set the class/method name from where it's called
        logger_name = inspect.stack()[1][3]
        # creat logger 
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG) 
        # create console handler or file handler and set the log level
        filehandler = logging.FileHandler("./loggers/logs/automation.log", mode='a')
        filehandler.setLevel(logLevel)
        # creat formatter - how to you want you logs to be look like 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
        # Add formatter to the console or file
        filehandler.setFormatter(formatter)
        # Add console handler to the logger 
        logger.addHandler(filehandler)
        return logger

