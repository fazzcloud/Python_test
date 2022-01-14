#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/8   fazz
project：浏览器前进后退

'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(6)

driver.find_element_by_xpath("//*[@id='kw']").send_keys("lj")
driver.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)

try:
    driver.back()   #控制浏览器返回
    time.sleep(3)
    driver.forward()    #控制浏览器前进
    time.sleep(3)
    print("test pass,control Chrome successful")
except Exception  as error:
    print("test fail,%s"%(error))

