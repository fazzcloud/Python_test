#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/8   fazz
project：刷新页面

'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(5)

try:
    driver.refresh()    #页面刷新方法
    print("test pass,refesh successful")
except Exception as  error:
    print("test fail,%s"%(error))

driver.quit()