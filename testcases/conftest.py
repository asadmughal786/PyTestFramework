import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.get('https://phptravels.com/demo')
    driver.maximize_window()
    time.sleep(5)  # import time
    request.cls.driver = driver
    yield
    driver.close()
    