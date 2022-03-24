from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    logo=(By.XPATH,"//span[contains(@class,'logo-svg')]")
    AppTitle = (By.XPATH, "//a[contains(@class,'link grey-40')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def get_homepage_title(self):
        return self.get_title()

    def homepage_logo_IsVisible(self):
        return self.is_element_enabled(self.logo)
    def getapp_title(self):
        return self.get_element_text(self.AppTitle)