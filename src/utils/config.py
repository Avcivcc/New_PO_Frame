"""
读取全局配置
"""

import configparser


class Config:

    # 初始化配置文件的路径
    def __init__(self):
        # 配置文件的路径
        # self.file = './config/config.ini'

        # 配置文件的死地址，测试使用
        self.file = 'D:/tools/Code/New_PO_Frame/config/config.ini'

    # 获取配置
    def get_config(self, section, name):
        # 初始化获取配置文件的方法
        config = configparser.ConfigParser()
        # 读取文件
        config.read(self.file, encoding='utf-8')
        # 输入section和name取到配置值
        value = config.get(section, name)
        # 把获取到的值返回出去
        return value


# if __name__ == '__main__':
#     cof = Config()
#     print(cof.get_config('system', 'log_path'))
