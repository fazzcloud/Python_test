#注释，包括创建时间，创建人项目名称
'''

Create 2021/11/4    fazz
project：获取百度页面-联系我们-邮箱

'''
'导入模块'
from selenium import webdriver
import re
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)   #隐式等待5秒，找到页面元素就结束等待

driver.get("http://home.baidu.com/contact.html")

doc = driver.page_source    #获取页面源代码

emails = re.findall(r'[\w]+@[\w\.-]+', doc) #利用正则，找出xx@xx字段，保存到emails列表

for email in emails:
    print(email)

driver.quit()



