import logging
'''
通过basicConfig方法控制日志的输出
level参数用来设置日志输出级别
低于info级别的日志都不会打印，而format参数用设置日志输出格式
'''
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s'
    #日志输出格式为：打印日志时间 - 打印文件名[line：行号] - 级别名称：日志信息
)
if __name__ == '__main__':
    logging.debug("-----debug-------")
    logging.info("-----info-------")
    logging.warning("-----warning-------")
    logging.error("-----error-------")
    logging.critical("-----critical-------")
