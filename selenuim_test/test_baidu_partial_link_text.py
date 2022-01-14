#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：利用partial_link_text定位

'''
from selenium import webdriver
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")

try:
    driver.find_element_by_partial_link_text("更多").click()  #加click()方法，可以触发点击事件
    print("test pass,element foud partial_link_text ")
except Exception as erorr:
    print("test fail,%s"%(erorr))

#river.quit()