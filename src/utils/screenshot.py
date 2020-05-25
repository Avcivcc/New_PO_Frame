"""
selenium截图功能封装
"""
import os
import datetime
from src.utils.log import Log
from src.utils.config import Config
from src.utils.constants import Global_constants
from selenium import webdriver


class ScreenShot:

    def __init__(self):
        # 初始化配置文件
        self.conf = Config()
        # 初始化全局变量参数的函数
        self.cons = Global_constants()
        # 初始化时间
        self.now_time = datetime.datetime.now()
        # 初始化日志
        self.logger = Log()

        # 获取存照片地址的部分配置
        self.png_report_path = self.conf.get_config('system', 'screenshot_path')
        # 设置照片的存放地址
        self.png_report_folder = self.png_report_path + '/' + self.now_time.strftime('%Y-%m-%d')
        # 设置生成照片的名字
        self.png_report_file = self.now_time.strftime('%H-%M-%S')
        # 把新增加的地址和文件名存到全局字典中，以后好调用
        self.cons.set_value('png_report_folder', self.png_report_folder)
        self.cons.set_value('png_report_file', self.png_report_file)

        if not os.path.exists(self.png_report_folder):
            os.makedirs(self.png_report_folder)

        # 初始化浏览器
        # self.driver = webdriver.Chrome()

    def return_photo_path(self, img_name):
        # try:
        #     driver.get_screenshot_as_file(self.png_report_folder + img_name
        #                                   + self.now_time.strftime('%H_%M_%S') + ".png")
        #     self.logger.add_log("Had take screenshot and saved!")
        # except Exception as e:
        #     self.logger.add_log("Failed to take screenshot!%s" % e)

        screenshot_file = self.png_report_folder + '/' + img_name + self.now_time.strftime('%H_%M_%S') + ".png"

        return screenshot_file

# if __name__ == '__main__':
#     sb = ScreenShot()
#     print(sb.return_photo_path('百度'))
