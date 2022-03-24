import pytest

from Pages.HomePage import HomePage
from Tests.test_base import BaseTest

#pytest test_Home.py -v -s --capture sys --html="FirstReport.html"


class TestHome(BaseTest):

    def test_verify_title(self):
        self.homepage = HomePage(self.driver)
        act = self.homepage.get_homepage_title()
        assert act == "ABB Drive and Motor Selecto"

    def test_verify_logo(self):
        self.homepage = HomePage(self.driver)
        act = self.homepage.homepage_logo_IsVisible()
        assert  act

    def test_verify_app_title(self):
        self.homepage = HomePage(self.driver)
        act = self.homepage.getapp_title()
        assert act == "DRIVE AND MOTOR SELECTOR"

