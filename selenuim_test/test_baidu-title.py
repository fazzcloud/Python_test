#coding=utf-8

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/9   fazz
project：获取当前测试页面的title

'''
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#点击贴吧，打开贴吧页面
driver.find_element_by_xpath('//*[@id="s-top-left"]/a[6]').click()
time.sleep(3)

#切换新窗口
#首先获取主句柄，作为灯塔，防止迷路
mainWindow = driver.current_window_handle

#获取所有的句柄
handles = driver.window_handles

#使用for循环，遍历所有handles，便于判断
for hendle in handles:
    #使用driver.switch_to.window()，切入句柄所在窗口
    driver.switch_to.window(hendle)

    #判断“贴吧”是否在当前窗口的title中，如果在，跳出循环
    if "贴吧" in driver.title:
        break

print(driver.title) #打印当前页面标题

driver.switch_to.window(mainWindow) #切回主句柄
print(driver.title)
time.sleep(3)
driver.quit()