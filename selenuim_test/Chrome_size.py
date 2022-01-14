#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/3    fazz
project：打开Chrome浏览器，并调整浏览器大小

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
def get_size(driver):
    '''
    获取窗口尺寸并打印
    '''
    size = driver.get_window_size() #获取窗口尺寸
    print(size)
    time.sleep(3)   #打开窗口后暂停三秒
    return

driver.get("https://www.baidu.com")
get_size(driver)
driver.set_window_size(800,600) #设置窗口大小为800*600
get_size(driver)
driver.minimize_window()    #设置窗口为最小
get_size(driver)
driver.maximize_window()    #设置窗口为最大
get_size(driver)
driver.quit()