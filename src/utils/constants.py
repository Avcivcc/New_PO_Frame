"""
配置当前的运行常量
"""


class Global_constants:

    # 初始化
    def __init__(self):
        global global_dict
        self.global_dict = {}

    def set_value(self, key, value):
        self.global_dict[key] = value

    def get_value(self, key):
        try:
            return self.global_dict[key]
        except KeyError:
            return


# if __name__ == '__main__':
#     glo = global_constants()
#     glo.set_value('test', 'zhouhuanxue')
#     print(glo.get_value('te1'))