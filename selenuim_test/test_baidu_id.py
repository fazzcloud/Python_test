#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：利用ID定位

'''
from selenium import webdriver
#引入webdriver打开浏览器，访问百度，并将浏览器最大化，同时等待5秒
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#捕获异常，若可定位到ID，则测试通过，捕获失败，则给出提示
try:
    driver.find_element_by_id("kw1")
    print("test pass:ID found")
except Exception as error:
    print("test fail，%s"%(error))   # %是格式化字符串

driver.quit()


