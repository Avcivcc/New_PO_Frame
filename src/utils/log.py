"""
日志写入
"""

import logging
import os
import datetime
from src.utils.config import Config
from src.utils.constants import Global_constants


class Log:

    # 初始化日志写入文件，读取配置，创建文件夹，设置输出log日志的格式
    def __init__(self):
        # 初始化读取配置设置
        conf = Config()
        self.log_path = conf.get_config('system', 'log_path')
        # 初始化时间设置
        now_time = datetime.datetime.now()
        # 日志文件夹名
        self.log_folder = self.log_path + now_time.strftime("%Y-%m-%d")
        # 日志文件名
        self.log_file = now_time.strftime("%H-%M")
        # 判断当前是否有文件夹，没有的话就创建一个文件夹
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        # 配置日志输出参数
        logging.basicConfig(
            # 设置输出等级，此处设置不设置不影响，因为不打印控制台
            level=logging.INFO,
            # 时间，日志存放地址，代码行号，日志级别，日志信息
            # 代码行号和日志级别信息在这里用不上，放在这里只是为了以后好复制
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            # 设置报错所显示的时间信息
            datefmt="%a, %d %b %Y %H:%M:%S",
            # 日志所写入的文件夹地址
            filename=self.log_folder + "/" + self.log_file + '.log',
            # 日志的写入方式，w覆盖，a追加，r只读
            filemode='a'
        )

    # 写入日志,写的信息都只会加入到message中
    # 这里可以再优化到断言里面去，暂时就这样了
    # def add_log(self, page, function, description):
    #     out_str = page + "：" + function + "：" + description
    #     logging.info(out_str)

    # 写入日志,写的信息都只会加入到message中
    def add_log(self, description):
        out_str = description
        logging.info(out_str)


# if __name__ == '__main__':
#     log = Log()
#     log.add_log('aa', 'bb', 'cc')
