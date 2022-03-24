from logging import critical

import pytest
import allure

from Pages.HomePage import HomePage
from Tests.test_base import BaseTest

### installations required ####
#1.pip install pytest
#2.pip install pytest-xdist  -->for parallel execution
#3.pip install pytest-html   -->for html reports
#4.pip install pytest-failed-screenshot   -->for failure will attach screenshot in allure report
#5.pip install allure-pytest  -->for allure reports
#pytest  -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py
#pip install pytest-failed-screenshot
#pytest  --screenshot=on --screenshot_path=on -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py

## pytest  --screenshot=on --screenshot_path=on D:\PytestDemo\Tests\screenshot -v -s --capture sys --alluredir="../Reports" test_HomeAllure.py


@pytest.mark.usefixtures('init_driver')
class TestHome(BaseTest):


    @allure.severity(allure.severity_level.MINOR)
    def test_verify_title(self,init_driver):
        self.homepage = HomePage(init_driver)
        act = self.homepage.get_homepage_title()
        assert act == "ABB Drive and Motor Selecto"

    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_logo(self,init_driver):
        self.homepage = HomePage(init_driver)
        act = self.homepage.homepage_logo_IsVisible()
        assert act

    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_app_title(self,init_driver):
        self.homepage = HomePage(init_driver)
        act = self.homepage.getapp_title()
        assert act == "DRIVE AND MOTOR SELECTOR"

