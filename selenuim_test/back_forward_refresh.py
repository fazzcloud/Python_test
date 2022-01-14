#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/3    fazz
project：刷新，前进和后退

'''
from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.get("http://106.14.135.177/phpwind/")
time.sleep(3)

#前进后退
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)

#对网页进行刷新
driver.refresh()
time.sleep(3)
driver.quit()
