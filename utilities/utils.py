'''Utils file: This file contains all the assertion use in the Project'''
'''softest is use for soft assertion means the scripts will not stop execution it any of the test is failed'''



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