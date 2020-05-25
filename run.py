from src.utils.HTMLTestRunner_PY3 import HTMLTestRunner
from src.utils.HtmlReport import HtmlReport
from src.utils.config import Config
import unittest, time, os


filename = './src/gui/story'
suit = unittest.defaultTestLoader.discover(filename, pattern='test_*.py')
html = HtmlReport()
html_path = html.get_html_path()

if __name__ == '__main__':
    runner = HTMLTestRunner(open(html_path, 'wb'), title='测试报告', description='测试')
    runner.run(suit)