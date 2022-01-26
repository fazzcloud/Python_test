# 导入 logging 库
import logging
#创建日志对象
logger = logging.getLogger("LoggingTest04")
#设置日志级别
logger.setLevel(logging.DEBUG)

#创建文件实例，若文件不存在，则自动创建
#mode参数设置为追加，也就是增量；encoding是设置编码格式
sh = logging.StreamHandler()
fh = logging.FileHandler('api.log',mode='a',encoding='utf-8')
#设置文件输出的级别
sh.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)

#设置日志输出文件的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)
fh.setFormatter(formatter)#类似java中，对私有变量赋值的get/set方法

#加载文件实例到logger对象中
logger.addHandler(sh)
logger.addHandler(fh)
if __name__ == "__main__":
    logger.debug('----- 调试信息 [debug]-----')
    logger.info('----- 有用的信息 [info]-----')
    logger.warning('----- 警告信息 [warning]-----')
    logger.error('----- 错误信息 [error]-----')
    logger.critical('----- 严重错误信息 [critical]-----')

