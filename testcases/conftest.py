# import time
# import os
# import pytest
# import pytest_html
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# @pytest.fixture(scope='class')
# def setup(request):
#     driver = webdriver.Chrome()
#     driver.get('https://phptravels.com/demo')
#     driver.maximize_window()
#     time.sleep(5)  # import time
#     request.cls.driver = driver
#     yield
#     driver.close()

# # ----------------------------------------Default reports without Screenshot------------------------------

# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     outcome = yield
# #     report = outcome.get_result()
# #     extras = getattr(report, "extras", [])
# #     if report.when == "call":
# #         # always add url to report
# #         extras.append(pytest_html.extras.url("http://www.example.com/"))
# #         xfail = hasattr(report, "wasxfail")
# #         if (report.skipped and xfail) or (report.failed and not xfail):
# #             # only add additional html on failure
# #             extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
# #         report.extras = extras

# # -------------------------------------Custom reports-------------------------

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         extras.append(pytest_html.extras.url("http://www.DemoLogicSquards.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             file_name = str(int(round(time.time()*1000))) + ".png"
#             # file_name= report.nodeid.replace("::","_")+".png"
#             destinationFile = os.path.join(report_directory,file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 # html =  "<div><img scr = '%S' alt= 'screenshot' style='width: 300px;height: 200px ;' onclick='window.open(this.src)' align = 'right'/></div>'%file_name 
#                 img_html = f"<div><img src='%S' alt='screenshot' style='width: 300px;height: 200px;' onclick='window.open(this.src)' align='right'/></div>"
                
#                 extra.append(pytest_html.extras.html(img_html))
#         report.extras = extras
    
# def pytest_html_report_title(report):
#     report.title = "DemoLogicSquard Automation Report"


import time
import os
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='class', autouse=True)
def setup(request):
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get('https://phptravels.com/demo')
        driver.maximize_window()
        time.sleep(5)  # import time
        request.cls.driver = driver
        yield
    finally:
        if driver is not None:
            driver.quit()


# Custom reports

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.DemoLogicSquards.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time()*1000))) + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver = item.funcargs["setup"].driver
            driver.save_screenshot(destination_file)
            if file_name:
                img_html = f"<div><img src='%s' alt='screenshot' style='width: 300px;height: 200px;' onclick='window.open(this.src)' align='right'/></div>" % file_name
                extras.append(pytest_html.extras.html(img_html))
        report.extras = extras



def pytest_html_report_title(report):
    report.title = "DemoLogicSquard Automation Report"
