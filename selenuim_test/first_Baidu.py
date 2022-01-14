#coding=utf-8

#先设置编码，一般放在第一行，如上

#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/3    fazz
project：打开Chrome浏览器，并打开百度首页

'''

from selenium import webdriver  #导入selenium库中的wbedriver模块（这里要安装selenium3，原本安装的4，无法导入webdriver）
import sys
C_driver = webdriver.Chrome()    #调用webdriver下面，Chrome类，赋值给变量driver（Chrome()类要注意大小写）,这里注意，用pycharm，一定要在setting中project interpreter安装selecnuim
C_driver.maximize_window()  #最大化浏览器
C_driver.get("https://www.baidu.com") #调用Chrome()类中的get方法，访问百度首页
C_driver.quit()
#关闭浏览器


