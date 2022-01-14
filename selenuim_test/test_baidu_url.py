#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/9   fazz
project：获取当前测试页面的url

'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
driver.implicitly_wait(5)
print(driver.current_url)   #打印当前页面的url
driver.quit()

