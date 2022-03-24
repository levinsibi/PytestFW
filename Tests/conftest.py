from datetime import time, datetime

import allure
import pytest

# from selenium import webdriver
from selenium import webdriver as selenium_webdriver
from Config.config import TestData
import time
from datetime import datetime
import pytest
from selenium import webdriver
import os


#@pytest.fixture(params=["chrome","firefox","edge"],scope='class')
# @pytest.fixture(params=["chrome"],scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = selenium_webdriver.Chrome()
#     if request.param == "firefox":
#         web_driver = selenium_webdriver.Firefox()
#     if request.param == "edge":
#         web_driver = selenium_webdriver.Edge()
#     request.cls.driver = web_driver
#
#     yield
#     web_driver.close()

# @pytest.fixture(scope='class')
# def init_driver():
#     driver = webdriver.Chrome()
#
#     yield driver
#     driver.close()
#     driver.quit()


@pytest.fixture(params=["chrome","firefox","edge"],scope='class')
def init_driver(request):
        if request.param == "chrome":
            driver = selenium_webdriver.Chrome()
        if request.param == "firefox":
            driver = selenium_webdriver.Firefox()
        if request.param == "edge":
            driver = selenium_webdriver.Edge()
        request.cls.driver = driver

        yield driver
        driver.close()
        driver.quit()




    # @pytest.mark.usefixtures("init_driver")
    # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    # def pytest_runtest_makereport(item, call):
    #     """
    #      get the hook function for the state of each use case
    #     :param item:  test case
    #     :param call:  test procedure
    #     :return:
    #     """
    #     #  get the result of the call to the hook method
    #     out_come = yield
    #     rep = out_come.get_result()  # get the test report from the result of the call to the hook method
    #     # rep.when represents the test step and only gets the use case call  the result of the execution is a failure.   does not include setup/teardown
    #     if rep.when == "call" and rep.failed:
    #         mode = "a" if os.path.exists("failures") else "w"
    #         with open("failures", mode) as f:
    #             if "tmpdir" in item.fixturenames:
    #                 extra = " (%s)" % item.funcargs["tmpdir"]
    #             else:
    #                 extra = ""
    #             f.write((rep.nodeid + extra + "\n"))
    #         #  add screenshot of allure report
    #         dirver = web_driver
    #         if hasattr(dirver, "get_screenshot_as_png"):
    #             with allure.step(' add a screenshot of the failure when the use case execution fails ...'):
    #                 print(" use case execution failed to capture the current page ......")
    #                 allure.attach(dirver.get_screenshot_as_png(), " failed screenshot ", allure.attachment_type.PNG)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         mode = 'a' if os.path.exists('failures') else 'w'
#         try:
#             with open('failures', mode) as f:
#                 if 'browser' in item.fixturenames:
#                     web_driver = item.funcargs['browser']
#                 else:
#                     print('Fail to take screen-shot')
#                     return
#             allure.attach(
#                 web_driver.get_screenshot_as_png(),
#                 name='screenshot',
#                 attachment_type=allure.attachment_type.PNG
#             )
#         except Exception as e:
#             print('Fail to take screen-shot: {}'.format(e))
# # set up a hook to be able to check if a test has failed
# # set up a hook to be able to check if a test has failed
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)
#
# # check if a test has failed
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     # request.node is an "item" because we use the default
#     # "function" scope
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             driver = request.node.funcargs['selenium_driver']
#             take_screenshot(driver, request.node.nodeid)
#             print("executing test failed", request.node.nodeid)
#
# # make a screenshot with a name of the test, date and time
# def take_screenshot(driver, nodeid):
#     time.sleep(1)
#     file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
#     driver.save_screenshot(file_name)