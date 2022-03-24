import pytest

@pytest.mark.usefixtures("init_driver")
class TestG2:
    def test_login_success(self, init_driver):
       init_driver.get("https://github.com/fungaegis/pytest-failed-screenshot")
       assert False