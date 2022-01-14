#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/3    fazz
project：截图

'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.get_screenshot_as_file("D:\Pycharm\\123.png")    #截图
driver.quit()