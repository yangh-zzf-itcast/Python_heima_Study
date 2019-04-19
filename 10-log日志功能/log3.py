import logging

# 第一步：创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步：创建一个handler，用于写入日志文件
log_file = './log.txt'
fh = logging.FileHandler(log_file, mode='a')  # 打开日志文件的方式
fh.setLevel(logging.DEBUG)  # 输出到file中的log等级开关

# 第三步：再创建一个handler 用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到控制台的log等级开关

# 第四步：定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步：将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)

# 日志
logging.debug('这是 logging debug message')
logging.info('这是 logging info message')
logging.warning('这是 logging warning message')
logging.error('这是 logging error message')
logging.critical('这是 logging critical message')
