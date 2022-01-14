#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/5    fazz
project：元素定位,BY的用法

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.zhihu.com/")

ele = driver.find_element_by_xpath(
    '//*[@id="root"]/div/main/div/div/div/div[4]/div[1]/a'
)#利用xpath进行定位

ele.click() #点击定位到的元素
driver.back()

time.sleep(5)
ele = driver.find_element(
    By.XPATH,'//*[@id="root"]/div/main/div/div/div/div[4]/div[1]/a'
)

ele.click()
driver.back()


eles = driver.find_element_by_class_name("Input")

print(eles)
#print(len(eles))
time.sleep(5)

eles = driver.find_elements(By.CLASS_NAME,'Input')
print(eles)
#print(len(eles))