import unittest

import ddt
from src.utils.readXls import ExcelUtil
from src.utils.driver import Driver
from time import sleep

file = '../../../data/data.xls'
sheet_name = 'data'
excel = ExcelUtil(file, sheet_name)

@ddt.ddt
class Test_DDT(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.drvier = Driver().get_Chrome_driver()
        self.drvier.maximize_window()

    @classmethod
    def tearDownClass(self):
        # self.driver = Driver().get_Chrome_driver()
        self.drvier.quit()

    def setUp(self):
        self.drvier.get('https://www.baidu.com')

    def tearDown(self):
        pass

    @ddt.data(*excel.obtain())
    def test_001(self, data):

        self.drvier.find_element_by_id('kw').clear()
        self.drvier.find_element_by_id('kw').send_keys(data['目的'])
        self.drvier.find_element_by_id('su').click()
        sleep(3)



if __name__ == '__main__':
    unittest.main()