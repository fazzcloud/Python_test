import logging
#实例化一个log对象,getlogger需要传入一个name形参
logger = logging.getLogger("LoggingTest02")
#设置日志级别
logger.setLevel(logging.DEBUG)
#实例化一个控制台对象
sh = logging.StreamHandler() #StreamHandler是一个class，也就是一个类，下面包含了很多函数
#设置控制台输出级别
sh.setLevel(logging.DEBUG) #setLevel是StreamHandler中的一个函数
#设置控制台打印的格式
format = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s:%(message)s')
sh.setFormatter(format)
#加载控制台实例到logger对象中
logger.addHandler(sh)

if __name__ == '__main__':
    logging.debug("-----debug-------")
    logging.info("-----info-------")
    logging.warning("-----warning-------")
    logging.error("-----error-------")
    logging.critical("-----critical-------")
