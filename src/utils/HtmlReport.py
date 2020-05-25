"""
html报告生成封装
"""
import os
import datetime
from src.utils.config import Config
from src.utils.constants import Global_constants



class HtmlReport:

    def __init__(self):
        # 初始化配置文件
        self.conf = Config()
        # 初始化全局变量参数的函数
        self.cons = Global_constants()
        # 初始化时间
        self.now_time = datetime.datetime.now()

        # 获取存html片地址的部分配置
        self.html_report_path = self.conf.get_config('system', 'html_path')
        # 设置html的存放地址
        self.html_report_folder = self.html_report_path + '/' + self.now_time.strftime('%Y-%m-%d')
        # 设置生成html的名字
        self.html_report_file = self.now_time.strftime('%H-%M') + '.html'
        # 把新增加的地址和文件名存到全局字典中，以后好调用
        self.cons.set_value('html_report_folder', self.html_report_folder)
        self.cons.set_value('html_report_file', self.html_report_file)

        if not os.path.exists(self.html_report_folder):
            os.makedirs(self.html_report_folder)

    def get_html_path(self):
        html_file_path = self.cons.get_value('html_report_folder') + '/' + self.cons.get_value('html_report_file')
        return html_file_path

# if __name__ == '__main__':
#     sb = HtmlReport()
#     print(sb.get_html_path())