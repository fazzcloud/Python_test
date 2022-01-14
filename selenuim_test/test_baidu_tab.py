#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/12   fazz
project：打开一个新的tab

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.baidu.com/")

ele = driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND,'t')
