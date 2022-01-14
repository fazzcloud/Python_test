#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：利用tag name定位

'''
from selenium import webdriver
#引入webdriver打开浏览器，访问百度，并将浏览器最大化，同时等待5秒
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com/")

#捕获异常，若可定位到tag_name，则测试通过，捕获失败，则给出提示
try:
    driver.find_element_by_tag_name("form1")
    print("test pass:found tag_name")
except Exception as erorr:
    print("test faill，",format(erorr)) # format是打印，这里打印了报错的信息

driver.quit()

