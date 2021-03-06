import logging

# filename 和 filemode设置日志输入的文件路径，以及写入的方式

logging.basicConfig(level=logging.DEBUG,
                    filename='./log.txt',
                    filemode='w',
                    format='%(asctime)s-%(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')

# 默认的level是WARNING，大于等于warning级别才会写入日志
# 实际调试中，设置level为DEBUG
# 发布程序时，一般设置为INFO

logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critical message')
