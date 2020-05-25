from src.gui.page.baidu_page import BaiduPage
from src.utils.readXls import ExcelUtil
from src.utils.screenshot import ScreenShot
from time import sleep
import unittest, ddt

base = BaiduPage()
file = './data/data.xls'
sheet_name = 'data'
excel = ExcelUtil(file, sheet_name)

@ddt.ddt
class TestBaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        base.open_url()

    @classmethod
    def tearDownClass(self):
        base.close_browser()

    @ddt.data(*excel.obtain())
    def test_baidu_search(self, data):
        base.input_keywords('id=>kw', data['目的'])
        base.click_element('id=>su')
        sleep(2)
        base.screen_png(data['结果'])
        base.evel_assert(data['目的'])