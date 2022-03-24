from logging import critical

import pytest
import allure

from Pages.HomePage import HomePage
from Tests.test_base import BaseTest

#pytest  -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py
#pip install pytest-failed-screenshot
#pytest  --screenshot=on --screenshot_path=on -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py

## pending--how to take screenshot on failure

@pytest.mark.usefixtures("init_driver")
class TestG2(BaseTest):
    def test_login_success(self, init_driver):
       init_driver.get("https://github.com/fungaegis/pytest-failed-screenshot")
       assert False
#
# @pytest.mark.usefixtures("init_driver")
# class TestH1(BaseTest):
#        def test_verify_title(self, init_driver):
#         init_driver.get("https://github.com/fungaegis/pytest-failed-screenshot")
#         assert False
