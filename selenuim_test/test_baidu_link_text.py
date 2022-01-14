#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/3    fazz
project：利用link_text定位

'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com/")

try:
    driver.find_element_by_link_text("新闻")
#    driver.find_element_by_xpath(
#       "//*/div[@id = 'u1']/a[text()='新闻']"
#    )
    print("test pass,element foud link text")
except Exception as  erorr:
    print("test fail,%s"%(erorr))

driver.quit()