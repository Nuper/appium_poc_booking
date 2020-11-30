import unittest

from pageobjects.home_screen import HomeScreen
from webdriver import Driver


class TestCases(unittest.TestCase):

    def setUp(self):
        print('Setting up driver')
        self.driver = Driver()

    def test_car_rental_search_flow(self):
        print('test_car_rental_search_flow')
        home = HomeScreen(self.driver)
        car_rental_screen = home.tap_navbar_car_rental()
        location = car_rental_screen.tap_location()
        car_rental_screen = location.select_car_rental_location('Barcelona')
        date_selection = car_rental_screen.tap_dates()
        date_selection.tap_select_dates(15)
        car_rental_screen = date_selection.tap_confirm_dates_car()
        car_rental_screen.tap_search()

    def tearDown(self):
        print('Quit driver')
        # self.driver.instance.quit()
