import unittest

import ddt
from src.utils.readXls import ExcelUtil
from src.utils.driver import Driver
from time import sleep
from src.utils.basepage import BasePage
from src.utils.browser_engine import Browser
from src.utils.log import Log


# logger = Log()
file = './data/data.xls'
sheet_name = 'data'
excel = ExcelUtil(file, sheet_name)
driver = Browser()


class BaiduPage:

    def open_url(self):
        self.base = BasePage(driver.open_browser())

    def close_browser(self):
        driver.quit_browser()

    def input_keywords(self, select, keys):
        self.base.input(select, keys)

    def click_element(self, select):
        self.base.click(select)

    def evel_assert(self, expectation):
        unittest.TestCase().assertIn(expectation, self.base.take_page())

    def screen_png(self, img_name):
        self.base.take_screenshot(img_name)


