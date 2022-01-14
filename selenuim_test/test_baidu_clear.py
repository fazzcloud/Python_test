#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：clear清除文本

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#根剧xpath进行定位，定位到百度首页的的搜索栏，并输入“Selenium”
driver.find_element_by_xpath("//*[@id='kw']").send_keys("Selenium")
time.sleep(3)

try:
    #根剧xpath定位，使用clear()方法清除文本
    driver.find_element_by_xpath("//*[@id='kw']").clear()
    time.sleep(3)
    print("test pass,clean successful")
except  Exception as error:
    print("test fail,%s"%(error))

