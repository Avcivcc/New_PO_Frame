import xlrd


class ExcelUtil:

    def __init__(self,excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)

        # 获取第一行作为keys值

        # self.keys = self.table.row_values((0))
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

        for i in range(0, 4):
            self.keys = self.table.row_values(i)


    def dict_data(self):

        if self.rowNum < 1:
            print('1')
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                value = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = value[x]
                    r.append(s)
                    j += 1
                    return r


if __name__ == '__main__':
    excel_path = '../../data/data.xls'
    sheet_name = 'data'
    ex = ExcelUtil(excel_path, sheet_name)
    for i in ex.keys:
        print(i)