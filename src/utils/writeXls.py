"""
生成xls测试报告
"""
import xlrd, os, datetime
from xlwt import *
from xlutils.copy import copy
from src.utils.config import Config
from src.utils.constants import Global_constants


class Report:

    def __init__(self):
        # 初始化读取配置的函数
        self.conf = Config()
        # 初始化设置全局变量的参数
        self.cons = Global_constants()
        # 时间变量声明
        self.now_time = datetime.datetime.now()
        # 设置报告的生成路径和名称
        # 把路径存到变量里面
        excel_report_path = self.conf.get_config('system', 'excel_report_path')
        # 设置生成报告的文件夹名
        excel_report_folder = excel_report_path + self.now_time.strftime('%Y-%m-%d')
        # 设置生成报告的文件名
        excel_report_file = self.now_time.strftime('%H-%M-%S')
        # 把文件夹名和文件夹名传到全局变量中去，方便以后好取
        self.cons.set_value('excel_report_folder', excel_report_folder)
        self.cons.set_value('excel_report_file', excel_report_file)

        # 判断有无到处的文件夹啊，无的话就创建
        if not os.path.exists(excel_report_folder):
            os.makedirs(excel_report_folder)

        # 创建导出excel的报告模板
        excel_file = Workbook(encoding='utf-8')
        excel_sheet = excel_file.add_sheet('测试报告')
        # 创建基础信息
        for i in range(0, 4):
            excel_sheet.col(i).width = 256 * 40
        excel_sheet.write(0, 0, label='测试业务')
        excel_sheet.write(0, 1, label='测试行为')
        excel_sheet.write(0, 2, label='描述')
        excel_sheet.write(0, 3, label='测试时间')
        excel_file.save(excel_report_folder + '/' + excel_report_file + '.xls')

        # 初始化保存报告的文件
        self.output_file = self.cons.get_value('excel_report_folder') + '/' + self.cons.get_value('excel_report_file') \
                           + '.xls'

    def add_excel(self, story, action, des):
        # 打开数据表
        rexcel = xlrd.open_workbook(self.output_file, formatting_info=True)
        # 返回工作表的内容，把内容存到row中
        row = rexcel.sheets()[0].nrows
        # 将xlrd.book复制到xlwd.workbook中进行输入数据
        addexcel = copy(rexcel)
        addsheet = addexcel.get_sheet(0)
        addsheet.write(row, 0, story)
        addsheet.write(row, 1, action)
        addsheet.write(row, 2, des)
        addsheet.write(row, 3, self.now_time.strftime('%Y-%m-%d %H:%M:%S'))
        addexcel.save(self.output_file)


# if __name__ == '__main__':
#     test_report = Report()
#     test_report.add_excel('11', '22', '33')