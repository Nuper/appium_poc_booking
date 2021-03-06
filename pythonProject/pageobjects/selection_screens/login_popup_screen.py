import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pageobjects.home_screen import HomeScreen
from Locators.LocatorsLoginPopUpScreen import LocatorsLoginPopUpScreen
from Logger import log_assert


class LoginPopupScreen:
    def __init__(self, driver):
        self.driver = driver
        try:
            self.popup = WebDriverWait(self.driver.instance, 5).until(EC.visibility_of_element_located((
                MobileBy.ID, LocatorsLoginPopUpScreen.popup_android)))
        except TimeoutException:
            self.popup = None

    def account_selection(self):
        self.popup.click() if self.popup else log_assert(False, 'Test Failed')
        return HomeScreen(self.driver)
