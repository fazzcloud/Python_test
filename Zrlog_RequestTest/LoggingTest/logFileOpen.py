import logging
logger = logging.getLogger("logFileOpen")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sh.setFormatter(formatter)

logger.addHandler(sh)

#加入异常处理，文件不存在则给出提示
try:
    open('path/to/does/not/exist','rb')
    logger.info("文件打开正常")
except Exception as  e:
    logger.error("文件不存在")