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


@ddt.ddt
class Test_DDT(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # self.drvier = Driver().get_Chrome_driver()
        # self.drvier.maximize_window()
        self.base = BasePage(driver.open_browser())

    @classmethod
    def tearDownClass(self):
        # self.driver = Driver().get_Chrome_driver()
        # self.drvier.quit()
        driver.quit_browser()

    def setUp(self):
        # self.drvier.get('https://www.baidu.com')
        pass

    def tearDown(self):
        pass

    @ddt.data(*excel.obtain())
    def test_001(self, data):

        self.base.input('id=>kw', data['目的'])
        self.base.click('id=>su')
        # self.drvier.find_element_by_id('kw').clear()
        # self.drvier.find_element_by_id('kw').send_keys(data['目的'])
        # self.drvier.find_element_by_id('su').click()
        sleep(3)



if __name__ == '__main__':
    unittest.main()