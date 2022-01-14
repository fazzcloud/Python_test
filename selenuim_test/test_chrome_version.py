#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/8   fazz
project：打印浏览器版本号

'''
from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.maximize_window()
driver.implicitly_wait(5)

print(driver.capabilities["chrome"])    #chrome要用chrome关键字，不能用version
print(driver.capabilities['chrome']['chromedriverVersion'])  #打印chromedriver的值版本
driver.quit()