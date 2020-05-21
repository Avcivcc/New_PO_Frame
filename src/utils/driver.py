"""
管理driver驱动
"""
from selenium import webdriver


class Driver:

    def __init__(self):
        # chrome驱动
        # self.driver_chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
        # chrome驱动死地址，测试使用
        self.driver_chrome = webdriver.Chrome(executable_path='D:/tools/Code/New_PO_Frame/driver/chromedriver.exe')

        # IE驱动

        # firefox驱动

    # 调用Chrome
    def get_Chrome_driver(self):
        return self.driver_chrome

    # 调用IE
    def get_Ie_driver(self):
        pass

    # 调用Firefox
    def get_Firefox_driver(self):
        pass


# if __name__ == '__main__':
#     dr = Driver()
#     dr.get_chrome_driver()
