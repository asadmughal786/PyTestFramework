import pytest
import softest
from pages.demo_form_page import launchPage
from utilities.utils import Utils
from ddt import ddt , data, unpack , file_data


# HERE WE WILL WRITE ALL THE BUSINESS TEST CASES WHICH COULD BE UNDERSTANDABLE TO THE LAYMEN AS WELL.

@pytest.mark.usefixtures("setup")
@ddt                                       # This ensure that this class is Data driver test.
class TestFormVerification(softest.TestCase): 
    # log = Utils.custom_logger()
    #definig the objects
    def class_setup(self):
        self.lp = launchPage(self.driver)
        self.ut = Utils(self.driver)

            # --------------------------Hard code method to try DDT---------------------
    # @data(('',"Asad","IT","mughalasad720@gmail.com"),("Muhammad","Ali","Business","mughalasad720@gmail.com"),("Muhammad","Zubair","IT","mughalasad720@gmail.com")) # this is the test data (Note: the data must be aligned with the parameters of the function on which its implementing.
    # # the data must be in the format of 'Set')
    # @unpack # this method now unpack the data coming in the @data decorator and will send it to the function

    # ------------------------------DDT using JSON file data------------------------------------
    @file_data("../testdata/testdata.json")
    # --------------------------- DDT usign YMAL file data------------------------------------
    # @file_data("../testdata/testml.yml")
    def test_Form_functionality(self,firstName,LastName,Business,Email):

        # Made the constructor for the class
        lp = launchPage(self.driver)
        lp.FormFunctionalityverification(firstName,LastName,Business,Email)
        
