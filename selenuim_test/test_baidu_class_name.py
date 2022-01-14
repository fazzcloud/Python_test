#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：利用class_name定位

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")

try:
    driver.find_element_by_class_name("s_ipt").send_keys("测试")
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[2]/input").click()
    time.sleep(3)
    driver.back()
    print("test pass,element found class")
except Exception as error:
    print("test fail,%s"%(error))
