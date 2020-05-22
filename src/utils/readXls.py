"""
读取数据
"""
import xlrd

class ExcelUtil:

    def __init__(self, file, sheet_name):
        # 检查表格是否存在
        try:
            # 获取表格
            self.data = xlrd.open_workbook(file)
            # 根据工作表名读取哪张表
            self.table = self.data.sheet_by_name(sheet_name)
            # 获取有数据的最大行数
            self.row_Num = self.table.nrows
            # 获取又数据的最大列数
            self.col_Num = self.table.ncols

            # 获取第一行作为表的值
            self.keys = self.table.row_values(0)
        except Exception:
            print('The data is none')

    def obtain(self):
        # 创建储存的变量
        r = []
        # 减去1是因为第一行被作为键了所以少循环一次
        for i in range(self.row_Num - 1):
            # 创建储存临时数据的变量
            s = {}
            # 加1是为了跳过第一个获取第二行的值
            value = self.table.row_values(i + 1)
            # 减一是为了不读取到第一行的建
            for x in range(self.col_Num - 1):
                s[self.keys[x]] = value[x]
            r.append(s)
        return r


# if __name__ == '__main__':
#     file = '../../data/data.xls'
#     sheet_name = 'data'
#     ex = ExcelUtil(file, sheet_name)
#     print(ex.obtain())